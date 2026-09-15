# Google Sheets research register

Use one spreadsheet with exactly six thematic tabs. Keep each tab as a flat table with one header row, frozen headers, filters, typed date fields, wrapped text, direct URLs, and controlled status/priority values.

## 1. Weekly Summary

Run ID; Run date; Coverage start; Coverage end; Topic; Report type; Word limit; Actual words; Literature added; Researchers added; Conferences added; Funding added; Labs added; Repeats suppressed; Sources planned; Sources checked; Sources unavailable; Source limitations; ACT NOW count; USE IN THESIS count; COLLABORATE count; Top findings; Thesis-gap change; Strongest contradiction; Instruments added; Opportunity outcomes; Proposed profile changes; Digest link; Source-coverage audit link; User notes.

## 2. Literature

Record ID; Date found; Publication date; Evidence type; Action label; Confidence badge; Title; Authors; Journal/source; DOI; Discovered via; Verified via; Access limitations; Indexing status; Indexing evidence URL; Study design; Sample/context; Main findings; Limitations; Thesis chapter; Construct/variable; Research question; Proposed thesis use; Expected contribution; Transfer risk; Relationship to evidence; Related record IDs; Instrument name; Instrument construct/task; Population/language; Scoring dimensions; Reliability/validity; Availability; Permission/licence; Adaptation notes; Primary URL; Digest run; Review status; Feedback label; User notes.

## 3. Researchers

Researcher ID; Date found; Action label; Confidence badge; Name; Current role; Institution; Country; ORCID; Shared topics; Complementary expertise; Representative work; Recent relevant activity; Collaboration hypothesis; Proposed first joint output; Institutional profile; Verified public contact route; Last verified; Outreach status; Owner; Feedback label; User notes.

## 4. Conferences

Conference ID; Date found; Action label; Confidence badge; Conference; Organizer; Discovered via; Verified via; Country/city; Format; Event start; Event end; Call status; Call opens; Abstract deadline; Deadline timezone; Acceptance notification; Funding verified; Funding details; Travel-grant deadline; Official eligibility; Eligibility pre-check; Eligibility reason; Missing eligibility facts; Topic fit; Official call URL; Last verified; Priority; Pipeline stage; Proposed next stage; Feedback label; User notes.

## 5. Funding

Opportunity ID; Date found; Action label; Confidence badge; Program; Funder; Type; Discovered via; Verified via; Access limitations; Amount; Currency; Covered costs; Official eligibility; Eligibility pre-check; Eligibility reason; Missing eligibility facts; Geography; Opens; Deadline; Deadline timezone; Status; Topic fit; Official URL; Last verified; Priority; Application status; Outcome; Feedback label; User notes.

## 6. Labs & Institutions

Organization ID; Date found; Action label; Confidence badge; Institution; Lab/group; Country; Research focus; Why relevant; Key researchers; Complementary assets/expertise; Collaboration hypothesis; Proposed first joint output; Recent development; Primary URL; Verified public contact route; Last verified; Relationship status; Owner; Feedback label; User notes.

## Update rules

- Match literature by DOI, then canonical URL.
- Match researchers by ORCID, then institutional-profile URL.
- Match conferences and funding by official identifier, then official-call URL.
- Match labs and institutions by primary institutional URL.
- Update factual fields and `Last verified`; never overwrite user notes, owner, outreach/application/relationship status, or a manually assigned priority.
- Never overwrite conference pipeline stage, proposed-next-stage decision, application status, outcome, feedback label, or manually edited thesis mappings.
- Keep instrument records inside `Literature` so the workbook remains exactly six tabs. Use one row per publication and include multiple instruments as semicolon-delimited named entries only when their permissions match; otherwise create a second record row with the same DOI plus an instrument suffix.
- Use controlled values from `references/research-intelligence-features.md` for action, confidence, eligibility, pipeline, evidence relationship, availability, and feedback fields.
- Add formulas to Weekly Summary for record counts, but keep the deduplication ledger separate and authoritative.
