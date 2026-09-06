# Sprint 4 — First Recording Presentation

## Goal
Make the existing `Malo → Fisher Price → REC RonanTest → STOP → PLAY` loop visually legible without expanding gameplay scope.

## Added
- `FisherPriceVisual` procedural carried-device placeholder.
- Held Fisher Price appears on Malo only after pickup.
- REC indicator on the carried device follows the real Recorder state.
- `Christmas1982Director` presentation-only beat progression.
- HUD objective line for Find Fisher → Record Ronan → Play recording → Complete.
- `test_presentation_contract.gd` headless acceptance test.
- presentation lock documentation.

## Explicitly not added
- inventory or equipment menus;
- save/load;
- dialogue tree;
- NPC navigation;
- Radio Malo;
- MK2 mechanics;
- pitch, Sound-on-Sound or multitrack;
- final character or prop assets.

## Acceptance contract
1. Malo starts with no carried recorder visible.
2. Taking Fisher Price reveals the carried placeholder and binds it to the equipped Recorder.
3. HUD objective advances to Ronan.
4. REC makes the carried device REC lamp visible.
5. STOP creates the RonanTest clip and switches the lamp off.
6. HUD asks the player to PLAY the recording.
7. PLAY followed by STOP marks the first-recording presentation beat complete.
8. Existing gameplay and visual/blocking contracts remain unchanged.

## Validation
- Static validator: must report `0 failure(s)`.
- Godot tests: `tests/run_headless.sh` now includes the Sprint 4 presentation contract.
- Real engine/MCP visual inspection remains required before final acceptance.
