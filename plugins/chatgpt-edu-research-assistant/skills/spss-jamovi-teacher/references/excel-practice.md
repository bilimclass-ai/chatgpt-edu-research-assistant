# Excel data for beginner practice

After the three initial questions and the learner's reply, a beginner asking “teach me” practical SPSS/jamovi analysis should receive an actual downloadable `.xlsx` when no suitable data are available. This also applies to equivalent requests in Kazakh and Russian. Do not ask a fourth question just for permission to create it. If the learner supplies suitable data, use those; respect requests for theory only, no files or another format.

## Choose and reuse a small appropriate dataset

- For a first lesson without a chosen analysis, start with descriptive statistics on the bundled [paired dataset](../assets/paired-workshop.csv); use the same file later for change before/after. Its 12 rows and [checked key](../assets/paired-answer-key.json) reduce repeated generation and calculation.
- For missing codes, reverse scoring and questionnaire preparation, use the bundled [scoring dataset](../assets/jamovi-scoring.csv) with its [key](../assets/jamovi-scoring-key.json). It teaches scoring, not validation or factor structure.
- For another selected method, create suitable synthetic data: independent groups require distinct people and a group column; paired analysis needs matched measurements in the same row; correlation needs two meaningfully related varying measures; ANOVA needs the selected groups. Usually a few dozen rows suffice for a basic mechanics lesson, but this is not a sample-size recommendation for real research. Advanced models need an appropriate larger example and a checked specification.
- Do not generate zero-variance columns, perfectly correlated outcomes or artificially identical group values unless that problem is the lesson. Do not reroll data to force significance. Record the seed if random generation is used. Preserve existing files and use a new output name for changed data.

## Workbook contract

Use available spreadsheet/file-authoring tools to create genuine Excel content, never a renamed CSV or a promise to create it. Follow applicable spreadsheet tooling instructions in the environment. A simple workbook is sufficient:

1. `Data`: the first sheet, containing one header row and one observation per row; short stable identifiers such as `id`, `group`, `pre`, `post`; numeric values stored as numbers. No merged cells, titles above headers, totals, blank separator rows or explanatory text within the data range.
2. `Guide`: a brief explanation in the selected language, explicit “synthetic training data” notice, variable meanings, units, category/missing codes, row count and intended analysis. State which sheet to import. Include a simple task, not a whole textbook.

Use readable widths, a styled header and a frozen header row. Keep computed values as actual values in the import sheet; Excel formula caches must not be required for SPSS/jamovi to receive the data. No macros or external links. For ordinary lessons use clean complete values; introduce missingness deliberately only when relevant. Keep teacher answers separate from learner instructions when an independent exercise is requested.

## Verify and deliver

Reopen the saved workbook and check sheet names, headers, number types, row count, unique IDs at the intended unit, legal ranges, group membership or pair matching, and missing-value definitions. Check a few descriptive values against the existing key or independent calculations. Follow the applicable spreadsheet skill's formatting verification. Do not claim native SPSS/jamovi execution merely because the Excel file was verified.

Attach a link, explain the learning question in simple language, and give the first one to three actions using actual sheet and column names. Reuse the same workbook throughout the lesson rather than recreating it every turn. Do not dump all rows into chat. If file creation is genuinely unavailable, state that limit and supply a small copyable table as a fallback without claiming it is an Excel attachment.
