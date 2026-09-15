# ChatGPT EDU Research Assistant

A multilingual Workspace Agent and skill bundle for university and research-institute workflows in Kazakhstan.

## Open the agent

[ChatGPT EDU Research Assistant](https://chatgpt.com/agents/a/agt_6aa91eea812881a4a8421047e2d5909b)

The deployed agent is currently private to its owner in the ChatGPT Edu workspace. This link does not grant access to other users.

## Download the bundle

The GitHub repository distributes the complete source as `chatgpt-edu-research-assistant.zip`. Download and extract that archive to obtain `.codex-plugin/`, `skills/`, and `packages/`. The `packages/` directory contains six separate skill ZIP files ready for the Agent Builder upload control.

## Included skills

1. `chatgpt-edu-research-assistant` — routes cross-stage requests.
2. `literature-review-helper` — verified literature evidence workbench.
3. `living-knowledge-monitor` — recurring research-intelligence digests.
4. `kazakhstan-science-grants` — grant-application development.
5. `kz-research-funding-readiness` — eligibility and submission audit.
6. `spss-jamovi-teacher` — beginner-friendly statistics teaching.

## ChatGPT EDU setup

1. In ChatGPT, open **Agents** and select **Create**.
2. Use the name and description in `AGENT_INSTRUCTIONS.md`.
3. In the builder, upload the six ZIP files from the extracted `packages/` directory.
4. Paste the Workspace Agent instructions and add the starter prompts.
5. Enable Web search and Data analysis if these controls are available in your workspace. Add institution-approved apps as needed. The deployed version has no additional app connections or automatic schedules configured.
6. Preview with the scenarios in `TEST_PLAN.md`, then create the agent and choose the appropriate workspace access level.

ChatGPT EDU availability and permissions depend on workspace administrator settings.

## Repository layout

- `.codex-plugin/plugin.json` — plugin metadata.
- `skills/` — the six reusable skills and their resources.
- `AGENT_INSTRUCTIONS.md` — ready-to-paste Workspace Agent configuration.
- `TEST_PLAN.md` — acceptance tests before publishing.

## Verification status

The package's JSON, six skill entry points, local Markdown links, and archive structure were checked. The native agent was created and all six attached skill names were verified in the builder. The scenarios in `TEST_PLAN.md` are a manual acceptance plan; they have not yet been executed end to end.

## License

MIT. Third-party source materials remain subject to their original licenses and terms.
