# Sprint 5 — Offline hardening pass

## Purpose
Record the work completed while live Work/Godot-MCP access was unavailable. This document is a handoff aid; `SPRINT5_STATUS.md` remains the main sprint status.

## What was safely advanced without live Godot

### Player feel
- Added left-click context interaction alongside E.
- Added Space as preferred PLAY-latest input while keeping P during the prototype.
- Preserved hold-R / release-R Recorder behaviour.
- Preserved physical-key movement for QWERTY/AZERTY compatibility.

### Visual Slice
- Added external 1982 material resources.
- Added reversible material/light/readability pass around the canonical scene.
- Added visual-only skirting, fireplace mantel, sofa cushions and sparse tree ornaments.
- Hid large in-world Fisher/Ronan debug labels in the Visual Slice only.
- Improved the world Fisher Price placeholder with visual-only cassette panel, cassette window, handle and buttons.
- Preserved all canonical gameplay collisions and blocking.

### Character review
- Added `CharacterReadabilityPreview.tscn` for side-by-side Malo/Ronan review.
- Added a dedicated review protocol instead of changing character geometry blindly.

### Higgsfield 3D pipeline
- Created one 3D Jutsu technical project and imported one catalog coffee-table candidate.
- Created no batch asset pipeline and no runtime Higgsfield dependency.
- Added a runnable isolated Godot preview scene with floor, camera, lights and target envelope.
- Added asset provenance manifest with explicit unapproved/unverified state.
- The actual GLB remains absent from the repository until Work can validate it.

### House / Cyclops planning
- Added room-zone topology and indicative metre-scale dimensions.
- Added sonic opportunity map tying future rooms to recording value.
- Added exact 5.4 Cyclops execution plan and stop conditions.
- Corridor and kitchen glimpse remain non-playable in the first architecture pass.

### Validation hardening
- Added static contracts for Player Feel, Visual Slice, external asset pipeline, house planning, character preview and Sprint 5 TSCN resources.
- Added `tests/run_sprint5_validation.sh` as a one-command validation entry point.
- Added a GitHub Actions static-validation workflow for `sprint-5`.
- Integration-authored commits did not show an immediate Actions run during this session, so Work should still execute validation directly.

## Important things deliberately not done
- No `Recorder` implementation change.
- No `InteractionContext` implementation change.
- No `MaloController` implementation change.
- No canonical `Christmas1982.tscn` change.
- No inventory, save/load, dialogue, NPC navigation, Radio Malo, MK2, pitch, Sound-on-Sound or multitrack.
- No free 360-degree camera.
- No Cyclops installation yet.
- No Phantom Camera installation yet.
- No production character replacement.
- No production approval of Higgsfield assets.

## Credit discipline
During this hardening pass, no new Higgsfield image/video/audio generation was submitted. Existing 3D Jutsu revision data was only retrieved/read for pipeline preparation.

## First command for Work
From the repository root on branch `sprint-5`:

```bash
bash tests/run_sprint5_validation.sh
```

Then perform the live-engine sequence documented in `SPRINT5_STATUS.md`.
