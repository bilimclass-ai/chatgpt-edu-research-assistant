# Method selection and interpretation

This is a decision aid, not an automatic test selector. First establish the target quantity, outcome type, observational unit, sampling/design, number of conditions, dependence, missingness, and whether the analysis was planned. Sources: B2–B4, W4–W6, W11–W15 in [sources](sources.md). The cautions below reconcile older teaching examples with current statistical reasoning.

| Question/design | Candidate | Checks and interpretation |
|---|---|---|
| Describe a categorical variable | Counts, percentages, bar chart | State denominator and missing count; numeric category codes are not quantities |
| Describe a quantitative variable | Mean/SD and/or median/IQR; histogram, boxplot | Distribution, outliers, range, units; plots do not prove assumptions |
| One mean versus a planned reference | One-sample t-test | Independent units, meaningful scale and distribution/outliers; give mean difference and CI |
| Two independent group means | Welch t-test is often a useful starting choice; pooled Student test if justified | Independence, group-specific distributions, precision; identify which SPSS row/jamovi option is used. Do not let a nonsignificant Levene test prove equality |
| Two measurements of the same units | Paired t-test | Correct ID matching, complete pairs, distribution of differences rather than two separate normality tests; give direction and paired n |
| Two independent ordinal/distributional outcomes | Mann–Whitney rank-sum | Independence, ties, distribution shapes; not generically a test of medians. A location/median interpretation needs additional assumptions |
| Paired rank-based comparison | Wilcoxon signed-rank | Differences, ties/zeros, symmetry for a location interpretation; it does not test exactly the same hypothesis as a paired mean test |
| More than two independent means | One-way ANOVA or Welch ANOVA | Residuals/group variability; planned contrasts or adjusted comparisons. Tukey corresponds to equal-variance analysis, Games–Howell to unequal variances |
| More than two independent rank/distribution comparisons | Kruskal–Wallis | Independent units, comparable outcome scale, ties and distributional interpretation; follow-up comparisons require an appropriate multiplicity adjustment |
| More than two repeated rank comparisons | Friedman test | Complete matched blocks/participants and an appropriate ordinal outcome; not an independent-groups test or a generic solution to missing repeated measures |
| More than two repeated conditions | Repeated-measures ANOVA or a justified mixed model | Subject dependence; sphericity where applicable, correction and corrected df; mixed-model covariance choices must also be justified |
| Several factors or adjustment | Factorial ANOVA / ANCOVA | Interactions, covariates, coding, model specification; do not reduce an interaction to isolated main-effect claims |
| Association of two quantitative variables | Pearson r for a linear relationship; Spearman for a monotonic rank relationship | Scatterplot, influential points, independence; neither implies causation or measures pre/post change |
| Association between categorical variables | Contingency table, chi-square or appropriate exact test | Counts rather than percentages as input; expected counts, independence, sparse cells; state continuity/exact settings. Paired binary data need a paired method such as McNemar |
| Continuous outcome with predictors | Linear regression | Functional form, residual pattern/variance, influence, collinearity, design; report B, CI, fit and units. Predictors themselves need not be normal |
| Binary outcome with predictors | Binary logistic regression | Event coding, reference group, separation/sparsity, continuous-predictor functional form; odds ratios are not risk ratios |
| Internal consistency of a multi-item measure | Alpha and, where appropriate, omega | Construct, item direction, missingness, dimensionality and model assumptions; neither establishes validity |
| Rater or repeated-measure agreement | Appropriate ICC / kappa | ICC model, single vs average measurement, agreement vs consistency, CI; kappa is sensitive to marginal distributions. Do not replace agreement with correlation |
| Explore latent constructs | EFA when justified | Distinguish common factor analysis from PCA; consider item types, extraction, factor retention, oblique rotation, sample adequacy and interpretability |

## Guardrails that change decisions

- A single Shapiro–Wilk result is not a method-selection algorithm. Small samples provide little diagnostic power; large samples detect small departures. Examine the appropriate distribution, outliers and design, then consider robustness and the estimand. A rank test is not automatically preferable for small n or uniformly less powerful.
- For paired inference, pairs may be internally dependent, but different participants should be independent unless the model handles clustering. Repeated observations or students within classes can require a multilevel/design-aware analysis. Do not count repeated rows as new independent participants.
- Sphericity concerns equality of variances of pairwise differences. Compound symmetry is sufficient but stronger; do not treat them as equivalent. With only two repeated levels, sphericity is automatic. When using Greenhouse–Geisser correction, report its corrected df and p rather than mixing corrected and uncorrected entries.
- Missingness can change the target population. Per-analysis deletion, listwise deletion and imputation are different choices. Do not invent universal missing-percent thresholds or automatically mean-impute. Describe the mechanism assumptions when discussing multiple imputation; lack of a detected pattern does not prove MCAR.
- Pre-specify the primary question and contrast where possible. For multiple outcomes/comparisons explain the selected adjustment or exploratory status. Do not recommend deleting cases, changing tails or trying many tests to obtain significance.
- A p-value is not the probability that H0 is true, the probability the result happened “by chance”, the effect magnitude, or the chance of replication. A large p does not demonstrate equivalence. Use a designed equivalence test with a justified margin if that is the research question. See W11.
- A frequentist 95% CI describes the long-run coverage of an interval procedure; do not claim a 95% posterior probability for the fixed parameter. Explain precision in ordinary language without changing this meaning.
- Use effect sizes with their definition: paired `d_z = mean(post-pre) / SD(post-pre)` differs from independent-group d and other paired standardizers. An independent Python/R check is not evidence that SPSS/jamovi uses the same standardizer. For ANOVA distinguish eta-squared, partial eta-squared and omega-squared. For contingency tables distinguish Cramér's V from odds/risk ratios.
- Reliability is not validity, and alpha ≥ .70 is not a universal pass mark. Reverse-code by item meaning, not merely to raise alpha; do not delete items solely for a higher coefficient. A single Likert item is ordinal; treating a defensible multi-item composite as quantitative requires an explicit rationale.

## Output reading order

Identify table/model and variables → check valid n and exclusions → identify descriptive pattern → check relevant diagnostics → identify estimate and CI → read test statistic, df and p → state effect definition → interpret within the design. Distinguish overall model tests from individual coefficients and omnibus effects from pairwise comparisons.

If there is no data or output, supply a proposed analysis and a report template, not numerical findings. If only part of an output is visible, state exactly which inference is supported and which needed values are missing.
