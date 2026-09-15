# Optional study reminder button

After a completed teaching answer, offer one follow-up action using the Codex app's supported Markdown button syntax. Skip onboarding, brief exchanges, skill maintenance, reminder setup/runs, a previously declined offer, or an already configured relevant schedule. Put it after the answer and artifact links, outside code/writing blocks. In Kazakh use this exact label:

```text
- :codex-followup[SPSS сабағын тұрақты еске салу]{prompt="SPSS сабағын жүйелі оқу үшін тұрақты еске салу кестесін орнат. Әңгімеде белгісіз болса, алдымен қай күндері, қай уақытта және қай уақыт белдеуі бойынша еске салу керегін нақтыла. Содан кейін сол кестемен осы тапсырмаға еске салуды орнат. Әр еске салу қысқа болып, соңғы оқу тақырыбын жалғастыруды ұсынсын."}
```

Emit the actual unescaped list item, not the surrounding code fence. For Russian use the label “Регулярно напоминать об уроках SPSS”; for English use “Remind me to study SPSS regularly”, translating the complete action prompt without changing its meaning. If follow-up buttons are unsupported, offer an ordinary short text invitation instead; do not claim a working button exists.

## When the learner selects it

Treat the submitted follow-up as a request to set a reminder, not another statistics lesson. Do not restart the three-question teaching introduction or create a PDF/Excel file for reminder setup. Reuse known schedule preferences and timezone; ask only for missing days/frequency and time, and timezone if unavailable or ambiguous. Do not choose an arbitrary schedule or ask again for permission once the schedule is specified.

Discover the current `automation_update` capability and follow its schema and instructions. Prefer a heartbeat attached to the current task for recurring study reminders. Check for a matching existing automation before creating a duplicate; update it when the learner is changing the same schedule. Use native scheduling tools rather than Google Calendar, email, shell scheduling or handwritten automation directives unless the user specifically requests another destination.

The saved prompt should request a short reminder in the learner's language, tied to their latest known SPSS learning topic, with one small practice suggestion. Explicitly allow delivery at each scheduled study time; this is a requested reminder, not a change-only monitor. Do not generate a new course, PDF or workbook, repeat onboarding, or offer this same reminder button inside automated runs. Do not claim the learner completed work without evidence.

Confirm the days, local time and timezone only after the tool reports successful scheduling. If the result is merely proposed/pending, say so. If scheduling is unavailable or fails, explain the limitation rather than saying reminders are active. A displayed button alone never means the schedule was installed.
