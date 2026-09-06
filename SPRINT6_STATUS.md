# Sprint 6 — Recording Memory (DESIGN ONLY)

## Implementation status
**NOT STARTED.**

Sprint 6 implementation is gated by live acceptance of Sprint 5.

No cassette library, save/load system, memory annotation service, temporal capture backend, MK2 feature or Radio Malo mechanic has been added by this planning work.

## Thesis
Turn recordings into personal memories without turning BO into a conventional inventory/collectible game.

## Start here
Work/Codex should read:

1. `docs/SPRINT6_DESIGN_INDEX.md`
2. `docs/CASSETTE_MEMORY_STATUS.md`
3. only the specific deeper document needed for the implementation phase.

Do not review all planning documents chronologically.

## Prepared decisions
- Raw audio remains represented by `RecordingClip`.
- Stable recording identity is separate from display title.
- Malo's editorial state lives in a separate annotation layer.
- No global quality score.
- `FAILED_KEEP` / `RATÉ MAIS GARDER` is first-class.
- Favourite and `GOOD` are distinct.
- Retry does not imply deletion.
- Physical cassette/box metaphor comes before a modern full-screen library.
- Persistence belongs to a separate archive service, not `Recorder`.
- Later memory callbacks add meaning without rewriting childhood annotations.
- Fisher -> MK2 -> Radio Malo complexity progresses with Malo's age and equipment.

## Candidate implementation phases
- 6.0 stable ids + annotation + in-memory archive;
- 6.1 playback/review + optional child title + keep state;
- 6.2 physical cassette/box review surface;
- 6.3 versioned persistence;
- 6.4 second imperfect recording source, preferably gate if available.

## Validation already present
```bash
python tests/static_validate_cassette_memory_design.py
```

This validator is also included in:

```bash
bash tests/run_sprint5_validation.sh
```

Its purpose while on Sprint 5 is to ensure the future design remains documented **without leaking implementation into Recorder/RecordingClip prematurely**.

## Gate before starting
Do not implement until Sprint 5 has:
- static validation passing;
- Godot headless contracts passing;
- Player Feel tested live;
- Visual Slice reviewed live;
- canonical first-recording loop confirmed intact.
