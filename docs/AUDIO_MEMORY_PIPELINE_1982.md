# BO_Ta_Vie — Audio Memory Pipeline 1982

## Purpose

Define the sonic identity that separates BO from a conventional exploration game.

A meaningful sound can exist in three perceptually distinct states:

1. **WORLD** — what Malo hears in the room or outdoors;
2. **FISHER CAPTURE** — what the child's built-in microphone manages to record;
3. **CASSETTE PLAYBACK** — what Malo hears when the captured sound is played back from the recorder.

This document defines creative targets only. It does **not** add DSP, new gameplay requirements, or new mandatory recordings to Sprint 5. `ronan_test` remains the only required recording for Sprint 5 acceptance.

## Core principle

The recording must not sound like a clean digital copy of the world.

The player should be able to close their eyes and understand whether they are hearing:

- the real environment;
- Malo listening through the limitations of his recorder;
- or a memory being replayed from cassette.

The degradation is not a punishment. It is part of the emotional reward: **Malo transforms reality simply by recording it.**

---

# 1 — WORLD layer

WORLD audio is the spatial and physical truth of the scene.

Characteristics:

- normal environmental frequency range;
- source-appropriate transient detail;
- 3D distance and orientation;
- room / outdoor acoustic context;
- obstruction and sound bleed when relevant;
- no cassette hiss or tape flutter;
- no artificial lo-fi filter merely because the story is set in 1982.

The world itself should not sound like an old movie. The *recording device* creates the archival character.

---

# 2 — FISHER CAPTURE layer

The Fisher Price recording is a child's imperfect acoustic photograph.

## Creative baseline

Suggested starting values for later Godot/audio implementation. These are tuning targets, not measured hardware specifications.

- mono capture;
- high-pass target: roughly 120–180 Hz;
- low-pass target: roughly 5.5–6.5 kHz;
- gentle midrange emphasis around speech / mechanical detail;
- mild dynamic compression / automatic-level feeling;
- softened very sharp transients;
- modest saturation on louder moments;
- audible but restrained recorder self-noise;
- subtle distance-dependent loss of clarity;
- no stereo spatial image retained in the stored clip.

## Microphone behaviour

### Sweet spot

Approximate creative target: **0.35–1.20 m** from a source.

Inside this range:

- source is recognisable;
- enough room remains to feel homemade;
- dialogue remains intelligible;
- mechanical details remain interesting.

### Too close

Below roughly 0.25–0.35 m:

- transient thumps can become aggressive;
- breath / handling detail increases;
- louder events may saturate;
- low-frequency mechanical bumps become more obvious before filtering.

This can later create playful experimentation without becoming a fail state.

### Far away

Beyond roughly 2–3 m:

- room / environment increasingly dominates;
- consonants and small mechanical details soften;
- noise becomes more perceptible relative to source;
- the recording remains usable as memory, even if less technically clean.

## Important rule

Do **not** make weak recordings useless. A distant or imperfect recording may be emotionally more interesting than a perfect one.

---

# 3 — CASSETTE PLAYBACK layer

Playback adds a second transformation on top of the captured signal.

Suggested starting character:

- same mono image as the recorded clip;
- slightly narrower top end than capture monitor target;
- small additional saturation;
- consistent low-level hiss;
- very subtle wow/flutter rather than caricature;
- small transport start/stop mechanical signature;
- speaker coloration: modest low end, strong readable midrange, softened highs;
- playback volume should feel like a small physical recorder in a room, not headphones glued to the player's ears.

The cassette effect must remain subtle enough that Ronan's recorded voice is emotionally readable.

---

# Device mechanics as punctuation

The Fisher Price should have a recognisable tactile grammar:

- **REC press** — firm mechanical clack;
- **transport engage** — short internal mechanism response;
- **recording** — no exaggerated continuous machine noise required, only restrained physical presence;
- **STOP** — satisfying release / disengage click;
- **PLAY** — distinct transport engagement;
- **playback start** — a very short gap before recorded content can help sell the cassette medium;
- **playback end** — optional mechanical tail / hiss bed depending on implementation.

These mechanics should eventually become as recognisable as UI sounds in another game, but remain diegetic.

---

# P0 sound treatments

## A. Gate — `gate_squeak`

### WORLD

- metallic hinge with a stable tonal identity;
- initial hand/latch impulse if used;
- squeak changes slightly with speed;
- outdoor reflections minimal;
- wind may coexist but must not mask the hinge signature.

### FISHER CAPTURE

- metallic midrange becomes more prominent;
- deepest metal resonance is reduced;
- close capture can become slightly abrasive / saturated;
- distance removes fine scraping detail faster than the main squeal;
- mono collapse makes the event feel more like an object Malo has collected.

### CASSETTE PLAYBACK

- squeal remains immediately identifiable;
- high metallic edge softens;
- hiss is audible in the gaps;
- slight tape instability may make the sustained squeak feel uncannily alive.

### Narrative function

This is a candidate **signature sound** for BO. It should be recognisable when heard again much later, even under another recorder generation.

---

## B. Wind in the tree — `garden_wind_tree`

### WORLD

- moving layers: broad wind, leaves, occasional branch movement;
- gust rhythm matters more than raw loudness;
- avoid storm-scale drama;
- room for Mother's distant call in the known PISTE 0 scene.

### FISHER CAPTURE

- the microphone should struggle slightly with gusts;
- low-frequency wind energy is reduced but not entirely absent;
- stronger gusts can create soft overload / turbulence character;
- leaf detail collapses into a textured midrange wash at distance;
- the result should feel like Malo trying to capture something inherently difficult.

