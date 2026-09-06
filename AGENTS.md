# BO_Ta_Vie — Agent Rules

## Project scope

This repository is the Godot prototype for **La Bande originale de ta vie — PISTE 0 / Christmas1982**.

The only gameplay loop currently in scope is:

`Malo -> Fisher Price -> REC -> capture RonanTest -> STOP -> PLAY`

Do not add unrelated systems, mechanics, menus, progression, inventory, combat, crafting, open-world features, MK2 features, pitch, Sound-on-Sound, multitrack, or production art unless explicitly requested.

## Godot MCP

This project is intended to use the `godot-mcp` server from `@yanhuifair/godot-mcp`.

Rules for Codex/Astra:

- Never guess MCP tool names. Use `search_tools` first with a precise keyword.
- Begin every new session with `get_status`.
- If the editor or runtime bridge is unavailable, call `get_status`, report what is missing, and stop retrying blindly.
- Prefer file-level tools when a change does not require the live editor.
- Use `editor_*` tools only for live editor operations.
- Use `runtime_*` tools only after the game is actually running.
- Read a scene before changing its node hierarchy.
- Read a script before rewriting it.
- When an editor command fails, inspect the scene tree/property/class information before retrying.
- If an editor scene edit is wrong, prefer the MCP undo operation instead of reconstructing the previous state manually.
- After each meaningful code or scene change, validate scripts/project references before launching the game.
- Keep all changes small and reversible. Commit a working state before broad edits.

## Acceptance test for Sprint 2

A Sprint 2 change is accepted only if the recorder path still works and the visual greybox remains traversable:

1. Launch `Christmas1982`.
2. Move Malo.
3. Interact with the Fisher Price.
4. Approach `RonanTest`.
5. Hold REC.
6. Release REC to STOP and create a `RecordingClip`.
7. Press PLAY.
8. Hear the captured RonanTest source.
9. HUD reflects STOP / REC / PLAY and recording duration.
10. REC before Fisher Price pickup is rejected cleanly.
11. A second REC/PLAY operation cannot start while the Recorder is busy.

12. The salon greybox remains bounded and the sofa, fireplace, coffee table and tree collisions do not make the Fisher Price or RonanTest unreachable.

No visual improvement is more important than preserving this loop.

## Sprint 3 character/blocking lock

- Preserve `PlaceholderHumanoid3D` as temporary art only; do not treat its proportions/colors as final character likeness.
- Preserve the `Blocking/*` markers as staging contracts unless a task explicitly revises scene blocking.
- Do not add NPC AI, navigation, dialogue trees or a full animation state machine while validating Sprint 3.
- Malo's placeholder gait may be corrected for engine/runtime issues, but the gameplay loop and input contract must remain unchanged.

## Sprint 4 lock
- Preserve the first-recording beat order: FIND_FISHER → RECORD_RONAN → PLAY_RECORDING → COMPLETE.
- `Christmas1982Director` is presentation-only; do not move Recorder logic into it.
- `FisherPriceVisual` observes Recorder state; it must not become a second recorder implementation.
- Do not add inventory, dialogue, save/load, Radio Malo or MK2 mechanics while validating Sprint 4.

## Sprint 5 visual vertical-slice lock
- Sprint 5 improves environment, lighting, materials, character readability and cinematography; it does not broaden the gameplay loop.
- Preserve the spatial contracts in `docs/CHRISTMAS1982_LAYOUT.md` and `docs/CHRISTMAS1982_BLOCKING.md` unless a task explicitly revises and documents them.
- Treat `docs/VISUAL_VERTICAL_SLICE.md` as the visual acceptance target.
- Follow `docs/OPEN_SOURCE_ADOPTION.md` before introducing an external addon or imported asset.
- Introduce at most one runtime addon at a time and keep its integration isolated and reversible.
- Do not replace `Recorder`, `InteractionContext`, `MaloController` or the Sprint 4 presentation ownership model with addon-specific logic.
- `Cyclops Level Builder` should be evaluated first as an editor productivity tool, not as a gameplay dependency.
- `Phantom Camera` may be evaluated only behind the existing cinematic-camera contract; gameplay code must not depend directly on it.
- Do not integrate Dialogue Manager, Godot State Charts, inventory, NPC navigation, Radio Malo, MK2, pitch, Sound-on-Sound or multitrack during Sprint 5 unless the sprint scope is explicitly changed.

## Sprint 5.1 player-feel lock
- Movement remains action-based and uses the physical WASD cluster, giving WASD on QWERTY and ZQSD on AZERTY.
- The numeric keypad must not be required for core play.
- `E` and left mouse button are equivalent context-interaction inputs; left click is not a raycast targeting system yet.
- `R` remains hold-to-REC and release-to-STOP.
- `Space` is the preferred PLAY-latest input while legacy `P` remains accepted during the prototype.
- Do not add unrestricted mouse-look or a GTA-style free camera during Sprint 5.1.
- Input changes must continue to route through Godot actions; do not hard-code keyboard or mouse events into `Recorder` or interaction domain logic.

