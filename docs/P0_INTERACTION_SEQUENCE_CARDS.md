# BO_Ta_Vie — P0 Interaction Sequence Cards

## Status
Design only. These cards are future implementation references, not Sprint 5 scope expansion.

## Purpose
Give Work/Codex a compact per-object sequence so it can implement one interaction at a time without re-deriving state, feedback, sound and recovery behaviour.

---

# Card 1 — Fisher Price pickup

## Intent
Teach that the recorder is a physical object Malo takes into his hands, not a menu capability.

## Before action
- Fisher readable in gift area;
- beige/burgundy silhouette;
- contextual prominence through placement;
- prompt only when actionable according to guidance profile.

## Action
`TAKE`

## Immediate feedback
- pickup acknowledged immediately;
- world Fisher disappears/disables as placed interactable;
- carried Fisher appears;
- HUD advances toward Ronan recording beat.

## State
`PLACED -> EQUIPPED`

## Audio
- optional small handling/plastic sound later;
- no generic pickup jingle.

## Recovery
No destructive failure. If player is out of range, world remains unchanged.

## Acceptance
- first-time player understands object was physically taken;
- no inventory screen appears;
- Recorder domain ownership remains unchanged.

---

# Card 2 — Fisher REC / STOP / PLAY

## Intent
Make the device state legible through tactile mechanics, not only text.

## REC
Input: hold R.

Feedback:
- REC/transport clack;
- REC lamp;
- carried device state changes;
- compact HUD may reinforce state.

## STOP
Input: release R while recording.

Feedback:
- transport disengage sound;
- REC lamp off;
- clip creation remains owned by Recorder.

## PLAY
Input: Space preferred / P legacy prototype.

Feedback:
- play transport sound;
- playback begins;
- device enters active visual state.

## Acceptance
The player should be able to infer REC/STOP/PLAY state even if HUD visibility is reduced.

---

# Card 3 — Garden gate / BONJOUR

## Intent
First true post-prototype physical micro-quest and temporal sound capture proof.

## Pre-cue
Possible sequence:
1. player hears a faint gate squeak or sees gate geometry;
2. partial world beyond gate creates curiosity;
3. handle/latch reads as usable;
4. prompt appears only when close enough.

## Action
`OPEN`

## Physical sequence
1. latch releases;
2. gate begins rotation;
3. hinge squeak occurs over motion;
4. open silhouette/path becomes clear.

## Sound-memory sequence
If REC was already active:
- latch + squeak occur naturally on world audio path;
- optional neighbour `BONJOUR` may overlap depending on authored beat;
- resulting temporal recording preserves actual timing.

If player starts REC too late:
- early transient is genuinely absent;
- player may keep imperfect take;
- gate can be used again naturally.

## Closing
`CLOSE`

Sequence:
- hinge movement;
- closing squeak variant;
- latch settles;
- prompt returns to `Open gate`.

## Guidance
GUIDED:
- stronger pre-cue;
- earlier prompt;
- hint after missed timing.

NATURAL:
- sound and geometry first;
- prompt in ordinary interaction range.

FREE:
- same physical feedback;
- minimal interpretation.

## Acceptance
- gate is understandable without glowing outline;
- state transition never tells Recorder what clip to make;
- missed timing is recoverable;
- recording while interacting remains possible.

---

# Card 4 — Fridge / Mother

## Intent
Turn ordinary household experimentation into comedy and memory.

## Pre-cue
- compressor hum may already exist;
- visible handle and door seam;
- Mother may be present elsewhere in kitchen flow.

## Action
`OPEN`

## Immediate feedback
- seal release;
- door rotates;
- interior light on;
- hum/acoustic perspective changes.

## Persistent state
Door state and compressor state are separate.

A fridge can be:
- closed + compressor running;
- closed + compressor idle;
- open + compressor running;
- open + compressor idle.

Do not collapse all of this into one four-state generic enum if orthogonal state is clearer in implementation.

## Repeat-action comedy
First uses:
- no reaction or glance.

Repeated uses:
- Mother notices;
- short comment;
- eventual intervention;
- cooldown.

The fridge state machine does not own Mother's reaction counter.

## Recording
Temporal capture later can include:
- compressor hum;
- seal release;
- close impact;
- Mother's distant line;
- accidental overlapping sounds.

## Recovery
No lockout and no mission failure.
The humour should not permanently punish experimentation.

## Acceptance
The player can understand both physical state and comic consequence without a quest tracker.

---

# Card 5 — Bathroom tap

## Intent
Introduce a sustained sound source whose world state persists after interaction.

## Pre-cue
- familiar fixture geometry;
- reflective bathroom acoustic;
- no special quest marker.

## Action
`TURN ON`

## Feedback
- handle motion;
- valve/mechanical sound;
- visible water;
- water source starts;
- room resonance changes.

## State
`OFF -> RUNNING`

## While running
- player can move away;
- source remains active;
- temporal recording later captures actual overlap;
- no need to hold the interaction button continuously.

## Action
`TURN OFF`

## Feedback
- handle motion;
- water stop;
- residual drip optional later.

## Acceptance
This proves object state can enable a persistent recordable source while Recorder remains generic.

---

# Card 6 — Cassette review surface

## Intent
Turn recordings into physical childhood organisation rather than a modern media database.

## Pre-cue
- boxes/piles labelled `CASSETTES`, `BIEN`, `RATÉS MAIS GARDER`;
- handwritten quality;
- cassette handling sounds;
- small number of recordings in first proof.

## Primary sequence later
1. select physical cassette;
2. PLAY / listen;
3. optional child title;
4. choose/place into a physical editorial state;
5. preserve raw recording and stable ID.

## Important
`RATÉ MAIS GARDER` is not failure punishment.
It is a meaningful classification choice.

## Acceptance
- player can understand archive state spatially;
- no Spotify-like grid is required;
- no quality score appears;
- Recorder remains unaware of boxes/favourites/titles.

---

# Card 7 — Fireplace

## Intent
Demonstrate that a meaningful sound can invite recording without inviting manipulation.

## Pre-cue
- crackle;
- flicker;
- warm light;
- Father's ambient activity later.

## Player action
No default `INTERACT` verb.

The player may simply:
- approach;
- listen;
- record.

## Acceptance
This prevents BO from teaching that every interesting thing must show an interaction prompt.

---

# Shared Work checklist

Before accepting a new object:
- verify current state visually;
- verify semantic prompt matches state;
- verify action gives immediate physical/audio feedback;
- verify no object-specific code was pushed into `InteractionContext`;
- verify no sound-source-specific code was pushed into `Recorder`;
- verify action remains understandable in NATURAL guidance;
- verify FREE retains physical usability;
- verify GUIDED adds help without different content;
- verify retry/repetition remains narratively plausible;
- run canonical Fisher/Ronan regression loop.
