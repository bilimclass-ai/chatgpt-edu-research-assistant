# Bilim AI Research Assistant

Standalone archive installation for ChatGPT EDU, independent of GitHub synchronization.

- Plugin identifier: `bilim-ai-research-assistant`
- Display name: **Bilim AI Research Assistant**
- Developer: **Bilim AI**
- Version: `1.0.0`
- Package: [bilim-ai-research-assistant-v1.0.0.tar.gz](bilim-ai-research-assistant-v1.0.0.tar.gz)
- Branding: supplied Bilim AI logos for light and dark themes.

The archive contains the complete `.codex-plugin/plugin.json`, `skills/`, and `assets/` source. All six skills are unchanged from the prior validated ChatGPT package. This is a separate plugin from `chatgpt-edu-research-assistant`; the original plugin is not deleted or replaced.

## Installation

In ChatGPT, open **Admin > Plugins > Add > Upload plugin**, upload the archive, and review the import. Then open **Bilim AI Research Assistant** in the workspace plugin directory and install it in your own account. Workspace import and personal installation are separate steps.

Do not change the workspace-wide installation policy unless organization-wide installation is intended. No GitHub connector, MCP server, or new API key is required by this package. Host capabilities and workspace restrictions still apply.

This archive does not enable automatic GitHub updates. The existing repository marketplace entry targets the older plugin and must not be used as a synchronization entry for this standalone plugin without a separate reviewed migration.

## Checks

Manifest identity, publisher metadata, asset paths, six skill entry points, and byte-for-byte preservation of skill files were checked locally. The standard Python validator was unavailable because Python was not installed. Behavioral acceptance scenarios have not been run end to end.
