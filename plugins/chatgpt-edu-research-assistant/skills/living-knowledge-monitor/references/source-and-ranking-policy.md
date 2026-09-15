# Source and ranking policy

## Source hierarchy

Use the strongest available primary source for each claim.

1. **Research:** publisher or journal record, DOI landing page, official repository, dataset record, or clearly labeled preprint server.
2. **Laboratory and technology news:** laboratory, university, research institute, company research division, conference, or standards body announcement. Use independent reporting as context, not as the sole basis for a technical claim when a primary page exists.
3. **Standards and regulation:** issuing standards organization, regulator, ministry, accreditor, or official gazette. Distinguish proposal, consultation, approval, effective date, and enforcement date.
4. **Opportunities:** official funder, university, institute, vacancy, or program application page. Aggregators may help discovery but cannot verify open status, deadline, or eligibility.
5. **Researchers:** current institutional profile, ORCID or other stable researcher identifier, and representative recent publications. Bibliometric profiles may support—but not replace—identity and affiliation verification.

Prefer sources with a stable URL, explicit date, named issuer/authors, and enough text to verify the claim. Do not include an item that can only be supported by an inaccessible snippet unless the limitation is explicit and the claim is independently verified.

## Publication handling

- Label peer-reviewed articles, reviews, conference papers, datasets, protocols, and preprints accurately.
- Do not describe a preprint as peer reviewed.
- Treat an online-first date as the publication date when it is the newest authoritative date.
- Prefer DOI as the stable identifier.
- Note retractions, expressions of concern, corrections, or substantial version changes when discovered.
- Summarize findings conservatively; distinguish reported results from causal conclusions and from the digest author's inference.

## Opportunity handling

Verify on the run date:

- Open/closed status.
- Deadline and timezone, if stated.
- Applicant level and eligibility.
- Host/location or remote status.
- Funding, salary, duration, or position type when officially stated.
- Official application route.

Exclude expired opportunities unless reporting a newly announced successor call. If no deadline is stated, write “deadline not stated” rather than guessing.

## Featured researcher handling

Assess topic fit using multiple signals: current role, lab or group focus, recent representative work, funded projects where public, and sustained contribution. Do not rank people using protected characteristics or private information. Avoid claiming that a person will collaborate or is the “best”; describe why outreach may be relevant.

Prefer a new person each run. Repeat a person only for a material development, and label the reason.

## Scoring

Score each candidate from 0 to 5 on three dimensions:

- `relevance_score`: direct match to the profile, audience, region, and exclusions.
- `evidence_score`: authority, primary-source access, date clarity, and corroboration.
- `significance_score`: likely effect on research, teaching, practice, funding, compliance, or collaboration.

Suggested weighted score:

`0.45 × relevance + 0.30 × evidence + 0.25 × significance`

Apply urgency as a tie-breaker for deadlines and regulatory effective dates. Normally exclude candidates with relevance below 3 or evidence below 3. A low-evidence item may appear only in a clearly labeled watchlist, never as an established development.

After scoring, assign the evidence-confidence badge and primary action label using `research-intelligence-features.md`. Do not derive a high confidence badge from the numeric score alone: the decisive question is whether a primary authoritative source supports the specific delivered claim. A source may be highly relevant yet remain `B`, `C`, or `D`.

When sources address comparable constructs, compare them before ranking. Prefer a concise evidence-convergence or contradiction synthesis over several isolated summaries. Rank an instrument separately from its study finding when its availability, permission, or validation evidence differs.

## Balance and compression

Avoid letting a high-volume publisher, institution, or subtopic dominate. Cluster closely related papers or announcements into one synthesis when this improves comprehension. Keep the canonical identifiers of every clustered item in the delivered candidate file so memory remains effective.

Use a short digest when evidence is sparse. Empty categories are informative.
