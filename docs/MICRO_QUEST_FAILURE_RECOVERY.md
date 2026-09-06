# BO_Ta_Vie — Micro-quest Failure and Recovery

## Status
Design only. Future narrative/gameplay contract.

## Principle
BO should permit mistakes because imperfect recordings are part of the fiction.

A failed attempt must usually produce one of four outcomes:

1. **interesting failure** — the recording is imperfect but worth keeping;
2. **soft retry** — the world naturally offers another attempt;
3. **adaptive assistance** — the game increases clarity after repeated confusion;
4. **story continuation** — optional memories may simply pass without blocking progression.

Never default to `MISSION FAILED`.

## Failure categories

### A. Timing miss
Example: Malo presses REC after the gate latch has already clicked.

Response:
- keep the partial recording if one exists;
- allow the gate to be used again after a short natural reset;
- do not rewind the whole scene automatically;
- on GUIDED/NATURAL, increase the pre-event cue after repeated misses.

### B. Wrong distance / position
Example: wind is too weak where Malo stands.

Response:
- audible difference should teach the player;
- nearby stronger locations can become progressively clearer;
- no red `too far` warning unless absolutely necessary.

### C. Player ignores the opportunity
Example: the moped passes while Malo is doing something else.

Response:
- if optional, let it go;
- schedule another plausible pass later if the beat should remain available;
- never freeze the world waiting for the player.

### D. Interaction misunderstanding
Example: player hears the gate but does not realise it can be opened.

Escalation:
1. repeat/strengthen sound or character gaze;
2. subtle object motion / light composition;
3. contextual prompt at proximity;
4. diegetic nudge;
5. explicit objective wording in GUIDED or after prolonged blockage.

### E. Poor but meaningful recording
Example: Mother's voice overlaps the gate and obscures part of the squeak.

Response:
- never mark it as objectively bad;
- allow playback;
- allow `RATÉ MAIS GARDER` later;
- the accidental content may gain narrative value.

## Anti-frustration timing
Do not require frame-perfect REC timing.

Future temporal-capture beats should support hidden tolerance where appropriate:
- short pre-roll candidate for GUIDED/NATURAL if technically safe;
- source lead-in cues before important transient events;
- replayable/resettable object interactions;
- generous REC recognition around onboarding beats.

FREE may reduce explicit help, but should not secretly make input latency harsher or controls less responsive.

## Adaptive assistance
Assistance should escalate from evidence of confusion, not immediately.

Possible signals:
- several interactions with irrelevant nearby objects;
- multiple timing misses on the same beat;
- prolonged inactivity near the source;
- repeated recorder activation with no usable capture;
- explicit player hint request.

Do not infer incompetence from free exploration.

## Hint ladder
For ordinary beats:

### Hint 0 — environment only
No explicit help.

### Hint 1 — perceptual nudge
Repeat sound, character glance, object movement.

### Hint 2 — contextual control hint
Example: `Hold R to record` when close to the relevant source.

### Hint 3 — intention hint
Example: `That gate makes a strange sound.`

### Hint 4 — explicit action
Example: `Try recording the gate as you open it.`

GUIDED may start at Hint 2 or 3.
NATURAL starts at 0 or 1 and escalates.
FREE remains at 0/1 unless help is requested.

## Optional beats
Optional memories should almost never block progression.

If missed:
- they may recur naturally;
- be revisitable later;
- move to Archive Mode later;
- or remain genuinely missed in that playthrough.

Missing an optional moment can itself make the player's memory history personal.

## Mandatory beats
Mandatory beats must be robust.

Rules:
- strong affordance;
- generous timing;
- automatic retry opportunity;
- escalating hints;
- no permanent lockout;
- never require perfect recording quality.

Current mandatory onboarding remains Fisher -> Ronan.

## Relationship to cassette memory
A poor attempt does not equal failure of the game.

The cassette-memory system should preserve:
- imperfect duration;
- background voices;
- late starts;
- accidental overlaps;
- surprising sounds.

These may become the most memorable recordings.

## Work implementation rule
When implemented, failure/recovery logic should live near narrative beat orchestration and assistance presentation, not inside `Recorder` domain logic.

`Recorder` should report what happened; it should not decide whether the player has failed a story beat.
