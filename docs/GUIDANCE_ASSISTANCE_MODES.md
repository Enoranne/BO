# BO_Ta_Vie — Guidance / Assistance Modes

## Status
Design only. This is a future accessibility/presentation contract, not a Sprint 5 implementation request.

## Core decision
BO uses one narrative campaign with the same story content and the same playable beats for everyone.

Do **not** split the campaign into easy/medium/hard content branches.

Instead expose a player-adjustable guidance profile that changes how explicit the game is while preserving the same situations, recordings, characters and narrative outcomes.

## Profiles

### GUIDED
For players who want clear direction or who are unfamiliar with narrative exploration games.

May use:
- explicit objective wording when a beat begins;
- stronger contextual prompts;
- clearer REC/PLAY reminders;
- reinforced sound cues;
- more generous timing windows;
- one or more progressive hints after inactivity or repeated failed attempts;
- optional visual emphasis on the relevant object or direction.

Example — Gate:
`Try recording the gate's squeak.`

The player still performs the same interaction and recording as every other profile.

### NATURAL — default
The intended baseline BO experience.

Prefer:
- environmental sound first;
- character gaze/movement;
- composition and lighting;
- contextual prompts only near the relevant interaction;
- short verbal or diegetic nudges when the player has clearly missed the intent;
- forgiving but not exaggerated timing.

Example — Gate:
The player hears the squeak, sees Malo orient toward it, and only receives an interaction prompt at the gate.

No explicit quest sentence is required unless the player becomes stuck.

### FREE
For players who prefer discovery with minimal assistance.

Prefer:
- no explicit objective text for ordinary memory beats;
- no automatic visual highlight;
- minimal prompts beyond required controls;
- natural timing and source audibility;
- hints only if the player explicitly requests help or changes the profile.

The world still needs to be readable. FREE is not an excuse for obscure or broken design.

## Player control
The guidance profile should be changeable during play without restarting the story or invalidating progress.

A player may move temporarily from FREE to GUIDED for one difficult beat and then return to NATURAL.

Do not frame this as failure or lower skill.

## Difficulty versus assistance
The profile should not change:
- story content;
- which memories exist;
- which recordings are valuable;
- narrative rewards;
- save compatibility;
- character relationships;
- access to endings.

It may change:
- clarity of instruction;
- prompt frequency;
- hint escalation;
- timing tolerance;
- sound-source emphasis;
- optional object/direction emphasis.

## Two modes

### STORY MODE
The canonical narrative campaign.

Uses one of the three guidance profiles above.

### ARCHIVE MODE — future candidate
A separate, lower-pressure return space unlocked progressively or later in the project.

Possible functions:
- revisit an era or location;
- replay recordings;
- re-record optional sounds;
- test alternate takes;
- experiment with later devices;
- inspect cassette boxes and memory annotations.

Archive Mode must not become a second campaign or a completionist checklist by default.

## Default
Default profile: `NATURAL`.

## Guidance hierarchy
Before showing explicit objective text, prefer:
1. sound;
2. character orientation / movement;
3. light / composition;
4. object animation or state;
5. contextual prompt;
6. short diegetic hint;
7. explicit objective wording.

GUIDED may reach steps 6–7 earlier.
FREE should usually remain within steps 1–5.

## Work handoff rule
When this system is eventually implemented, Work must treat guidance as a presentation/accessibility layer observing narrative state. It must not duplicate quest logic or create three versions of every beat.

Do not implement this before Sprint 5 live acceptance unless explicitly authorised.
