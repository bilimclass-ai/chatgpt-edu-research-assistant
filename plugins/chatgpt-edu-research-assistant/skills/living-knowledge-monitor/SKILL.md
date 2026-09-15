---
name: living-knowledge-monitor
description: Create recurring, evidence-linked weekly or monthly research-intelligence digests for a scientific, technical, or professional field. Use for monitoring publications, methods and instruments, laboratory news, technologies, standards and regulation, PhD/PostDoc/funding/grant and funded-conference opportunities, researchers and collaborators, thesis development, or course-update proposals. Maintain cross-run memory, suppress repeats, track contradictions and feedback, map evidence to thesis needs, and prepare—but never automatically apply—course or outreach changes.
---

# Living Knowledge Monitor

Produce a verified, prioritized digest that helps a professor or instructor stay current without rereading old items. Keep durable memory outside the conversation context.

## Start modes

Interpret a natural-language request; never require the user to edit JSON manually.

- **Guided setup:** Turn the user's context into a monitoring profile, show a compact summary of the interpreted settings, and resolve only missing choices that would materially change the search.
- **Pilot:** Research a one-time seven-day sample, show the digest and proposed profile, and use temporary state. Do not commit durable memory or create a recurring schedule until the user approves activation.
- **Activate:** Create persistent profile and state, run the first digest, commit delivered items, and optionally configure a separate recurring automation after delivery details are confirmed.
- **Continue:** Load an existing monitor ID, cover the period since its last successful run, filter repeats, and commit the new digest.
- **Status or revise:** Report memory/run counts or update profile preferences without discarding history.

Accept a minimal start such as: `Use $living-knowledge-monitor in pilot mode for quantum sensing, for a physics professor, in English.` Apply these defaults when omitted: global coverage, English output and search, weekly cadence, Monday delivery day, seven-day pilot window, all categories enabled, and no external delivery. State the defaults in the pilot header.

For first-time users, collect at most these essential inputs before a live run:

1. Topic or research area.
2. Audience and intended use, such as research, teaching, funding, recruitment, or collaboration.
3. Output language and any geographic or eligibility constraints.
4. Pilot versus persistent monitoring.

Treat everything else as optional enrichment. Examples include keywords, excluded subtopics, methods, organisms or populations, technology readiness, favorite journals/labs, career stage, nationality or mobility constraints for opportunities, course/module context, and collaboration goals.

## Required resources

- Read `references/source-and-ranking-policy.md` before researching.
- Read `references/academic-source-catalog.md` when planning or running searches for publications, conferences, journal calls, scholarships, internships, funding, jobs, researchers, communities, or policy environments.
- Read `references/memory-and-output.md` before the first run, when changing the profile, or when repairing state.
- Read `references/google-sheet-register.md` before creating or updating a research-intelligence spreadsheet.
- Read `references/research-intelligence-features.md` before using thesis mappings, action labels, confidence badges, eligibility assessments, collaboration dossiers, contradiction analysis, instrument records, monthly synthesis, or feedback personalization.
- Copy `assets/monitor-profile.template.json` to a writable data directory and customize it for each recipient/topic.
- Use `scripts/memory_store.py` for deduplication and run history. Do not substitute chat memory for this ledger.
- Use `scripts/check_word_budget.py` before delivering a digest with a word cap.
- Use `assets/digest-template.md` as the default deliverable structure, adapting section sizes to the evidence found.
- Use `assets/source-coverage.template.json` for the per-run platform audit.

## Workflow

### 1. Establish the monitoring profile

Create or load one profile per recipient and research area. Require a monitor ID, topic, audience, keywords, exclusions, geography, languages, cadence, priority categories, and preferred sources. Ask only for missing choices that materially change results; otherwise use the template defaults and label them.

Enable the Thesis Evidence Matrix automatically when the user supplies a thesis title, research questions, chapter plan, or thesis-development goal. Leave it disabled for general monitoring unless requested.

Generate a readable monitor ID from the topic and audience, then let the user correct it. Before activation, show a short profile preview rather than the raw JSON. Save the full structured profile only after the user chooses persistent monitoring.

