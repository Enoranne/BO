# BO_Ta_Vie — Family Dialogue Event Architecture

## Status
Design only. Future implementation seam.

## Goal
Allow short family speech/reactions to observe world events and produce spatial audio without coupling dialogue to `Recorder`, `InteractionContext` or object-specific gameplay.

## Ownership model

```text
Gameplay / object / narrative events
        |
        v
FamilyReactionDirector / BarkSelector   (future)
        |
        +--> gesture request             (presentation)
        +--> bark request                (presentation)
        v
CharacterVoicePresenter / AudioStreamPlayer3D
        |
        v
World audio bus / temporal capture path when active
```

Core rule:
**events may cause speech; speech never owns the gameplay event.**

## Suggested future event shape
Conceptual only:

```text
FamilyEvent
- event_id
- source_actor
- target_actor
- zone
- tags
- intensity_hint
- timestamp
- repeat_context
```

Examples:
- `recorder.active_near.ronan`
- `fridge.open.repeated`
- `garden.wind_recording`
- `fireplace.tended`

Do not use localized bark text as event ids.

## Bark selection inputs
A lightweight selector may consider:
- character;
- event tags;
- current narrative beat;
- prior reactions in this context;
- cooldown;
- distance/room;
- guidance profile only when a diegetic hint is justified;
- whether a stronger authored scene is active.

It should not inspect Recorder internals beyond public events/signals exposed by presentation/domain seams.

## Priority
Suggested broad priority:

- P0 authored scene dialogue / signature beat;
- P1 direct contextual reaction;
- P2 ambient family bark;
- P3 nonverbal texture.

A higher-priority event may suppress or interrupt a lower-priority bark.

## Cooldown and anti-repeat
Track reaction history in the family/dialogue layer, not in interactables.

Useful values per bark family:
- minimum cooldown;
- maximum repeats per context;
- cannot-repeat-consecutively;
- escalation stage;
- reset condition.

Do not persist every trivial bark permanently unless later narrative design proves it matters.

## Voice playback
Use spatial character-attached playback for in-world speech.

Later production target:
- `AudioStreamPlayer3D` or equivalent character voice emitter;
- appropriate attenuation;
- room/doorway treatment if supported;
- subtitle event emitted separately;
- no global UI voice by default.

## Recording coexistence
When temporal capture exists, world dialogue should travel through the same recordable world route when appropriate.

The dialogue service must **not** manually copy a bark into `RecordingClip`.

Preferred behaviour:
1. character speaks in world;
2. world audio routes normally;
3. if Recorder is actively capturing that world bus, the line is captured naturally;
4. playback later reveals the actual overlap.

This is essential for `RATÉ MAIS GARDER` memories.

## Subtitles
Subtitles observe voice events.

Keep subtitle ownership separate from:
- guidance profile;
- Recorder;
- character animation state.

Future accessibility settings may include:
- subtitles on/off;
- speaker labels;
- subtitle size/background;
- off-screen indicators if needed.

FREE guidance must not disable subtitles.

## Animation relationship
A bark may request a gesture through the future presentation seam:
- glance;
- shrug;
- head turn;
- short intervention gesture.

Gesture failure must not prevent voice playback.
Voice failure must not corrupt gameplay state.

## Localization
Store stable localization keys and language resources separately.

Canonical source-writing language for this household: French.

Later English localization should preserve:
- age;
- family relationship;
- brevity;
- humour;
- period-natural wording.

Do not translate signature proper concepts like `Radio Malo` into a different brand/name unless explicitly decided.

## First proof after Sprint 5 acceptance
Keep tiny:

1. event: Recorder active near Ronan;
2. selector chooses nonverbal or one R1 Ronan bark;
3. voice plays spatially from Ronan;
4. Recorder loop remains functional;
5. repeated trigger respects cooldown;
6. no dialogue tree/UI panel appears.

Only after that proof add Mother wind/fridge cases.

## Explicitly deferred
- branching conversation trees;
- lip-sync production pipeline;
- relationship-stat dialogue variations;
- procedural LLM dialogue;
- large localization database;
- full NPC schedule simulation;
- persistent conversation history for every bark.
