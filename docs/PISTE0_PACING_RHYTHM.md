# BO_Ta_Vie — PISTE 0 Pacing and Rhythm

## Status
Design only. Future narrative pacing contract.

## Goal
Prevent PISTE 0 from becoming either:
- a passive walking simulator;
- or an exhausting chain of explicit tasks.

The experience should alternate between listening, intention, action, surprise, review and breathing space.

## Core rhythm
A useful BO rhythm unit is:

`NOTICE -> WANT -> TRY -> RESULT -> REPLAY/REACTION -> RELEASE`

Not every beat needs all six steps, but a sequence of several beats should contain them collectively.

## Intensity bands

### CALM
Purpose:
- establish place;
- make the player listen;
- create anticipation;
- allow emotional absorption.

Examples:
- fireplace bed;
- distant house sounds;
- inspecting cassette boxes;
- waiting for a gull.

Risk: boredom if too long without a fresh intention.

### PLAYFUL
Purpose:
- curiosity;
- tactile experimentation;
- small comedy;
- repeatable actions.

Examples:
- Fisher buttons;
- fridge experiments;
- portal retries;
- biscuit special edition.

### FOCUSED
Purpose:
- clear short-term goal;
- timing or positioning challenge;
- active attention.

Examples:
- catching a moped pass;
- waiting for the right gust;
- recording Ronan without being noticed.

### CHAOTIC
Purpose:
- overlapping family life;
- accidents;
- humour;
- memorable imperfect recordings.

Examples:
- family crowd;
- Mother calling during wind;
- Ronan reacting;
- simultaneous household sounds.

Use sparingly so chaos remains special.

### REFLECTIVE
Purpose:
- replay;
- classification;
- emotional recontextualisation;
- transition.

Examples:
- listening back alone;
- `RATÉ MAIS GARDER`;
- adult Malo callback later.

## Recommended cadence
Avoid more than two highly similar beats in succession.

Examples of good alternation:
- CALM -> PLAYFUL -> FOCUSED -> CHAOTIC -> REFLECTIVE
- PLAYFUL -> CALM -> FOCUSED -> REFLECTIVE

Examples to avoid:
- five passive ambience discoveries in a row;
- five explicit timing challenges in a row;
- five dialogue-heavy scenes without recorder agency.

## Beat length targets
These are design targets, not strict timers.

- micro beat: 20-60 s;
- short beat: 1-3 min;
- developed beat: 3-7 min;
- major transition/creation beat: 5-10 min.

A player who experiments should be able to extend many beats naturally.

## Early PISTE 0 pacing proposal

### 1. First Fisher / Ronan
Band: PLAYFUL -> FOCUSED -> REFLECTIVE
Purpose: teach the loop and create immediate payoff.

### 2. Fisher mechanics fascination
Band: PLAYFUL
Purpose: tactile pleasure after onboarding.

### 3. House audible / fireplace / small sounds
Band: CALM
Purpose: teach listening without explicit tasking.

### 4. Gate / BONJOUR
Band: FOCUSED -> PLAYFUL
Purpose: first true micro-quest and retryable transient sound.

### 5. Wind / Mother call
Band: CALM -> FOCUSED -> CHAOTIC
Purpose: surprise overlap and meaningful imperfection.

### 6. Fridge / Mother
Band: PLAYFUL -> CHAOTIC
Purpose: comedy and family friction.

### 7. Cassette review / boxes
Band: REFLECTIVE
Purpose: let previous activity settle and acquire meaning.

This sequence intentionally oscillates rather than escalating constantly.

## Anti-boredom rules
1. Every calm stretch needs a new perceptual detail or emerging intention.
2. Every explicit objective should be followed by freedom or reflection.
3. Repetition should change context, not just repeat input.
4. At least some beats should produce surprises the player did not request.
5. Family members should occasionally interrupt Malo's plan.
6. Playback should reveal something new often enough to justify recording.
7. Do not fill silence just because the player is idle.

## Anti-fatigue rules
1. Do not stack repeated timing windows.
2. Do not force immediate replay/classification after every recording.
3. Do not overuse jokes or interruptions.
4. Do not make every sound narratively important.
5. Allow the player to wander between authored beats.

## Assistance interaction
Guidance profile changes clarity, not pacing identity.

GUIDED may shorten confusion time with earlier hints.
FREE may allow longer self-directed exploration.
The authored order and emotional cadence remain the same.

## Archive Mode interaction
Archive Mode can remove most narrative pacing pressure and become a deliberate sandbox/revisit space.

Story Mode should retain authored rhythm and transitions.

## Work rule
When implementing future beat orchestration, store pacing metadata outside `Recorder` and `InteractionContext`.
Narrative pacing belongs to beat/director layers.
