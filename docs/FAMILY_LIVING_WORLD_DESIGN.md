# BO_Ta_Vie — Family Living World Design

## Status
Design only. No NPC AI/navigation implementation is authorised during Sprint 5.

## Goal
Make the family home feel alive enough that memory beats emerge from people, routines and interruptions rather than static quest markers.

The player should often feel that Malo is recording **around family life**, not that family members exist only to serve Malo's objectives.

## Core principle
Family activity runs on lightweight authored behaviour, not open-world simulation.

Prefer:
- short routines;
- contextual reactions;
- scheduled/triggered micro-events;
- occasional overlaps;
- repeatable but varied gestures;
- authored handoffs between rooms.

Avoid:
- full life simulation;
- complex schedules for every minute;
- expensive navigation before the house is ready;
- dialogue trees for ordinary household reactions.

## Character roles

### Malo
Role: listener / experimenter / instigator.

His actions create many situations, but he should not control all of them.

### Ronan
Role: brother, moving target, comic antagonist, occasional collaborator.

Useful behaviours:
- crosses a room while talking;
- notices Malo recording;
- performs for the recorder sometimes;
- deliberately ruins a take sometimes;
- becomes suspicious when followed;
- laughs unexpectedly;
- later contributes to Radio Malo.

Important: Ronan must not become a quest dispenser.

### Mother
Role: household rhythm, interruption, grounding reality.

Useful behaviours:
- calls Malo from another room;
- opens/closes fridge or cupboards;
- comments on repeated noise experiments;
- passes through a recording unexpectedly;
- creates emotionally valuable background voice material;
- occasionally tells Malo to stop doing something without hard-blocking play.

### Father
Role: quieter domestic presence, observation, occasional technical or affectionate support.

Useful behaviours:
- tends the fire;
- handles objects/tools;
- observes Malo's experimentation;
- exchanges glances with Mother;
- may explain or help repair something later;
- provides calm contrast to Ronan/Mother energy.

## Behaviour categories

### AMBIENT
Low-intensity presence that gives life to space.
Examples:
- Mother crosses kitchen;
- Father adjusts fireplace;
- Ronan reads/plays nearby.

### REACTIVE
Triggered by Malo's action.
Examples:
- Ronan notices REC light;
- Mother reacts to repeated fridge openings;
- Father looks over after an unusual noise.

### INTERRUPTIVE
Temporarily changes Malo's plan.
Examples:
- `MALO TU FAIS QUOI ?` during wind;
- Ronan walks through a carefully framed recording;
- Mother asks Malo to move.

### COLLABORATIVE
Family member contributes to the experiment.
Examples:
- Ronan performs a voice;
- Father demonstrates a sound/object;
- Mother unintentionally supplies a useful phrase.

### CALLBACK
Later response to prior behaviour.
Examples:
- Ronan remembers Malo recorded him;
- Mother jokes about the fridge incident;
- a family phrase later appears on tape.

## Reaction intensity
Use three broad levels:

### 0 — ignore
Family continues routine.

### 1 — acknowledge
Glance, short line, gesture, mild comment.

### 2 — intervene
Walk over, interrupt, change object state, speak directly.

Do not escalate every repeated action immediately. Household tolerance should vary by character and situation.

## Repeat-action design
Repeated experimentation should generate variation instead of identical responses.

Example — fridge:
1st open: no reaction;
2nd/3rd: Mother glances;
4th: comment;
continued: short intervention or comic line;
then cooldown/reset.

Do not count this visibly for the player.

## Interruptions as content
Interruptions are not punishment.

A family interruption may:
- ruin the intended sound;
- create a better memory;
- make Malo retry;
- produce comedy;
- reveal character;
- become `RATÉ MAIS GARDER` material.

## Spatial presence
Before full navigation exists, use authored anchors and short path segments:
- salon sofa;
- fireplace;
- kitchen threshold;
- corridor crossing;
- garden doorway;
- Ronan stand/lean positions.

NPC movement can initially be staged between known anchors rather than relying on a general-purpose roaming system.

## Dialogue philosophy
Ordinary family lines should be:
- short;
- interruptible;
- contextual;
- repeat-safe with variation;
- not presented as dialogue-choice trees unless the scene truly needs choice.

## Interaction with guidance profiles
GUIDED may make relevant family cues slightly clearer.
NATURAL uses ordinary staging.
FREE does not remove family behaviour; it only removes explicit interpretation of it.

## Interaction with pacing
Family activity is a pacing tool:
- CALM: quiet presence;
- PLAYFUL: teasing, reactions;
- FOCUSED: moving target or timing;
- CHAOTIC: overlaps and interruptions;
- REFLECTIVE: quiet after the family leaves the space.

## First living-family implementation candidates
After Sprint 5 acceptance, prefer tiny isolated proofs:
1. Ronan reacts once to being recorded;
2. Mother voice interruption on the wind beat;
3. Mother escalating fridge reaction;
4. Father ambient fireplace routine.

Do not start with free roaming AI for all family members.

## Work rule
When implemented, keep family behaviour above domain systems.

Do not put NPC reaction logic inside:
- `Recorder`;
- `RecordingClip`;
- `InteractionContext`.

Use narrative/director/character-behaviour layers that can observe events without owning the recording system.
