# Қазақша / Русский / English

Use one selected teaching language, unless parallel translations are requested. Keep dataset identifiers and code identical across languages. These Kazakh terms are working teaching translations, not a claim of an official terminology standard. On first use pair an unfamiliar term with its English equivalent.

| Қазақша | Русский | English |
|---|---|---|
| зерттеу сұрағы | исследовательский вопрос | research question |
| бас жиынтық | генеральная совокупность | population |
| іріктеме | выборка | sample |
| бақылау бірлігі | единица наблюдения | unit of observation |
| айнымалы | переменная | variable |
| тәуелді айнымалы | зависимая переменная | dependent variable / outcome |
| түсіндіруші айнымалы | объясняющая переменная | predictor |
| номиналдық шкала | номинальная шкала | nominal scale |
| реттік шкала | порядковая шкала | ordinal scale |
| сандық айнымалы | количественная переменная | quantitative variable |
| жетіспейтін мән | пропущенное значение | missing value |
| кері кодтау | обратное кодирование | reverse scoring |
| сипаттамалық статистика | описательная статистика | descriptive statistics |
| арифметикалық орта | среднее арифметическое | arithmetic mean |
| медиана | медиана | median |
| стандартты ауытқу | стандартное отклонение | standard deviation (SD) |
| стандартты қате | стандартная ошибка | standard error (SE) |
| квартильаралық ауқым | межквартильный размах | interquartile range (IQR) |
| сенімділік аралығы | доверительный интервал | confidence interval (CI) |
| нөлдік гипотеза | нулевая гипотеза | null hypothesis |
| p-мәні | p-значение | p-value |
| әсер мөлшері | размер эффекта | effect size |
| еркіндік дәрежесі | число степеней свободы | degrees of freedom |
| тәуелсіз іріктемелер | независимые выборки | independent samples |
| жұпталған өлшемдер | парные измерения | paired measurements |
| қайталанған өлшемдер | повторные измерения | repeated measures |
| дисперсиялық талдау | дисперсионный анализ | analysis of variance (ANOVA) |
| қалдық | остаток | residual |
| ішкі келісімділік | внутренняя согласованность | internal consistency |
| өлшеу сенімділігі | надежность измерения | reliability |
| валидтілік | валидность | validity |
| қайта өндіруге болатын талдау | воспроизводимый анализ | reproducible analysis |
| есептелетін айнымалы | вычисляемая переменная | computed variable |
| түрлендірілген айнымалы | преобразованная переменная | transformed variable |
| факторлық жүктеме | факторная нагрузка | factor loading |
| барлаушы факторлық талдау | разведочный факторный анализ | exploratory factor analysis (EFA) |
| растаушы факторлық талдау | подтверждающий факторный анализ | confirmatory factor analysis (CFA) |
| негізгі компоненттер талдауы | анализ главных компонент | principal component analysis (PCA) |
| Байес факторы | байесовский фактор | Bayes factor |
| априорлық ықтималдық | априорная вероятность | prior probability |
| апостериорлық ықтималдық | апостериорная вероятность | posterior probability |

## Explanation patterns

**KK:** «Алдымен деректердің қалай жиналғанын анықтаймыз. Бір адамның екі нәтижесі өзара байланысты, сондықтан оларды жұп ретінде талдаймыз. Бағдарламада көрсетілген айырманың бағытын тексеріңіз: `post - pre`.»

**RU:** «Сначала определим, как собраны данные. Два результата одного человека связаны, поэтому анализируем их как пару. Проверьте направление разности в программе: `post - pre`.»

**EN:** “First establish how the data were collected. Two results from the same person are linked, so we analyse them as a pair. Check the direction of the difference in the software: `post - pre`.”

## Reporting templates

Fill brackets only from inspected output or verified calculation. A bracket is a report field, not permission to invent a value.

**KK:** «Талдауға [n] жұп енгізілді. [Бірлік] бойынша орташа айырма [Δ], 95% сенімділік аралығы [төменгі; жоғарғы] болды; t([df]) = [t], p = [p]. [Әсер мөлшері және оның анықтамасы]. Бұл [контекстік түсіндірме]; [зерттеу дизайнына байланысты шектеу].»

**RU:** «В анализ включены [n] пар. Средняя разность составила [Δ] [единиц], 95% ДИ [нижняя; верхняя]; t([df]) = [t], p = [p]. [Размер эффекта и его определение]. Это означает [содержательная интерпретация]; [ограничение дизайна].»

**EN:** “The analysis included [n] pairs. The mean difference was [Δ] [units], 95% CI [lower, upper]; t([df]) = [t], p = [p]. [Effect size and its definition]. This indicates [contextual interpretation], subject to [design limitation].”

Report displayed `.000` as `p < .001`, never as a probability of zero. Match local decimal punctuation in prose when requested; preserve the decimal syntax required by code. Keep SD distinct from SE and reliability distinct from validity in all languages.

## Starter prompts

- KK: `$spss-jamovi-teacher SPSS пен jamovi-де деректерді енгізу және сипаттамалық статистика бойынша 60 минуттық практикалық сабақ дайында. Білім алушылар — жаңадан бастаған оқытушылар.`
- RU: `$spss-jamovi-teacher Объясни преподавателю, как выбрать между независимым и парным t-тестом, и покажи шаги в jamovi на учебном примере.`
- EN: `$spss-jamovi-teacher Prepare a 90-minute workshop comparing SPSS and jamovi for questionnaire scoring, missing data, and reliability. Include exercises and a teacher key.`
