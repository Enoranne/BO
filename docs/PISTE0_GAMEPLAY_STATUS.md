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
3. `data/piste0_beat_dependencies.json`
4. `docs/PISTE0_IMPLEMENTATION_ROLLOUT.md`
5. `docs/PISTE0_PACING_RHYTHM.md`
6. only then the specific beat in `docs/PISTE0_NARRATIVE_GAMEPLAY_BEATS.md`

## Deep references
- `data/piste0_narrative_beats.json`
- `data/guidance_profiles.json`
- `data/assistance_recovery_rules.json`
- `data/piste0_pacing_model.json`
- `docs/GUIDANCE_ASSISTANCE_MODES.md`
- `docs/MICRO_QUEST_FAILURE_RECOVERY.md`
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
```

Also included in:
```bash
bash tests/run_sprint5_validation.sh
```
