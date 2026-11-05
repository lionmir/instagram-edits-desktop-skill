# Shipped action discovery map

Names below were observed in executable strings in installed build 454.0.0.38.112 on 2026-11-05. These are **discovery hints**, not authenticated tools, schemas, or execution-tested API contracts. Actions may be internal, wrapped, gated, screen-dependent or stubs. Call only tools/actions actually exposed by the connected server, using live schemas.

For a complete function request, inspect current manifests and capabilities across home/editor when practical. Record purpose, screen, input schema, effect on project, dependencies and implementation status. If no suitable project is open, report editor coverage as uninspected rather than creating an unwanted project.

## App, projects and archives

`appState`, `getCapabilities`, `projects`, `newProject`, `openProject`, `closeProject`, `saveProject`, `renameProject`, `duplicateProject`, `deleteProject`, `toggleFavorite`, `togglePin`, `homeSelection`, `exportMcomp`, `importMcomp`, `duplicateViaMcomp`.

Resolve project identities from current results. Archive support does not establish lossless mobile interchange. Inspect compatibility errors before relying on `.mcomp` export. Destructive actions need user scope to cover them.

## Media and inspection

`state`, `clips`, `tracks`, `elements`, `getElement`, `clipMetadata`, `mediaStatus`, `mediaBin`, `searchMedia`, `probeMedia`, `addMedia`, `importMedia`, `importToMediaBin`, `importToMediaPanel`, `getMediaPanelItems`, `getMediaPanelSort`, `setMediaPanelFilter`, `setMediaPanelSort`, `openMediaManager`, `addLibraryMedia`, `addGif`.

Bin import and timeline insertion differ. Inspect duration, dimensions, orientation, frame rate, sound and missing-media status.

## Playback and selection

`seek`, `play`, `pause`, `step`, `playFromStart`, `togglePlayback`, `getLoop`, `setLoop`, `jumpToNextClip`, `debugPlayhead`, `select`, `selectById`, `clearSelection`, `selectAll`, `copy`, `paste`, `keyPress`.

Check time units and selection model. Keyboard bindings are configurable.

## Timeline construction

`split`, `splitClip`, `splitAt`, `duplicate`, `delete`, `trim`, `trimStart`, `trimEnd`, `trimClip`, `slipClip`, `move`, `reorderClip`, `rippleState`, `setRippleTiers`, `undo`, `redo`, `convertToMain`, `moveToLayer`, `setLayerVisibility`.

Distinguish source/timeline ranges. Refresh elements after topology/ripple changes before reusing IDs and positions.

## Canvas, transforms and compositing

`getCanvas`, `setCanvas`, `setAspectRatio`, `setFrameRate`, `setProjectDynamicRange`, `projectDynamicRange`, `getTransform`, `setTransform`, `setTransforms`, `setFlip`, `setCrop`, `clearCrop`, `cropClip`, `autoReframe`, `splitScreen`, `addOverlay`, `addSticker`, `addStickerFromCutout`, `addShape`, `setMask`, `toggleMaskKeyframe`, `setOpacity`.

Read coordinate conventions and fit/crop modes. Check subject framing and visible layer order throughout the shot.

## Motion, transitions and speed

`getTransformKeyframes`, `setTransformKeyframes`, `removeTransformKeyframe`, `toggleKeyframe`, `setKeyframeEasing`, `addTransition`, `transitions`, `listTransitionsCatalog`, `setSpeed`, `setSpeedCurve`, `listSpeedCurvePresets`, `selectSpeedPanelPreset`, `setReversed`, `reverseClip`, `cancelReverse`.

Read actual presets, properties, easing enums and duration units. Speed changes alter duration/sync. Reverse can require an asynchronous job.

## Color, LUTs, filters and effects

`getColor`, `getAdjustState`, `setHSL`, `setColorWheel`, `setCurve`, `setColorGrade`, `applyAdjust`, `showAdjust`, `applyLUT`, `listFilters`, `applyFilter`, `listEffects`, `applyEffect`, `applySubjectEffect`, `trackObject`, `listCatalog`, `listCatalogKinds`, `getCatalogItem`, `updateCatalogItem`, `removeCatalogItem`.

Inspect grade, source log/HDR and catalog IDs. Avoid double conversions. Check whether tracking/effects depend on jobs or network services.

## Text, fonts and styles