Keep recipient contact details out of the profile unless delivery through an authorized connector is explicitly requested.

### 2. Resolve persistent storage

Use a stable, writable directory such as `living-knowledge-data/<monitor-id>/`. Keep these separate:

- `profile.json`: monitoring preferences.
- `state.json`: compact deduplication ledger, created by the script.
- `runs.jsonl`: append-only run audit.
- `feedback.jsonl`: append-only explicit user judgments and notes.
- `source-coverage/YYYY-MM-DD.json`: per-run audit of enabled platforms checked, unavailable, or skipped with reason.
- `digests/YYYY-MM-DD.md`: finished digest archive.
- `syntheses/YYYY-MM.md`: monthly cross-run synthesis when enabled.
- `candidates/YYYY-MM-DD.json`: structured items considered for the successful run.

Initialize state before research:

```powershell
python scripts/memory_store.py init --state-dir <data-directory>
python scripts/memory_store.py status --state-dir <data-directory>
```

If the available Python executable has a different path, invoke that executable directly.

For pilot mode, use a clearly labeled temporary data directory and leave the durable monitor untouched. After approval, create the persistent directory and commit only items included in the approved first digest.

### 3. Define the evidence window

For a weekly run, search from the previous successful run through the current run time, with a default seven-day fallback. For a monthly run, use the analogous monthly window. Include online-first publication dates and clearly label preprints.

If a run was missed, cover the full gap but favor a concise high-value digest. State the exact coverage dates.

### 4. Research every enabled category

Browse current sources; cached model knowledge is insufficient. Search the enabled categories independently:

1. Peer-reviewed articles, reviews, datasets, protocols, and preprints.
2. Journal special issues, article collections, thematic series, and calls for papers.
3. Scientific, technology, professional, and top-lab news.
4. Standards, accreditation, policy, and regulatory changes.
5. Conferences, workshops, summer schools, travel grants, and funded-participant calls.
6. Scholarships, PhD, PostDoc, fellowships, grants, internships, visiting positions, research jobs, and mobility opportunities.
7. Researchers, laboratories, consortia, learned societies, and relevant academic-community announcements.
8. One featured professor or research leader with a strong, verifiable record relevant to the topic.
9. Course or syllabus implications when course context is available.

Use the profile's language and geography rules. Search across languages when useful, but write the digest in the requested output language.

Before searching, build the per-run source plan from `references/academic-source-catalog.md`, the profile's `academic_source_registry`, preferred sources, enabled categories, disciplines, and geographies. Review every accessible source marked `always_review`; review relevant category sources and record coverage even when no item is included. Use discovery platforms to find leads, but verify every operational or reputational claim on an authoritative primary page. Save the source-coverage audit with the successful run.

### 5. Verify and structure candidates

Apply `references/source-and-ranking-policy.md`. Open the primary page for every included item. Do not use a search-results snippet as evidence.

Create a UTF-8 JSON array of candidates. Each included candidate should contain as applicable:

```json
{
  "kind": "article|review|dataset|preprint|protocol|special_issue|journal_call|conference_signal|summer_school|lab_news|technology|standard|regulation|scholarship|phd|postdoc|fellowship|funding|grant|internship|visiting_position|research_job|community_announcement|professor|course_signal",
  "title": "Canonical title",
  "authors": [],
  "evidence_type": "peer-reviewed article|conference abstract|preprint|official call|other",
  "url": "Primary URL",
  "doi": "10.xxxx/xxxx",
  "external_id": "ORCID, grant ID, standard number, or vacancy ID",
  "person_or_org": "Name or organization",
  "source": "Publisher or institution",
  "discovered_via": [],
  "verified_via": [],
  "source_access_limitations": "",
  "published_at": "YYYY-MM-DD",
  "deadline": "YYYY-MM-DD or null",
  "study": {
    "design": "",
    "population_context": "",
    "intervention_or_exposure": "",
    "reported_findings": "",
    "limitations": ""
  },
  "event": {
    "organizer": "",
    "venue_or_format": "",
    "event_dates": "",
    "call_opens": "",
    "deadline_timezone": "",
    "acceptance_notification": ""
  },
  "opportunity": {
    "official_status": "",
    "funding_amount_or_coverage": "",
    "official_eligibility": "",
    "application_route": ""
  },
  "collaboration": {
    "current_role_and_institution": "",
    "representative_work": [],
    "recent_relevant_activity": "",
    "verified_public_contact_route": ""
  },
  "relevance_score": 0,
  "evidence_score": 0,
  "significance_score": 0,
  "confidence_badge": "A|B|C|D",
  "action_label": "ACT NOW|READ|USE IN THESIS|COLLABORATE|WATCH",
  "thesis_map": {
    "chapter": "",
    "construct": "",
    "research_question": "",
    "method_or_instrument": "",
    "expected_contribution": ""
  },
  "eligibility_assessment": "probably eligible|conditionally eligible|not eligible|unknown|not applicable",
  "eligibility_reason": "",
  "contradicts_or_supports": [],
  "instrument": {
    "name": "",
    "purpose": "",
    "availability": "available|adaptable|permission required|not provided|unknown"
  },
  "force_include_reason": ""
}
```

