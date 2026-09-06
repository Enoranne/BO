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

### HUD / interaction UX
- Added `docs/HUD_UX_SPRINT5.md`.
- Kept the canonical development HUD defaults unchanged.
- Added wrapper-only `Period1982HUDPass` for smaller warm-neutral typography and reduced visual dominance.
- Added context-first hint progression: take → record → release to stop → play.
- Visual Slice teaches Space as the primary PLAY command while legacy P remains technically available in Sprint 5.1.
- REC can receive stronger red emphasis; STOP is intentionally muted.
- No crosshair or raycast UI was introduced.
- Added `tests/static_validate_hud_ux.py`.

### Sound design preparation
- Added `docs/CHRISTMAS1982_SOUND_MAP.md` linking each future zone to meaningful sonic opportunities.
- Added a production sound catalog with P0/P1/P2 priorities, target durations, zones and file naming.
- Added `docs/SOUND_BIBLE_1982.md` for the analogue / domestic sound-language target.
- Only `ronan_test` remains a required gameplay sound during Sprint 5; future sounds remain preparation only.
- Added `tests/static_validate_sound_catalog.py`.

### Character review / art direction
- Added `CharacterReadabilityPreview.tscn` for side-by-side Malo/Ronan review.
- Added a dedicated review protocol instead of changing character geometry blindly.
- Added `docs/CHARACTER_ART_DIRECTION_1982.md` defining the production-facing age, scale, clothing, silhouette and sibling-readability targets.
- Existing procedural characters remain placeholders and are not treated as final likenesses.

### P0 prop preparation
- Added `docs/ASSET_BACKLOG_1982.md` to rank assets by narrative value, camera visibility and gameplay relevance.
- Added `docs/P0_ASSET_BRIEFS_1982.md` for Fisher Price, sofa, fireplace, Christmas tree, coffee table and gift pile.
- Asset intake now requires metre scale, clean origins, portable materials and provenance/licensing review before production approval.

### Technical budget
- Added `docs/TECHNICAL_BUDGET_SPRINT5.md` with provisional triangle, texture, material, lighting and audio guardrails.
- These are conservative iteration targets pending real Godot profiling, not final optimisation limits.
- 4K textures, excessive material slots, per-bulb shadow lights and high-complexity generated assets require a demonstrated locked-camera benefit.

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

### Camera preparation
- Added a Phantom Camera spike protocol.
- Default decision remains **do not adopt** unless live testing demonstrates a concrete advantage over the existing `CinematicCamera` contract.
- No unrestricted mouse-look / GTA-style camera has been introduced.

### Validation hardening
- Added static contracts for Player Feel, Visual Slice, HUD UX, sound catalog, external asset pipeline, house planning, character preview and Sprint 5 TSCN resources.
- Added `tests/run_sprint5_validation.sh` as a one-command validation entry point.
- Added a GitHub Actions static-validation workflow for `sprint-5`.
- Integration-authored commits did not show an immediate Actions run during this session, so Work should still execute validation directly.

## Important things deliberately not done
- No `Recorder` implementation change.
- No `InteractionContext` implementation change.
- No `MaloController` implementation change.
- No canonical `Christmas1982.tscn` geometry/gameplay change.
- No inventory, save/load, dialogue, NPC navigation, Radio Malo, MK2, pitch, Sound-on-Sound or multitrack.
- No free 360-degree camera.
- No Cyclops installation yet.
- No Phantom Camera installation yet.
- No production character replacement.
- No production approval of Higgsfield assets.
- No batch sound or asset generation.

## Credit discipline
During this hardening pass, no new Higgsfield image/video/audio generation was submitted after the single 3D Jutsu coffee-table technical import. Existing 3D Jutsu revision data was only retrieved/read for pipeline preparation. The user later reported that their Higgsfield credit balance appeared unchanged.

## First command for Work
From the repository root on branch `sprint-5`:

```bash
bash tests/run_sprint5_validation.sh
```

Then perform the live-engine sequence documented in `SPRINT5_STATUS.md`.
