# jamovi questionnaire-scoring practical / Практика / Практикалық жұмыс

Use one language section and the shared data/key. [CSV](../assets/jamovi-scoring.csv) · [checked numerical key](../assets/jamovi-scoring-key.json). These eight rows and item prompts are newly invented training material, not a validated questionnaire or empirical findings. The four-item completeness rule is a teaching choice, not a universal scoring recommendation. Sources for the workflow: B5/B6 §6.3.3 and §15.5.1; W18–W20 and W12 in [sources](sources.md).

## Shared dictionary / Ортақ сөздік / Общий словарь

One fictional person per row; `id` is an identifier. Each item uses integers 1–5, from strongly disagree to strongly agree. `99` means missing and must be declared missing for all four item columns before calculations. `q3` is negatively worded and needs reversal. Preserve original item columns.

| Item | Қазақша | Русский | English |
|---|---|---|---|
| `q1` | Орташа мәнді түсіндіре аламын | Я могу объяснить среднее значение | I can explain a mean |
| `q2` | Зерттеу сұрағына сәйкес әдісті таңдай аламын | Я могу выбрать метод под исследовательский вопрос | I can choose a method for a research question |
| `q3` | Деректермен жұмыс істеуден қашқақтаймын | Я избегаю работы с данными | I avoid working with data |
| `q4` | Талдау нәтижесін түсіндіре аламын | Я могу интерпретировать результат анализа | I can interpret an analysis result |

Formula targets for the exercise, using the actual variable names:

```text
q3r = 6 - q3
score = (q1 + q2 + q3r + q4) / 4
```

Enter only the expression to the right of `=` in each jamovi formula field and put the name in the variable-name field. These arithmetic expressions target complete-item scoring. Verify missing-value propagation using rows 7 and 8 in the installed application; never treat missing as zero. An alternative missing-aware `MEAN` formula must not silently relax the required count. The equivalent reusable transformation expression is `6 - $source`, applied to `q3` only.

## Қазақша: 45 минуттық практикалық жұмыс

**Мақсат:** жетіспейтін кодты дұрыс белгілеп, кері тармақты қайта кодтау, толық жауаптардан шкала балын есептеу және альфа көрсеткішінің шегін түсіндіру.

**Барысы:** 0–5 минут — сұрақтар мағынасын және шкаланы талқылау; 5–15 — CSV ашып, `id` және тармақ түрлерін тексеру, әр тармақ үшін `99` мәнін Missing values бөлімінде белгілеу; 15–25 — `q3r` және `score` есептеу; 25–35 — балдарды тексеріп, сенімділік талдауын көрсету; 35–45 — түсіндіру және сақтау.

Data → Add → Computed Variable арқылы екі жаңа баған жасаңыз. Формулалар өрісіне жоғарыдағы өрнектерді енгізіңіз. Тек төрт жарамды жауабы бар жолға балл беріледі. Алдымен 7 және 8-жолды тексеріңіз: олардың қорытынды балы бос қалуы тиіс.

Сенімділік көрсеткішін көрсету үшін осы оқу деректерінің алты толық жолын ғана қолданыңыз; бұл мысалда `id <= 6` сүзгісі сол жолдарды таңдайды. Analyses → Factor → Reliability Analysis бөлімінде `q1`, `q2`, `q3r`, `q4` тармақтарын таңдаңыз. `q3r` қайтадан Reverse Scaled Items тізіміне енгізілмейді. Талдаудың n мәні 6 екенін тексеріңіз. Жұмысты `.omv` ретінде сақтап, сүзгінің мақсатын жазыңыз.

**Тапсырмалар:** Неге `99` санын балл ретінде қолдануға болмайды? Неге 7-жолға 4,00 балл берілмейді? Неге альфа шамамен 0,766 болуы осы төрт сұрақтың валидтілігін дәлелдемейді?

**Жауап:** `99` — жауаптың жоқтығын белгілейтін код. 7-жолда үш жауап қана бар; тапсырма төрт жауапты талап етеді. Алты толық жол бойынша орташа шкала балы 3,125, шикі альфа ≈ 0,766. Бұл шағын жасанды мысал тек есептеу мен бағдарлама қадамдарын үйретеді; ол факторлық құрылым не өлшеу валидтілігі туралы дәлел емес.

