# BO_Ta_Vie — Audio memory status

## Why this exists

This file is the short handoff for the sound/recording design work prepared while live Godot/Work access was unavailable.

Do not read every audio design file before validating Sprint 5. Start here.

## Sprint 5 runtime truth

The implemented gameplay remains:

`Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY`

Current `Recorder` still uses the simple static `RecordableSource.audio_stream` model.

That is intentional for Sprint 5.

Do **not** implement temporal bus recording before live Sprint 5 acceptance.

## What has been designed offline

### Three-stage memory sound

Every important sound can eventually exist as:

1. WORLD — physical scene truth;
2. FISHER CAPTURE — mono / narrower / imperfect child-recorder capture;
3. CASSETTE PLAYBACK — further speaker/tape character.

Primary reference:

- `docs/AUDIO_MEMORY_PIPELINE_1982.md`
- `data/audio_memory_profiles_1982.json`

### P0 sound choreography

Detailed behavior is prepared for:

- Fisher Price controls;
- Ronan;
- gate;
- wind/tree;
- fridge;
- fireplace;
- moped.

Primary reference:

- `docs/P0_INTERACTION_SOUND_CHOREOGRAPHY.md`
- `data/p0_sound_event_design.json`

### Temporal capture architecture

The preferred **future** proof is to evaluate real recording of a dedicated recordable-world audio bus over the player's actual REC interval.

This is designed to preserve:

- late starts;
- early stops;
- overlaps;
- passive ambience;
- triggered interactions;
- moving sources;
- accidental content.

Primary references:

- `docs/FUTURE_TEMPORAL_CAPTURE_ARCHITECTURE.md`
- `docs/ADR_001_TEMPORAL_AUDIO_CAPTURE.md`

ADR-001 is **Proposed**, not implemented or accepted.

### Recorder sonic grammar

REC / STOP / PLAY should eventually be understandable through physical mechanical sound before synthetic UI feedback.

Primary reference:

- `docs/RECORDER_SONIC_GRAMMAR.md`

## Key design rules

- The world itself does not sound artificially lo-fi because the story is in 1982.
- The recording device creates the archival coloration.
- Partial recordings are valid.
- No numeric recording-quality score.
- No automatic replacement of imperfect clips with pristine full samples.
- No permanent `RECORD THIS` markers.
- Interaction and recordability remain separate roles composed on world objects.
- Recorder playback must not feed the normal recordable-world capture path by default.
- Sound-on-Sound remains a later deliberate device capability.

## First future temporal-capture proof — after Sprint 5

Use only:

1. Ronan voice;
2. fireplace passive ambience;
3. one triggered gate proxy.

Pass criteria:

- actual REC start/STOP window matters;
- gate event before REC is absent;
- gate event during REC is present;
- fireplace can overlap it;
- result is still a normal playable `RecordingClip`;
- playback does not feed back into capture;
- existing simple Recorder tests remain supported.

Do not proceed to wind/fridge/moped until that proof works and feels meaningfully better than the static-source prototype.

## Sprint 5 stop gate

Before any audio-architecture implementation:

1. run `bash tests/run_sprint5_validation.sh`;
2. complete live input/gameplay validation;
3. validate `Christmas1982_VisualSlice.tscn` visually;
4. resolve blockers;
5. explicitly close Sprint 5.

Only then evaluate ADR-001 as a Sprint 6 candidate.

## Validation protection

`tests/static_validate_audio_memory_design.py` checks that:

- the audio profiles remain design-only;
- `ronan_test` is still the only required Sprint 5 recording;
- no temporal capture implementation has been inserted into `Recorder` prematurely;
- P0 sound/event IDs remain tied to the production sound catalog;
- partial recordings and anti-feedback rules remain explicit.
