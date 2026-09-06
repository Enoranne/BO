# BO_Ta_Vie — Family Dialogue & Bark Design

## Status
Design only. No dialogue runtime system is authorised during Sprint 5.

## Goal
Make Christmas1982 feel inhabited by a real family without turning ordinary domestic life into dialogue trees, exposition dumps or quest delivery.

A bark is a short authored line or vocal reaction triggered by context. It may be captured accidentally by Malo's recorder and may therefore become memory material.

## Core rule
**Dialogue belongs to family life first and gameplay explanation second.**

Characters should speak because they are doing, noticing, interrupting or reacting to something — not because the game needs an objective marker with a voice.

## Source language
Canonical authored source for the 1982 French household is French.

Use stable localization keys so later English and other localizations can be produced without changing narrative logic.

Example:

```text
family.mother.wind_call.01
FR: MALO, TU FAIS QUOI ?
```

Do not use localized display text as a gameplay identifier.

## Bark families

### AMBIENT
Unprompted low-stakes household speech.

Examples:
- Mother speaking from kitchen;
- Ronan muttering while occupied;
- Father short practical remarks.

Purpose: life and spatial presence.

### REACTIVE
Response to Malo or Recorder state.

Examples:
- Ronan notices the recorder;
- Mother notices repeated fridge openings;
- Father reacts to a strange repeated sound.

Purpose: acknowledge player behaviour.

### INTERRUPTIVE
Temporarily collides with Malo's intention.

Examples:
- `MALO TU FAIS QUOI ?` during wind recording;
- Ronan speaks over a carefully prepared take.

Purpose: create imperfect memories and comedy.

### COLLABORATIVE
Family willingly plays along.

Examples:
- Ronan performs into the recorder;
- a family member repeats a phrase for Malo.

Purpose: relationship and creative evolution.

### CALLBACK
References something Malo did earlier.

Examples:
- Mother jokes later about the fridge;
- Ronan remembers being recorded.

Purpose: continuity and sense of memory.

## Intensity model
Use reaction intensity independently from bark family.

- **R0** — nonverbal only: glance, sigh, laugh, breath, gesture.
- **R1** — short acknowledgement: one clause or tiny line.
- **R2** — direct reaction/interruption: one or two short lines.
- **R3** — authored scene dialogue: reserved for actual narrative beats, not ordinary barks.

Most domestic responses should remain R0–R2.

## Length targets
Targets, not hard limits:

- R0 vocalization: 0.2–1.5 s;
- R1 bark: 0.5–2.5 s;
- R2 bark: 1.0–4.5 s;
- R3 scene line: authored case-by-case.

Avoid ordinary reactive barks longer than ~5 seconds unless a beat explicitly needs a longer line.

## Variation rule
Never solve repetition with random text alone.

Variation should come from:
- silence / no response;
- nonverbal reaction;
- alternate wording;
- different character state;
- spatial distance;
- overlap with another activity;
- cooldown before another response.

Recommended minimum for a repeatedly triggerable family reaction:
- 1 nonverbal option;
- 2–4 verbal variants;
- a meaningful no-response chance or cooldown state.

## Repetition policy
Do not visibly count repetitions.

A useful pattern for repeated domestic action:

1. first occurrence may be ignored;
2. next occurrence may get a glance/nonverbal;
3. later occurrence may get R1;
4. repeated abuse may get R2;
5. then cooldown / temporary tolerance reset.

The exact sequence varies by character and beat.

## Character voice rules

### Malo, age 6
Malo's spoken lines should be sparse during player agency.

Prefer:
- short self-talk;
- concrete nouns;
- small reactions;
- occasional naming impulse.

Do not narrate every player intention aloud.

### Ronan
Voice qualities:
- older brother confidence;
- teasing;
- mild suspicion;
- occasional performance instinct;
- genuine laughter is valuable.

Avoid making him constantly sarcastic or antagonistic.

### Mother
Voice qualities:
- practical household rhythm;
- affection beneath interruption;
- ability to cut across the house spatially;
- comic irritation when Malo repeats an experiment.

Her distant voice is especially valuable as accidental recording content.

### Father
Voice qualities:
- quieter;
- economical;
- observant;
- practical/technical when appropriate;
- occasional warmth rather than constant commentary.

His contrast with Mother/Ronan helps pacing.

## Recorder interaction
A bark may exist in four relationships to recording:

1. **world-only** — heard but not inside active capture;
2. **captured-intended** — player was deliberately recording that speaker;
3. **captured-accidental** — line overlaps another target;
4. **playback-callback** — later heard on cassette and recontextualized.

Do not author a separate fake version of every bark for cassette playback. Use the same event/recording pipeline when temporal capture exists.

## Interruptibility
Ordinary barks should be interruptible by:
- distance / leaving the area where appropriate;
- a stronger authored beat;
- another higher-priority family event;
- cut/transition rules.

Do not make Recorder wait for a bark to finish.

## Spatial audio rule
Family speech should support navigation and memory.

Where possible later:
- voices originate from the actual character/room;
- occlusion/muffling may suggest room boundaries;
- distant Mother calls should sound spatial, not like UI voice-over;
- playback cassette coloration is separate from world spatialization.

## Subtitles
Future subtitles should be available independently from guidance difficulty.

Do not make FREE guidance remove subtitles or accessibility options.

For off-screen/distant family speech, subtitle speaker labeling may be useful, but should remain visually restrained.

## Guidance profiles
Guidance must not rewrite character personality.

- GUIDED may trigger a clarifying bark earlier only when diegetically plausible.
- NATURAL uses authored normal timing.
- FREE removes interpretation/help, not family life.

Avoid lines like `Malo, press R to record me`.

## Canonical signature phrases
Known PISTE 0 phrases may receive stable keys.

Examples:
- `family.mother.wind_call.01` → `MALO, TU FAIS QUOI ?`
- `radio_malo.ronan.praise.01` → `Radio Malo est complètement génial.`

Do not over-repeat signature phrases merely because they are memorable.

## First implementation candidates after Sprint 5
Recommended tiny proof set:

1. Ronan R0/R1 reaction to active REC;
2. Mother off-screen wind interruption;
3. Mother fridge escalation with silence/nonverbal/verbal variants;
4. one Father fireplace ambient line or nonverbal;
5. verify that any line can overlap active REC without blocking Recorder.

## Anti-patterns
Avoid:
- dialogue tree for every family exchange;
- NPC speech icon above heads;
- repeated identical bark every trigger;
- constant chatter filling silence;
- tutorial instructions disguised as unnatural dialogue;
- lines that wait for the player to finish recording;
- gameplay logic keyed to literal localized text.

## Ownership
Future architecture should keep:
- event/beat state in narrative/character layers;
- bark selection in a lightweight dialogue presentation/service layer;
- audio playback in character/presentation audio;
- Recorder independent from dialogue content.

Never put bark catalogs, localization keys or cooldown state inside `Recorder` or `InteractionContext`.
