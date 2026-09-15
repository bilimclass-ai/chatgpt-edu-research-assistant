# ChatGPT EDU Research Assistant

Developer: **Bilim AI**. Version **1.0.2** updates publisher metadata, organization links, and the supplied light/dark Bilim AI logos. The six skills are unchanged.

Ғылыми әдебиет, зерттеу мониторингі, Қазақстан гранттары және SPSS/jamovi бойынша қазақша, орысша және ағылшынша жұмыс істейтін плагин.

This repository contains an installable six-skill ChatGPT/Codex plugin and a GitHub marketplace catalog. It does not require an MCP server, API key, or a new external app connection. Tool availability still depends on the host workspace.

## Install in ChatGPT EDU

For a new one-time installation, download [chatgpt-edu-research-assistant-bilim-ai-v1.0.2.tar.gz](chatgpt-edu-research-assistant-bilim-ai-v1.0.2.tar.gz), then use **Admin > Plugins > Add > Upload plugin**. After adding it to the workspace, install it in your own account from the plugin directory. If the plugin already exists, do not delete it or create a duplicate to update branding; preserve its ID and installation policies. The ZIP is the original Agent Builder bundle, not the latest plugin version.

GitHub synchronization requires an authorized GitHub connection and may require MFA. Without that connection, use the archive installation; it does not enable automatic synchronization.

A workspace administrator can import this repository using **Admin > Plugins > Add > Import marketplace**:

- Source: `https://github.com/bilimclass-ai/chatgpt-edu-research-assistant`
- Path: leave empty.
- Branch, tag, or commit: leave empty for the default branch, or pin a reviewed commit.

Review the source and the trust prompt. Authorize GitHub only for repositories needed for this import. Review import results and plugin access policies, then install **ChatGPT EDU Research Assistant** from the workspace plugin directory in your own account. Importing a marketplace is not the same as personally installing its plugin. Do not choose workspace-wide automatic installation unless that is intended.

GitHub-managed marketplaces may sync updates daily. Review source changes before merging. See [OpenAI's marketplace import documentation](https://learn.chatgpt.com/docs/enterprise/plugin-management).

## Included skills

1. `chatgpt-edu-research-assistant` — coordinates cross-stage research requests.
2. `literature-review-helper` — literature search, evidence maps, and source-grounded synthesis.
3. `living-knowledge-monitor` — research-intelligence digests; scheduling requires an explicitly configured host task.
4. `kazakhstan-science-grants` — Kazakhstan grant application development.
5. `kz-research-funding-readiness` — eligibility, evidence, and submission-readiness audits.
6. `spss-jamovi-teacher` — statistics teaching and interpretation in SPSS/jamovi.

The five supplied source skills retain their supporting resources. Version 1.0.1 removes the unsupported `policy.products` metadata field; the skill instructions are unchanged. The sixth skill is the coordinating router. The assistant must not invent citations, eligibility decisions, datasets, analysis results, or scheduled monitoring.

## Repository layout

```text
.agents/plugins/marketplace.json
plugins/chatgpt-edu-research-assistant/
  .codex-plugin/plugin.json
  assets/
  skills/
.github/workflows/publish-plugin-source.yml
chatgpt-edu-research-assistant.zip
AGENT_INSTRUCTIONS.md
TEST_PLAN.md
```

The manually triggered publishing workflow safely expands the reviewed ZIP, checks archive paths and six skill entry points, and commits the source and marketplace to this repository. It does not execute scripts inside the skills. It refuses to overwrite independently edited plugin source. The checked-in `plugins/` directory is the source used by ChatGPT marketplace imports.

## Existing Workspace Agent

[Open ChatGPT EDU Research Assistant](https://chatgpt.com/agents/a/agt_6aa91eea812881a4a8421047e2d5909b).

The agent was created privately for its owner. The link does not grant access to other accounts or workspaces. Agent access and plugin installation are separate.

The original ZIP also includes `packages/` with six separate skill ZIP files for the Agent Builder. See `AGENT_INSTRUCTIONS.md` for manual agent configuration.

## Verification and limits

JSON, six skill entry points, local Markdown links, and archive structure have been checked. GitHub source publication passed its workflow checks. `TEST_PLAN.md` contains the behavioral acceptance scenarios; they have not been executed end to end. This is not an official OpenAI plugin and is not a substitute for institutional ethics, statistical, or grant-eligibility review.

## License

MIT for the authored integration. Supplied and third-party source materials retain their original licenses and terms.
