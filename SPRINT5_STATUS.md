# Sprint 5 — Visual Vertical Slice

## Goal
Transform the existing Christmas1982 greybox into a convincing playable visual slice while preserving the validated Sprint 4 gameplay loop and presentation contract.

The gameplay loop remains:

`Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY`

Sprint 5 is primarily a **visual, environmental and cinematographic** sprint. It must not broaden gameplay scope.

## Target outcome
A player should be able to launch `Christmas1982`, understand the salon as a believable late-1970s / early-1980s family interior, identify Malo/Ronan/Fisher Price immediately, complete the first-recording beat, and feel that the project has moved from technical greybox toward an authored narrative game.

## Planned work
- Preserve all existing spatial blocking markers and gameplay positions.
- Improve salon proportions, architectural readability and set dressing.
- Establish a reusable 1982 material palette: wood, wallpaper, carpet/rug, upholstery, painted surfaces and warm plastics.
- Improve practical lighting around fireplace and Christmas tree without changing gameplay visibility.
- Improve Malo and Ronan placeholder readability without treating them as final likenesses.
- Evaluate `Cyclops Level Builder` for faster room construction and future house expansion.
- Evaluate `Phantom Camera` as an optional camera implementation detail behind the existing cinematic camera contract.
- Document a controlled adoption path for external open-source tools.

## Explicitly not added
- inventory;
- save/load;
- dialogue tree;
- NPC navigation or open-world simulation;
- Radio Malo;
- MK2 mechanics;
- pitch, Sound-on-Sound or multitrack;
- combat, vehicles, GTA-style systems;
- final production character likenesses.

## Acceptance contract
1. The Sprint 4 first-recording beat order remains FIND_FISHER -> RECORD_RONAN -> PLAY_RECORDING -> COMPLETE.
2. Malo can still reach the Fisher Price and RonanTest without collision regressions.
3. REC/STOP/PLAY behaviour remains owned by the existing Recorder system.
4. Spatial locks in `docs/CHRISTMAS1982_LAYOUT.md` and `docs/CHRISTMAS1982_BLOCKING.md` remain valid unless a specific visual change is documented.
5. Visual improvements remain separable from gameplay logic.
6. Any external addon is evaluated on a branch-safe, reversible basis and must not become a hard dependency before validation.
7. Static validation must still report `0 failure(s)`.
8. Godot headless acceptance tests must still pass when the runtime is available.
9. Real editor/MCP visual inspection is required before Sprint 5 can be considered visually accepted.

## Current state
- Branch: `sprint-5`
- Base: Sprint 4 commit `41e0cfd8ec1682a7b056c343828094405911e42d`
- Status: planning/scaffolding started; no gameplay change yet.
