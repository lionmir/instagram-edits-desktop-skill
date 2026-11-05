# Desktop feature coverage

Checked 2026-11-05. **Desktop documented** means confirmed by official desktop sources. **Bundled candidate** means present in installed build strings but not execution-tested. **Mobile/general** does not establish desktop parity.

## Desktop documented

From [desktop product page](https://edits.instagram.com/desktop/):

| Area | Capability |
| --- | --- |
| Platform | macOS, Apple silicon M1 or newer; no Windows desktop version listed |
| Account/price | Instagram sign-in; free download |
| Editing | Multi-track timeline, keyframes, audio waveforms |
| Color/type | Wheels, curves, LUT imports, font-file imports |
| Captions | Unlimited automatic generation |
| Delivery | Horizontal/vertical formats, 4K without watermark, Instagram publishing |

From [November 5 desktop launch post](https://edits.instagram.com/blog/edits-desktop-video-editor/):

| Area | Additional capability |
| --- | --- |
| Cutting/color | Split, cut, trim, log conversions |
| Libraries | Licensed and royalty-free music, sound/video effects |
| Personalization | Saved mobile audio/text styles on desktop; customizable/imported shortcuts |
| Captions | Multiple languages |
| Agents | MCP enabled through Settings |
| Publishing | Tags, location, trial reels |
| Roadmap | Weekly updates; seamless mobile/desktop project editing still in progress |

Saved styles/audio do not establish complete project synchronization. These desktop sources do not establish an exact codec menu, frame-rate ceiling, maximum duration, caption-language list or universal keyboard bindings.

## Installed-build evidence

Read-only inspection of `/Applications/Edits.app/Contents/Info.plist` on the research Mac found Edits 454.0.0, internal version 454.0.0.38.112, build 1106192771, bundle ID `com.burbn.basel.mac`, minimum macOS 15.1. This is one build's requirement, not a promise about future releases.

Bundled action strings cover projects, timeline, media, motion, color, captions, text, sound, voiceover, analysis and exports. See [tool-map.md](tool-map.md). Strings do not prove runtime availability.

## Mobile/general: verify desktop controls first

| Feature | Official source and distinction |
| --- | --- |
| Caption editing | [Captions](https://edits.instagram.com/tutorials/captions/): transcript correction, font/color customization; mobile toolbar |
| Advanced captions | [Subtitle guide](https://edits.instagram.com/blog/adding-video-subtitles/): word/auto highlights, capitalization, punctuation, profanity controls, bulk replacement; desktop parity unverified |
| Translation/lyrics | [Audio/captions update](https://edits.instagram.com/blog/multi-language-captions/): bilingual captions, lyrics, audio filters, audio extraction/import; multilingual transcription alone does not prove translation support |
| Sound | [Audio tutorial](https://edits.instagram.com/tutorials/advanced-audio-editing-tools/): music/voice/SFX imports, noise reduction, balancing, fades |
| Motion | [Keyframes](https://edits.instagram.com/tutorials/keyframes/): clip zooms, text, overlays, cutouts; discover desktop properties |
| Text styles | [Text styling](https://edits.instagram.com/tutorials/text-styling/): spacing, outline width, colors, presets |
| Object effects | [Effects](https://edits.instagram.com/tutorials/effects/): object-targeted effects; effect tags differ from account tags |
| Cinematic treatment | [Filter/crop/blur](https://edits.instagram.com/tutorials/cinematic-filters-crop/): composition/background treatments |
| Templates | [Templates](https://edits.instagram.com/tutorials/template/): reuse timing/design with replacement clips and creator credit |
| Versions/alignment | [Workflow update](https://edits.instagram.com/blog/workflow-editing/): versions, snapping, template overlays/locks; 15-minute export statement explicitly iOS-specific |
| AI Restyle | [Restyle](https://edits.instagram.com/tutorials/restyle/) and [effects update](https://edits.instagram.com/blog/video-effects/): presets/prompts, regional/usage limits; tutorial's 10-second clip limit is not universal across effects |
| Carousels | [Announcement](https://edits.instagram.com/blog/edits-carousel-editor/): launch instructions specify iOS; desktop unverified |
| In-app assistant | [Announcement](https://edits.instagram.com/blog/edits-assistant/): US rollout, account insights/ideas, daily prompt limit; distinct from external Claude/Codex control |
| Capture/scripts | [Camera](https://edits.instagram.com/tutorials/enhanced-camera/), [teleprompter](https://edits.instagram.com/tutorials/teleprompter/): mobile filming/countdown/scripts; bundled desktop teleprompter names do not prove camera parity |
| Planning | [Ideas](https://edits.instagram.com/tutorials/ideas/), [storyboards](https://edits.instagram.com/tutorials/storyboards/), [inspiration](https://edits.instagram.com/tutorials/creative-copilot/): notes, references, shot planning, recommendations |
| Green screen | [Guide](https://edits.instagram.com/blog/using-green-screens/): live/imported-media workflows; source describes phone processing |

Do not assume Intel/Windows support, full mobile parity, cloud handoff, particular paid tiers, every language, cross-platform music rights or an exhaustive public API.
