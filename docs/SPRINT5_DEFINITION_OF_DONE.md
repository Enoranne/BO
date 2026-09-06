# Sprint 5 — Definition of Done

## Purpose
Prevent Sprint 5 from expanding indefinitely. The sprint is complete when the Christmas1982 vertical slice is visually convincing, playable, stable and still architecturally clean — not when every future idea has been implemented.

## Non-negotiable blockers
Sprint 5 cannot be accepted if any of these is true:

- `Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY` is broken;
- Malo cannot reliably reach Fisher Price or Ronan;
- Recorder state ownership moved into UI / Director / imported asset code;
- canonical blocking markers were accidentally moved;
- the Visual Slice fails to load cleanly;
- input is unusable on the available keyboard layout;
- Visual Slice readability is worse than the canonical greybox;
- an external addon becomes a required runtime dependency without explicit approval;
- a production asset has unknown/unacceptable provenance or license status.

## Weighted scorecard
Target: **80/100 minimum**, with no non-negotiable blocker.

### 1. Core gameplay integrity — 25 points
- 5 — Fisher Price cannot be used before pickup and pickup works once.
- 5 — Ronan source can be recorded.
- 5 — release R stops and creates the clip.
- 5 — Space plays the latest clip; P remains compatible during prototype.
- 5 — objective beat completes without state desynchronisation.

### 2. Player feel / controls — 15 points
- 5 — WASD/QWERTY and ZQSD/AZERTY physical-layout intent works.
- 3 — E and left click both perform contextual interaction.
- 3 — hold/release R feels understandable.
- 2 — Space is the obvious PLAY action.
- 2 — no unnecessary numeric-keypad or free-camera dependence.

### 3. Visual identity — 20 points
- 5 — palette clearly reads warm late-70s / early-80s rather than generic greybox.
- 5 — fireplace / tree practical-light hierarchy feels motivated.
- 4 — sofa, wood, floor, walls and Christmas dressing form a coherent period palette.
- 3 — Fisher Price reads as a special object rather than a beige cube.
- 3 — frame avoids modern teal/neon/game-UI contamination.

### 4. Gameplay readability — 15 points
- 4 — Fisher Price location/action remains understandable without floating world debug label.
- 4 — Ronan is clearly distinguishable from Malo.
- 3 — recording state is obvious within one second.
- 2 — Visual Slice HUD is readable but subordinate to the scene.
- 2 — player can infer the next step without an instruction wall.

### 5. Camera / composition — 10 points
- 4 — locked/semi-fixed framing preserves first-recording staging.
- 2 — limited follow does not lose important objects.
- 2 — characters remain framed/readable during key actions.
- 2 — no nausea / uncontrolled mouse-look / GTA-style drift.

### 6. Technical stability / performance — 10 points
- 3 — static Sprint 5 contracts pass.
- 3 — Godot headless contracts pass.
- 2 — no obvious runtime errors or broken resource imports.
- 2 — frame pacing remains acceptable on development hardware.

### 7. Production maintainability — 5 points
- 2 — Visual Slice remains separable from canonical gameplay scene.
- 1 — imported assets remain replaceable.
- 1 — asset provenance is tracked.
- 1 — Cyclops/Phantom/Higgsfield remain tools/pipelines, not hidden gameplay dependencies.

## Visual target threshold
The visual objective is not “final game art”. It is:

> A player seeing a single locked-camera screenshot should recognise a warm Christmas 1982 family interior and understand that the Fisher Price is narratively important.

The slice should feel materially closer to a shippable narrative-game scene than to a greybox.

## Sprint 5 stop rule
Once the scorecard reaches 80/100 with no blockers:

- stop adding unrelated visual experiments;
- document accepted A/B evidence;
- commit/tag the accepted state;
- move new mechanics (sound collection, dialogue, living family, garden gameplay, MK2) to later sprints.

## Items allowed to remain placeholder after Sprint 5
If the visual target passes, Sprint 5 does **not** require:

- final character likenesses;
- final Fisher Price licensed/product-accurate mesh;
- complete house;
- playable kitchen/bathroom/garden;
- final dialogue system;
- Radio Malo;
- MK2;
- final sound library;
- final animation set.

## Evidence package for acceptance
Work should retain or describe:

1. canonical greybox screenshot A;
2. Visual Slice screenshot B;
3. optional Cyclops shell screenshot C;
4. short live gameplay validation of the full first-recording loop;
5. static/headless test results;
6. any accepted imported-asset comparison screenshot;
7. final scorecard with reasons for deductions.
