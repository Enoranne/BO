# BO_Ta_Vie — Cassette Memory Design Status

## Scope
Sprint 6+ design preparation only. No cassette-library mechanics are implemented in Sprint 5.

## Core decision
A `RecordingClip` remains the raw captured audio object.

Malo's editorial/memory judgement is a separate layer keyed by stable recording id.

Do not make `Recorder` own:
- favourites;
- boxes;
- child titles;
- keep states;
- memory associations;
- save/load UI state.

## Childhood keep language
Primary states prepared:
- `UNREVIEWED`
- `KEEP`
- `GOOD`
- `FAILED_KEEP` = `RATÉ MAIS GARDER`
- `RETRY`
- `IMPORTANT`
- `ARCHIVED`

`GOOD` and `favourite` are deliberately different concepts.

A failed recording may be a favourite.

## Early physical organisation
Preferred boxes/piles:
- `CASSETTES`
- `BIEN`
- `RATÉS MAIS GARDER`
- optional `À REFAIRE`

The first review experience should be a physical world-space cassette/box metaphor, not a Spotify/iTunes-style menu.

## Naming
At age six, titles are short, concrete and optional.

Examples:
- `RONAN`
- `RIRE RONAN`
- `PORTAIL`
- `ENCORE PORTAIL`
- `VENT FORT`
- `BRUIT BIZARRE`

Stable ids must never depend on these display titles.

## First Sprint 6 proof
Recommended smallest useful loop:

1. create a recording;
2. assign stable recording id;
3. mark it `UNREVIEWED`;
4. play it back;
5. optionally title it;
6. classify as `BIEN` or `RATÉ MAIS GARDER`;
7. show/place it in a physical cassette/box review surface;
8. repeat with a second take;
9. only then add persistence.

## Signature example
A gate recording begins too late, but Mother's distant voice appears in the background.

The player chooses:

`ENCORE PORTAIL` -> `RATÉ MAIS GARDER`

No score, rarity or collectible reward is displayed. The value comes from the accidental memory.

## Implementation gate
Do not begin Sprint 6 cassette-library implementation until Sprint 5 is accepted live in Godot.

First read:
- `docs/CASSETTE_LIBRARY_DESIGN.md`
- `data/cassette_memory_schema.json`
- `docs/CASSETTE_PHYSICAL_UX.md`
- `docs/SPRINT6_RECORDING_MEMORY_PLAN.md`
- `data/child_recording_title_rules.json`
- `data/cassette_memory_examples.json`

Validation:

```bash
python tests/static_validate_cassette_memory_design.py
```

## Explicitly deferred
- full inventory;
- save/load implementation;
- permanent deletion;
- tape capacity simulation;
- automatic transcription;
- score/rarity systems;
- full-screen media library;
- MK2-specific editing;
- Radio Malo.
