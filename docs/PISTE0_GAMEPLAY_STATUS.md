# BO_Ta_Vie — PISTE 0 Gameplay Design Status

## Status
**DESIGN PREPARED / IMPLEMENTATION NOT STARTED beyond existing Christmas1982 loop.**

## Current implemented gameplay
Only:

`Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY`

No other PISTE 0 memory beat is currently authorised as Sprint 5 gameplay.

## Design thesis
PISTE 0 is a memory field, not a quest chain.

The player should:
- hear before being told;
- follow curiosity;
- record imperfect moments;
- keep accidents when they matter;
- revisit places because context changes, not because icons respawn.

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

## Guidance contract
Prefer:
1. sound;
2. character movement;
3. composition/light;
4. object animation/state;
5. contextual prompt;
6. explicit objective text only when genuinely needed.

Never default to minimap markers or a permanent quest tracker.

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
2. `data/piste0_beat_dependencies.json`
3. `docs/PISTE0_IMPLEMENTATION_ROLLOUT.md`
4. only then the specific beat in `docs/PISTE0_NARRATIVE_GAMEPLAY_BEATS.md`

## Deep references
- `data/piste0_narrative_beats.json`
- `docs/PISTE0_PLAYABLE_STRUCTURE.md`
- `docs/CHRISTMAS1982_SOUND_MAP.md`
- `docs/AUDIO_MEMORY_STATUS.md`
- `docs/CASSETTE_MEMORY_STATUS.md`
- `SPRINT6_STATUS.md`

## Validation
```bash
python tests/static_validate_piste0_narrative_design.py
```

Also included in:
```bash
bash tests/run_sprint5_validation.sh
```
