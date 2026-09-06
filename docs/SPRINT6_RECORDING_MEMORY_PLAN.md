# BO_Ta_Vie — Sprint 6 candidate plan: recordings become memories

## Status
Design preparation only. Do not start this sprint until Sprint 5 is live-engine validated.

## Sprint thesis
Sprint 6 should prove one thing:

> A recording can become personally meaningful after it has been captured, without turning the game into an inventory manager.

The sprint should stay compact. It does not need Radio Malo, MK2, pitch, Sound-on-Sound, multitrack or a full house.

## Proposed playable proof
Use the existing Christmas1982 slice and add only enough functionality to support:

1. create at least two recordings;
2. play them back later;
3. assign or accept a child-like title;
4. mark one as `BIEN` or `RATÉ MAIS GARDER`;
5. place/review it through a physical cassette/box metaphor;
6. reopen it later and hear the same recording.

The key proof is persistence of *meaning*, not quantity of content.

## Recommended first sources

### Required anchor
`ronan_test`

Keep the current onboarding source as the compatibility bridge.

### First additional source
Prefer `gate_squeak` if the garden/gate exists by then.

Why:
- discrete and recognisable;
- easy to retry;
- interesting at different speeds/distances;
- strongly compatible with `RATÉ MAIS GARDER`;
- supports temporal capture architecture.

If the gate is not yet playable, use a small salon source such as wrapping paper or a Fisher mechanical sound before expanding world scope.

## Minimal domain additions

### 1. Stable recording identity
Each recording needs a stable id independent of its display title.

Do not use `clip_name` as identity.

### 2. `MemoryAnnotation`-style layer
A separate data object/resource should reference a recording id and hold:
- display title;
- keep state;
- favourite flag;
- child note;
- box assignment;
- optional memory associations.

Do not put all editorial state directly into `Recorder`.

### 3. Small library/repository service
Owns the association between recordings and annotations.

Responsibilities:
- add recording;
- retrieve recording by stable id;
- update annotation;
- enumerate a small collection;
- later persist/restore.

Non-responsibilities:
- audio DSP;
- world interaction selection;
- HUD state;
- device-specific mechanics.

### 4. Physical review surface
Preferred prototype options:

A. one cassette box/desk surface in Malo's room;
B. a simple physical cassette tray near the Christmas scene if bedroom is not ready.

Avoid implementing a generic pause-menu inventory for the proof.

## Suggested implementation order

### 6.0 — Architecture proof
- stable recording ids;
- annotation data model;
- in-memory library service;
- tests only;
- no persistence yet.

### 6.1 — Review loop
- newly created recording enters `UNREVIEWED`;
- playback available;
- title can be accepted/edited/left blank;
- choose one simple keep state;
- no deletion.

### 6.2 — Physical metaphor
- one world-space cassette/box review point;
- show only a small number of recordings;
- tactile selection and playback;
- no full-screen library by default.

### 6.3 — Persistence
- save/load only after data model survives the previous steps;
- preserve recording identity + annotation;
- ensure audio backing is restorable.

### 6.4 — Second source / failed take
- add gate or equivalent retryable source;
- demonstrate that a technically imperfect take can be deliberately kept;
- no quality score.

## Acceptance scenario

A valid Sprint 6 vertical proof might be:

1. Malo records Ronan.
2. Clip appears as `UNREVIEWED`.
3. Malo plays it back.
4. Player accepts/edits a child-like title such as `RONAN`.
5. Player classifies it `BIEN`.
6. Malo records a second sound badly.
7. The second clip can still be heard.
8. Player classifies it `RATÉ MAIS GARDER`.
9. Both are visible through the physical cassette/box metaphor.
10. Leaving and returning preserves both recordings and their judgements once persistence is enabled.

## UX rule
The player should not spend more time organising recordings than listening to them.

Target interaction ratio:
- capture/listen: primary;
- title/keep: secondary;
- organisation: tertiary.

## Narrative rule
`IMPORTANT` must not become a disguised quest-item rarity tier.

A recording becomes important because of story context or later memory association, not because the UI awards it a gold badge.

## Deletion / overwrite
Defer destructive deletion.

If later introduced, prefer physical consequences:
- overwriting tape;
- losing a cassette;
- reusing limited medium;
- intentional erasure.

This is more faithful to BO than a generic Delete button.

## Sprint 6 non-goals
- Radio Malo;
- MK2;
- pitch;
- Sound-on-Sound;
- multitrack;
- cloud/media library UI;
- automatic speech transcription;
- rarity/score systems;
- dozens of recording sources;
- collectible completion percentage;
- inventory grids.

## Dependency on Sprint 5
Do not begin implementation until:
- Sprint 5 player feel is accepted;
- Visual Slice is accepted or consciously revised;
- Recorder regression tests pass;
- live interaction loop remains stable.

If Sprint 5 reveals fundamental Recorder problems, fix those first rather than layering memory management on top.
