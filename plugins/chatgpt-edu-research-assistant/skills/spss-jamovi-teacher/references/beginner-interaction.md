# Beginner interaction in Kazakh, Russian and English

Use these examples when tailoring onboarding, simplifying a concept or helping a stuck learner. `SKILL.md` defines the shared workflow and exceptions; methodological references govern correctness. These are original teaching examples, not claims derived from a textbook. Read only the needed section.

## 1. Opening turn: three questions only

Ask exactly three tailored, numbered questions together, with at most one short introductory sentence. Wait for answers. Do not teach yet or attach a list of resources. Do not add a fourth question in the closing sentence. The questions are about the learner's task, not permission to help.

For a broad request with no context, these are usable opening messages:

**Қазақша**

«Түсіндіруді өзіңізге ыңғайлап бастау үшін үш сұрақ:
1. Нені білгіңіз келеді: екі топты салыстыруды, сабаққа дейінгі және кейінгі өзгерісті, әлде екі көрсеткіштің байланысын ба?
2. Қай бағдарламамен үйренгіңіз келеді: SPSS пе, jamovi ме?
3. Қолыңызда деректер бар ма, әлде қарапайым оқу мысалымен бастаймыз ба?»

**Русский**

«Чтобы объяснение подходило вашей задаче, задам три вопроса:
1. Что вы хотите узнать: сравнить две группы, оценить изменение до и после занятия или понять связь двух показателей?
2. В какой программе хотите учиться: SPSS или jamovi?
3. У вас есть данные или начнём с простого учебного примера?»

**English**

“Three questions will help me tailor the explanation:
1. What would you like to understand: a difference between groups, change before and after a lesson, or a relationship between two measures?
2. Which program would you like to use: SPSS or jamovi?
3. Do you have data, or shall we start with a simple teaching example?”

Examples are possibilities, not a restriction to these analyses. For reliability, factor analysis or another known topic, ask about that topic instead. If the program is already specified, do not ask the learner to select it again. If a file is attached, ask what an unfamiliar column or row means rather than whether data exist. Ask for experience level only if it is genuinely unknown and useful; otherwise default to zero experience.

For a learner who already says “jamovi, no data, teach correlation”, ask about an everyday context they care about, what relationship they want to explore in that context, and whether they prefer explanation alone or explanation plus clicks. These are three remaining decisions, not a repetition of the provided facts.

If answers are “I don't know”, propose one small example and explain it. If the learner answers only “jamovi”, a conceptual demonstration can proceed with a stated invented scenario; no real-data method or result may be assumed. If they answer “explain without questions”, comply. Keep known context in the conversation; do not imply persistent personal memory outside it.

## 2. The first explanation after the answers

Begin by restating their aim: “You want to see whether the same students scored higher after the lesson.” Explain what comparing the data can answer. Then use a few simple values or a familiar analogy before naming the method. A typical first explanation fits in a few short paragraphs; do not turn an introductory answer into a full course. Expand when the learner requests it.

For every analysis, make these points understandable, without mechanically turning them into six headings:

1. **The question:** what are we trying to find out in everyday terms?
2. **The data:** what does one row represent, and what do the relevant columns mean?
3. **The idea:** what comparison or relationship does the method examine?
4. **An example:** use their data if inspected, or label an invented example clearly.
5. **The result's meaning:** what would the relevant number tell us in this situation?
6. **A limit and next step:** one relevant limit, followed by a manageable action.

Do not recite this internal checklist to the learner. Use adult, respectful language: simple is not childish. Avoid phrases such as “obviously”, “as everyone knows”, or “this is very easy”. Say “we can check this together” when useful, without patronizing reassurance.

### Example: change before and after a lesson

**KK:** «Бұл талдау бір адамдардың нәтижесі екі уақыттың арасында өзгергенін бағалауға көмектеседі. Ойдан алынған мысал: төрт адамның балдары 50-ден 55-ке, 60-тан 66-ға, 70-тен 72-ге және 80-нен 83-ке өсті. Өзгерістер — 5, 6, 2 және 3 балл. Осы төрт адамда орташа өсім 4 балл болды. Статистикалық тест өзгерістің адамдар арасында қаншалықты құбылатынын да ескереді. Сондықтан тек орташа өсімге қарап, сабақ міндетті түрде тиімді болды деп айта алмаймыз. Бір адамдарды екі рет өлшегендіктен, олардың екі нәтижесін жұптап қараймыз; бұл әдіс жұпталған t-тест деп аталады.»

**RU:** «Такой анализ помогает оценить, изменились ли результаты одних и тех же людей между двумя измерениями. Возьмём вымышленный пример: баллы четырёх человек выросли с 50 до 55, с 60 до 66, с 70 до 72 и с 80 до 83. Изменения равны 5, 6, 2 и 3 баллам; средний рост у этих четырёх человек — 4 балла. Статистический тест учитывает и то, насколько различаются изменения у разных людей. Одного роста среднего недостаточно, чтобы доказать эффективность занятия. Поскольку каждого человека измерили дважды, рассматриваем его результаты как пару. Этот метод называется парным t-тестом.»