## Sprint 5.4 architecture lock
- Treat `data/christmas1982_house_zones.json` as a planning contract, not runtime truth.
- The salon remains the canonical anchor and its current blocking markers are not moved during the Cyclops spike.
- Build only architectural context first: wall thickness, one doorway, corridor suggestion and shallow kitchen glimpse.
- Corridor and `kitchen_glimpse` begin as non-playable visual depth; do not create new objectives there.
- Use `docs/SPRINT5_4_ARCHITECTURE_EXECUTION.md` as the execution order and stop conditions.
- Use `docs/CHRISTMAS1982_SOUND_MAP.md` only to justify future room value; do not implement those future sound sources during the 5.4 shell spike.
- Cyclops must remain an authoring accelerator only. Do not create gameplay logic that depends on Cyclops nodes or classes.
- If Cyclops cannot be cleanly converted/exported to ordinary Godot-friendly geometry, discard the addon experiment rather than coupling the project to it.

## Sprint 5 HUD UX lock
- The canonical `Christmas1982.tscn` development HUD keeps its existing defaults; the cinematic treatment is opt-in through `Christmas1982_VisualSlice.tscn`.
- `RecorderHUD` remains presentation-only. Do not move Recorder state ownership, clip storage, interaction selection or input handling into the HUD.
- Visual Slice hints are context-first: take → record → release to stop → play. Do not show every available command simultaneously.
- Teach `Space` as the player-facing PLAY command; legacy `P` may remain supported internally during Sprint 5.1 but should not dominate the production-facing HUD.
- Do not add a permanent crosshair or reticle while interaction remains proximity/context based.
- REC may receive stronger visual emphasis; STOP should remain neutral and subordinate.
- Prefer warm cream / analogue-compatible UI colours. Do not introduce cyan/teal or modern neon-gaming UI language.
- Treat `docs/HUD_UX_SPRINT5.md` as the presentation contract and validate with `tests/static_validate_hud_ux.py`.

## Higgsfield credit-safety lock
- Follow `docs/HIGGSFIELD_CREDIT_POLICY.md` before submitting any new Higgsfield generation/import workflow.
- Read-only inspection/search/retrieval of existing project state is preferred when it can answer the question.
- Before any image/video/audio/3D generation or any mutation with unclear billing behaviour, tell the user what is being submitted and that it may consume credits unless a reliable zero-cost guarantee exists.
- Do not batch-generate BO assets before one candidate has completed the full asset → Godot → rights/performance review loop.
- The existing coffee-table 3D Jutsu import is a technical candidate only; the user's observation that credits appeared unchanged does not establish that future operations are free.

## Sprint 6 cassette-memory design lock
- Sprint 6 cassette/memory documents on `sprint-5` are preparation only. Do not implement them before Sprint 5 live-engine acceptance.
- Keep raw `RecordingClip` data separate from Malo's editorial/memory layer. Do not add `keep_state`, favourite, box assignment or child-title ownership directly to `Recorder`.
- Stable recording identity must be independent from display titles such as `RONAN`, `PORTAIL` or `VENT FORT`.
- No global recording-quality score, rarity system or collectible completion percentage.
- `GOOD` and favourite are distinct; a failed take may be emotionally important or a favourite.
- Preserve `FAILED_KEEP` / `RATÉ MAIS GARDER` as a first-class editorial state.
- Retry does not imply deletion; early childhood gameplay should avoid a generic destructive Delete command.
- Prefer a physical cassette/box review metaphor before a full-screen media-library UI.
- Playback/listening is the primary review action; naming and classification remain secondary.
- Read `docs/CASSETTE_MEMORY_STATUS.md` first for the compact handoff, then `docs/CASSETTE_LIBRARY_DESIGN.md`, `data/cassette_memory_schema.json`, `docs/CASSETTE_PHYSICAL_UX.md` and `docs/SPRINT6_RECORDING_MEMORY_PLAN.md` if implementation is explicitly authorised later.

## PISTE 0 narrative-beat design lock
- `docs/PISTE0_NARRATIVE_GAMEPLAY_BEATS.md`, `docs/PISTE0_PLAYABLE_STRUCTURE.md` and `data/piste0_narrative_beats.json` are design preparation, not an implementation mandate during Sprint 5.
- Keep the mandatory spine extremely small. The only currently implemented required recording remains `ronan_test`.
- Do not add a quest log, minimap objectives, sound-collection percentage, XP, rarity or `MISSION PASSED/FAILED` language for PISTE 0 memory beats.
- Prefer guidance through sound first, then character movement, composition/light, object animation and only then a contextual prompt.
- Gate, wind, fridge, moped, gull and other memory beats should generally be optional or semi-optional and tolerate imperfect/missed recordings.
- Do not make players collect a fixed number of sounds to unlock story progression.
- A failed recording may remain valuable; do not automatically replace it when the player retries.
- Do not couple `Recorder` or `InteractionContext` directly to narrative beat IDs. Future beat orchestration belongs in presentation/narrative layers above the domain contracts.
- Radio Malo and MK2 beats are later evolution stages, not Sprint 5 feature requests.
- Validate the planning boundary with `tests/static_validate_piste0_narrative_design.py`.
