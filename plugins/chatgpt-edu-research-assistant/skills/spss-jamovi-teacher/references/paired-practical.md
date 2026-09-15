# Paired-samples workshop in three languages

Use the section matching the learner's language. Shared resources: [original synthetic CSV](../assets/paired-workshop.csv), [SPSS syntax](../assets/paired-workshop.sps), [machine-readable answer key](../assets/paired-answer-key.json). The example was deliberately constructed for teaching and does not represent an empirical workshop evaluation. Its large standardized change is not a forecast of real teaching effectiveness.

## Қазақша: бір топтың сабаққа дейінгі және кейінгі нәтижелері

**Мақсат:** білім алушы жұпталған деректерді таниды, SPSS немесе jamovi-де жұпталған t-тестті орындайды және орташа айырманы сенімділік аралығымен түсіндіреді.

**Деңгейі мен ұзақтығы:** жаңадан бастаушылар, 60 минут. Арифметикалық орта туралы бастапқы түсінік қажет. Қажетті құралдар: таңдалған бағдарлама және оқу CSV файлы. Екі бағдарламаны бір сабақта толық қайталау керек болса, уақытты ұзартыңыз.

**Жағдаят:** 12 шартты қатысушының семинарға дейінгі және кейінгі тест балдары берілген. Бұл — оқыту үшін жасалған деректер. Зерттеу сұрағы: «Сол қатысушылардың орташа балы екі өлшем арасында өзгерді ме?»

| Айнымалы | Мағынасы | Дерек құрылымы |
|---|---|---|
| `id` | Шартты қатысушы коды | Бір жол — бір қатысушы; талданатын балл емес |
| `pre` | Семинарға дейінгі балл | 0–100, сандық |
| `post` | Семинардан кейінгі балл | 0–100, сандық |

**Сабақ барысы:** 0–5 минут — сұрақ пен болжам; 5–15 — деректерді ашып, түрлерін және 12 жолды тексеру; 15–25 — орта, SD және `post - pre` айырмаларын қарау; 25–40 — оқытушымен бірге тест; 40–52 — дербес түсіндіру; 52–60 — қысқа тексеру мен жұмысты сақтау.

**SPSS қадамдары:** CSV файлын ашып, `pre` және `post` айнымалыларын Scale ретінде тексеріңіз. Analyze → Compare Means → Paired-Samples T Test терезесінде бірінші орынға `post`, екінші орынға `pre` қойыңыз; 95% сенімділік аралығын таңдаңыз. Paste арқылы синтаксисті сақтап, орындаңыз. Немесе бос оқу сессиясында берілген `.sps` мысалын қолданыңыз; онда деректер бар. Жұп айырмаларының таралуын да қарастырыңыз. Мәзір атауы нұсқаға қарай аздап өзгеруі мүмкін.

**jamovi қадамдары:** CSV файлын ашыңыз; `id` үшін ID, балдар үшін Continuous өлшем түрін таңдаңыз. Analyses → T-Tests → Paired Samples T-Test бөлімінде `post`, `pre` жұбын осы ретпен беріңіз. Student's paired test, екіжақты гипотеза, сипаттамалар, орташа айырма мен оның 95% CI көрсеткіштерін таңдаңыз; айырмалардың Q–Q графигін қараңыз. Қажет болса әсер мөлшерін қосып, оның анықтамасын тексеріңіз. Жобаны `.omv` түрінде сақтаңыз.

**Білім алушыға тапсырмалар:** Неге тәуелсіз t-тест жарамайды? Айырманың бағыты қандай? Орташа айырма мен CI нені көрсетеді? Егер бір `post` мәні жоқ болса, осы тестке неше жұп қалады? Нәтиже семинардың себептік әсерін дәлелдей ме?

**Оқытушының жауап кілті:** 12 толық жұп; `pre`: M = 63,50, SD = 8,98; `post`: M = 67,00, SD = 10,08. Орташа `post - pre` = 3,50 балл, 95% CI [2,58; 4,42]; t(11) = 8,38, p < 0,001; d_z = 2,42, мұнда бөлгіш — жұп айырмаларының SD мәні. Бір `post` мәні жетіспесе, 11 толық жұп қалады және нәтижелер қайта есептеледі. Бір адамның екі өлшемі байланысты. Бұл жасанды мысал семинардың тиімділігін дәлелдемейді; нақты бақылау тобы жоқ зерттеуде де себептік түсіндірме шектеулі болар еді.

## Русский: результаты одной группы до и после занятия

**Цель:** слушатель распознаёт парные данные, выполняет парный t-тест в SPSS или jamovi и интерпретирует среднюю разность вместе с доверительным интервалом.

**Уровень и время:** начинающие, 60 минут; достаточно базового понимания среднего. Нужны выбранная программа и учебный CSV. Для полного выполнения в обеих программах увеличьте время.

**Ситуация:** представлены баллы 12 условных участников до и после семинара. Данные искусственные. Вопрос: «Изменился ли средний балл тех же участников между двумя измерениями?»

