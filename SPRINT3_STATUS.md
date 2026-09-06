# Sprint 3 Status — Character Presence & Blocking

## Goal

Give Malo and Ronan readable human placeholder silhouettes and establish explicit staging markers for the `Christmas1982` opening loop without adding gameplay scope.

## Implemented

- Added reusable procedural `PlaceholderHumanoid3D`.
- Malo now has child proportions with head, torso, arms, legs, feet and facing marker.
- Ronan now has a visibly taller older-brother silhouette.
- Malo placeholder gait is driven by actual horizontal movement speed.
- Ronan receives only a subtle idle sway; no NPC AI was added.
- Added blocking markers:
  - `MaloStart`
  - `FisherPickupBeat`
  - `RonanRecordBeat`
  - `RonanStand`
  - `CameraStart`
- Added `docs/CHRISTMAS1982_BLOCKING.md`.
- Added `tests/test_blocking_contract.gd` and wired it into the headless test runner.

## Acceptance contract

The existing loop remains unchanged:

`Malo → Fisher Price → REC → RonanTest → STOP → PLAY`

No dialogue system, NPC navigation, final character art, inventory, saves, Radio Malo, MK2, pitch, Sound-on-Sound or multitrack has been added.

## Validation

Run static validation:

```bash
python tests/static_validate.py
```

Run authoritative engine tests once Godot 4.7.x is available:

```bash
./tests/run_headless.sh
```

The final engine/MCP smoke test remains required because this build environment does not provide a Godot executable.
