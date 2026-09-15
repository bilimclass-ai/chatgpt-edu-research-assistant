#!/usr/bin/env python3
"""Persistent, deterministic deduplication ledger for living-knowledge-monitor."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

VERSION = 1
TRACKING_KEYS = {
    "fbclid", "gclid", "mc_cid", "mc_eid", "ref", "ref_src", "source",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_text(value: str) -> str:
    value = value.casefold().strip()
    value = re.sub(r"[^\w\s]", " ", value, flags=re.UNICODE)
    return " ".join(value.split())


def digest_text(prefix: str, value: str) -> str:
    normalized = normalize_text(value)
    return f"{prefix}:{hashlib.sha256(normalized.encode('utf-8')).hexdigest()[:24]}"


def normalize_doi(value: str) -> str:
    value = value.strip().casefold()
    value = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", value)
    return value.rstrip(" .")


def canonical_url(value: str) -> str:
    if not value.strip():
        return ""
    parts = urlsplit(value.strip())
    scheme = parts.scheme.casefold() or "https"
    netloc = parts.netloc.casefold()
    path = re.sub(r"/{2,}", "/", parts.path).rstrip("/") or "/"
    kept = []
    for key, val in parse_qsl(parts.query, keep_blank_values=True):
        key_lower = key.casefold()
        if key_lower.startswith("utm_") or key_lower in TRACKING_KEYS:
            continue
        kept.append((key, val))
    return urlunsplit((scheme, netloc, path, urlencode(sorted(kept)), ""))


def aliases_for(item: dict[str, Any]) -> list[str]:
    aliases: list[str] = []
    doi = normalize_doi(str(item.get("doi") or ""))
    if doi:
        aliases.append(f"doi:{doi}")
    external_id = normalize_text(str(item.get("external_id") or ""))
    if external_id:
        aliases.append(f"external:{external_id}")
    url = canonical_url(str(item.get("url") or ""))
    if url:
        aliases.append(f"url:{url}")
    title = str(item.get("title") or "").strip()
    if title:
        kind = str(item.get("kind") or "unknown").strip()
        owner = str(item.get("person_or_org") or "").strip()
        title_scope = title if kind == "publication" else f"{kind} {title} {owner}"
        aliases.append(digest_text("title", title_scope))
    if str(item.get("kind") or "") == "professor":
        person = str(item.get("person_or_org") or "").strip()
        if person:
            aliases.append(digest_text("person", person))
    return list(dict.fromkeys(aliases))


def primary_key(item: dict[str, Any], aliases: list[str]) -> str:
    if aliases:
        return aliases[0]
    payload = json.dumps(item, ensure_ascii=False, sort_keys=True)
    return f"record:{hashlib.sha256(payload.encode('utf-8')).hexdigest()[:24]}"


def default_state() -> dict[str, Any]:
    return {
        "version": VERSION,
        "created_at": utc_now(),
        "updated_at": utc_now(),
        "last_successful_run": None,
        "items": {},
        "runs": 0,
    }


def paths(state_dir: Path) -> tuple[Path, Path]:
    return state_dir / "state.json", state_dir / "runs.jsonl"


def load_state(state_dir: Path) -> dict[str, Any]:
    state_path, _ = paths(state_dir)
    if not state_path.exists():
        raise FileNotFoundError(f"State not initialized: {state_path}")
    with state_path.open("r", encoding="utf-8") as handle:
        state = json.load(handle)
    if state.get("version") != VERSION or not isinstance(state.get("items"), dict):
        raise ValueError("Unsupported or invalid state.json")
    return state


def atomic_write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def read_candidates(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, list) or not all(isinstance(item, dict) for item in payload):
        raise ValueError("Candidates file must contain a JSON array of objects")
    return payload


def alias_index(state: dict[str, Any]) -> dict[str, str]:
    index: dict[str, str] = {}
    for key, record in state["items"].items():
        for alias in record.get("aliases", []):
            index[alias] = key
    return index


def filter_candidates(state: dict[str, Any], candidates: list[dict[str, Any]]) -> dict[str, Any]:
    index = alias_index(state)
    unseen, repeated = [], []
    batch_aliases: dict[str, int] = {}
    for position, original in enumerate(candidates):
        item = dict(original)
        aliases = aliases_for(item)
        force_reason = str(item.get("force_include_reason") or "").strip()
        prior_key = next((index[a] for a in aliases if a in index), None)
        duplicate_position = next((batch_aliases[a] for a in aliases if a in batch_aliases), None)
        memory = {
            "aliases": aliases,
            "primary_key": primary_key(item, aliases),
            "matched_key": prior_key,
            "duplicate_candidate_position": duplicate_position,
            "forced": bool(force_reason),
        }
        item["_memory"] = memory
        if force_reason:
            unseen.append(item)
        elif prior_key is not None or duplicate_position is not None:
            repeated.append(item)
        else:
            unseen.append(item)
            for alias in aliases:
                batch_aliases[alias] = position
    return {
        "generated_at": utc_now(),
        "counts": {"input": len(candidates), "unseen": len(unseen), "repeated": len(repeated)},
        "unseen": unseen,
        "repeated": repeated,
    }


def cmd_init(args: argparse.Namespace) -> None:
    state_dir = Path(args.state_dir).resolve()
    state_path, runs_path = paths(state_dir)
    state_dir.mkdir(parents=True, exist_ok=True)
    (state_dir / "candidates").mkdir(exist_ok=True)
    (state_dir / "digests").mkdir(exist_ok=True)
    if not state_path.exists():
        atomic_write_json(state_path, default_state())
    runs_path.touch(exist_ok=True)
    print(json.dumps({"state_dir": str(state_dir), "initialized": True}, ensure_ascii=False))


def cmd_status(args: argparse.Namespace) -> None:
    state_dir = Path(args.state_dir).resolve()
    state = load_state(state_dir)
    kinds: dict[str, int] = {}
    forced = 0
    for record in state["items"].values():
        kind = record.get("kind") or "unknown"
        kinds[kind] = kinds.get(kind, 0) + 1
        forced += int(record.get("forced_inclusions", 0))
    print(json.dumps({
        "state_dir": str(state_dir),
        "last_successful_run": state.get("last_successful_run"),
        "runs": state.get("runs", 0),
        "items": len(state["items"]),
        "items_by_kind": kinds,
        "forced_inclusions": forced,
    }, ensure_ascii=False, indent=2, sort_keys=True))


def cmd_filter(args: argparse.Namespace) -> None:
    state_dir = Path(args.state_dir).resolve()
    state = load_state(state_dir)
    result = filter_candidates(state, read_candidates(Path(args.candidates)))
    if args.output:
        atomic_write_json(Path(args.output).resolve(), result)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


def cmd_commit(args: argparse.Namespace) -> None:
    state_dir = Path(args.state_dir).resolve()
    state = load_state(state_dir)
    candidates = read_candidates(Path(args.candidates))
    run_date = date.fromisoformat(args.run_date).isoformat()
    index = alias_index(state)
    committed = 0
    forced_count = 0
    for item in candidates:
        item = {key: value for key, value in item.items() if key != "_memory"}
        aliases = aliases_for(item)
        key = next((index[a] for a in aliases if a in index), primary_key(item, aliases))
        force_reason = str(item.get("force_include_reason") or "").strip()
        if key in state["items"]:
            record = state["items"][key]
            record["aliases"] = list(dict.fromkeys(record.get("aliases", []) + aliases))
            for alias in aliases:
                index[alias] = key
            record["last_delivered"] = run_date
            record["delivery_count"] = int(record.get("delivery_count", 1)) + 1
            if force_reason:
                record["forced_inclusions"] = int(record.get("forced_inclusions", 0)) + 1
                record.setdefault("force_reasons", []).append({"date": run_date, "reason": force_reason})
                forced_count += 1
        else:
            record = {
                "aliases": aliases,
                "kind": item.get("kind"),
                "title": item.get("title"),
                "url": item.get("url"),
                "person_or_org": item.get("person_or_org"),
                "published_at": item.get("published_at"),
                "first_delivered": run_date,
                "last_delivered": run_date,
                "delivery_count": 1,
                "forced_inclusions": int(bool(force_reason)),
            }
            if force_reason:
                record["force_reasons"] = [{"date": run_date, "reason": force_reason}]
                forced_count += 1
            state["items"][key] = record
            for alias in aliases:
                index[alias] = key
        committed += 1
    state["last_successful_run"] = run_date
    state["runs"] = int(state.get("runs", 0)) + 1
    state["updated_at"] = utc_now()
    state_path, runs_path = paths(state_dir)
    atomic_write_json(state_path, state)
    audit = {
        "committed_at": utc_now(),
        "run_date": run_date,
        "digest": str(Path(args.digest).resolve()),
        "candidate_file": str(Path(args.candidates).resolve()),
        "delivered_items": committed,
        "forced_inclusions": forced_count,
    }
    with runs_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(audit, ensure_ascii=False, sort_keys=True) + "\n")
    print(json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name, function in (("init", cmd_init), ("status", cmd_status)):
        sub = subparsers.add_parser(name)
        sub.add_argument("--state-dir", required=True)
        sub.set_defaults(function=function)
    sub = subparsers.add_parser("filter")
    sub.add_argument("--state-dir", required=True)
    sub.add_argument("--candidates", required=True)
    sub.add_argument("--output")
    sub.set_defaults(function=cmd_filter)
    sub = subparsers.add_parser("commit")
    sub.add_argument("--state-dir", required=True)
    sub.add_argument("--candidates", required=True)
    sub.add_argument("--run-date", required=True)
    sub.add_argument("--digest", required=True)
    sub.set_defaults(function=cmd_commit)
    return parser


def main() -> int:
    try:
        args = build_parser().parse_args()
        args.function(args)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