| Переменная | Значение | Структура |
|---|---|---|
| `id` | Код условного участника | Одна строка на человека; это не количественный результат |
| `pre` | Балл до семинара | Количественный, 0–100 |
| `post` | Балл после семинара | Количественный, 0–100 |

**Ход занятия:** 0–5 минут — вопрос и прогноз; 5–15 — импорт, типы и проверка 12 строк; 15–25 — средние, SD и разности `post - pre`; 25–40 — тест с преподавателем; 40–52 — самостоятельная интерпретация; 52–60 — проверка понимания и сохранение.

**SPSS:** откройте CSV и проверьте Scale для `pre` и `post`. В Analyze → Compare Means → Paired-Samples T Test задайте пару: сначала `post`, затем `pre`; выберите 95% ДИ. Сохраните синтаксис через Paste и выполните его. Альтернатива — готовый `.sps` с включёнными данными в новой учебной сессии. Изучите распределение парных разностей. Название меню может зависеть от версии.

**jamovi:** откройте CSV; задайте ID для `id` и Continuous для баллов. В Analyses → T-Tests → Paired Samples T-Test задайте пару `post`, `pre`. Выберите парный тест Стьюдента, двустороннюю гипотезу, описательные показатели, среднюю разность и её 95% ДИ; изучите Q–Q график разностей. При добавлении размера эффекта проверьте его определение. Сохраните проект как `.omv`.

**Задания слушателю:** Почему не подходит независимый t-тест? Как направлена разность? Что показывают средняя разность и ДИ? Сколько пар останется, если одно значение `post` пропущено? Доказывает ли результат причинное влияние семинара?

**Ключ преподавателя:** 12 полных пар; `pre`: M = 63,50, SD = 8,98; `post`: M = 67,00, SD = 10,08. Средняя разность `post - pre` = 3,50 балла, 95% ДИ [2,58; 4,42]; t(11) = 8,38, p < 0,001; d_z = 2,42, знаменатель — SD парных разностей. При одном пропуске `post` остаётся 11 полных пар, и результаты нужно пересчитать. Измерения одного человека связаны. Искусственный пример не доказывает эффективность семинара; в реальном исследовании без контрольной группы причинный вывод также был бы ограничен.

## English: one group's scores before and after a workshop

**Objective:** the learner identifies paired observations, runs a paired t-test in SPSS or jamovi, and interprets the mean difference with its confidence interval.

**Level and duration:** beginners, 60 minutes; basic understanding of the mean is sufficient. Use the selected application and the training CSV. Allow more time if both applications must be completed in full.

**Scenario:** the dataset contains pre- and post-workshop scores for 12 fictional participants. These are synthetic data. Ask: “Did the mean score of the same participants change between the two measurements?”

| Variable | Meaning | Structure |
|---|---|---|
| `id` | Fictional participant identifier | One person per row; not a quantitative outcome |
| `pre` | Pre-workshop score | Quantitative, 0–100 points |
| `post` | Post-workshop score | Quantitative, 0–100 points |

**Timing:** minutes 0–5 question and prediction; 5–15 import, types and 12-row check; 15–25 means, SDs and `post - pre` differences; 25–40 guided test; 40–52 independent interpretation; 52–60 understanding check and saving.

**SPSS:** open the CSV and check that `pre` and `post` are Scale. In Analyze → Compare Means → Paired-Samples T Test, put `post` first and `pre` second; request a 95% CI. Use Paste to save syntax, then run it. Alternatively, use the supplied self-contained `.sps` in a fresh teaching session. Inspect the distribution of pair differences. Menu wording can vary by version.

**jamovi:** open the CSV; set `id` to ID and the scores to Continuous. Under Analyses → T-Tests → Paired Samples T-Test, enter the pair `post`, `pre` in that order. Select the paired Student test, a two-sided alternative, descriptives, mean difference and its 95% CI; inspect the Q–Q plot of differences. If adding an effect size, check its definition. Save as `.omv`.

**Learner tasks:** Why is an independent t-test inappropriate? Which direction does the difference have? What do the mean difference and CI show? How many pairs remain if one `post` value is missing? Does the result establish a causal workshop effect?

**Teacher key:** 12 complete pairs; `pre`: M = 63.50, SD = 8.98; `post`: M = 67.00, SD = 10.08. Mean `post - pre` = 3.50 points, 95% CI [2.58, 4.42]; t(11) = 8.38, p < .001; d_z = 2.42, standardized by the SD of pair differences. One missing `post` leaves 11 complete pairs and requires recalculation. Measurements from the same participant are linked. The synthetic example is not evidence of workshop effectiveness; even real single-group data without a control group would limit causal interpretation.

## Verification boundary

The key was calculated with SciPy and checked against the defining t formula. It is not exported SPSS or jamovi output. Native menu steps and the `.sps` example need to be run in the learner's installed application before claiming native execution. Normality or other diagnostic outcomes have not been invented. Sources for the procedure are B2, W5 and W16 in [the source register](sources.md).

Optional extension in the selected language: reverse the pair order and explain which results change sign; then remove a single measurement in a working copy and reconcile n. Preserve the original example and recalculate, rather than reusing the original numerical key.