## Русский: практикум на 45 минут

**Цель:** правильно задать пропуски, перекодировать обратный пункт, рассчитать балл по полным ответам и объяснить ограничения альфы.

**Ход:** 0–5 минут — смысл пунктов и шкалы; 5–15 — импорт CSV, проверка типов и задание `99` как Missing values для каждого пункта; 15–25 — расчёт `q3r` и `score`; 25–35 — проверка баллов и демонстрация надежности; 35–45 — интерпретация и сохранение.

Создайте два столбца через Data → Add → Computed Variable и введите выражения, приведённые выше. Балл рассчитывается только при четырёх допустимых ответах. Проверьте строки 7 и 8: итоговый балл должен оставаться пропущенным.

Для демонстрации надежности используйте шесть полных строк; в этом учебном файле их выбирает фильтр `id <= 6`. В Analyses → Factor → Reliability Analysis включите `q1`, `q2`, `q3r`, `q4`. Не помещайте уже перекодированный `q3r` в Reverse Scaled Items. Убедитесь, что n = 6. Сохраните `.omv`, указав назначение фильтра.

**Задания:** Почему `99` нельзя считать баллом? Почему строке 7 не присваивается 4,00? Почему альфа около 0,766 не доказывает валидность этих четырёх вопросов?

**Ключ:** `99` обозначает отсутствие ответа. В строке 7 только три ответа, а правило упражнения требует четыре. Средний балл шести полных строк равен 3,125; нестандартизированная альфа ≈ 0,766. Маленький искусственный набор служит для освоения расчётов и интерфейса; он не подтверждает факторную структуру или валидность измерения.

## English: 45-minute practical

**Objective:** define missing values, reverse-score an item, calculate a complete-item score, and explain alpha's limitations.

**Timing:** minutes 0–5 discuss item meanings and response scale; 5–15 import CSV, check types and declare `99` missing for each item; 15–25 calculate `q3r` and `score`; 25–35 check scores and demonstrate reliability; 35–45 interpret and save.

Create two columns via Data → Add → Computed Variable, entering the expressions above. Score a row only when all four items are valid. Check rows 7 and 8: their scores must remain missing.

For the reliability demonstration use the six complete rows; in this particular training file the filter `id <= 6` selects them. In Analyses → Factor → Reliability Analysis enter `q1`, `q2`, `q3r`, `q4`. Do not also place the already reversed `q3r` in Reverse Scaled Items. Confirm n = 6. Save `.omv` and describe the filter's purpose.

**Questions:** Why is `99` not a score? Why does row 7 not receive 4.00? Why does alpha around .766 not establish the validity of these four questions?

**Key:** `99` denotes no response. Row 7 has only three answers, whereas this exercise requires four. Mean score across the six complete rows is 3.125; raw alpha ≈ .766. The tiny synthetic dataset teaches calculations and interface operations; it does not establish factor structure or measurement validity.

## Row-level teacher key / Жолдар бойынша жауап / Ответы по строкам

| id | q3r | Valid items / Жарамды жауап / Валидные ответы | score |
|---|---|---|---|
| 1 | 2 | 4 | 1.75 |
| 2 | 1 | 4 | 2.25 |
| 3 | 4 | 4 | 3.25 |
| 4 | 3 | 4 | 3.75 |
| 5 | 5 | 4 | 4.50 |
| 6 | 4 | 4 | 3.25 |
| 7 | 4 | 3 | missing / жоқ / пропуск |
| 8 | missing / жоқ / пропуск | 0 | missing / жоқ / пропуск |

Verification: scores were calculated independently; raw alpha = 0.7658979734 was cross-checked using variance and covariance formulas on the same six complete cases. Neither jamovi's formula editor nor native output was executed during authoring. Do not invent omega, confidence intervals or factor-analysis results from this key. Translate this execution-status note when delivering the practical in one language.
