# BO_Ta_Vie — PISTE 0 Implementation Rollout

## Status
**DESIGN ONLY.**

This is the preferred order for turning the prepared narrative beats into actual gameplay after Sprint 5 live acceptance.

The rule is deliberately conservative:

> prove one systemic capability with one small memory beat before expanding the world around it.

## Step 0 — Finish Sprint 5
Do not skip this gate.

Required:
- static contracts pass;
- Godot headless tests pass;
- Player Feel works live;
- Visual Slice is visually accepted or corrected;
- Fisher -> Ronan -> REC -> STOP -> PLAY is intact;
- first external GLB and Cyclops spike are judged rather than blindly adopted.

No broad narrative-beat implementation before this.

---

# Step 1 — Sprint 6.0: recording identity + minimal archive

## Prove
- stable recording IDs;
- separate memory annotation layer;
- in-memory archive;
- existing Ronan take can be reviewed without changing Recorder ownership.

## Content proof
Use **MB00 First Fisher** only.

Do not add a new world source yet.

## Why
This isolates archive/data risk from new audio-capture risk.

---

# Step 2 — Sprint 6.1/6.2: physical review language

## Prove
- optional child title;
- `BIEN`;
- `RATÉ MAIS GARDER`;
- physical cassette/box review surface;
- no modern inventory feel.

## Content proof
Use two or three existing/test recordings only.

## Why
The player must understand why imperfect recordings matter before the game creates many of them.

---

# Step 3 — Temporal capture proof

## Prove
- actual time-window capture between REC and STOP;
- WORLD -> capture -> cassette playback separation;
- anti-feedback routing;
- current Recorder API remains conceptually stable.

## Content proof
Start with a controlled temporary source in the salon or test scene.

Do not immediately build the garden.

---

# Step 4 — First new signature beat: Gate / BONJOUR

## Target beat
`MB02_gate_bonjour`

## Why gate first
The gate is the best systems proof because it combines:
- a tactile interaction;
- a highly recognisable transient sound;
- timing matters;
- repeatability exists without feeling artificial;
- accidental voice bleed can be meaningful;
- it naturally sits at the boundary between house and wider world.

## Minimum implementation
- small garden/gate access only;
- open/close interaction;
- latch + squeak sound event;
- temporal recording;
- optional neighbour `BONJOUR` variant/event;
- resulting recording can enter cassette review.

## Explicitly not required
- full street;
- NPC navigation;
- neighbourhood simulation;
- quest marker;
- quality score.

## Acceptance moment
Player can produce two different gate recordings and genuinely prefer the imperfect one for personal reasons.

---

# Step 5 — Wind / Mother's call

## Target beat
`MB03_wind_mother_call`

## New thing being proved
A passive, changing sound source rather than a button-triggered object.

## Minimum
- garden wind states;
- quiet/moderate/gust variation;
- player may wait or reposition;
- Mother's distant call can overlap occasionally under authored timing;
- recording may begin too early/late without failing gameplay.

## Why after gate
Gate proves triggered temporal capture. Wind proves passive temporal capture.

Do not add gull/moped simultaneously.

---

# Step 6 — House density: kitchen/fridge

## Target beat
`MB04_fridge_mother`

## New thing being proved
A domestic machine cycle and acoustic bleed between rooms.

## Minimum
- playable kitchen slice;
- fridge compressor state cycle;
- door/seal interaction if stable;
- Mother presence can create overlap;
- no kitchen task list.

## Value
The player learns that BO's important sounds are not only spectacular outdoor targets.

---

# Step 7 — Living family / Ronan suspect

## Target beat
`MB05_ronan_suspect`

## New thing being proved
Character behaviour can create recordable situations without becoming an NPC simulation game.

## Minimum
- one authored Ronan movement/event;
- off-screen sound cue;
- one or two possible player approaches;
- optional recording;
- comic interpretation by Malo.

## Avoid
- detective evidence UI;
- behaviour trees for every family member;
- full dialogue system unless separately justified.

---

# Step 8 — Expand outdoor acoustic ecology

Only after gate + wind work.

Candidate order:
1. swing squeak;
2. gull;
3. moped pass;
4. neighbour/street bleed.

Each should prove a distinct timing/listening pattern rather than merely add another collectible.

---

# Step 9 — Studio enfant

## Target beat
`MB09_child_studio_boxes`

## New thing being proved
The archive becomes spatial and autobiographical.

Add:
- handwritten sound lists;
- boxes/piles;
- visible accumulated cassettes;
- retry intentions;
- `TOUJOURS PRENDRE LE RIRE` as a discovered personal rule when narratively earned.

---

# Step 10 — Radio Malo genesis

## Target beat
`MB07_radio_malo_genesis`

## Gate
Do not begin until recordings already have personal meaning.

## First version
No DAW.

Use simple performative verbs:
- announce;
- play a chosen recording;
- react;
- perhaps trigger a jingle/second element;
- hear Ronan/family response.

Then `Édition spéciale biscuits` can become the first comic content variation rather than a separate system.

---

# Step 11 — Persistence and experimentation

Use beats like:
- horse/persistence;
- TV bricolage;
- tape repair;
- failed takes revisited later.

These deepen Malo's creative personality before a new recorder changes the rules.

---

# Step 12 — MK2

Only now broaden device capabilities.

Potential verbs:
- pitch;
- tracks;
- Sound-on-Sound;
- more deliberate juxtaposition.

The important design test is that the player feels:

**"I can do more with sound now"**

rather than:

**"the game opened another menu."**

---

# Content rollout rule
For each new beat, identify the single new systemic idea it is meant to prove.

If a beat requires three unproven systems at once, split the work or defer it.

# Recommended next post-Sprint-5 proof sequence

`Ronan archive -> physical review -> temporal capture test -> Gate -> Wind -> Fridge -> Ronan living beat -> outdoor ecology -> Radio Malo -> MK2`

This sequence maximises learning while minimising simultaneous technical risk.
