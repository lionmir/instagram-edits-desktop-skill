# Instagram Edits Desktop Skill

A portable skill for **Claude Code and Codex**, built for Instagram Edits on Mac. It covers video editing workflows and discovers the app's actual native MCP tools before operating them.

Research baseline: November 5, 2026; installed Edits 454.0.0 (454.0.0.38.112). Includes a broad map of shipped action names, desktop/mobile feature distinctions, setup guidance, editing procedures and an update process. Bundled names are provisional; authenticated tools and schemas are authoritative.

## Install

[Download the latest release ZIP](https://github.com/thebreakdownsi/instagram-edits-desktop-skill/releases/latest/download/instagram-edits-desktop-v0.1.0.zip), extract it, open Terminal in the extracted folder and run one command. Requires Python 3.9 or newer; no external Python packages.

```sh
# Claude Code, all local projects
python3 install.py --client claude

# Codex, all local projects
python3 install.py --client codex

# Both clients
python3 install.py --client both
```

Or install from GitHub with Git:

```sh
git clone https://github.com/thebreakdownsi/instagram-edits-desktop-skill.git
cd instagram-edits-desktop-skill
python3 install.py --client both
```

Choose `--client claude` or `--client codex` to install for one client only. Browse [all releases](https://github.com/thebreakdownsi/instagram-edits-desktop-skill/releases) for versioned downloads and SHA-256 checksums.

The installer refuses to overwrite an existing skill and changes no client settings or credentials. Restart the client if the skill does not appear.

Project-only installation:

```sh
python3 install.py --client both --scope project --project /absolute/path/to/project
```

Preview destinations without writing:

```sh
python3 install.py --client both --dry-run
```

Manual alternative: copy the entire `instagram-edits-desktop` folder to your chosen location:

| Client | Personal | Project |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/instagram-edits-desktop/` | `.claude/skills/instagram-edits-desktop/` |
| Codex | `~/.agents/skills/instagram-edits-desktop/` | `.agents/skills/instagram-edits-desktop/` |

Do not copy only `SKILL.md`; references are required. See official [Claude Code](https://code.claude.com/docs/en/skills) and [OpenAI](https://learn.chatgpt.com/docs/build-skills) skill documentation.

## Connect Edits for actual editing

Skill installation supplies instructions. Native MCP supplies app access.

1. Open Edits on your Mac and sign in.
2. Open Settings and find Automation. Enable its server when you want to authorize agent control.
3. Under Connect an AI client, use the app-generated Claude Code or Codex setup. Keep the token private and local; do not paste it into chat or distribute it with the skill.
4. Refresh the client and ask it to inspect Edits capabilities before editing.

Labels come from the installed build and may change. See [connection details](instagram-edits-desktop/references/connection.md). This package does not enable the server, store tokens or configure MCP automatically.

## Use

Claude Code:

```text
/instagram-edits-desktop Inspect my connected Edits tools and tell me what is available.
```

Codex:

```text
Use $instagram-edits-desktop to inspect my Edits tools and current project.
```

Other examples:

- “Turn these clips into a 30-second vertical cut. Add corrected captions and export locally.”
- “Apply a subtle push-in to this shot without changing my existing text animation.”
- “Explain which Edits features are confirmed on desktop versus mobile.”
- “Refresh the function inventory for my installed Edits version.”

## Coverage and validation

- Official desktop product/launch pages and topic tutorials were researched.
- Installed app metadata and bundled action-name strings were inspected read-only.
- Package structure, installer behavior and archive contents are checked locally.
- Native UI inspection failed with `Accessibility error: AXError.cannotComplete`. No authenticated MCP session, project edit or export was tested during creation.

This is a source-backed initial release, not a claim that every bundled function is executable or every future release is covered. Live discovery handles changing tools, screens and schemas. Some functions need UI access if not exposed through MCP.

## Sharing and removal

Share the ZIP or this source folder. No account-specific material is required. To remove, delete only the installed `instagram-edits-desktop` folder at the destination shown by the installer. Removing the skill does not revoke a separately configured Edits MCP connection; manage that in Edits/client settings.

Original skill instructions and installer are MIT-licensed; see [LICENSE](LICENSE). Unofficial community package, not affiliated with Meta, Anthropic or OpenAI. Product names belong to their owners. No Edits binaries or media are included.

## Contributing

Report issues or propose changes through [GitHub](https://github.com/thebreakdownsi/instagram-edits-desktop-skill/issues). For a feature report, include your Edits version, client, current screen, and redacted error. Never include access tokens, private footage, or account-specific project data. Mark bundled action names separately from tools you tested successfully.

To refresh coverage, follow [sources and updates](instagram-edits-desktop/references/sources-and-updates.md). Build release assets with:

```sh
python3 scripts/build_release.py
```
