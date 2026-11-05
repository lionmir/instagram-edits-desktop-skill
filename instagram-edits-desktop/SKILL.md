---
name: instagram-edits-desktop
description: Help plan, edit, caption, grade, mix, and export videos in Instagram Edits for Mac. Discover and use native Edits MCP tools when connected; otherwise provide verified desktop guidance. Use for Edits desktop workflows, automation setup, and troubleshooting.
---

# Instagram Edits Desktop

Operate Edits for Mac through native MCP when connected. This skill supplies editing knowledge and discovery rules; it does not install Edits or create an authenticated connection by itself.

## Establish the working surface

1. Determine whether the user wants guidance, an edit plan, or changes in Edits. Reuse an existing brief, media paths, and project identity.
2. Inspect available Edits tools and their input schemas. The installed build uses server name `metapilot-native`; client prefixes may differ. If disconnected, follow [connection.md](references/connection.md).
3. Inspect app state and the intended project. Tool availability changes between home and editor screens. Refresh discovery after opening/closing projects or receiving a tool-list notification. A missing editor tool on the home screen does not establish lack of support.
4. Read exposed capabilities/overview and current catalogs. Resolve project, clip, track, element, effect and font IDs from current results. Never manufacture IDs, arguments, units, shortcuts or catalog values from names in this package.

For product questions, read [features.md](references/features.md). For action discovery, read relevant sections of [tool-map.md](references/tool-map.md). A request for all functions requires current manifests/capabilities and explicit coverage of home/editor availability, including areas that could not be inspected.

## Edit within the brief

- Inspect source media, timeline, selection, audio and captions as relevant before changes. Verify project identity rather than relying only on the frontmost window.
- Translate the brief into source ranges, timeline positions, layers, text, motion, grade, sound and output settings. State substantive creative assumptions briefly, then proceed with reversible work in scope.
- Prefer native semantic tools over simulated clicks. Honor exposed access levels, dependencies, network-backed behavior and unimplemented/stub status. A bundled name is not proof that a tool works.
- Read timing and coordinate conventions from live schemas. Source time and timeline time differ; seconds, milliseconds and frames are not interchangeable. Refresh element IDs/ranges after trim, split, reorder or ripple edits.
- Make coherent changes, read back results and preview representative frames/playback. After a timeout, inspect whether a mutation succeeded before retrying. Use undo or a narrow correction for demonstrated failures.
- Duplicate a project when useful for a substantial alternate cut, if supported. Do not assume archive round trips preserve every feature.
- Follow existing user authorization and host permissions for editing, recording, export and posting. Preparing an edit does not authorize publishing, deleting source media or changing account settings. Do not add approval steps when the specific action is already authorized and permitted.

## Load only needed detail

| Need | Reference |
| --- | --- |
| Requirements, desktop support, mobile differences | [features.md](references/features.md) |
| MCP setup, authentication, changing tools | [connection.md](references/connection.md) |
| Function discovery across editing domains | [tool-map.md](references/tool-map.md) |
| Editing, preview, export, troubleshooting | [workflows.md](references/workflows.md) |
| New release, uncertain feature, sources | [sources-and-updates.md](references/sources-and-updates.md) |

## Verify and report

Verify changes through inspection and visual/audio preview. For exports, check job completion and the resulting file, not merely request acceptance. Report project/output identity, completed work, validation and real blockers. Distinguish plans from changes actually made.

Baseline: researched 2026-11-05; local Edits 454.0.0, internal version 454.0.0.38.112. Product information and shipped action names were inspected; authenticated MCP execution was not tested. For newer builds or “latest” questions, refresh relevant official sources and live capabilities. Do not promise exhaustive, permanently current knowledge from this snapshot.
