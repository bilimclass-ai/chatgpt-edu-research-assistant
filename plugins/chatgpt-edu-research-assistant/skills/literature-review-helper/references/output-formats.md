# Evidence workbench and professor handoff

## Standard workbook

Use stable IDs across sheets, readable wrapped text, filters and frozen identifiers. Localize headers; preserve original source titles/quotations. Do not force everything into a single very wide matrix: split related fields while keeping IDs visible. Scale tabs to the request; the following are roles, not mandatory empty sheets.

| Sheet / role | Contents |
|---|---|
| Start here | Scope, period, version, requested/core/full-text/quote counts, main unresolved issues, how to sort/filter |
| Evidence | ID, question, concept/theory, relevance and rationale, context, design, sample/data, methods/instruments, findings, novelty, separate author/reviewer limitations, applicability |
| Claims and quotes | Candidate paraphrased claim, supporting/counterevidence IDs and locators; exact quote in quotation marks, translation separately, printed/PDF page, section, version and quote-specific citation |
| Compare | Themes, similar results, contradictory results, neutral analytical stances, null/mixed/untested results, comparability explanation and unresolved question |
| Reading priorities | Relevance-based reading list; separate citation count and journal-metric views with provenance; foundational/recent/local strata where useful |
| Bibliography | Verified style reference, DOI/other identifier, publisher/repository URL, index verification level and date |
| Search and screening | Exact search log, exclusions/reasons, deduplication and study-family links, waiting full texts |
| QA and handoff | Verification status, shortfalls, disputed extractions, professor review queue, run manifest |

If requested, export bibliography to RIS/BibTeX/CSL JSON and evidence to CSV/JSON. Use a citation format only if its syntax is actually checked. Preserve full metadata and Unicode. Referencing scripts with empty output is not delivery. For the structured audit bundle use `record-schema.json`; it defines the validator contract and leaves domain-specific data extensible.

## Ranking without prestige bias

Eligibility first. Relevance is a reasoned category—direct, partial, background—with a short explanation tied to the actual question. Keep methodological confidence distinct and use appropriate design judgments, not a universal invented numeric quality score.

Record every bibliometric value with metric name, provider, observation date, metric year/category when applicable, entity (work or venue), source URL and verification state. Do not mix article citations with journal h, author h, impact factor, CiteScore, SJR or quartile. Missing is null/not available, never zero. A genuine zero requires an observed value from the named provider.

Default: direct relevance and suitability, then a selectable citation count view within comparable evidence strata. Offer a separate journal-metric view. If the user asks for journal h then citations, implement that order explicitly and disclose that it is a bibliometric ordering, not a validity ranking. Never silently substitute OpenAlex for Scopus or SCImago. Offer the available alternative and label it; a mandatory Scopus metric remains unresolved until verified.

Citation counts depend on database coverage, field and age; new but directly relevant studies must remain visible. Any citations-per-year value is a labeled approximation with an explicit denominator. Do not invent a composite relevance/citation/journal score unless the user requests and agrees to a transparent weighting scheme. Do not compare quartiles without category/year; books, conferences and journals need their own appropriate standing indicators.

## Brief handoff, not a ghostwritten chapter

Provide a short research memo with:

- strongest defensible findings and their boundaries, using linked IDs/citations;
- major disagreements and whether they are genuine or reflect different methods/context;
- candidate gaps with search-bounded language and possible research directions;
- a chapter outline using headings/questions/bullets, not ready prose;
- a prioritized professor queue: verify pivotal sources, adjudicate disputed judgments, choose theoretical framing, interpret context and write.

Useful reusable claims are evidence-linked propositions, not claims of originality or publication readiness. A professor may reject the model's interpretation. Do not imply that only proofreading remains or that scholarly judgment can be reduced to a final 20% mechanically.

## Completion and updates

Report exactly what met the request. For “at least 50 Scopus/KKSON sources,” 48 qualifying sources plus 3 unverified supplements is a shortfall, not success. Keep the supplements useful but separate. Continue feasible retrieval; if access blocks completion, deliver the verified work and name the remaining requirement plainly.

Store a manifest: skill version, scope revision, date, actual tools/providers, eligible count, independent study count if known, access limitations and validation results. On update retain stable IDs, add newly found works, mark changed/retracted records and revisit affected claims. Do not claim exhaustive coverage without a defensible method.
