# Work Handoff — Family Dialogue / Barks

## Status
Design prepared. Do not implement during Sprint 5 live acceptance unless explicitly authorised.

## Read first
1. `docs/FAMILY_DIALOGUE_BARKS_DESIGN.md`
2. `data/family_bark_catalog_1982.json`
3. `docs/FAMILY_DIALOGUE_EVENT_ARCHITECTURE.md`
4. `docs/FAMILY_LIVING_WORLD_DESIGN.md`

## Core decision
Use lightweight contextual barks and nonverbal reactions for ordinary family life.

Do **not** build a full dialogue-tree framework for fridge/gate/recorder reactions.

## Source language
Canonical authored source for Christmas1982 household dialogue is French.
Use stable localization keys for later English/localized versions.
Never key gameplay logic to localized text.

## First proof after Sprint 5 acceptance
Smallest useful test:
1. Ronan notices Malo recording;
2. choose silence/nonverbal or one short bark;
3. spatial voice originates from Ronan;
4. bark may overlap active REC;
5. repeated trigger respects cooldown/variation;
6. Recorder/InteractionContext remain unchanged.

Then add:
- Mother `MALO TU FAIS QUOI ?` on wind beat;
- fridge reaction escalation;
- Father fireplace ambient presence.

## Architecture lock
Future ownership:

```text
world/narrative event
 -> FamilyReactionDirector / BarkSelector
 -> voice + optional gesture presentation
 -> world audio
 -> temporal capture naturally if REC is active
```

Never manually inject bark audio into a `RecordingClip`.
Never put bark catalogs, localization keys, cooldowns or dialogue state into `Recorder` or `InteractionContext`.

## Repetition
Repeated actions should vary among:
- no response;
- nonverbal reaction;
- short verbal variants;
- stronger reaction;
- cooldown.

Do not repeat one identical line on every trigger.

## Guidance
GUIDED/NATURAL/FREE must not change family personality or available dialogue content.
Guidance may only alter timing/clarity of diegetic hints where plausible.
FREE does not remove subtitles or physical feedback.

## Do not implement now
- branching dialogue trees;
- procedural/LLM dialogue;
- relationship stats;
- lip-sync pipeline;
- full localization content pass;
- dialogue-choice UI;
- large NPC schedule simulation.

## Validation
Use `tests/static_validate_family_dialogue_design.py` once present, plus the Sprint 5 validation suite.
