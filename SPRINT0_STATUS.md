# Sprint 0 status — BO_Ta_Vie

## Implemented

- `Christmas1982` main scene with placeholder 3D geometry.
- Controllable `MaloController`.
- Semi-fixed cinematic camera with limited follow.
- Generic `Interactable` base.
- `FisherPrice` interactable device.
- Device-agnostic `Recorder` state machine: STOP / REC / PLAY.
- Independent `RecordingClip` resources.
- Generic `RecordableSource`.
- `RonanTest` recordable placeholder source.
- Hold-to-record (`R`) and release-to-stop.
- Latest-clip playback (`P`).
- Minimal HUD showing STOP / REC / PLAY, timer, source and controls.
- Placeholder audio for RonanTest.

## Deliberately not implemented

- MK2.
- Pitch control.
- Sound-on-Sound.
- Multitrack recording.
- Inventory, dialogue system, save system or narrative branching.
- Final characters, room art, animations or production audio.

## Validation performed in this environment

`tests/static_validate.py` verifies project structure, all scene resource paths, input actions, required class declarations, recorder API and placeholder WAV integrity.

The current execution environment does **not** contain a Godot binary, so the authoritative Godot parser/runtime smoke test has not been executed here. The included `tests/test_recorder.gd` is ready for Godot 4.7.2 headless execution.

## Godot runtime checks to run locally

```bash
godot --headless --path . --editor --quit
godot --headless --path . --script res://tests/test_recorder.gd
```

Then launch `Christmas1982` and validate the playable loop:

1. Move Malo to Fisher Price.
2. Press `E`.
3. Move near RonanTest.
4. Hold `R` for 1–3 seconds.
5. Release `R` and confirm STOP + stored clip.
6. Press `P` and confirm PLAY + audio playback.
