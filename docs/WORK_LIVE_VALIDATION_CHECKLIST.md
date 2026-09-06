# Sprint 5 — Work / Godot Live Validation Checklist

## Purpose
Give Work a deterministic order of operations when Godot-MCP becomes available again. This checklist is operational; it does not replace the later copy/paste handoff message prepared for the user.

## Phase 0 — Repository safety
1. Confirm repository: `Enoranne/BO`.
2. Confirm branch: `sprint-5`.
3. Confirm working tree before edits.
4. Do not reset/rebuild Sprint 1–4.
5. Read `AGENTS.md` and `SPRINT5_STATUS.md` before modifying files.
6. Call Godot-MCP status first.

## Phase 1 — Automated validation
From repository root:

```bash
bash tests/run_sprint5_validation.sh
```

Expected sequence includes:
- core static contract;
- Visual Slice contract;
- Player Feel contract;
- asset pipeline contract;
- house planning contract;
- character preview contract;
- TSCN resource contract;
- sound catalog contract;
- HUD UX contract;
- interaction planning contract;
- existing Godot headless contracts when Godot is available.

Stop and repair deterministic test failures before visual experimentation.

## Phase 2 — Canonical gameplay baseline
Open/run `Christmas1982.tscn` first.

Verify:
1. Malo spawns correctly.
2. movement works with the physical keyboard layout;
3. E takes Fisher Price;
4. left click also takes Fisher Price when context is valid;
5. held recorder visual appears;
6. approach Ronan;
7. hold R starts REC;
8. release R stops and creates `RonanTest` clip;
9. Space plays latest recording;
10. P still works as prototype fallback;
11. first-recording beat completes.

Capture baseline screenshot A from the locked camera.

Do not change the canonical scene simply because the Visual Slice looks different.

## Phase 3 — Visual Slice 5.2
Open/run `Christmas1982_VisualSlice.tscn`.

Verify material/readability pass:
- floor;
- cream walls;
- sofa upholstery;
- coffee-table wood;
- fireplace stone;
- Fisher beige/burgundy/dark cassette details.

Verify dressing:
- skirting;
- mantel;
- sofa cushions;
- tree ornaments.

Verify lighting:
- fireplace key is warm but not clipped;
- tree practical supports the right side of frame;
- fill retains Malo/Ronan readability;
- shadows are not crushed into unreadable brown/black masses.

Verify debug cleanup:
- floating Fisher and Ronan labels are hidden;
- interactions remain understandable through staging/HUD.

Capture screenshot B from the same camera framing as A.

## Phase 4 — HUD / interaction UX
In Visual Slice only, confirm:

- objective no longer visually shouts `OBJECTIVE`;
- STOP is subdued;
- REC gains stronger visual emphasis;
- hint sequence is contextual rather than showing all keys at once;
- before pickup: Fisher instruction is clear;
- after pickup and near Ronan: `Hold R  Record`;
- during REC: `Release R  Stop`;
- after clip creation: acknowledgement appears briefly, then `Space  Play`;
- during playback: playback state is readable;
- P remains supported even though it is not taught prominently;
- no crosshair appears.

If a hint becomes ambiguous, adjust presentation only; do not move action ownership into HUD.

## Phase 5 — Character readability preview
Open `CharacterReadabilityPreview.tscn`.

Review:
- Malo reads younger/smaller than Ronan;
- clothing colour families separate the brothers;
- silhouette remains readable at gameplay distance;
- placeholder limitations are documented rather than over-polished.

Use `docs/CHARACTER_ART_DIRECTION_1982.md` for future candidate review.

## Phase 6 — Higgsfield coffee-table round trip
Only after Phases 1–5 are stable:

1. retrieve Higgsfield revision-1 GLB for `BO_CoffeeTable_Test`;
2. place it at `assets/3d/higgsfield/coffee_table_test.glb`;
3. do not place it directly in canonical Christmas1982;
4. assign it only to `CoffeeTableAssetPreview.tscn` / ExternalAssetSlot;
5. inspect scale against target envelope;
6. inspect origin/orientation;
7. inspect materials/textures;
8. obtain triangle/material/texture counts where possible;
9. check provenance/license state;
10. compare period credibility to current placeholder.

Decision:
- KEEP AS PIPELINE CANDIDATE;
- REWORK;
- DISCARD.

Do not import a second Higgsfield production prop until this decision is made.

## Phase 7 — Cyclops 5.4 spike
Only after Visual Slice and first asset round trip are stable.

Follow `docs/SPRINT5_4_ARCHITECTURE_EXECUTION.md`.

Build only:
- believable wall thickness;
- room corners;
- one corridor doorway;
- short corridor visual depth;
- shallow kitchen glimpse;
- optional trim.

Do not rebuild furniture in the first Cyclops pass.

Capture screenshot C from the locked camera.

Explicitly decide:
- ADOPT CYCLOPS AS AUTHORING TOOL;
- DISCARD CYCLOPS.

No neutral/implicit adoption.

## Phase 8 — Optional Phantom Camera spike
Run only if the existing `CinematicCamera` demonstrates a concrete problem.

Follow the Phantom Camera spike document.

Do not replace the existing camera merely because an addon is available.

## Phase 9 — Sprint 5 scorecard
Complete `docs/SPRINT5_DEFINITION_OF_DONE.md`.

Sprint 5 can close at 80/100 or higher with no blocker.

If the score is below target, fix the highest-impact deduction first instead of adding new systems.

## Absolute stop conditions
Stop live experimentation and report before continuing if:
- Recorder loop regresses;
- blocking moves unexpectedly;
- imported asset corrupts scene/resource state;
- Cyclops requires runtime coupling;
- camera framing becomes unstable;
- Visual Slice fails to load;
- a generated/imported asset has unresolved rights status but is about to be treated as production art.
