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
