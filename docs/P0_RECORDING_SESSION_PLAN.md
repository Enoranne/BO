# BO_Ta_Vie — P0 Recording Session Plan

## Purpose
Provide a repeatable capture procedure for the identity-critical sound families before any source is accepted as production audio.

This is not a requirement to record everything personally. It is a capture standard for original Foley/field recordings when practical, and a reference standard when evaluating library or generated substitutes.

## Session rules
- Preserve raw WAV masters.
- Target 48 kHz / 24-bit when the recorder/interface allows it.
- Record at conservative levels with headroom; do not chase maximum loudness.
- Capture at least 10–20 seconds of room tone for every new location.
- Slate or log each take immediately.
- Do not bake EQ, Fisher coloration, cassette hiss or strong compression into the source master.
- Record real physical variations instead of manufacturing all variation with pitch shifting.

## Take log fields
For every take record:

```text
family:
take:
location:
source/object:
distance:
angle:
performance/action:
channel format:
raw filename:
noise/problem notes:
provenance/owner:
approved for review: yes/no
```

# Session A — Fisher mechanics

## Goal
Build the recorder's physical sonic grammar.

### Setup
- quiet interior;
- microphone close enough to capture mechanism detail but not touching the housing;
- one alternate position slightly farther away for natural object perspective;
- recorder placed as it would plausibly be used by a child when possible.

### Capture list
For each mechanical state, record at least 4–6 isolated performances even if only 2–3 are eventually selected.

#### REC
- deliberate normal press;
- lighter press;
- firmer press;
- release;
- transport engagement after press if separately audible.

#### STOP
- normal press;
- quick press;
- release;
- transport disengagement.

#### PLAY
- normal press;
- light press;
- release;
- transport engagement.

#### Motor/transport
- motor start;
- steady short run if audible;
- motor stop;
- cassette inserted/removed only if narratively useful later.

### Review question
Can REC / STOP / PLAY be distinguished without looking at the device?

# Session B — Gate

## Goal
Create one recognisable recurring sound object rather than a generic library gate.

### Capture positions
1. close, roughly 0.5–1 m;
2. medium, roughly 2–3 m;
3. optional house/garden listening position for natural world perspective.

### Capture actions
- latch open × 3+;
- very slow opening × 3+;
- normal opening × 3+;
- faster opening × 3+;
- controlled close × 3+;
- latch close × 3+;
- optional firmer close/slam × 2;
- optional wind-driven micro-movement if authentic.

### Important
Keep the full action sequence on at least two long takes:

`hand/latch → opening squeak → pause → close → latch`

These long takes are useful for validating temporal recording causality.

# Session C — Fireplace

## Goal
Create a restrained domestic bed, not spectacle.

### Capture
- 2–3 long beds, ideally 45–90 seconds raw each;
- several isolated small pops;
- ember/log settling details;
- room tone with the fireplace quieter or absent if possible.

### Avoid
- overly close roaring flames;
- giant crack transients that read like cinematic effects;
- heavy denoising that removes the natural air of the room.

# Session D — Fridge

## Goal
Capture the machine as a stateful domestic appliance.

### Capture
- compressor off room tone;
- compressor start;
- at least 30 seconds steady compressor state;
- compressor stop;
- second full cycle if practical;
- optional fridge door/latch only as a separate future family.

### Distances
- close machine detail;
- typical child/listener position in the kitchen.

### Important
Do not edit a start/steady/stop cycle into physically impossible timing.

# Session E — Wind/tree

## Goal
Obtain long naturally varying beds with quiet gaps.

### Conditions
Prefer multiple short sessions under genuinely different wind conditions rather than trying to fake all intensity in post.

### Capture states
- calm leaf movement;
- medium wind;
- gust sequence;
- optional sheltered perspective;
- optional exposed perspective for future microphone-buffeting experiments.

### Raw duration
Aim for several minutes of usable material per weather state if practical.

### Avoid
- clipping from gusts;
- constant high wind that leaves no dynamic contrast;
- aggressive high-pass filtering in the source master.

# Session F — Moped

## Goal
Capture an authentic moving event with real timing and distance.

### Safety
Record only from a safe static location. No chase recording or behavior that distracts a rider/driver.

### Capture
If access to a suitable period-appropriate vehicle is practical:
- distant pass;
- medium residential pass;
- closer but safe pass;
- multiple genuine passes rather than digital duplication.

Capture several seconds before approach and several seconds after departure.

### Evaluation
The full approach → pass → recede envelope must be usable without reconstruction from tiny fragments.

# Session G — Ronan

## Goal
Keep onboarding intelligible while introducing natural human variation.

### Takes
- clean/clear canonical take;
- natural laugh or spontaneous alternate;
- slightly off-axis alternate;
- slightly more distant alternate;
- optional imperfect but charming take.

### Direction
Avoid performance that sounds like a voice actor demonstrating a game mechanic. It should feel overheard or naturally recorded by Malo.

# Post-session ingest

1. Copy raw files without renaming the originals destructively.
2. Back up the raw session.
3. Select candidates into the planned `audio/masters/...` structure.
4. Update `audio/audio_manifest.json` with exact provenance.
5. Rename only approved working masters according to `data/p0_sound_production_matrix.json`.
6. Do not create Fisher/cassette baked masters as the primary source assets.
7. Create preview derivatives only under `audio/previews/`.
8. Listen in context before `production_approved = true`.

# If using a library or generated substitute
Evaluate it against the same questions:
- does it have enough physical variation?
- does it support the required distances/timing?
- is provenance/licence documented?
- does it still read after Fisher/cassette transformation?
- does it sound period/plausibility appropriate?

A substitute is not acceptable simply because it is technically clean.
