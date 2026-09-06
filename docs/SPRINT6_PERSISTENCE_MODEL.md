# BO_Ta_Vie — Sprint 6 candidate persistence model

## Status
Design preparation only. No save/load system is authorised during Sprint 5.

## Purpose
Define what must survive between sessions once recordings become memories.

The objective is not to design a generic game save. It is to preserve the **history of Malo's archive** without coupling persistence to the Recorder, HUD or world scene.

## Core principle
Persist identity and meaning separately from runtime scene nodes.

Never serialize direct Node references as long-term memory state.

## Data layers

### 1. Recording index
Stable information needed to find/reconstruct a recording.

Candidate fields:
- stable `recording_id`;
- raw/derived audio backing reference;
- capture creation time or story-relative ordering;
- source metadata snapshot;
- device id;
- duration;
- capture era;
- integrity/version information.

### 2. Malo annotation
Per `data/cassette_memory_schema.json`:
- display title;
- keep state;
- favourite;
- child note;
- box assignment;
- person/place/object/event associations known at that age;
- transformation history later.

### 3. Narrative callback associations
Per `data/recording_memory_callback_schema.json`.

These must be allowed to evolve later without mutating the original annotation.

### 4. Physical archive state
Only persist what is narratively meaningful.

Candidate fields:
- cassette/tape assignment;
- side/order if physical tape simulation is retained;
- box/pile assignment;
- physical label text;
- optional wear/state later.

Do not persist incidental transform positions of every cassette prop unless the game genuinely relies on them.

## Stable identity rule
A recording id must survive:
- title changes;
- box changes;
- later favourite changes;
- new narrative associations;
- device-specific derived versions.

Do not use:
- display title;
- filename alone;
- source id alone;
- array index;
- scene node path
as durable recording identity.

## Candidate id format
Implementation may use UUID or another stable opaque id.

Human-facing text should never expose this id during normal play.

## Raw audio backing
Potential future approaches:

### A. Saved WAV/resource per captured recording
Simple and explicit for true temporal captures.

### B. Deterministic source reference + capture window metadata
May remain useful for prototype/static sources but is not sufficient for fully dynamic accidental recordings.

### Recommendation
Once true temporal capture exists, persist the resulting captured audio artifact rather than relying on the world source still existing in the same form later.

## Save versioning
Start versioned from day one.

Example conceptual root:

```json
{
  "schema_version": 1,
  "recordings": [],
  "annotations": {},
  "associations": {},
  "physical_archive": {}
}
```

Even the first prototype should include `schema_version` so future MK2/Radio Malo changes do not require brittle migration guesses.

## Migration rule
Never silently discard an old recording because its metadata schema changed.

When migration cannot fully understand a field:
- preserve raw data where feasible;
- warn in development;
- keep the audio playable if possible.

The archive is narratively important data.

## Persistence ownership
Recommended future service:

`RecordingArchive` / `MemoryArchive` domain service

Responsibilities:
- stable ids;
- recording index;
- annotation lookup/update;
- association lookup/update;
- serialization boundary;
- migration/versioning.

Non-responsibilities:
- REC/STOP state machine;
- audio bus capture;
- HUD wording;
- world interaction detection;
- physical cassette animation.

## Recorder integration
`Recorder` should emit/return a completed recording.

A higher-level archive service can then register it.

Avoid making `Recorder` save files directly.

Conceptual future flow:

`Recorder completes clip -> archive assigns stable id -> annotation starts UNREVIEWED -> persistence layer records state`

## Save timing
Potential safe moments:
- after a recording is finalised;
- after annotation/box change;
- after narrative association discovery;
- explicit checkpoint/scene transition.

Do not write to disk every frame or while REC is actively capturing.

## Incomplete recordings / crash safety
A future temporal capture backend may need temporary files while recording.

Recommendation:
- use a temporary/in-progress capture identity;
- only promote to durable archive after STOP finalises successfully;
- clean orphaned temporary captures safely on startup;
- never present half-written audio as a normal cassette without explicit recovery design.

## Derived recordings
Later MK2 transformations should preserve lineage.

Example:

`recording_original_id`
→ `derived_recording_id`
→ transformation metadata

A derivative can have its own annotation while retaining provenance to the original.

Do not destructively replace the source clip when applying pitch or Sound-on-Sound experiments.

## Radio Malo compositions
Later compositions should reference recordings/derivatives by stable ids.

This makes old childhood captures reusable without copying their entire metadata into every programme.

## Deletion policy
Early Sprint 6: no destructive delete.

Later if physical overwrite exists:
- archive semantics must explicitly distinguish `lost/overwritten` from `deleted by UI`;
- narrative systems may still need provenance that a recording once existed;
- actual audio retention policy must be designed carefully before implementation.

## Privacy / export
No cloud sync or external media export is needed for the first implementation.

Keep the prototype local and deterministic.

## Acceptance for persistence phase
Persistence is accepted only if:

1. two recordings survive a restart;
2. stable ids remain unchanged;
3. child titles survive;
4. `GOOD` / `FAILED_KEEP` states survive;
5. favourite survives independently;
6. physical box assignment survives;
7. playback still resolves the correct audio;
8. schema version is present;
9. corrupted/missing audio fails clearly rather than loading the wrong clip;
10. Recorder remains unaware of save-file mechanics.

## Sprint 5 boundary
Do not add save/load code now.

This document exists so Work will not have to redesign persistence from scratch when Sprint 6 reaches that phase.