`addText`, `createTextSticker`, `editText`, `setTextPosition`, `setTextStyle`, `setTextFont`, `setTextAnimation`, `setTextVisibility`, `setEmphasis`, `listTextPresets`, `applyTextPreset`, `listFonts`, `importAccountFont`, `deleteAccountFont`.

Retrieve real font/style IDs. Check duration, wrapping and contrast in output preview. Local import does not prove cross-device portability.

## Captions and generated speech

`transcribeClip`, `generateCaptions`, `captions`, `deleteCaptions`, `listCaptionStyles`, `setCaptionStyle`, `editCaption`, `splitCaption`, `mergeCaptions`, `setCaptionHighlights`, `setCaptionHighlightColor`, `listTTSVoices`, `applyTextToSpeech`.

Transcript analysis, timeline captions, translation, lyrics and narration differ. Inspect existing captions to avoid duplicates. Retrieve languages/voices; proofread and preview.

## Mix and audio analysis

`getSound`, `setSound`, `getAudioState`, `audioLevels`, `getVolume`, `setVolume`, `setFade`, `setDucking`, `muteTrack`, `unmuteTrack`, `extractAudio`, `replaceAudio`, `setSoundBypass`, `setVoiceEnhance`, `sampleOutputLevel`, `loudness`, `quietPoint`, `findPauses`, `audioSpectrum`, `audioOnsets`, `audioChords`, `processAudio`.

Discover gain units and enhancement controls. Preserve sync after extraction/replacement. Listen for clipping, speech damage and abrupt boundaries.

## Music, SFX and beats

`openMusicLibrary`, `browseMusicCategories`, `searchMusic`, `getMusicTrackList`, `getMusicTrackDetails`, `listMusicTracks`, `getSavedTracks`, `previewMusicTrack`, `favoriteMusicTrack`, `addSongToComposition`, `addMusicTrack`, `trimMusicClip`, `expandMusicClip`, `removeMusicTrack`, `licensedMusicStatus`, `getSyncState`, `listSoundEffects`, `searchSoundEffects`, `previewSoundEffect`, `addSoundEffect`, `replaceSoundEffect`, `deleteSoundEffect`, `muteSoundEffect`, `splitSoundEffect`, `dragSoundEffectTrack`, `beatMarkers`, `addBeatMarker`, `removeBeatMarker`, `setBeatDensity`.

Search current catalogs. Account, region and intended use can affect eligibility. Licensed and royalty-free music are distinct. Beat alignment should preserve speech meaning.

## Voiceover and teleprompter

`recordVoiceover`, `startVoiceoverRecording`, `stopVoiceoverRecording`, `cancelVoiceoverRecording`, `getVoiceoverState`, `getVoiceoverPanelState`, `getVoiceoverRecordingState`, `getVoiceoverAudioLevels`, `listVoiceoverClips`, `setVoiceoverVolume`, `slipVoiceover`, `deleteVoiceoverClip`, `openTeleprompter`, `closeTeleprompter`, `getTeleprompterText`, `setTeleprompterText`, `listTeleprompterScriptKeys`, `getCountdownEnabled`, `setCountdownEnabled`.

Recording needs a recording request; writing a script alone does not imply microphone capture. These names do not establish desktop camera parity.

## Preview, analysis and delivery

`describeClip`, `sampleFrames`, `captureSourceFrames`, `captureFrame`, `frameSheet`, `detectCuts`, `detectShots`, `detectSubjects`, `previewVideo`, `previewVideoStatus`, `previewVideoFrames`, `export`, `exportStatus`, `cancelExport`, `jobStatus`, `wait`, `title`, `setTitle`.

Source frames and composited frames differ. Verify rendered text/grade/layers and async job completion. No publishing action was authenticated during research; discover actual posting support before promising automated publishing.

## UI controls

`tools`, `selectTool`, `dismissTool`, `scrollToTool`, `pressControl`, `scrollToControl`, `scroll`, `getZoom`, `setZoom`, `speedPanel`, `selectSpeedTab`, `valueFields`, `editValueField`, `selectVolumeTab`, `openVolumePanel`, `dismissVolumePanel`, `dismissSpeedPanel`, `dismissTransformPanel`, `dismissOpacityPanel`, `getToast`, `dismissToast`, `toggleApplyAll`.

Prefer semantic operations where available. Retrieve controls afresh rather than reusing stale UI indexes. Live server can provide separate screenshot/progress tools.
