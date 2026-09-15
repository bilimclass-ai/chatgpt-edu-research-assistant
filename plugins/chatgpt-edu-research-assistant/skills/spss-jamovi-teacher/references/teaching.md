# Teaching lecturers and their students

## Adaptable teaching sequence

Follow the onboarding and teaching workflow in `SKILL.md`; consult [beginner interaction examples](beginner-interaction.md) only when needed. Teaching level defaults to no prior experience. The course map below is for selecting content internally; it is not the first response to a confused beginner.

For a concept question, use a short explanation and one example. For a workshop, move through research question → data structure → inspect/prepare → choose analysis → run → interpret → reproduce. Ask learners to predict a pattern before clicking. Avoid a long menu demonstration with no explanation of what is being estimated.

After onboarding, explain what the analysis means with the learner's own data or an explicitly invented example before giving software actions. For interactive tutoring give one to three related actions at a time, tell the learner what should become visible, and wait for their result when it determines the next action. For a requested complete handout, provide the complete handout without forcing an interactive conversation.

For a lesson include a measurable learning outcome, prerequisites, materials/data dictionary, teacher demonstration, guided practice, independent transfer task, and evidence of learning. Time allocations should add to the stated duration. Offer scaffolding through annotated outputs and a partially completed analysis, and extension through a design or diagnostic question. Do not mistake extra arithmetic for deeper learning.

## Optional learning progression

Use only the modules relevant to the requested course. These are original teaching design choices, not an official curriculum or a book's table of contents.

| Stage | Learning outcome | Demonstration or assessed evidence |
|---|---|---|
| 1. Orientation | Distinguish rows, variables, values, labels and measurement levels | Correct a small data dictionary; save and reopen work |
| 2. Preparation | Import correctly, identify missing codes and preserve raw data | Validate ranges and categories; explain every exclusion |
| 3. Description | Match summaries and graphs to variable types | Report n, mean/SD or median/IQR; explain a distribution |
| 4. Estimation | Distinguish SD, SE, CI and p | Explain uncertainty without claiming a probability for H0 |
| 5. Two-condition comparisons | Distinguish independent from paired observations | Complete the bundled paired practical; justify design |
| 6. More than two conditions | Distinguish one-way, factorial and repeated designs | Explain an omnibus test, contrasts, multiplicity and interaction |
| 7. Relationships | Distinguish correlation from change and regression from causation | Scatterplot, coefficients, CI, residual diagnostics |
| 8. Categorical data | Work with counts, proportions and expected counts | Cross-tabulation; chi-square or suitable exact procedure |
| 9. Questionnaires | Reverse-score and define a defensible scale score | Item-level missingness, alpha/omega with limits, scoring rule |
| 10. Reproducible project | Re-run a transparent analysis | Raw data, dictionary, transformation record, syntax/project, report |

Advanced extension on request: logistic regression, ANCOVA, mixed models, EFA, power planning, mediation or moderation. Verify software support and statistical requirements before giving an executable lesson. Do not automatically use stepwise selection, a fixed cases-per-predictor rule, or a sample-size threshold as a substitute for design reasoning.

For jamovi-specific course requests, use [jamovi learning modules](jamovi-learning-modules.md): the supplied books add a progression through graphics, recoding, model interpretation, psychometrics and Bayesian reasoning. Use [the scoring practical](jamovi-scoring-practical.md) when teachers need a second exercise beyond a t-test. Do not require completion of the entire book before answering a focused software question.

## Practical deliverables

For a software practical normally supply: a short scenario; variables and units; commands or menu actions; a learner task; one intentionally plausible misconception; a teacher key with checked numbers or explicitly qualitative expectations. Use [the practical](paired-practical.md) as a worked example, not a template that forces every task to be a t-test.

An adaptable 10-point rubric: correct design/method (2), data preparation (2), settings/reproducibility (2), numerical interpretation including uncertainty (2), limitations and clear communication (2). Change it to the teacher's criteria when provided. Grading should reward reasoning as well as correctly clicking the software.

For a classroom comparison, have learners match SPSS and jamovi by variables, valid n, test type, tail, group/pair order, missingness and CI level before comparing p-values. Differences can be legitimate consequences of settings; do not assert that either program is wrong solely because their outputs differ.