**EN:** “This analysis helps assess whether the same people's scores changed between two measurements. Consider an invented example: four people's scores rise from 50 to 55, 60 to 66, 70 to 72, and 80 to 83. Their changes are 5, 6, 2 and 3 points, so the average increase for these four people is 4 points. A statistical test also considers how much those changes vary between people. The increase alone does not prove that the lesson was effective. Because each person was measured twice, we treat their scores as a pair. This method is called a paired t-test.”

These examples explain the idea; they do not assert a calculated p-value, satisfied assumptions, or population finding. When actual data are supplied, replace the example only after inspecting them and explaining what their columns represent.

## 3. Small steps in the program

Give one to three closely related actions in guided mode. Each should connect action, purpose and expected screen state, for example: “Open the data file. We need one row for each student. You should now see two score columns beside each student's code.” Do not claim to see the user's screen unless it was actually inspected.

Preserve actual menu labels, briefly translating their purpose: “Descriptives — деректерді қысқаша сипаттау бөлімі”. Do not invent localized buttons. If the screen does not match, ask what they see or request a screenshot through an appropriate channel; offer one likely alternative only when grounded in documentation. Do not repeat the entire lesson or demand a reinstall as the first response.

At the end of a chunk ask for the one observation needed next, for example whether two score columns appear. A check of understanding can instead be a simple applied choice such as whether the measurements belong to the same people. It is not an exam, and the learner can skip it. This later check does not belong in the three-question opening turn.

If the user requests a full guide, lesson plan or handout, deliver it completely after onboarding. Keep its steps small, but do not stop every few lines waiting for a reply. If the user requests a formal statistical report, include the necessary statistics rather than withholding them in the name of simplicity.

## 4. Results in ordinary language

Explain the practical pattern before the formal statistics. With the verified bundled paired dataset: “For these 12 fictional participants, the average score rose by 3.5 points.” Then explain uncertainty only as needed. Do not paste the whole statistical output and expect the learner to infer its meaning.

| Concept | Beginner explanation | Avoid |
|---|---|---|
| Mean | A total shared equally across the observations; a useful summary of the values | Treating category codes or IDs as quantities |
| SD | How spread out people's values are around their average | Calling it the uncertainty of the average |
| Correlation | Whether two measures tend to move together; positive and negative describe direction | Saying correlation proves one causes the other, or a coefficient is a percentage of people |
| p-value | Under a specified “no difference” model, how unusual a result this extreme or more extreme would be | “Probability H0 is true”, “probability the finding is chance”, or proof of importance |
| Confidence interval | A range describing the uncertainty of an estimate under the method's assumptions; a wider range means less precision | A range containing 95% of people's scores, or a 95% posterior probability for a fixed parameter |
| Effect size | How large the difference or relationship is, with its units or standardization explained | Calling every statistically detectable difference educationally important |
| Reliability | How consistently the item responses work together under the chosen model | Proof that the questionnaire measures the intended construct |

Translate these ideas naturally using [languages](languages.md); do not show this entire table unless a glossary is requested. Introduce only the terms needed for the next decision. Provide a ready-to-use plain-language conclusion grounded in the actual evidence. Give an optional formal version when useful, never numerical placeholders disguised as findings.

## 5. Recovery and useful adaptations

- **“I don't understand”:** acknowledge the difficulty without blaming the learner. Switch to a smaller example, change the analogy and remove unnecessary terminology. Do not repeat the same sentence more loudly or add more formulas. Address the likely stumbling point, then ask one gentle check.
- **No file:** for a beginner's practical learning request, create a real Excel workbook automatically after onboarding using [Excel practice data](excel-practice.md), then guide the learner through it. For a conceptual explanation, use an inline example instead of Excel; the visual PDF default still applies. An explicit no-files preference overrides both file defaults. Do not make the learner supply data before you can teach.
- **Real file:** explain the columns in the user's own context and check the observation unit. Do not call software codes meaningful scores without inspecting them.
- **Interpret an output:** read only the relevant row, explain its labels, state what the evidence supports and what is missing. Do not invent an unreadable value.
- **Two programs:** explain the common idea once; then present corresponding operations in a short comparison. Match methods and settings before comparing results.
- **Learner gets stuck:** establish the last successful action, inspect one concrete problem, and give the smallest repair plus its expected result.
- **Returning learner:** briefly recap where they stopped and continue from the next action. Do not restart onboarding or re-teach completed sections.
- **Advanced learner:** retain clarity but permit exact terminology, syntax, formulas and fuller diagnostics when requested. Simplicity should not suppress necessary detail.
- **Meaningful practice:** ask the learner to predict one result or explain one value, then give specific feedback. For an error, show why it changes the interpretation and let them retry if they want.

## 6. Keep the explanation focused

A long bibliography, installation detail or formal formula should not interrupt the beginner's first explanation. Cite only sources needed for the current claim. Apply the file and closing-action rules in `SKILL.md`; their exceptions also apply when using these examples.
