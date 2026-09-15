# Book-informed jamovi learning modules

Use these modules selectively in the user's teaching language. B5 (2025) and B6 (0.75, 2022 preface) are two editions of the same textbook. Their section structure is useful for learning, but screenshots, pagination and defaults can differ. Sources and inspected page locators are in [sources](sources.md). The route and tasks below are an original teaching synthesis, not copied book exercises.

## Route from first use to independent interpretation

| Module | What the lecturer should be able to teach | Learner evidence | Reading anchor |
|---|---|---|---|
| Orientation and design | Rows, variables, outcomes, measurement and observational units; import and save | Explain why numeric participant codes are not outcomes | B5/B6 chapters 2–3; W2 |
| Description and graphics | Match mean/SD or median/IQR to the question; inspect histograms, boxplots and scatterplots | Explain a plot before interpreting a test | B5/B6 chapters 4–5; existing methods guide |
| Preparation | Computed versus transformed variables, ordered recodes, missing codes, filters | A dictionary and correctly derived score with missing cases retained | Inspected §6.3.3 in B5/B6; W18–W20 |
| Estimation and comparisons | Sampling uncertainty, CI, paired versus independent tests and ANOVA | The bundled paired practical plus an explanation of test choice | B5/B6 chapters 8–11 and 13; W4–W6 |
| Correlation and models | Association, multiple regression, adjusted coefficients and diagnostics | State the meaning and units of a coefficient; avoid causal overclaim | B5/B6 chapter 12; W24; methods guide |
| Questionnaires | Distinguish item scoring, reliability, EFA/PCA and CFA | Scoring practical; a justified analysis plan for a larger instrument dataset | Inspected B5 §§15.1.3, 15.5.1 and B6 §15.5.1; W12, W23 |
| Bayesian introduction | Distinguish Bayes factors, prior odds and posterior odds | Interpret a specified BF direction and identify required assumptions | Inspected B5/B6 §16.2.2; W22 |

Chapter-level reading anchors are a navigation map, not a claim that every chapter was inspected or that all its examples were run. To teach a particular book exercise, fetch that exercise and its actual data first. The author's website provides routes to data; confirm the file and installed data-library module rather than inventing a module name or silently substituting a similar dataset.

## Correlation and regression lesson decisions

In jamovi's Correlation Matrix choose the intended coefficient explicitly and request n, CI and plots when available. Compare scatterplot shape with the coefficient. Pearson r near zero need not mean there is no nonlinear relationship. When different correlations use different complete pairs, report their respective n. W24 documents options; its simplified claim about zero correlation must not become a general independence claim.

For linear regression place a quantitative outcome in the dependent field and distinguish quantitative covariates from categorical factors. Verify the selected version's dialog. Model terms, interactions and reference categories determine the coefficient interpretation. Inspect residuals, influence and collinearity; use B values and their CI in context, not a ranked list of p-values. Do not standardize or categorize solely to make significance appear.

## Reliability and factor analysis

Use Analyses → Factor → Reliability Analysis for appropriately coded item columns, selecting alpha/omega and item-rest statistics according to the learning objective. Report n and the missing-data treatment. In the teaching example, use already reversed `q3r`; do not additionally mark it reversed in the analysis. Explain that a negative alpha can reveal a scoring error or incompatible items; investigate before removing items.

Omega is model-dependent, not assumption-free. Do not automatically describe `1 - alpha` or `1 - omega` as an exact fraction of measurement error without a justified measurement model. A high coefficient does not prove a single factor, content coverage or validity. These qualifications refine the introductory discussion at B5 PDF 424 and B6 PDF 486.

Before EFA ask whether the aim is latent-variable exploration or data reduction. EFA and PCA are different. In Factor → Exploratory Factor Analysis, identify item columns and choose retention, extraction and rotation explicitly; W23 documents parallel analysis and rotation options. Evaluate scree/parallel evidence together with interpretability; KMO and Bartlett results are diagnostics rather than a guarantee of a good factor model. With correlated constructs an oblique rotation is often reasonable. Hiding small displayed loadings does not set them to zero or remove items.

Ordinal item coding deserves methodological attention; changing the measure label to Continuous does not itself justify treating categories as interval data. Verify the correlation matrix/estimator the procedure actually uses. Do not assume every version's base EFA supports polychoric correlations. For CFA, start from a specified model and check estimator, identification, fit and substantive plausibility; exploratory model revisions on the same data are not independent confirmation. Verify the required procedure or module before giving executable instructions.

Use a suitably sized, appropriate dataset for real factor work. The eight-row scoring exercise is intentionally unsuitable for establishing factor structure or population reliability.

## Bayesian introduction without changing the user's analysis goal

Introduce Bayesian analysis only when requested or relevant to the lesson. State both models, whether the reported factor is BF10 or BF01, and the parameter priors. For a composite alternative the marginal likelihood depends on its parameter prior; a BF is not prior-free even though it separates out prior model odds.

For BF10 = 4, the data multiply H1-versus-H0 prior odds by four. Equal prior model odds imply posterior odds 4:1; different prior odds give a different posterior. This is not `p = .25`. BF01 is the reciprocal for the same model pair. Report the number rather than treating verbal evidence bands as universal rules. If a log BF is shown, identify the logarithm base and transform it before ordinary-ratio interpretation. A factor near one indicates little discrimination between the specified models, not that they are equally true in all circumstances.

For a Bayesian t-test verify the procedure, alternative, prior width and displayed BF direction in the current jamovi version; do not interpret a frequentist CI as a Bayesian credible interval. Record prior sensitivity when relevant. The introductory book discussion is not blanket permission for unrestricted optional stopping or post-hoc model searches.

## Three-language checks of understanding

- **KK:** «`MEAN(q1,q2)` мен `VMEAN(q1)` нені есептейді? Неге жоғары альфа валидтілікті дәлелдемейді? BF10 = 4 болса, априорлық ықтималдықсыз қандай қорытынды жасауға болады?»
- **RU:** «Что вычисляют `MEAN(q1,q2)` и `VMEAN(q1)`? Почему высокая альфа не доказывает валидность? Что можно сказать о BF10 = 4, не задав априорные вероятности моделей?»
- **EN:** “What do `MEAN(q1,q2)` and `VMEAN(q1)` compute? Why does high alpha not establish validity? What can BF10 = 4 tell us without specifying prior model probabilities?”

Teacher key: row mean versus column mean; internal consistency does not establish the intended interpretation of a measure; BF10 updates prior model odds by a factor of four but does not alone specify posterior model probabilities.
