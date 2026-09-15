# jamovi teaching workflow

Use official sources W1–W7, W10, W18–W24 and the uploaded jamovi books B5–B6 in [the source register](sources.md). Read [learning modules](jamovi-learning-modules.md) for a book-informed lesson or an advanced analysis, and [the scoring practical](jamovi-scoring-practical.md) for a ready exercise in Kazakh, Russian or English. jamovi is conventionally written in lowercase. Confirm version and installed modules when they affect the task. Do not claim a current module inventory from this static skill.

## Core operations

Open the dataset through the file menu. Double-click a variable header to inspect data type, measure type, levels and missing values. Explain that numeric storage and a continuous measurement level are different. Check imported types rather than trusting automatic inference. Data → Compute/Transform/Filters supports derived variables and selection; verify formula behavior, especially with missing values, before teaching a scoring rule (W2–W3).

For a documented independent t-test use Analyses → T-Tests → Independent Samples T-Test; place the outcome in Dependent Variables and the factor in Grouping Variable (W4). For paired data use Paired Samples T-Test and define a pair in the requested order (W5). Select required descriptives, mean-difference CI, diagnostics and effect-size options explicitly. A default option is not a methodological decision.

For one-way comparison locate ANOVA → One-Way ANOVA, place outcome(s) and group factor, and select the intended Welch or equal-variance procedure. Games–Howell and Tukey correspond to different variance assumptions; do not choose them simply because a checkbox is available (W6).

For other procedures navigate the Analyses categories (Exploration, Regression, Frequencies, Factor, and installed extensions) and verify the particular path in documentation or the learner's interface. Reliability options can include alpha, omega, item-rest statistics and reversed items (W12). Do not assign an item to a “reverse” list after reversing its data manually.

## Reproduce and compare

### Formula and transformation choices

Use a computed variable for a one-off expression such as `post - pre`; use a reusable transformation when several items need the same rule. In a transformation, `$source` refers to the selected original column. For a confirmed 1–5 reversed item use `6 - $source` after defining missing codes. Recode conditions use the first matching condition, so review their order and test boundary values. These operations are documented in W18–W19 and illustrated in B5 §6.3.3 and B6 §6.3.3.

Distinguish row functions such as `MEAN(q1,q2)` from whole-column functions such as `VMEAN(q1)` (W20). A column mean repeated down the sheet is not a participant's scale score. Do not silently convert a continuous variable to categories just to simplify an analysis; keep the original values and justify cut points. For missing-data scoring use [the practical](jamovi-scoring-practical.md), whose complete-item rule is explicit and testable.

### Project and analysis record

Save data and analyses in `.omv`. For repeatable teaching setups, `.omt` templates can be useful; imported data must still be checked (W10). Copy/export tables and plots for a report, retaining the project for reproduction.

R Syntax Mode displays R code for analyses; it does not run SPSS `.sps` syntax and does not include the data-import step. Rj is a separate module for running R; its current dataset is exposed as `data` (W3). Use those tools when requested or helpful for reproducibility, not as a prerequisite for a beginner GUI lesson.

For a native comparison align:

1. Dataset contents, excluded rows, missing definitions and valid n.
2. Variable types, factor levels/reference category, grouping and pair direction.
3. Test family and variant: pooled/Welch, Pearson/Spearman, one/two-sided.
4. CI level, effect-size standardizer and multiple-comparison correction.
5. Weights/design, exact vs asymptotic settings, continuity corrections and model coding.

Compare numerical values to an appropriate rounding tolerance; inspect differences before declaring equivalence. Where software requires an extension, verify name, source and version and explain that dependency. Do not invent a built-in menu for mediation, multilevel models or other advanced analysis.

## Frequent learner problems

If an analysis rejects a variable, inspect its measurement and data types and whether a grouping variable has the required number of nonmissing levels. If output changes after editing data, confirm that the change was intended; live recalculation is normal. If results disappear, inspect filters and valid cases. If a shared file cannot reproduce an extension analysis, compare installed modules and versions, especially when using System R.
