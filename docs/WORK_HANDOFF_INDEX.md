# BO_Ta_Vie — Work Handoff Index

## Purpose
This is the **single navigation page** for resuming BO in Work/Godot-MCP.

Do not review Sprint 5 commits chronologically.
Do not read every planning document.
Use the current `sprint-5` HEAD and open only the compact handoffs relevant to the current task.

## Repository
- repo: `Enoranne/BO`
- active branch: `sprint-5`
- default GitHub branch is still `main`; do **not** resume from `main`
- Sprint 5 base: `41e0cfd8ec1682a7b056c343828094405911e42d`

Git rules: `docs/GIT_WORKFLOW_SPRINT5.md`

## Mandatory first read
1. `README.md`
2. `SPRINT5_STATUS.md`
3. `AGENTS.md`
4. this file

Then run:

```bash
bash tests/run_sprint5_validation.sh
```

Do not claim acceptance until static + headless + live editor/runtime checks are complete.

---

# Current task priority — Sprint 5 live acceptance

## 1. Player Feel
Read only if validating controls:
- `docs/PLAYER_FEEL_INPUTS.md`

Validate:
- WASD / physical ZQSD;
- E + left click contextual interaction;
- hold R REC / release STOP;
- Space + legacy P PLAY.

## 2. Visual Slice
Read:
- `docs/SPRINT5_2_VISUAL_REVIEW.md`

Scenes:
- canonical: `scenes/piste_0/christmas_1982/Christmas1982.tscn`
- wrapper: `scenes/piste_0/christmas_1982/Christmas1982_VisualSlice.tscn`

Compare A/B before further visual expansion.

## 3. Coffee-table GLB proof
Read:
- `docs/HIGGSFIELD_3D_PIPELINE.md`
- `docs/HIGGSFIELD_CREDIT_POLICY.md`

Preview:
- `scenes/piste_0/christmas_1982/CoffeeTableAssetPreview.tscn`

Do not trigger new potentially billable Higgsfield actions without explicit user approval.

## 4. House/Cyclops spike
Read only after 5.2/5.3 are stable:
- `docs/SPRINT5_4_ARCHITECTURE_EXECUTION.md`
- `docs/CYCLOPS_SPRINT5_SPIKE.md`

Do not move canonical blocking markers.

---

# Prepared design packs — NOT current implementation scope

## Guidance / assistance
Compact handoff:
- `docs/WORK_GUIDANCE_HANDOFF.md`

Decision:
- one Story Mode;
- `GUIDED / NATURAL / FREE` guidance profiles;
- `NATURAL` default;
- future Archive Mode separate.

## Physical affordances
Compact handoff:
- `docs/WORK_AFFORDANCE_HANDOFF.md`

Decision:
- world-first cues;
- small physical verb vocabulary;
- Interactable and RecordableSource remain separate;
- gate is first major post-prototype temporal interaction candidate.

## Character animation / gestures
Compact handoff:
- `docs/WORK_CHARACTER_ANIMATION_HANDOFF.md`

Decision:
- gameplay owns logic;
- animation owns presentation;
- do not build a giant animation graph now;
- validate a small P0 gesture batch first.

## Family dialogue / barks
Compact handoff:
- `docs/WORK_DIALOGUE_HANDOFF.md`

Decision:
- short contextual French-source barks + nonverbal reactions;
- stable localization keys;
- no dialogue tree for ordinary domestic life;
- voice lives in world space and may be captured naturally when REC is active;
- first later proof should be one Ronan reaction with cooldown/variation.

## Cassette-memory / Sprint 6
Compact start:
- `SPRINT6_STATUS.md`
- `docs/CASSETTE_MEMORY_STATUS.md`

Status: DESIGN ONLY / NOT STARTED.

## Audio memory / temporal capture
Compact start:
- `docs/AUDIO_MEMORY_STATUS.md`

Status: architecture prepared, not implemented in Sprint 5.

## PISTE 0 narrative gameplay
Compact start:
- `docs/PISTE0_GAMEPLAY_STATUS.md`

Design thesis:
- authored micro-quests that feel like memories;
- no conventional quest tracker/collect-all loop;
- soft failure;
- alternating pacing;
- family life creates variation.

---

# Deep documents — read only when implementing that subsystem

## Sound
- `docs/SOUND_BIBLE_1982.md`
- `docs/P0_SOUND_PRODUCTION_MATRIX.md`
- `docs/P0_RECORDING_SESSION_PLAN.md`
- `docs/AUDIO_MEMORY_PIPELINE_1982.md`
- `docs/ADR_001_TEMPORAL_AUDIO_CAPTURE.md`

## Cassette memory
- `docs/CASSETTE_LIBRARY_DESIGN.md`
- `docs/CASSETTE_PHYSICAL_UX.md`
- `docs/SPRINT6_PERSISTENCE_MODEL.md`
- `docs/RECORDING_MEMORY_CALLBACKS.md`

## Narrative beats / pacing
- `docs/PISTE0_NARRATIVE_GAMEPLAY_BEATS.md`
- `docs/PISTE0_PLAYABLE_STRUCTURE.md`
- `docs/PISTE0_IMPLEMENTATION_ROLLOUT.md`
- `docs/PISTE0_PACING_RHYTHM.md`
- `docs/FAMILY_LIVING_WORLD_DESIGN.md`
- `docs/FAMILY_DIALOGUE_BARKS_DESIGN.md`
- `docs/FAMILY_DIALOGUE_EVENT_ARCHITECTURE.md`

## Affordances
- `docs/PHYSICAL_AFFORDANCE_LANGUAGE.md`
- `docs/OBJECT_INTERACTION_FEEDBACK.md`
- `docs/P0_INTERACTION_SEQUENCE_CARDS.md`

## Character production
- `docs/CHARACTER_ART_DIRECTION_1982.md`
- `docs/CHARACTER_GESTURE_LANGUAGE.md`
- `docs/CHARACTER_ANIMATION_ARCHITECTURE.md`
- `docs/CHARACTER_GESTURE_SEQUENCE_CARDS.md`
- `docs/ANIMATION_PRODUCTION_BACKLOG.md`
- `data/character_rig_requirements.json`

---

# Live Work order
Unless the user explicitly changes priority:

1. verify branch/status;
2. run validation suite;
3. validate Player Feel live;
4. compare canonical vs Visual Slice;
5. fix presentation-only defects if required;
6. validate existing Higgsfield coffee-table round trip in isolated preview;
7. decide keep/reject candidate;
8. run Cyclops shell spike only if prior gates pass;
9. report evidence/issues;
10. do **not** begin Sprint 6 or post-prototype memory beats automatically.

## Critical principle
Prepared design is there to reduce future reasoning cost, **not to silently expand the current sprint**.
