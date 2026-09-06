# Work Handoff — Cinematic Gameplay Camera

## Status
Design prepared. Current salon camera remains the live baseline.

## Read first
1. `docs/CINEMATIC_GAMEPLAY_CAMERA_LANGUAGE.md`
2. `data/camera_zone_profiles_1982.json`
3. `docs/PHANTOM_CAMERA_SPRINT5_SPIKE.md`
4. `docs/CHRISTMAS1982_BLOCKING.md`

## Core decision
BO keeps authored fixed/semi-fixed cinematic framing.
Do not convert to unrestricted 360 mouse-look or a conventional over-the-shoulder camera.

## Existing baseline
Preserve `scenes/piste_0/christmas_1982/cinematic_camera.gd` until live comparison proves a better presentation layer.

## Future grammar
- C0 anchored tableau;
- C1 soft bounded follow;
- C2 threshold handoff;
- C3 rare beat emphasis;
- C4 listening composition;
- C5 broader exterior authored frame.

## First future proof
After Sprint 5 live acceptance + house shell readiness:
1. keep salon camera A;
2. add one corridor anchor B;
3. test one threshold only;
4. compare CUT vs short blend;
5. preserve screen direction and player control;
6. verify active REC continues across the transition;
7. do not add camera ownership to Recorder/MaloController.

## Interaction rule
Do not auto-center/zoom every interactable.
Camera may help staging but world affordance must remain understandable independently.

## Recorder rule
REC is not automatically a camera event.
Do not snap/zoom when REC starts.
Do not stop REC for camera transitions.

## Accessibility
Future reduced-camera-motion setting may prefer cuts and smaller moves.
It stays independent from guidance and story content.

## Phantom Camera
Default remains: do not adopt unless one real authored handoff problem is demonstrated and the addon clearly improves it without becoming a runtime gameplay dependency.

## Validation
Use `tests/static_validate_camera_design.py` once present, plus Sprint 5 validation.
