# Sprint 5 — Interaction & HUD UX

## Objective
Make BO's interface feel like a discreet narrative-game layer rather than a debug dashboard, while preserving the existing Sprint 4/5 interaction and Recorder contracts.

The HUD must remain presentation-only. `Recorder`, `InteractionContext`, `MaloController` and `Christmas1982Director` remain the sources of gameplay truth.

## Current prototype problem
The canonical HUD deliberately exposes everything at once:

- objective;
- recorder state;
- timer;
- current source;
- interaction / control hint.

This is useful for development but visually heavy for the Christmas1982 vertical slice.

## Design principles

### 1. World first
The salon, Malo, Ronan and the Fisher Price should dominate the frame. UI must never become the primary focal point.

### 2. Context instead of instruction walls
Show the smallest instruction needed for the current action.

Examples:

- near Fisher Price: `E / click  Take`;
- near Ronan with recorder: `Hold R  Record`;
- after a clip exists: `Space  Play`;
- rejected action: a short temporary explanation.

Do not teach every future action simultaneously.

### 3. Recorder feedback should feel diegetic where possible
The carried Fisher Price REC lamp is the preferred recording-state cue. HUD REC feedback remains as accessibility / prototype reinforcement, not the sole source of truth.

### 4. STOP is neutral
STOP should not visually compete with REC. REC is the exceptional state; STOP is the resting state.

### 5. Warm analogue visual language
Use warm cream / paper / tungsten-compatible neutrals. Avoid modern cyan/teal, neon gaming UI and glossy sci-fi panels.

### 6. No permanent crosshair
Current interaction is proximity/context based, not raycast aiming. Do not introduce a crosshair merely because mouse input exists.

## Sprint 5 Visual Slice hierarchy

### Objective
Small and quiet. It establishes intent but should not look like a quest tracker.

Preferred phrasing:

- `Find the Fisher Price`
- `Record Ronan`
- `Play it back`

Avoid permanently prefixing the visible line with a large `OBJECTIVE` label in final presentation.

### Recorder state
Priority order:

1. `● REC` — high visibility while recording;
2. `▶ PLAY` — medium visibility during playback;
3. `STOP` — low-emphasis neutral state.

### Timer
Useful primarily during REC and immediately after clip creation. It should be subordinate to state.

### Source
Useful development information but not necessarily final-player information. Keep it visually de-emphasised in Sprint 5 and consider removing it from the production HUD once sound-source readability is validated.

### Hint
The most context-sensitive element. It should be readable quickly and disappear from attention when no decision is required.

## Prototype input wording

- `E / click  Take`
- `Hold R  Record`
- `Release R  Stop`
- `Space  Play`

`P` remains technically supported during Sprint 5.1, but the presentation should teach **Space** as the primary playback action so the UI does not display two equivalent keys forever.

## Feedback timing

- normal contextual hint: persistent only while context remains valid;
- rejection / error: ~1.5 s is acceptable for the prototype;
- recording-saved acknowledgement: ~1.5 s;
- no modal confirmation for ordinary recording actions.

## Visual Slice presentation pass
`visual/period_1982_hud_pass.gd` may adjust only presentation properties on the existing HUD instance:

- font sizes;
- warm neutral text colours;
- opacity / emphasis;
- spacing / margin values;
- wording that does not change gameplay meaning.

It must not:

- emit gameplay actions;
- call Recorder methods;
- select interactables;
- own objectives;
- change input mappings;
- require a new UI addon.

## Acceptance review in Work
Compare canonical HUD vs Visual Slice HUD from the locked camera.

The Visual Slice version passes if:

1. the environment is visually dominant;
2. Fisher / Ronan actions remain understandable without world debug labels;
3. REC is obvious within one second;
4. STOP is less visually aggressive than REC;
5. Space is learned as the preferred PLAY command;
6. no important gameplay information becomes ambiguous;
7. the first-recording loop remains unchanged.

## Deferred
Do not implement yet:

- radial menus;
- inventory UI;
- cassette library browser;
- subtitle system redesign;
- remapping UI;
- accessibility presets;
- point-and-click reticle;
- MK2 multitrack interface;
- Radio Malo interface.
