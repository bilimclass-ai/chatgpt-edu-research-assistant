# IBM SPSS Statistics teaching workflow

Start from B4 for orientation and B1 for reproducibility; use current official documentation for uncertain commands or interface differences. The verified mapping in W7 covers independent t-tests; W8 covers missing treatment. Menu labels below are English labels in documented desktop workflows, not a promise of an identical menu in every release.

## Navigation anchors

| Task | Usual path / approach | What to explain |
|---|---|---|
| Define variables | Data Editor → Variable View | Name, type, label, Values, Missing, Measure are different properties |
| Frequencies | Analyze → Descriptive Statistics → Frequencies | Frequencies and valid percentages; suppress huge continuous-value tables |
| Distribution diagnostics | Analyze → Descriptive Statistics → Explore | Dependent List, Factor List when relevant, plots and group-specific results |
| Independent means | Analyze → Compare Means → Independent-Samples T Test | Outcome in Test Variable(s); Grouping Variable; Define Groups with actual codes |
| Paired means | Analyze → Compare Means → Paired-Samples T Test | Put matched measures in the intended order; report that direction |
| One-way means | Analyze → Compare Means → One-Way ANOVA | Factor/outcome, Welch if appropriate, comparisons and diagnostics |
| Correlation | Analyze → Correlate → Bivariate | Pearson/Spearman; tails and missing-data rule |
| Cross-tabulation | Analyze → Descriptive Statistics → Crosstabs | Row/column role, observed and expected counts, percentage denominator |
| Linear regression | Analyze → Regression → Linear | Outcome/predictors, coding, coefficient CIs and residual diagnostics |
| Reliability | Analyze → Scale → Reliability Analysis | Item columns, score direction, model and missingness |
| Recode/compute | Transform → Recode into Different Variables / Compute Variable | Preserve raw values; check new-variable distribution |

Some releases rename the Compare Means menu. If the learner cannot find it, verify version or inspect their interface, rather than claiming the installation is faulty. Exact tests, advanced models and extension procedures can depend on edition/licensing; verify instead of promising availability.

## Syntax as a learning bridge

Use **Paste** from an analysis dialog to generate syntax for that installed version. Explain the variable list, slash subcommands and terminating period. Have the learner run it and compare it with their original output. Saving a syntax file alone does not run it.

Prefer minimal, task-specific commands over a large boilerplate script. An independent comparison for a confirmed fresh dataset with numeric groups 1 and 2 might be:

```spss
T-TEST GROUPS=group(1 2)
 /VARIABLES=score
 /MISSING=ANALYSIS
 /CRITERIA=CI(.95).
```

Teach the distinction between the pooled-variance and unequal-variance rows and state which answers the selected analysis. Do not implement a mechanical Levene p-value gate. Use confirmed group codes, not the displayed text labels if the variable is numeric.

For the bundled practice, [paired-workshop.sps](../assets/paired-workshop.sps) constructs its own synthetic data and requests `post WITH pre (PAIRED)`. Its commands have been reviewed against documentation; native SPSS execution has not been claimed. Use the independently calculated [key](../assets/paired-answer-key.json) to check actual output.

For SPSS scoring teach `MISSING VALUES`, `RECODE`, `COMPUTE`, and the minimum-valid-value suffix only as relevant. For automation progress to `DO IF`/`DO REPEAT`, validated joins and reshaping, then OMS or Python integration if requested. B1's SPSS 15 and legacy Python examples are conceptual references, not current executable environment instructions. Avoid unnecessary `EXECUTE` after every transformation; understand when a procedure reads pending transformations (B1).

## Troubleshooting by evidence

- Empty group: inspect actual values, variable type, missing definitions, filters and group codes.
- Wrong sample size: reconcile per-analysis/listwise missingness, active filtering, weights, split state and complete pairs.
- Reversed sign: check pair/group order before changing any data.
- Huge score mean: check untreated missing codes, decimal import, units and reverse scoring.
- Syntax error: inspect the exact error, preceding command terminator, variable name, file path and version-dependent option. Repair a copy and re-run the smallest affected section.
- Different results from jamovi: use the parameter-matching checklist in [jamovi](jamovi.md); a display rounding difference is not an algorithm failure.
