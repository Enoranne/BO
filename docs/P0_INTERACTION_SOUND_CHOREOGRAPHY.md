# BO_Ta_Vie — P0 interaction + sound choreography

## Purpose

Define how the first important objects should **behave, sound and teach the player** without turning BO into a checklist game.

This is a production-design document. Except for the already implemented Fisher/Ronan prototype loop, these interactions are **not Sprint 5 gameplay requirements**.

Core philosophy:

> The player should learn the world by listening and touching, not by following icons.

---

# Interaction grammar

## Player-facing verbs in the early game

Keep the vocabulary intentionally small:

- move;
- context interact;
- hold REC;
- release to STOP;
- PLAY latest.

Do not add a generic inventory/use/inspect verb set before the narrative requires it.

## UI rule

An interaction prompt explains **what Malo can do now**, not everything the system supports.

Examples:

- `Take Fisher Price`
- `Open gate`
- `Open fridge`
- `Turn on tap`

Recordability should normally be learned through sound and the REC affordance, not a floating `RECORD THIS` icon.

---

# 1 — Fisher Price

## Role

First object of desire, tutorial device, physical interface for the game's central mechanic.

## Pickup choreography

1. Malo approaches the present / recorder area.
2. Context prompt appears: `Take Fisher Price`.
3. Player presses E or left click.
4. World Fisher disappears / carried Fisher appears.
5. One restrained physical handling/clack cue confirms the object moved into Malo's hands.
6. HUD objective advances toward Ronan.

No inventory screen.

## REC choreography

### Press / hold R

Immediate feedback hierarchy:

1. tactile REC-button clack;
2. red REC lamp;
3. state becomes REC;
4. timer / minimal HUD state appears if retained;
5. world continues normally.

Target feeling: **pressing REC changes Malo's relationship to the world immediately.**

Avoid a synthetic UI beep as primary feedback.

## STOP choreography

### Release R

1. transport disengage / STOP clack;
2. REC lamp dies immediately;
3. clip seals;
4. restrained temporary confirmation such as `Recorded` may appear;
5. next contextual priority becomes PLAY.

No triumphant collectible jingle.

## PLAY choreography

1. player presses Space;
2. PLAY transport clack;
3. optional 80–180 ms physical lead-in / tape gap;
4. restrained hiss / speaker presence;
5. captured content plays;
6. on completion, transport returns to STOP.

The first playback should feel like a **revelation**, not a menu action.

---

# 2 — Ronan

## Role

First human recording and emotional proof that the recorder preserves a moment.

## World behaviour

Ronan exists as a person first and a sound source second.

Do not place a permanent 'record Ronan' icon above him in production presentation.

For the first tutorial beat, objective/HUD may guide Malo toward Ronan while keeping the actual sound interaction diegetic.

## Recording behaviour

- Malo approaches within a useful range;
- holds R;
- Ronan voice/laugh event is captured;
- if temporal capture arrives later, nearby room tone/fireplace may also enter naturally;
- player chooses when to release R.

## Playback function

The first playback should establish the thesis:

`That was Ronan a moment ago — but now it is also Malo's recording.`

This is more important than technical fidelity.

---

# 3 — Gate

## Role

Future signature sound landmark and one of Malo's first deliberate field-recording targets.

## Interaction states

Suggested simple future state machine:

- CLOSED;
- OPENING;
- OPEN;
- CLOSING.

No lock/key system required for PISTE 0 unless narrative later demands it.

## Player choreography

### Not recording

1. approach gate;
2. prompt: `Open gate` / `Close gate`;
3. press context interaction;
4. latch / hinge / movement sound happens naturally in world.

### Recording

1. player presses and holds R **before** touching the gate;
2. presses E / left click to open or close it;
3. the entire gate event occurs while Recorder stays in REC;
4. player releases R when satisfied.

This is the ideal demonstration of temporal capture.

## Important rule

If Malo begins REC **after** the latch happened, the final clip must not magically contain the latch.

A partial recording is valid.

## Variation value

Gate should later support audible variation from:

- opening speed;
- closing speed;
- latch vs no latch segment;
- small wind movement;
- distance.

Do not require all of these variations for first implementation.

---

# 4 — Wind / tree

## Role

Passive environmental target that cannot be commanded by the player.

This is important because it teaches patience rather than button sequencing.

## Interaction model

No E interaction required for wind itself.

Player:

