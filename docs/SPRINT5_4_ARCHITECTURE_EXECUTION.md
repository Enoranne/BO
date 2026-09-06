# Sprint 5.4 — Architecture / Cyclops execution plan

## Objective
Turn Christmas1982 from an isolated salon box into the first believable fragment of a compact family house, without expanding gameplay scope.

## Preconditions
Do not start the live architecture spike until:

1. `tests/static_validate.py` passes;
2. `tests/static_validate_sprint5.py` passes;
3. `tests/static_validate_player_feel.py` passes;
4. the Sprint 5.2 A/B visual review has been completed;
5. the canonical first-recording path still works.

If any precondition fails, fix it before architecture work.

## Working strategy
Use a temporary experimental scene/branch layer. The canonical `Christmas1982.tscn` remains the source of gameplay truth.

Recommended comparison states:
- A — canonical Sprint 4 scene;
- B — Sprint 5.2 Visual Slice;
- C — Sprint 5.4 architectural shell.

## Pass 1 — prove Cyclops value
Time-box the first experiment conceptually to the smallest possible shell.

Build only:
1. a replacement floor shell matching the current salon footprint;
2. back/left/right walls with believable thickness;
3. one doorway opening toward a corridor;
4. a 1.35 m-ish corridor suggestion extending 3–5 m;
5. one shallow kitchen-glimpse volume beyond the transition.

Do not rebuild:
- sofa;
- fireplace furniture detail;
- coffee table;
- tree;
- gifts;
- Malo/Ronan/Fisher;
- lights unless needed because of wall occlusion.

## Pass 2 — locked-camera check
From the canonical camera framing, verify:

- wall thickness is visible but not distracting;
- doorway adds depth instead of visual clutter;
- corridor does not create a bright/empty tunnel;
- kitchen glimpse reads as another room without becoming a second focal point;
- fireplace / Fisher / Ronan remain visually prioritised;
- no new wall intersects the locked camera or player route.

Capture C from the same framing used for A/B.

## Pass 3 — traversal check
Even if corridor remains non-playable, verify the new shell does not alter:

- Malo spawn;
- Fisher pickup route;
- Ronan recording range;
- interaction sensor behaviour;
- camera offsets;
- existing collisions of sofa/table/tree/fireplace.

No new collision is accepted merely because Cyclops generated it automatically. Collision must be intentional.

## Pass 4 — period read
Use only existing Sprint 5 palette materials initially.

Target read:
- warm cream walls;
- dark warm floor / trim hierarchy;
- non-modern proportions;
- no bright white surfaces;
- no glossy contemporary interior language.

Do not texture-detail the corridor before geometry is accepted.

## Pass 5 — decision gate
Cyclops is retained only if it improves at least three of these five categories:

1. authoring speed;
2. wall/doorway iteration speed;
3. visual depth;
4. geometric cleanliness;
5. export/replaceability.

And it must not worsen:
- gameplay stability;
- scene maintainability;
- camera consistency.

If the addon creates fragile scene ownership or runtime dependency, discard it and reproduce the accepted shell with native Godot meshes or exported GLTF.

## Indicative spatial contract
The planning data lives in `data/christmas1982_house_zones.json`.

Key values for 5.4:
- salon stays at current ~12 x 8 m footprint;
- corridor target width ~1.35 m;
- corridor height target ~2.65 m;
- kitchen glimpse target ~3.8 x 3.4 m;
- all new dimensions are adjustable after camera review;
- canonical blocking markers are not adjustable in this sprint.

## Acoustic design check
Use `docs/CHRISTMAS1982_SOUND_MAP.md` only as future-facing architecture rationale.

The corridor should already support the *idea* of sound bleed through layout, but no new Recorder source is required in Sprint 5.4.

## Required screenshots / evidence
Work should capture or report:

1. canonical A;
2. Visual Slice B;
3. Cyclops shell C;
4. scene tree showing experimental geometry isolation;
5. gameplay acceptance after C.

## Stop conditions
Stop the spike immediately if:

- canonical blocking must be moved to make Cyclops fit;
- Recorder or interaction scripts need modification;
- the addon forces runtime coupling;
- conversion/export cannot produce ordinary Godot-friendly geometry;
- camera framing becomes worse than B with no clear architectural benefit.

## Success output
A successful 5.4 handoff contains:

- one accepted architectural shell;
- one documented doorway/corridor relationship;
- one shallow kitchen glimpse;
- A/B/C visual evidence;
- gameplay regression pass;
- a clear keep/discard decision for Cyclops.

Only after this should the house become genuinely traversable beyond the salon.