### CASSETTE PLAYBACK

- hiss partially blends with recorded wind;
- gust envelopes remain clear;
- fine leaf detail is reduced;
- the boundary between tape noise and wind can become poetically ambiguous.

### Narrative function

Wind demonstrates that recording is not only collection but interpretation: the recorder cannot capture wind exactly, yet the failure becomes a memory texture.

---

## C. Kitchen fridge — `kitchen_fridge_hum`

### WORLD

- period domestic compressor hum with subtle mechanical cycling;
- low-mid body rather than modern near-silence;
- occasional cabinet/resonance component possible;
- should sit under conversation rather than dominate it.

### FISHER CAPTURE

- deep fundamental is reduced;
- harmonics / buzz become proportionally more important;
- from close range the recorder may reveal a surprisingly musical drone;
- room tone remains around it;
- mono capture can make it feel like a tiny found synthesiser.

### CASSETTE PLAYBACK

- hum loses further low-end weight;
- midrange drone survives;
- hiss can make steady-state sections feel denser;
- slight transport instability gives the drone character without turning it into an effect gag.

### Narrative function

The fridge teaches Malo that a boring household machine can become musical material. It also supports the existing mother/fridge comic beat.

---

## D. Fisher buttons and transport — `fisher_button_mechanics` / `fisher_transport_click`

### WORLD

- firm plastic/mechanical action;
- different signatures for REC, STOP and PLAY where feasible;
- tactile, not modern membrane-button soft;
- close and dry because Malo is physically holding the device.

### FISHER CAPTURE

Normally these mechanics are **device punctuation rather than a recordable world source** during Sprint 5.

Later, if self-recording / feedback experimentation is introduced, device handling can bleed naturally into recordings rather than being treated as a separate collectible source.

### CASSETTE PLAYBACK

A recorded button or handling sound, when it exists later, should sound especially intimate and oversized because it happened very close to the microphone.

### Narrative function

Buttons are the physical verbs of the game. Their sound should reinforce state changes without requiring HUD confirmation.

---

## E. Fireplace — `fireplace_crackle`

### WORLD

- low restrained bed;
- intermittent tiny crackles;
- occasional stronger pop, but no constant cinematic explosion;
- warmth should come partly from its location and lighting association, not only EQ.

### FISHER CAPTURE

- low rumble decreases;
- small crackles remain surprisingly clear;
- louder pops can saturate briefly;
- room noise becomes part of the recording;
- distance determines whether the clip feels like 'fire' or 'Christmas room'.

### CASSETTE PLAYBACK

- small crackles survive well;
- low-end warmth becomes thinner;
- hiss occupies similar spectral space to the smallest fire texture;
- recording should evoke a room memory rather than a high-fidelity fireplace sample.

### Narrative function

The fireplace is the acoustic glue of Christmas1982 and can become a subtle memory bed in later recalls.

---

## F. Moped pass — `street_moped_pass`

### WORLD

- period-appropriate small two-stroke character;
- clear approach → closest point → departure;
- Doppler/spatial movement should be felt naturally;
- the source exists to suggest the wider world, not vehicle gameplay.

### FISHER CAPTURE

- mono recording collapses the spatial trajectory, but level/timbre evolution still communicates movement;
- low-end engine body decreases;
- raspy upper-mid two-stroke character survives strongly;
- distant beginning/end can fall toward noise floor;
- a capture started too late should still create an interesting fragment rather than fail.

### CASSETTE PLAYBACK

- trajectory becomes a temporal memory rather than a spatial spectacle;
- tape hiss is most audible before approach and after departure;
- engine buzz remains recognisable;
- light wow/flutter should not compete with the natural pitch movement of the pass-by.

### Narrative function

The moped proves that a tiny domestic micro-hub can imply an entire world through sound alone.

---

# Ronan — canonical first test

`ronan_test` is the first opportunity to demonstrate the complete WORLD → CAPTURE → PLAYBACK idea.

For Sprint 5 acceptance the implementation may remain technically simple, but the eventual target is:

### WORLD

Ronan sounds present in the room and spatially anchored.

### FISHER CAPTURE

His voice becomes narrower, mono, slightly compressed, less polished, with room and distance embedded into the clip.

### CASSETTE PLAYBACK

The same voice becomes unmistakably 'just recorded' — close enough to recognise Ronan emotionally, transformed enough to feel magical to Malo.

The first playback is therefore not merely confirmation that REC worked. It is the first thematic statement of the game.

---

# Future implementation architecture — not Sprint 5 scope

When implemented later, avoid baking destructive processing into source assets.

Prefer a layered architecture:

`World source → capture profile → RecordingClip metadata / rendered capture → playback profile`

A future device profile can then change capture/playback character without changing `RecordableSource` or Malo:

- Fisher Price — narrow, noisy, intimate;
- MK2 — wider / more controlled;
- later devices — progressively different capabilities.

This supports the existing device-agnostic Recorder architecture.

## Metadata worth preserving later

Potential fields:

- source id;
- source title;
- capture device id;
- distance at capture;
- zone / room;
- capture timestamp;
- capture profile version;
- optional clipping / overload indicator;
- future pitch / track metadata only when those systems exist.

Do not add these fields to Sprint 5 gameplay merely because they are listed here.

---

# Acceptance principle

A good BO recording should satisfy all three:

1. **Recognisable** — the player can identify what Malo recorded.
2. **Transformed** — playback is clearly not identical to the world source.
3. **Emotional** — the transformation makes the recording feel more personal, not merely lower quality.

If the effect only sounds 'bad' or 'retro', it has failed.