1. hears the wind;
2. decides where to stand;
3. presses REC;
4. waits through gust variation;
5. releases when the captured moment feels interesting.

## Design value

Wind should be intentionally difficult to capture cleanly.

The game should never grade the player numerically for this.

A noisy gust can be more memorable than a clean quiet segment.

## Known PISTE 0 beat

Mother's distant `MALO TU FAIS QUOI ?` can later enter the same recording naturally.

That overlap is exactly the kind of accidental memory BO should encourage.

---

# 5 — Fridge

## Role

Domestic machine, comedy beat, early found-music object.

The fridge has two sonic layers:

- **passive** compressor/hum;
- **triggered** handle, seal, door, interior object handling.

## Passive recording

No interaction needed.

Malo can simply stand near the fridge and record its hum.

The closer he gets, the more the harmonics / mechanical texture can dominate.

## Door interaction

Suggested states:

- CLOSED;
- OPENING;
- OPEN;
- CLOSING.

Prompt:

- `Open fridge`;
- `Close fridge`.

Triggered sounds:

- handle / hand contact;
- door seal release;
- hinge / body movement;
- close / seal thump.

## Narrative possibility

Mother can interrupt or comment on Malo recording the fridge.

The joke should emerge from behaviour, not a quest marker reading `RECORD THE FRIDGE`.

---

# 6 — Fireplace

## Role

Emotional acoustic anchor of Christmas1982.

## Interaction model

For early PISTE 0, **do not make the fire a generic interactable** just because it is visible.

Malo can hear it and eventually record it, but does not need to poke/add wood/open a fire menu.

This protects the density principle: not every prop needs E interaction.

## Recording behaviour

- passive loop / evolving ambience;
- close recording emphasizes small crackles;
- further recording includes more salon room tone;
- occasional pop can create variation.

The recording can later become a memory bed associated specifically with Christmas.

---

# 7 — Moped pass

## Role

A moving, missable sonic event that implies the world outside the house.

## Interaction model

No direct player interaction.

The moped is an event in the environment.

Player can:

- hear it approaching;
- rush toward a better position;
- press REC early or late;
- catch only part of it;
- miss it completely and hear another one later if narrative pacing allows.

## Temporal rule

The stored clip must respect the player's start/stop timing.

Do not replace a late capture with a full pristine pass-by sample.

## Gameplay value

This demonstrates that BO is not about clearing sound icons.

The world sometimes moves without waiting for Malo.

---

# 8 — Interaction + recordability composition rule

A future object may be:

### Interactable only

Example:

- a silent drawer used for staging;
- a door whose sound is not yet eligible for capture.

### Recordable only

Example:

- wind;
- fireplace;
- distant voices;
- moped event.

### Both

Example:

- gate;
- fridge;
- tap;
- cupboard.

Do not collapse these categories into one giant `InteractiveRecordableObject` base class.

Use composition so interaction and recording remain independently testable.

---

# 9 — Early quality rules

## No score for recording quality

Do not display:

- 82% quality;
- microphone accuracy meters;
- stars;
- perfect-capture bonuses.

The player should judge recordings by listening.

## No automatic pristine correction

Do not secretly replace imperfect recordings with studio-perfect full events.

## No constant target markers

Allow sounds to be discovered through:

- direction;
- repetition;
- character reaction;
- curiosity;
- narrative context.

## Preserve mistakes

When technically feasible later, clips can contain:

- accidental speech;
- silence;
- room noise;
- late starts;
- early stops;
- background sound.

These are part of Malo's archive.

---

# 10 — Recommended implementation order after Sprint 5

Do not attempt all P0 sounds at once.

### Temporal Capture Proof A

- Ronan;
- fireplace bed;
- gate proxy.

Goal: prove overlapping passive + triggered capture.

### Proof B

- wind;
- distant voice overlap.

Goal: prove evolving ambience and accidental content.

### Proof C

- fridge passive hum + door interaction.

Goal: prove one object can be both interactable and recordable through composition.

### Proof D

- moped pass.

Goal: prove moving/missable event timing.

Only after these proofs should the system expand to the wider house catalogue.

---

# Definition of success

BO's P0 interaction model is working when the player can tell a story like:

> I heard something. I grabbed the recorder. I was a little late. The gate squeaked, Ronan said something in the background, and when I played it back it wasn't just the gate anymore — it was that moment.

That sentence describes the intended game better than a list of collectible sounds.