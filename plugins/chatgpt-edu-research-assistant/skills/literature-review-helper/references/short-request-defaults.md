# Short requests and named presets

## Shared short-request behavior

When a user asks for a literature review with a recognizable topic, use an editable XLSX evidence workbook as the default product, including the full extraction, comparison, bibliography, metrics and handoff described in output-formats.md. “Write me a literature review on X” alone does not override this default; “write the chapter/narrative text”, a specified prose word count, or an explicitly requested brief summary does. Preserve explicit instructions and supplied protocols.

For standard contemporary-topic reviews, aim for at least 50 eligible sources and the latest six calendar years through the search date. Explain genuine scarcity or access shortfalls; never pad. Historical/theoretical fields and requests for other depth/time windows retain the adaptive-intake exceptions. Attempt one short source-verified quotation per included source where appropriate and legally permitted; use genuine printed pages or section/paragraph locators. Record missing full text or unavailable quotable passages explicitly. Do not lower the count or omit extraction columns solely because the prompt is short.

State the proposed scope briefly and proceed if workable. A broad evidence map may cover the named field; ask only where ambiguity materially changes eligibility. For example, AI in higher education can be mapped across teaching, learning, assessment and institutional adoption without forcing the user to select a single subtopic. This is a structured evidence map, not automatically a formal systematic review.

## Named preset: AI in Higher Education

Use for equivalent topic-only requests in English, Kazakh or Russian unless the user supplies different settings. This preset captures the requested detailed workbook; do not apply its subject or Kazakhstan layer to unrelated reviews.

- Product: XLSX with at least 50 eligible sources, fully analyzed where accessible; shortfalls explicit. A prior 51-row file is a format/depth example, not a source set to recycle or a fixed count of 51.
- Period: latest six calendar years, search-date cutoff. In 2026 this means 1 January 2021 through the actual search date, with 2026 labeled partial. Recompute in later years; historical landmarks are supplementary unless criteria allow them.
- Scope: AI in university teaching, learning, assessment and institutional adoption; separate generative AI from other AI where useful.
- Sources: prioritize verified Scopus-indexed scholarship plus a separately labeled Kazakhstan ККСОН/КОКСН layer. Verify the relevant official listing and coverage date; user spelling “ККсон” maps to that verification task. Core papers may qualify through either required source layer; they do not need both indexes. If fewer than 50 qualify, continue feasible retrieval and state the shortfall. Unverified supplements never count toward the verified minimum.
- In the audit contract, required_indexes is conjunctive (all listed indexes required per record). For this either/or preset, leave that list empty and record an explicit index_policy with operator any_of and indexes Scopus/ККСОН/КОКСН; manually verify every core record meets one accepted route. The script does not enforce this any_of policy. Record that manual check in QA; never claim the script validated it.
- Analysis per source: main findings, theses/arguments, novelty, research question, methods, sample/data, limitations, author versus reviewer concerns, relevance and applicability.
- Group by theme, stance, similarities, contradictions and neutral analytical position; distinguish neutral position from non-significant/mixed results.
- Reading order within eligible directly relevant journal evidence: verified journal h-index descending, then article citation count descending. Keep separate relevance and citation-count views, metric provider/date/year and missing-value status. New relevant or local evidence remains visible even with missing metrics. Never equate this ordering with methodological validity.
- Quotations: attempt a short original-language quotation for every core source, in quotation marks, with verified page or honest alternative locator and APA 7 citation. Keep translations separate. Missing quotations remain explicit rather than invented.
- Final handoff: editable workbook, coverage/verification summary, remaining professor decisions; no ready-to-submit chapter.

A short request should therefore produce the same kind of analytical workbook as AI_Higher_Education_2021-2026_51_articles.xlsx, subject to actual retrieval and verification. Do not promise identical articles, counts, metrics or results, and do not claim success before the new file exists and has been checked.
