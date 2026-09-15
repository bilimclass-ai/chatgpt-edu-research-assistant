#!/usr/bin/env python3
"""Check a Markdown digest against a hard word budget."""

import argparse
import json
import re
from pathlib import Path


def count_words(text: str) -> int:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"!\[[^]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return len(re.findall(r"[^\W_]+(?:[-’'][^\W_]+)*", text, flags=re.UNICODE))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("--max-words", type=int, required=True)
    args = parser.parse_args()
    words = count_words(args.file.read_text(encoding="utf-8"))
    result = {"words": words, "max_words": args.max_words, "within_budget": words <= args.max_words}
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["within_budget"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
