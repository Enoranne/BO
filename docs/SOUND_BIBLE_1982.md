# Christmas1982 — Sound Bible

## Purpose
This document converts the sonic opportunity map into a production language for BO. It does not add new Sprint 5 gameplay requirements.

## Core principle
Sound is not decorative ambience in BO. It is simultaneously:

- a memory cue;
- a navigational cue;
- a recording target;
- a character cue;
- a material cue;
- and, later, creative raw material for Malo.

The sound design should therefore remain tactile, local and recognisable rather than broadly cinematic.

## Production hierarchy

### P0 — identity-critical
These sounds establish BO immediately and deserve the highest recording/generation quality:

- Ronan first-recording source;
- Fisher Price mechanical buttons / transport;
- fireplace bed;
- gate squeak;
- later: MK2 transport/mechanics when that device enters scope.

### P1 — world-density sounds
These make the house and garden feel alive and should be added as spaces graduate from visual shell to gameplay:

- wrapping paper;
- corridor floor creak;
- fridge hum;
- cutlery;
- garden wind;
- swing squeak;
- moped pass-by.

### P2 — later exploration/detail
These become valuable when private rooms and experimentation are playable:

- bathroom tap / plumbing resonance;
- cassette cases;
- drawers;
- turntable / records if retained;
- tape handling / repair.

## Naming convention

Use stable lower-case stems:

- `sfx_chr82_<zone>_<source>` for one-shot or source effects;
- `amb_chr82_<zone>_<source>` for ambient beds;
- suffix `_01`, `_02`, etc. only for real variations, not duplicate exports.

Examples:

- `sfx_chr82_gate_squeak_01.wav`
- `amb_chr82_salon_fireplace.wav`
- `sfx_chr82_fisher_transport_click.wav`

## File targets

Preferred production master:

- WAV;
- 48 kHz;
- 24-bit where source allows;
- mono for tightly localised mechanical sources unless stereo information is meaningful;
- stereo for ambience beds and pass-bys where spatial movement matters.

Godot import/compression should be decided later per category. Do not destructively compress source masters.

## Recording aesthetic

### Mechanical objects
Prioritise transient character and physical imperfection. The Fisher Price must sound like a chunky child-oriented cassette mechanism, not a modern UI click.

### Domestic ambience
Keep beds restrained. The house should feel occupied, not like a sound-effects showcase. Avoid stacking too many continuous loops in one room.

### Voices
Accidental and off-axis captures are part of BO's identity. Not every voice recording should sound studio-clean. However, the canonical onboarding `RonanTest` source must remain clear enough to teach the mechanic.

### Outdoor recordings
Use distance and wind variation deliberately. Passing moped, neighbour voice and gate should imply a wider world without requiring a large playable map.

## Recorder perspective
Eventually distinguish:

1. what the player hears in the world;
2. what Malo's microphone captures;
3. what the cassette playback reproduces.

The cassette playback version may later include bandwidth reduction, hiss, transport noise and level differences, but Sprint 5 must not implement that DSP prematurely.

## Dynamic-range rule
Do not make every collectible sound equally loud. The player should sometimes need to approach a source, face it, or wait for a quieter moment. However, onboarding sources must remain forgiving.

## Silence
Silence is part of the project language. Avoid permanent wall-to-wall ambience. Small quiet gaps make tape hiss, breathing, clicks and distant sounds more meaningful.

## Source-of-truth data
Production candidates and metadata live in `data/sound_catalog_1982.json`.

`docs/CHRISTMAS1982_SOUND_MAP.md` remains the spatial/narrative map; the JSON catalog is the production backlog.

## Sprint 5 constraint
Only `ronan_test` is required as a gameplay recording source for current acceptance. All other entries are preparation and must not silently expand Sprint 5 scope.
