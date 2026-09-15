# Persistent memory and output contract

## Why persistent files are required

Conversation context is temporary and may be summarized or unavailable to later scheduled runs. Use the on-disk ledger as the source of truth for deduplication. The ledger stores compact identifiers and minimal display metadata, not article bodies.

## Data directory

Create one directory per monitoring profile:

```text
living-knowledge-data/
└── <monitor-id>/
    ├── profile.json
    ├── state.json
    ├── runs.jsonl
    ├── feedback.jsonl
    ├── source-coverage/
    │   └── YYYY-MM-DD.json
    ├── candidates/
    │   └── YYYY-MM-DD.json
    ├── digests/
    │   └── YYYY-MM-DD.md
    └── syntheses/
        └── YYYY-MM.md
```

Keep the data directory outside the installed skill folder. This allows the skill to be upgraded or replaced without losing memory and lets the portable skill be shared without sharing a recipient's history.

## Deduplication behavior

`memory_store.py` derives multiple aliases when available:

- Normalized DOI.
- Stable external ID such as ORCID, grant ID, standard number, or vacancy ID.
- Canonical URL with tracking parameters and fragments removed.
- Normalized title fingerprint.
- Normalized person/organization fingerprint for professor entries.

An item is repeated when any strong alias already exists. A normalized title also blocks the same work discovered at a different URL. This is conservative by design.

A non-empty `force_include_reason` bypasses suppression for a correction, material update, or deadline reminder. The exception is stored in history and must be visible to the reader.

## State lifecycle

- Keep pilot state temporary and separate from an activated monitor.
- Show the proposed profile and pilot digest before activation.
- Run `init` once; it is safe to repeat.
- Run `filter` before drafting the digest.
- Commit only the candidates actually included in a completed digest.
- Never delete the ledger merely to make an item appear new.
- Back up or copy the whole data directory when moving monitoring to another machine.
- Use `status` to inspect item and run counts and the previous successful run date.

The script writes `state.json` atomically. Do not run two commits concurrently for the same monitor ID.

Keep feedback append-only and keyed by a stable item identifier plus timestamp. Preserve the user's original label and note. Derive ranking preferences at run time; never rewrite historical feedback or convert it into a hard exclusion without explicit approval.

## Digest contract

Place a compact executive summary first. Highlight the main findings, direct thesis or research implications, urgent deadlines, and recommended actions. Enforce the configured hard word limit across the complete output, counting all output languages together. Use exact dates, deadline timezones, funding amounts or covered costs, eligibility, stable identifiers, and direct official URLs whenever available.

The default digest includes:

1. Topic, recipient/audience, coverage window, run date, and a two-to-four sentence executive pulse.
2. Research publications.
3. Scientific, technology, and laboratory news.
4. Standards, policy, and regulatory changes.
5. PhD, PostDoc, fellowship, funding, and grant opportunities.
6. Featured professor/research leader and collaboration angle.
7. Teaching or syllabus implications as review proposals.
8. Watchlist and evidence limitations.
9. Method note: sources checked, deduplication result, and next scheduled review.

The method note summarizes source coverage by source set and discloses subscription, login, CAPTCHA, access-block, or other material limitations. The detailed source-coverage JSON is the audit record; a source counts as checked only when its platform or authorized feed was actually reviewed with a relevant query or filter.

Each delivered item also has one primary action label and one confidence badge. When thesis context exists, add a compact thesis mapping. Add contradiction and instrument sections only when evidence supports them. Request feedback on selected items without forcing a response.

Monthly synthesis is a separate artifact built from successful run records. It may cite previously delivered items as evidence but must not describe them as newly discovered or commit them again.

Every item should expose its primary link and date. Separate source facts from analysis. Keep “why it matters” recipient-specific.

## Research register synchronization

If enabled, update the six-tab Google Sheets research register only with records delivered in the final digest. Match existing rows by stable identifier or canonical URL. Preserve all user-managed notes, statuses, owners, and priorities. The register supports review and collaboration; it does not replace `state.json` and `runs.jsonl` for cross-run deduplication.

## Repeat metric

Measure avoidable repeats as delivered items suppressed by neither a valid correction, material update, nor deadline reminder. Target at least 90% elimination. Report exceptions transparently rather than optimizing the metric by hiding them.
