# BO_Ta_Vie — PISTE 0 Gameplay Design Status

## Status
**DESIGN PREPARED / IMPLEMENTATION NOT STARTED beyond existing Christmas1982 loop.**

## Current implemented gameplay
Only:

`Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY`

No other PISTE 0 memory beat is currently authorised as Sprint 5 gameplay.

## Design thesis
PISTE 0 is **not** a passive field of memories and **not** a conventional quest chain.

It uses authored **micro-quests that feel like memories**:
- hear before being told;
- want something concrete;
- try, fail or succeed imperfectly;
- replay/react;
- keep accidents when they matter;
- return to places because context changes, not because icons respawn.

## Prepared signature beats
- First Fisher / Ronan recording;
- Fisher mechanics fascination;
- Gate / `BONJOUR`;
- Wind / `MALO TU FAIS QUOI ?`;
- Fridge / Mother;
- Ronan suspect;
- Moped pass-by;
- Radio Malo genesis;
- Biscuit special edition;
- child studio / cassette boxes;
- `Toujours prendre le rire`;
- horse / persistence;
- television bricolage;
- gull patience;
- tape repair.

## Guidance / assistance decision
Use **one Story Mode** with the same narrative content for everyone.

Do not create separate Easy / Medium / Hard campaigns.

Instead expose three future guidance profiles:
- `GUIDED`
- `NATURAL` — default
- `FREE`

They may change:
- objective explicitness;
- prompt frequency;
- hint escalation;
- sound/visual emphasis;
- timing tolerance where appropriate.

They must not change:
- story content;
- available memories;
- endings;
- rewards;
- character relationships;
- recording value.

Guidance should be changeable during play without restarting.

A future `ARCHIVE MODE` may provide lower-pressure revisiting, replay and re-recording without becoming a second campaign.

Compact Work handoff: `docs/WORK_GUIDANCE_HANDOFF.md`.

## Guidance hierarchy
Prefer:
1. sound;
2. character movement;
3. composition/light;
4. object animation/state;
5. contextual prompt;
6. diegetic hint;
7. explicit objective text when genuinely needed.

Never default to minimap markers or a permanent quest tracker.

## Failure / recovery contract
BO uses soft failure.

A failed attempt may become:
- an interesting imperfect recording;
- a natural retry;
- an adaptive hint escalation;
- a missed optional moment that does not block progress.

No `MISSION FAILED` framing by default.

Mandatory beats must offer robust retry and escalating assistance.
Optional memories generally must not block progression.

See `docs/MICRO_QUEST_FAILURE_RECOVERY.md`.

## Pacing contract
PISTE 0 should alternate:
- `CALM`
- `PLAYFUL`
- `FOCUSED`
- `CHAOTIC`
- `REFLECTIVE`

Core rhythm:

`NOTICE -> WANT -> TRY -> RESULT -> REPLAY/REACTION -> RELEASE`

Do not stack more than two highly similar beats in succession.

Early proposed cadence:
`First Fisher/Ronan -> Fisher mechanics -> calm house listening -> Gate -> Wind/Mother -> Fridge/Mother -> cassette review`

This deliberately oscillates between action, humour, listening and reflection.

See `docs/PISTE0_PACING_RHYTHM.md` and `data/piste0_pacing_model.json`.

## Physical affordance contract
The world should explain interactions before the HUD does.

Affordance hierarchy:
1. silhouette / handle / physical form;
2. placement;
3. motion/state;
4. sound;
5. character attention;
6. framing/light;
7. contextual prompt.

Important consequences:
- no default glowing-outline language;
- a sound source does not automatically need an interaction verb;
- an interactable does not automatically become an inventory pickup;
- `Interactable` and `RecordableSource` remain separate by composition;
- FREE guidance removes explanation, not physical feedback;
- new interactions should remain usable while REC is active when temporal capture requires it.

Priority planned objects:
- Fisher Price — existing interaction, live affordance/feedback validation pending;
- gate — first recommended true post-prototype temporal interaction;
- fridge — passive hum + triggered door sounds + family reaction;
- tap — later sustained-source state experiment;
- cassette boxes — later physical review/archive surface;
- fireplace — deliberately meaningful and recordable without default interaction.

Read:
- `docs/PHYSICAL_AFFORDANCE_LANGUAGE.md`
- `data/p0_affordance_catalog.json`
- `docs/OBJECT_INTERACTION_FEEDBACK.md`
- `docs/WORK_AFFORDANCE_HANDOFF.md`

## Living-family contract
Family members should generate variations, interruptions and reactions rather than behave as quest dispensers.

Prepared design includes:
- Ronan reacting to REC / teasing / ruining or improving takes;
- Mother contextual interruption and escalating fridge reaction;
- Father as quieter domestic/technical presence;
- authored anchors and short routine segments before any free-roaming NPC AI.

See `docs/FAMILY_LIVING_WORLD_DESIGN.md`.

## Mandatory spine
Keep minimal.

At present, only the first Fisher/Ronan recording is mandatory.

Future major story/device transitions may be mandatory when explicitly authorised, but ordinary sound memories should remain optional or semi-optional.

## Best first post-prototype beat
**Gate / BONJOUR**.

Reason: it proves interaction + transient temporal sound + timing + optional human overlap + cassette memory value with limited world scope.

Do not implement it until:
- Sprint 5 is accepted live;
- minimal cassette-memory archive exists;
- temporal capture is proven in isolation;
- garden/gate access is ready.

## Preferred rollout
`Ronan archive -> physical review -> temporal capture test -> Gate -> Wind -> Fridge -> Ronan living beat -> outdoor ecology -> Radio Malo -> MK2`

## Start here for implementation planning
1. `docs/PISTE0_GAMEPLAY_STATUS.md`
2. `docs/WORK_GUIDANCE_HANDOFF.md`
3. `docs/WORK_AFFORDANCE_HANDOFF.md`
4. `data/piste0_beat_dependencies.json`
5. `docs/PISTE0_IMPLEMENTATION_ROLLOUT.md`
6. `docs/PISTE0_PACING_RHYTHM.md`
7. only then the specific beat in `docs/PISTE0_NARRATIVE_GAMEPLAY_BEATS.md`

## Deep references
- `data/piste0_narrative_beats.json`
- `data/guidance_profiles.json`
- `data/assistance_recovery_rules.json`
- `data/piste0_pacing_model.json`
- `data/p0_affordance_catalog.json`
- `docs/GUIDANCE_ASSISTANCE_MODES.md`
- `docs/MICRO_QUEST_FAILURE_RECOVERY.md`
- `docs/FAMILY_LIVING_WORLD_DESIGN.md`
- `docs/PISTE0_PLAYABLE_STRUCTURE.md`
- `docs/CHRISTMAS1982_SOUND_MAP.md`
- `docs/AUDIO_MEMORY_STATUS.md`
- `docs/CASSETTE_MEMORY_STATUS.md`
- `SPRINT6_STATUS.md`

## Validation
```bash
python tests/static_validate_piste0_narrative_design.py
python tests/static_validate_guidance_recovery_design.py
python tests/static_validate_piste0_pacing_design.py
python tests/static_validate_family_living_world_design.py
python tests/static_validate_affordance_design.py
```

Also included in:
```bash
bash tests/run_sprint5_validation.sh
```
