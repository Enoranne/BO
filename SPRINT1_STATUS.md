# Sprint 1 Status — Recorder Core Hardening

## Goal

Preserve the only accepted gameplay loop:

`Malo -> Fisher Price -> REC -> RonanTest -> STOP -> PLAY`

while decoupling proximity selection, recorder state, device state and HUD feedback.

## Implemented

- Added `InteractionContext` as the single proximity-selection component.
- `Interactable` now exposes prompt, priority, enable/disable and `can_interact()`.
- `RecordableSource` now exposes enable/disable, priority and metadata.
- `MaloController` delegates proximity selection to `InteractionContext`.
- Public player actions added: `try_begin_recording()`, `try_stop_recording()`, `try_play_latest()`.
- REC is refused before Fisher Price is equipped.
- REC is refused without a nearby recordable source.
- Recorder refuses concurrent REC/PLAY operations.
- `RecordingClip` now stores source title, duration, creation timestamp and metadata.
- Fisher Price has explicit `PLACED / EQUIPPED / ACTIVE` device states.
- Recorder exposes future-safe capability descriptors for track count, pitch and Sound-on-Sound, without implementing those systems.
- HUD now reacts to context prompts and rejected recorder actions.
- Added recorder contract tests and a scene-level gameplay contract test.
- Added `tests/run_headless.sh` for local Godot validation.

## Validation in this environment

- `python tests/static_validate.py`: **0 failures**.
- Godot engine runtime: **not available in this container**, therefore the authoritative GDScript parse/headless tests still need to run locally or through Godot-MCP.

## Authoritative local test

```bash
./tests/run_headless.sh
```

Then launch `Christmas1982` and verify:

1. Malo starts without a recorder.
2. REC before pickup is rejected.
3. E near Fisher Price equips it.
4. Move near RonanTest.
5. Hold R: state becomes REC and time increases.
6. Release R: state becomes STOP and exactly one RecordingClip is created.
7. P: state becomes PLAY and RonanTest audio is heard.
8. Playback returns to STOP.
