# Data preparation and reproducibility

Source anchors: B1 (raw protection, matching and duplicates), B2 (layout), B4 (variables, missing values and syntax), W1–W3 and W8–W10. See [source register](sources.md).

## Inspect before transforming

Create or inspect a dictionary with: variable identifier, teaching label, construct/role, type, measurement level, unit, legal values/value labels, missing code, and derivation. An ID may be stored numerically but should not be analysed as a continuous outcome.

Confirm what one row represents. Wide paired data usually place one participant per row with separate `pre` and `post` columns. Long data place occasion records in separate rows and require an ID and time/condition variable. A repeated ID in long data is not necessarily a duplicate. Verify join-key uniqueness at the intended unit before combining files; check matched, unmatched and resulting row counts. Never pair pre and post observations by row position unless their matching is established.

On import check encoding (especially Kazakh/Russian labels), delimiters, decimal separators, headers, numeric columns read as text, date representation, value labels and leading zeros in IDs. CSV does not retain the full SPSS/jamovi dictionary or analyses. Reinspect after moving `.sav` into jamovi; do not assume every property or analysis transfers.

## Missing and invalid values

In SPSS, distinguish numeric system-missing from explicitly defined user-missing codes; in jamovi, define missing codes in the variable editor. A code such as 99 or -99 remains a real value until handled as missing. Keep separate meanings such as “not applicable” in the dictionary where useful; a real zero is not missing.

Report missing counts by variable and the analysis-specific n. For a paired test exclude incomplete pairs from that test, not an arbitrary observation from the other column. Diagnose unexpected n through active filters, weights, split files, missing definitions and group coding.

Correct an invalid entry only with evidence. Otherwise flag it and document treatment. Explore outliers in context; a boxplot point is not an automatic deletion rule. Retain the raw value and distinguish correction from analytical exclusion.

## Questionnaire scoring

Read the instrument's actual scoring instructions. For a 1–5 item whose meaning is reversed, `6 - item` reverses direction after missing and invalid codes are handled. The general bounded-scale transform is `minimum + maximum - value`; keep a new variable. Do not reverse an already reversed item a second time.

Define the minimum answered-item rule from the instrument or explicitly label it an illustrative teaching decision. In SPSS `MEAN.3(q1,q2,q3r,q4)` requires at least three nonmissing values (W9). A plain arithmetic average and a missing-aware mean can return different results. In jamovi, verify the available formula's missing-value behavior and any minimum-count expression using rows with all, partial and no responses. Do not assume the SPSS dot-suffix syntax works in jamovi.

Reliability analysis uses item columns, not only the final total. Verify directions and missingness first, then consider alpha/omega and item-rest results in the context of dimensionality and the intended score.

The jamovi [scoring practical](jamovi-scoring-practical.md) provides missing-code and reverse-scoring edge cases with an independently checked answer key. It uses an explicit complete-item rule for teaching; it does not prescribe this rule for validated instruments. For reusable transformations and row versus column functions, see [jamovi](jamovi.md).

## State and deliverables

Work from a protected raw file into a separately named working copy. Record changes in syntax or in the jamovi project and a brief transformation note. Inspect filters, weights and split status on real user data; do not silently turn off a scientifically intended weight or design feature. Reset such state only for a fresh unweighted teaching dataset or when the selected analysis requires an explained change.

For SPSS retain `.sav` data, `.sps` syntax and `.spv` output when produced by the software. For jamovi retain `.omv` with analyses; `.omt` can distribute a template without observations (W10). An exported PDF/table communicates results but does not replace the reproducible analysis. Save actual software/module versions and data provenance; do not guess them.

The bundled [synthetic CSV](../assets/paired-workshop.csv), [SPSS example](../assets/paired-workshop.sps) and [answer key](../assets/paired-answer-key.json) support the [paired practical](paired-practical.md). They are original training materials, not student records or copied book datasets.
