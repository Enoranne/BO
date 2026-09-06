# Sprint 5 — Phantom Camera evaluation spike

## Purpose
Evaluate Phantom Camera only as a possible **implementation aid** for BO's existing cinematic-camera contract.

The design target does not change: BO uses fixed / semi-fixed authored framing, not a free third-person GTA-style camera.

## Preconditions
Do not install or enable Phantom Camera until:

1. Sprint 5.2 Visual Slice has been reviewed in the current `CinematicCamera`;
2. the first-recording gameplay loop passes regression tests;
3. the 5.4 architectural shell has at least a stable doorway/corridor composition, or there is a specific camera limitation to solve.

If the existing camera already satisfies the shot, there is no reason to add the addon.

## Current camera contract to preserve
The canonical camera currently provides:

- fixed cinematic anchor;
- limited follow around Malo's spawn anchor;
- deliberately constrained X/Z displacement;
- authored FOV;
- no player-controlled 360-degree orbit;
- no dependency from Recorder/gameplay code.

`scenes/piste_0/christmas_1982/cinematic_camera.gd` remains the contract owner during the experiment.

## Test cases

### Case A — current salon framing
Reproduce the current Christmas1982 opening/first-recording framing with Phantom Camera behind the abstraction.

Success means:
- same or better Malo/Fisher/Ronan readability;
- no perceptible camera jitter;
- no loss of authored composition;
- no gameplay code changes.

### Case B — corridor threshold
After the 5.4 shell exists, test one authored transition near the salon/corridor threshold.

Goal:
- smoothly shift emphasis from salon to corridor when Malo reaches a future trigger region;
- preserve orientation so the player does not become spatially confused;
- keep transition duration restrained and cinematic.

This is an evaluation only; the corridor does not need to become playable during Sprint 5.

### Case C — Fisher Price emphasis
Optionally test a short priority-camera emphasis around the Fisher Price pickup beat.

The camera must not become an interactive inspection orbit. It should behave like a directed shot.

## Isolation rule
If Phantom Camera is tested:

- add an adapter/presentation layer around or beside `CinematicCamera`;
- do not make `MaloController`, `Recorder`, `InteractionContext` or `Christmas1982Director` depend on Phantom Camera classes;
- keep the canonical camera implementation available for immediate rollback;
- introduce no more than one camera addon during the spike.

## Acceptance matrix
Adopt Phantom Camera only if it clearly improves at least two of:

1. authored transition quality;
2. camera-zone authoring speed;
3. target-follow stability;
4. future room-to-room camera scalability.

And it must not worsen:

- deterministic framing;
- player orientation;
- project maintainability;
- addon-free fallback;
- headless/gameplay test stability.

## Reject conditions
Reject the addon for Sprint 5 if:

- it encourages free-camera design;
- it requires gameplay code to know addon classes;
- equivalent behaviour is simpler in the current ~1 kB `cinematic_camera.gd`;
- it introduces fragile scene priorities before the house layout is stable;
- it complicates Godot 4.7.x compatibility.

## Evidence required from Work
If tested, report:

- current camera A screenshot/video;
- Phantom-equivalent B screenshot/video;
- scene-tree integration path;
- files changed;
- whether the current camera can be restored by disabling/removing the adapter;
- explicit KEEP or DISCARD verdict.

## Default decision
**Do not adopt by default.** BO's current camera is intentionally simple. Phantom Camera earns a place only by solving a demonstrated authoring problem.
