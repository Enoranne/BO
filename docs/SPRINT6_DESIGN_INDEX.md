# BO_Ta_Vie — Sprint 6 Design Index

## Status
Future design only. Do not implement Sprint 6 before Sprint 5 live-engine acceptance.

## One-sentence thesis
Sprint 6 should prove that **a captured sound can become a personally meaningful memory**, while keeping the Recorder, archive, annotation and narrative layers decoupled.

## Read order for Work
Do **not** read all Sprint 6 design files blindly. Use this order:

1. `docs/CASSETTE_MEMORY_STATUS.md` — 2-minute handoff summary.
2. `docs/SPRINT6_RECORDING_MEMORY_PLAN.md` — smallest playable proof and implementation order.
3. `data/cassette_memory_schema.json` — proposed editorial/memory data model.
4. `docs/CASSETTE_PHYSICAL_UX.md` — physical review metaphor.
5. `docs/SPRINT6_PERSISTENCE_MODEL.md` — only when persistence work begins.
6. `docs/RECORDING_MEMORY_CALLBACKS.md` — only after base archive/persistence is stable.
7. `docs/RECORDING_EVOLUTION_BY_ERA.md` — roadmap guardrail for Fisher -> MK2 -> Radio Malo.

Supporting files:
- `data/child_recording_title_rules.json`
- `data/cassette_memory_examples.json`
- `data/recording_memory_callback_schema.json`
- `docs/CASSETTE_LIBRARY_DESIGN.md`

Validation:

```bash
python tests/static_validate_cassette_memory_design.py
```

## Architecture decisions already made

### Raw capture remains raw
`RecordingClip` stays focused on captured audio data.

### Editorial meaning is separate
Malo/player state lives in a separate annotation layer keyed by stable recording id.

### Stable id != title
`RONAN`, `PORTAIL`, etc. are human-facing labels only.

### No quality score
The system does not grade recordings globally.

### `RATÉ MAIS GARDER` is first-class
A failed recording may be worth more than a technically clean one.

### Favourite != GOOD
Emotional value and technical/personal approval are different.

### Physical metaphor first
Early review should happen through cassette/boxes/piles before a full media-library UI.

### Persistence is its own service
Recorder must not own save/load mechanics.

### Old meanings are preserved
Later narrative callbacks add associations; they do not rewrite the child annotation.

### Device/age controls complexity
Fisher = capture/replay/keep.
MK2 = experimentation/transformation.
Radio Malo = composition/performance.

## Recommended smallest Sprint 6 sequence

### 6.0 Architecture
- stable recording id;
- annotation data/resource;
- in-memory archive service;
- tests.

### 6.1 Review
- new clip -> `UNREVIEWED`;
- PLAY;
- optional child title;
- `BIEN` / `RATÉ MAIS GARDER`;
- no deletion.

### 6.2 Physical presentation
- one small cassette/box review surface;
- 2–5 recordings maximum;
- tactile playback/classification.

### 6.3 Persistence
- versioned save schema;
- recording ids + annotations + audio resolution survive restart.

### 6.4 Second recording source
- gate preferred if available;
- demonstrate imperfect take worth keeping.

## Do not implement yet
- Radio Malo;
- MK2 transformations;
- pitch;
- Sound-on-Sound;
- multitrack;
- waveform editor;
- transcript system;
- rarity/completion system;
- large inventory;
- cloud sync;
- destructive delete;
- memory callback banners.

## Signature design test
A valid future session should allow:

`record gate -> miss part of squeak -> hear Mother's distant voice -> replay -> name ENCORE PORTAIL -> classify RATÉ MAIS GARDER`

If that moment feels valuable without points, rarity or a quest reward, the design is working.
