# GdUnit4 spike — Sprint 5

## Baseline

- protected source branch: `sprint-5`
- baseline commit: `8fa43a8130b38611163a70a17c3d9da0dce0db35`
- spike branch: `spike/gdunit4-sprint5`
- Godot target: `4.7.0 stable`
- GdUnit4 pinned version: `v6.2.1`

## Decision rule

VALUE > COMPLEXITY.

Adopt GdUnit4 only if it improves runtime regression coverage without coupling gameplay code to the test framework or replacing the existing static validation pipeline.

## Scope

This spike is intentionally narrow:

1. keep all Sprint 5 gameplay files unchanged;
2. keep the existing Python/static validation workflow unchanged;
3. add one GdUnit4 suite for the Recorder contract;
4. run it independently in GitHub Actions;
5. use CI installation of GdUnit4 rather than vendoring the full addon into the repository during the spike.

## Initial Recorder coverage

The suite validates:

- initial STOP state;
- clean rejection of PLAY without a clip;
- clean rejection of REC without a source;
- REC with a valid `RecordableSource`;
- rejection of a second REC while busy;
- creation and independent storage of `RecordingClip`;
- preservation of source id, title, metadata, duration and creation timestamp;
- PLAY of the latest clip;
- rejection of a second PLAY while busy;
- return to STOP;
- architectural decoupling of `Recorder` from narrative, quest, interaction-context and camera systems.

## Protected architecture

GdUnit4 must not become a dependency of production scripts. In particular:

- `Recorder` remains unaware of quests, NPCs, cameras and narrative state;
- `InteractionContext` remains separate from narrative progression;
- no change to the canonical `Christmas1982.tscn` is required for the test framework;
- existing headless/static tests remain valid during migration.

## Adoption criteria

### ACCEPT

Adopt GdUnit4 after the spike if:

- the GdUnit4 CI job passes reliably;
- test failures are more readable/actionable than the current hand-rolled SceneTree runner;
- setup remains isolated to tests/CI;
- no production file changes are needed;
- execution time and maintenance overhead remain reasonable.

### REJECT

Reject or postpone it if:

- Godot/GdUnit version pinning is fragile;
- CI installation becomes a recurring source of failures;
- it requires invasive project/plugin configuration;
- it duplicates existing validation without materially improving regression detection.

## Migration path if accepted

Do not mass-convert tests. Migrate in this order:

1. `test_recorder.gd`;
2. gameplay contract;
3. player input contract;
4. Sprint 5 scene contract;
5. presentation/visual contracts only where runtime assertions add value.

Keep Python design/static contracts as a separate layer.
