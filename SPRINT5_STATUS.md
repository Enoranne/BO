# Sprint 5 — Visual Vertical Slice

## Goal
Transform the existing Christmas1982 greybox into a convincing playable visual slice while preserving the validated Sprint 4 gameplay loop and presentation contract.

The gameplay loop remains:

`Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY`

Sprint 5 is primarily a **visual, environmental and cinematographic** sprint. It must not broaden gameplay scope.

## Target outcome
A player should be able to launch `Christmas1982`, understand the salon as a believable late-1970s / early-1980s family interior, identify Malo/Ronan/Fisher Price immediately, complete the first-recording beat, and feel that the project has moved from technical greybox toward an authored narrative game.

## Implemented scaffolding
- Branch `sprint-5` created directly from Sprint 4 commit `41e0cfd8ec1682a7b056c343828094405911e42d`.
- Sprint 5 lock added to `AGENTS.md`.
- Reusable period palette documented in `docs/MATERIAL_PALETTE_1982.md`.
- Six external Godot material resources added under `materials/period_1982/`.
- Presentation-only material override utility added at `visual/period_1982_visual_pass.gd`.
- Reversible wrapper scene added at `scenes/piste_0/christmas_1982/Christmas1982_VisualSlice.tscn`.
- Wrapper instances the canonical Sprint 4 scene rather than replacing it.
- Dedicated Sprint 5 static contract added at `tests/static_validate_sprint5.py`.
- Compact house expansion documented in `docs/CHRISTMAS1982_HOUSE_EXPANSION.md`.
- Cyclops evaluation protocol documented in `docs/CYCLOPS_SPRINT5_SPIKE.md`.
- Open-source adoption rules documented in `docs/OPEN_SOURCE_ADOPTION.md`.

## Sprint 5.1 — Player Feel
Implemented without changing `MaloController`, `Recorder` or `InteractionContext` domain behaviour:

- movement remains on Godot physical WASD positions, which correspond to WASD on QWERTY and ZQSD on AZERTY;
- `E` remains interaction;
- left mouse button is now an alternate context-interaction input;
- `R` remains hold-to-REC and release-to-STOP;
- `Space` is now the preferred PLAY-latest input;
- legacy `P` PLAY remains available during the prototype;
- the numeric keypad is not required;
- HUD hints teach the new controls;
- `docs/PLAYER_FEEL_INPUTS.md` documents the contract;
- `tests/static_validate_player_feel.py` validates the input architecture.

Left click currently acts on the interactable already selected by `InteractionContext`; it is deliberately not a point-and-click raycast yet. No unrestricted mouse-look has been added.

## Material targets currently prepared
- warm cream wallpaper;
- dark varnished wood;
- muted brown/orange upholstery;
- muted brown carpet/rug;
- aged Fisher Price beige plastic;
- muted burgundy Fisher Price panel plastic.

## Explicitly not added
- inventory;
- save/load;
- dialogue tree;
- NPC navigation or open-world simulation;
- Radio Malo;
- MK2 mechanics;
- pitch, Sound-on-Sound or multitrack;
- combat, vehicles, GTA-style systems;
- final production character likenesses;
- mouse raycast selection;
- free 360-degree camera;
- numeric-keypad dependency.

## Acceptance contract
1. The Sprint 4 first-recording beat order remains FIND_FISHER -> RECORD_RONAN -> PLAY_RECORDING -> COMPLETE.
2. Malo can still reach the Fisher Price and RonanTest without collision regressions.
3. REC/STOP/PLAY behaviour remains owned by the existing Recorder system.
4. Spatial locks in `docs/CHRISTMAS1982_LAYOUT.md` and `docs/CHRISTMAS1982_BLOCKING.md` remain valid unless a specific visual change is documented.
5. Visual improvements remain separable from gameplay logic.
6. Any external addon is evaluated on a branch-safe, reversible basis and must not become a hard dependency before validation.
7. `tests/static_validate.py` must still report `0 failure(s)`.
8. `tests/static_validate_sprint5.py` must report `0 failure(s)`.
9. `tests/static_validate_player_feel.py` must report `0 failure(s)`.
10. Godot headless acceptance tests must still pass when the runtime is available.
11. Real editor/MCP visual and input inspection is required before Sprint 5 can be considered accepted.

## Next live-engine validation
When Godot / Work is available:

1. run `tests/static_validate.py`;
2. run `tests/static_validate_sprint5.py`;
3. run `tests/static_validate_player_feel.py`;
4. run the existing headless Godot suite;
5. test movement on the available keyboard layout;
6. verify `E` and left click both take the Fisher Price when in interaction range;
7. verify hold/release `R` still creates the RonanTest clip;
8. verify `Space` and `P` both play the latest clip;
9. open canonical `Christmas1982.tscn` and capture the baseline camera view;
10. open `Christmas1982_VisualSlice.tscn` and compare the same view;
11. verify held Fisher Price receives beige/burgundy presentation overrides after pickup;
12. only after that begin the Cyclops architectural-shell spike.

## Current state
- Branch: `sprint-5`.
- Canonical gameplay architecture: preserved.
- Visual wrapper: created, not yet engine-validated.
- Player Feel 5.1 bindings: implemented, not yet engine-validated.
- Gameplay mechanics added in Sprint 5.1: none; only alternate input bindings and HUD guidance.
- Visual/input acceptance: pending live Godot/MCP inspection.
