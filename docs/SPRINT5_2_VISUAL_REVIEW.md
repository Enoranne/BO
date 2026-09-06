# Sprint 5.2 — Visual Slice Review

## Purpose
Validate that `Christmas1982_VisualSlice.tscn` reads as an authored late-1970s / early-1980s family interior rather than a technical greybox, while preserving the exact Sprint 4 gameplay loop and blocking.

## A/B scenes
- **A — baseline:** `scenes/piste_0/christmas_1982/Christmas1982.tscn`
- **B — visual slice:** `scenes/piste_0/christmas_1982/Christmas1982_VisualSlice.tscn`

The wrapper must not replace the canonical scene until B is visually and functionally accepted.

## Expected B-pass differences
### Materials
- walls read as warm cream rather than saturated brown blocks;
- floor reads darker and warmer, giving the furniture more separation;
- rug remains matte and muted;
- sofa becomes a restrained brown/orange fabric mass;
- coffee table and mantel read as dark varnished wood;
- fireplace surround becomes warm stone;
- Fisher Price reads beige with a burgundy front-panel accent.

### Lighting
- fireplace remains the dominant motivated warm source on the left;
- Christmas tree adds a softer secondary warm pool on the right;
- directional fill is reduced so the scene keeps depth and brown shadows;
- Malo, Ronan and the Fisher Price must remain readable at all gameplay positions.

### Set dressing
The visual-only layer adds:
- cream skirting boards on visible walls;
- a dark wood fireplace mantel;
- three sofa cushions;
- sparse muted-red tree ornaments.

These objects must never introduce collisions or alter navigation.

### UI cleanliness
- debug-world labels over Fisher Price and Ronan are hidden in B;
- HUD contextual guidance remains available;
- the player must still understand what can be interacted with.

## Mandatory camera checks
Capture the same framing in A and B from `CameraStart` and compare:
1. Malo silhouette against the floor/walls;
2. fireplace visual dominance without clipping into black;
3. sofa separation from the back wall;
4. Christmas tree readability on the right;
5. gift/Fisher pickup area readability;
6. Ronan readability from `RonanRecordBeat`.

## Mandatory gameplay regression path
In B, complete exactly:

`Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY`

Verify:
- Malo reaches Fisher Price;
- left-click/E interaction both work;
- Fisher Price pickup still reveals the held recorder;
- REC lamp still follows real Recorder state;
- RonanTest recording is created;
- Space/P playback still works;
- no visual-only object blocks the player;
- objective progression remains FIND_FISHER -> RECORD_RONAN -> PLAY_RECORDING -> COMPLETE.

## Go / no-go criteria
### GO to Sprint 5.3 if
- B is clearly more authored than A at first glance;
- atmosphere reads Christmas 1982 without becoming orange monochrome;
- silhouettes and interaction targets remain readable;
- all existing gameplay tests pass;
- no visual-only element intersects Malo/Ronan/Fisher in a distracting way.

### NO-GO / revise 5.2 if
- room becomes too dark or too orange;
- Fisher Price becomes harder to find after hiding its world label;
- cushions/mantel/ornaments visibly float or intersect;
- lighting flattens Malo or Ronan;
- any gameplay or blocking contract regresses.

## After acceptance
Only after this A/B review is accepted should Sprint 5.3 begin the Higgsfield 3D asset pipeline with one low-risk prop test before larger asset replacement.