Leave fields blank when the primary evidence does not supply them. Missing structured fields do not invalidate a candidate, but they must constrain the confidence badge and any eligibility, contradiction, instrument, or collaboration claim. Never infer operational dates, funding, methods, findings, contact routes, or eligibility from context alone.

Use `force_include_reason` only for a correction, material development, or time-sensitive deadline reminder. Explain the reason in the digest.

### 6. Remove repeats before writing

Run:

```powershell
python scripts/memory_store.py filter --state-dir <data-directory> --candidates <candidate-file> --output <filtered-file>
```

Use only `unseen` items from the filtered result. Review `repeated` to detect accidental duplication. The script matches DOI, stable external ID, canonical URL, and normalized title/person fingerprints.

Do not commit weak or discarded candidates. Persistent memory tracks what the recipient actually received, not everything found during research.

### 7. Rank and write the digest

Rank by profile fit, source quality, novelty, practical significance, urgency, and actionability. Prefer fewer strong items over a padded list. Target relevance of at least 80%.

Apply `references/research-intelligence-features.md`. Give every delivered item exactly one primary action label and one evidence-confidence badge. When thesis context is available, populate the Thesis Evidence Matrix. Compare studies when they support or contradict comparable claims. Extract reusable instruments only when their source and availability are clear.

For every item, provide:

- What changed or was published.
- Why it matters to this recipient.
- One primary evidence link and publication/event date.
- Confidence or evidence limitations when material.
- A concrete next action only when justified.

Apply the configured hard word budget to the complete delivered digest, counting all output languages together. Default to 1,200 words total and 180 words for the executive summary. Put the executive summary first. Use three to seven bullets, bold the decisive phrase in each bullet, and state the main findings, thesis implications, urgent deadlines, and recommended actions. Do not let bilingual repetition crowd out evidence; compress parallel translations when necessary.

Prefer actual operational details over generic descriptions: exact dates, deadline timezone, location or delivery format, organizer or funder, amount or covered costs, eligibility, DOI or stable identifier, and direct official URL when available. Before delivery, run:

```powershell
python scripts/check_word_budget.py <digest-path> --max-words <configured-total>
```

For the featured professor, verify institutional affiliation and research fit; cite an institutional profile plus representative recent work when possible. Frame the person as a potential collaborator to evaluate, never as an endorsement. Add a short, evidence-based collaboration angle and avoid sensitive personal data.

For opportunities, include eligibility, location, opening date, deadline and timezone, funding/position type, amount or covered costs, and official application page. Never report an opportunity as open unless its official page supports that status.

For conferences, monitor official calls for papers, funded-participant programs, travel grants, registration or fee waivers, and related support. Include a conference when its call is already open or will open after the current run and no later than the next scheduled report. Record event dates, venue/format, organizer, call opening date, submission deadline and timezone, acceptance-notification date, funding amount or covered costs, travel-grant deadline, eligibility, and official call URL. Label an item **funded** only when an official source explicitly verifies the funding; otherwise write “funding not verified.”

