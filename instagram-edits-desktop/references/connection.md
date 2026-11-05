# Native MCP setup

[Official desktop announcement](https://edits.instagram.com/blog/edits-desktop-video-editor/) confirms MCP in Settings. Specific labels below come from bundled strings in build 454.0.0.38.112; settings UI and authenticated connection were not exercised during packaging.

1. Open Edits on the user's Mac; sign in with Instagram if needed. User handles login credentials.
2. Open Settings. Look for **Automation**, **Enable Automation Server**, **Access token**, **Connect an AI client**. Follow current UI if labels changed.
3. User enables server when authorizing agent access. Copy setup generated for **Claude Code** or **Codex**. Use that endpoint and transport; do not guess ports or substitute unofficial bridges.
4. Review generated commands locally, then run in the intended client environment. Bundled help says Claude Code uses one copied command; Codex uses two copied lines before launching Codex.
5. Refresh/restart client as indicated. Confirm server appears, inspect tools, then call an exposed read-only app-state/capabilities operation. Configuration alone is not connection verification.

Bundled server identifier: `metapilot-native`; client prefixes may differ. Skill installer only copies files; MCP connection is separate.

## Credentials

The token grants project control while the server is enabled. Keep it on the user's machine in a client-supported secret/environment mechanism. Never put it in shared skills, archives, repositories, screenshots, logs or chat responses. Do not request token paste into chat or inspect Keychain/private stores to obtain it.

Bundled Codex setup references `METAPILOT_TOKEN`. An environment variable in one terminal may not reach an independently launched desktop client. Use app-generated setup and current client documentation. Do not silently write secrets into shell startup files. Token regeneration invalidates existing client authentication. Do not expose the listener publicly or disable authentication to fix a connection.

## Live discovery

Use client's MCP facilities instead of guessed raw HTTP requests. Inspect tools, schemas, resources and server instructions. Bundled URI candidates:

| URI candidate | Purpose |
| --- | --- |
| `metapilot://app-state` | Screen and actions |
| `metapilot://overview` | Capabilities, conventions, catalogs, recipes |
| `metapilot://clips` | Open-project clips |
| `metapilot://elements` | Timeline elements |

Use only URIs listed by the connected server. `appState`/`getCapabilities` may be actions behind a wrapper, not standalone tools. Read actual invocation schema. Tool set changes between home/editor; rediscover after navigation.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| No server | App open, user enabled Automation, setup added to this client, client refreshed |
| Connection refused | Current endpoint/port and server status; no port scanning |
| Unauthorized | Current token, regeneration, environment reaching client process |
| Missing tool | Current screen, selected project, refreshed manifest, dependencies/gates/stub status |
| Missing media | Path on the Mac running Edits, file existence, app-reported file access |
| Mutation timeout | Inspect state/job before retry to prevent duplicate changes |
| UI inspection fails | Native MCP if connected; otherwise guidance with execution limitation disclosed |

Without a connection, provide source-backed instructions or an edit plan and precise next setup step. Never claim an edit happened.
