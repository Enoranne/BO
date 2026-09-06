# Work Handoff — Character Animation / Gesture Layer

## Status
Design prepared. Do not implement a full production animation system before Sprint 5 live acceptance and authored-rig availability.

## Read first
1. `docs/CHARACTER_GESTURE_LANGUAGE.md`
2. `data/character_gesture_catalog_1982.json`
3. `docs/CHARACTER_ANIMATION_ARCHITECTURE.md`
4. `docs/CHARACTER_GESTURE_SEQUENCE_CARDS.md`
5. `docs/CHARACTER_ART_DIRECTION_1982.md`

## Current reality
`PlaceholderHumanoid3D` is a procedural proxy with simple arm/leg gait and idle sway.

Do not turn the primitive placeholder into a fake final animation rig.

## Core architecture decision
Gameplay owns logic. Animation owns presentation.

- `MaloController` owns movement/input intent.
- `Recorder` owns STOP/REC/PLAY and clip creation.
- object/device systems own their physical/domain state.
- future `CharacterAnimationPresenter` observes signals/read-only state and maps them to semantic animation intents.
- narrative/director layers request authored reactions.

No Recorder action should fail only because an animation clip is missing.

## Semantic animation intents
Prefer high-level intents:
- `IDLE`
- `LOCOMOTION`
- `LISTEN`
- `PICKUP_FISHER`
- `CARRY_RECORDER`
- `PRESS_REC`
- `RECORDING_HOLD`
- `PRESS_STOP`
- `PRESS_PLAY`
- `NOTICE_SOURCE`
- `REACTION_SHORT`
- `OPEN_HINGE`
- `HANDLE_CASSETTE`

Do not put vendor/rig-specific clip names into gameplay scripts.

## P0 visual priorities
Before adding many clips, prove these in order:
1. Malo child locomotion silhouette;
2. quiet idle/listening;
3. Fisher carry pose;
4. REC press timing;
5. STOP timing;
6. PLAY/listening distinction;
7. Fisher pickup transition;
8. Ronan simple reaction to being recorded.

## Player responsiveness
Ordinary interactions should remain short.

Targets:
- button press: ~0.15–0.35 s;
- Fisher pickup: ~0.7–1.4 s;
- simple hinge/latch: ~0.4–0.9 s.

Do not make routine gameplay feel like repeated mini-cutscenes.

## Root motion
Do not require root motion in the first pass.
Controller-authoritative locomotion remains preferred.

## Attention/look-at
Use cautiously.
Head/eyes first; avoid full-body forced auto-turns for ordinary sounds.
Never continuously gaze-track nearest `Interactable`.

## Animation failure fallback
If a gesture/clip is unavailable:
- gameplay continues;
- fall back to idle/carry pose;
- log/debug missing presentation intent;
- do not reject valid Recorder or interaction actions.

## Placeholder-safe tests
Before authored characters arrive, acceptable proxy tests are limited to:
- locomotion cadence;
- idle amount;
- facing readability;
- simple carried-recorder offset;
- rough timing of interaction beats.

Avoid creating detailed hand/finger production systems on primitive meshes.

## Authored rig acceptance
Validate candidates first in `CharacterReadabilityPreview.tscn`:
- age read;
- sibling hierarchy;
- silhouette at game camera distance;
- hand/arm suitability for recorder carry;
- deformation;
- head/neck look-at range;
- metre scale and skeleton cleanliness.

Only then test in `Christmas1982_VisualSlice.tscn`.

## Do not implement now
- giant AnimationTree/state machine;
- motion matching;
- complex full-body IK;
- facial capture/lip sync;
- ragdoll;
- combat locomotion;
- animation-owned REC/STOP/PLAY;
- animation-owned narrative progression.

## Validation
Use `tests/static_validate_character_animation_design.py` once present, plus `bash tests/run_sprint5_validation.sh`.
