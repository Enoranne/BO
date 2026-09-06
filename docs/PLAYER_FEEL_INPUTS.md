# Sprint 5.1 — Player Feel / Input Contract

## Goal
Make the first playable seconds of BO understandable without adding gameplay complexity or changing the cinematic camera contract.

## Keyboard layout policy
Movement uses Godot physical-key bindings rather than letter semantics.

That means the same physical four-key cluster works across common layouts:

- QWERTY: `W A S D`
- AZERTY: `Z Q S D`

The numeric keypad is deliberately not part of the core control scheme.

## Current bindings

| Action | Primary | Alternate | Behaviour |
|---|---|---|---|
| Move | WASD / ZQSD physical cluster | — | Move Malo |
| Interact | `E` | Left mouse button | Use the currently selected nearby interactable |
| Record | Hold `R` | — | Begin recording the currently selected nearby recordable source |
| Stop recording | Release `R` | — | Stop REC and create the RecordingClip |
| Play latest | `Space` | `P` | Play the latest RecordingClip |

## Mouse policy for Sprint 5.1
Left click is currently an alternate **context action**, not a point-and-click raycast.

The player still has to move Malo close enough for `InteractionContext` to select an object. Clicking then performs the same action as `E`.

This preserves the existing interaction architecture and avoids introducing cursor targeting before the camera language has been validated.

## Camera policy
Sprint 5.1 does not add free-look or unrestricted 360-degree mouse camera control.

The cinematic fixed/semi-fixed camera remains authoritative. A later experiment may allow subtle gaze/aim offset for examining or recording sounds, but it must not turn BO into a conventional third-person action camera.

## Design intent
Controls should become progressively less visible to the player:

1. walk to an interesting object;
2. interact with one obvious context action;
3. hold REC while listening;
4. release to stop;
5. press Space to hear the result.

The Fisher Price itself may later gain an authored REC / STOP / PLAY presentation layer, but it must continue to drive the existing `Recorder` instance rather than become a second recorder implementation.

## Deferred
- gamepad mapping;
- remapping UI;
- accessibility presets;
- mouse raycast targeting;
- camera look offset;
- MK2-specific controls;
- cassette/pitch/Sound-on-Sound controls.