For every opportunity, perform a transparent eligibility pre-check using only stated profile facts and official criteria. Never promise final eligibility. For conferences, assign a user-managed pipeline stage from `Discovered` through `Funding requested`; suggest changes but never advance the stage solely because time passed.

For the featured researcher, produce a compact collaboration dossier with shared topic, complementary expertise, representative work, a concrete joint-output idea, verified public contact route when appropriate, and current outreach status. Never infer willingness to collaborate.

### 8. Learn from explicit feedback

Read the latest explicit feedback from the enabled research register or `feedback.jsonl` before ranking. Treat `Useful`, `Follow up`, and `Already known` as ranking signals. Treat `Too broad` and `Not useful` as soft negative signals, not permanent exclusions. Change keywords, preferred sources, geography, or hard exclusions only after explicit user approval. Preserve the original feedback record.

### 9. Produce monthly synthesis when enabled

At the configured monthly boundary, synthesize prior successful weekly runs instead of repeating their item summaries. Report emerging themes, strongest evidence, contradictions, thesis-gap changes, methods and instruments, collaboration movement, opportunity outcomes, and proposed profile refinements. New urgent items may still appear with `ACT NOW`. Save the synthesis under `syntheses/YYYY-MM.md` and do not commit previously delivered items again.

### 10. Handle course implications safely

When a significant change affects teaching, prepare a proposal containing affected course/module, supporting evidence, suggested review owner, urgency, and a draft change. Do not edit a syllabus, curriculum, assessment, or academic policy automatically.

### 11. Update the research register

When the profile enables a Google Sheets research register, append or update the delivered records after the digest is finalized and before the run is marked complete. Follow `references/google-sheet-register.md`. Match records by DOI, ORCID, official opportunity identifier, or canonical URL. Preserve user notes, outreach status, application status, owners, and manual priority values. The register is an index and collaboration workspace; the deduplication ledger remains the authoritative record of what appeared in prior digests.

### 12. Commit only after successful delivery artifact creation

Save the final digest first, then create a JSON file containing only delivered candidates and run:

```powershell
python scripts/memory_store.py commit --state-dir <data-directory> --candidates <delivered-file> --run-date YYYY-MM-DD --digest <digest-path>
```

If delivery later fails, retain the digest and run record, report the delivery failure, and do not silently regenerate different content.

### 13. Deliver through an authorized channel

Create the digest without external delivery by default. Send email, chat, or calendar notifications only when the user explicitly authorizes the channel and recipient. A recurring Monday schedule is an automation around this skill, not part of chat memory; configure it separately with the user's local time and delivery destination.

## Quality gates

Before completion, confirm:

- Coverage dates and profile are explicit.
- Every factual item has a working primary evidence link.
- The source-coverage audit records all enabled platforms as checked, unavailable, or skipped with a reason; the digest does not overstate coverage.
- Discovery platforms are not used alone to verify peer-review status, deadlines, funding, eligibility, affiliation, or journal quality.
- No unsupported claims or invented dates, deadlines, affiliations, or metrics appear.
- Repeated items are absent unless a labeled exception applies.
- Opportunities are current as of the run date.
- The executive summary appears first, highlights the main points and thesis implications, and stays within its sub-limit.
- The complete digest stays within the configured hard word limit across all output languages.
- Conference records contain exact operational dates and distinguish verified funding from unverified funding.
- The featured researcher has verified topic fit and affiliation.
- Practical significance is specific to the recipient.
- Every delivered item has exactly one primary action label and one justified confidence badge.
- Thesis mappings distinguish source facts from the monitor's proposed use.
- Eligibility pre-checks explain known conditions and missing information without guaranteeing eligibility.
- Contradictions identify compared studies and design or context differences that may explain them.
- Instrument availability is stated; unavailable instruments are not reconstructed.
- Feedback changes ranking only within the user's approved scope.
- Monthly synthesis aggregates earlier runs without presenting them as new items.
- Course changes are proposals only.
- The digest, candidate set, state ledger, and run audit agree.
- When enabled, the research register matches delivered records and preserves user-managed fields.

If evidence is too thin for a category, say “No high-confidence update found” rather than filling space.
