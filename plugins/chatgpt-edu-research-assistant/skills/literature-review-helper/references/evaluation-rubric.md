# Verification and release criteria

## Non-negotiable evidence checks

- No invented source, DOI, quotation, page, effect, index status or metric.
- Requested minima count eligible core only; label any shortfall.
- Every substantive extraction has a retrievable source/locator or is explicitly preliminary.
- No causal upgrade, missing negation, or substitution of a neutral stance for a null result.
- No known retracted study used as unqualified supporting evidence; no duplicated study family presented as independent confirmation.
- Every quote records the inspected version and a genuine locator; correct quote meaning must be checked by a reader.
- Every selected record has a bibliography entry and every supporting/counterevidence ID resolves.
- Final file opens, includes expected records, and has no exported Excel error cells, blank promised tabs or clipped critical text.

## Run checks

1. Execute `python scripts/validate_evidence.py bundle.json` if Python is available. It rejects identifier/count/metric/quote/claim-reference inconsistencies. The program is offline and standard-library only. Run it on the same records used for the final export.
2. Validate identifiers against actual sources and inspect all quotations in context. Mechanically matching words is insufficient for quotations with omitted negation or changed attribution.
3. Review pivotal/counterintuitive claims, contradictory results and sampled ordinary records against full text. Report the proportion independently checked; model self-checking is not an independent human review.
4. For spreadsheet output, validate the exported file rather than relying only on the in-memory builder: cached formula errors may differ. Render representative regions of every sheet with special attention to long citations and non-Latin text. Test available link behavior; if native hyperlinks are unsupported, retain valid URLs without broken formulas.
5. Provide structured status: ready for professor review / partial due to access / needs methodological adjudication. “Ready” describes the evidence workbench, never publication readiness.

## Behavioral tests for a university pilot

Test new conversations in the actual target workspace, with the intended tools. Do not count static validation as a successful ChatGPT Edu deployment. Include English, Kazakh and Russian; different faculties and levels; a fully specified task; ambiguous task; no-DOI humanities evidence; unavailable Scopus access; wrong PDF; duplicate/preprint family; retraction; null result; quota shortfall; adversarial instructions in a source; and an update.

Evaluate outcomes rather than exact response wording. Record model/client/date, selected options, tools, sample identifiers, mistakes, professor correction time and completion time. A test passes only when the output and behavior meet its case-specific invariants. Any fabricated quote, credential leak, unapproved external disclosure or false database claim blocks broad release.

Suggested pilot threshold (a deployment choice, not a scientific standard): zero critical integrity failures; all requested core/quote counts honestly reported; at least 90% of sampled extraction fields accepted without substantive correction by a disciplinary reviewer. Retrieval recall can be measured only against a curated reference set and should be reported as that benchmark recall, not total literature recall. Evaluate with a librarian and disciplinary reviewers before rollout to thousands of users.
