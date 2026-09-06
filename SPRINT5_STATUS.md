# Sprint 5 — Visual Vertical Slice

## Goal
Transform the existing Christmas1982 greybox into a convincing playable visual slice while preserving the validated Sprint 4 gameplay loop and presentation contract.

The gameplay loop remains:

`Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY`

Sprint 5 is primarily a **visual, environmental and cinematographic** sprint. It must not broaden gameplay scope.

## Target outcome
A player should be able to launch `Christmas1982`, understand the salon as a believable late-1970s / early-1980s family interior, identify Malo/Ronan/Fisher Price immediately, complete the first-recording beat, and feel that the project has moved from technical greybox toward an authored narrative game.

## Implemented scaffolding
- Branch `sprint-5` created directly from Sprint 4 commit `41e0cfd8ec1682a7b056c343828094405911e42d`.
- Sprint 5 lock added to `AGENTS.md`.
- Reusable period palette documented in `docs/MATERIAL_PALETTE_1982.md`.
- Presentation-only material override utility added at `visual/period_1982_visual_pass.gd`.
- Reversible wrapper scene added at `scenes/piste_0/christmas_1982/Christmas1982_VisualSlice.tscn`.
- Wrapper instances the canonical Sprint 4 scene rather than replacing it.
- Dedicated Sprint 5 static contract added at `tests/static_validate_sprint5.py`.
- Compact house expansion documented in `docs/CHRISTMAS1982_HOUSE_EXPANSION.md`.
- Cyclops evaluation protocol documented in `docs/CYCLOPS_SPRINT5_SPIKE.md`.
- Open-source adoption rules documented in `docs/OPEN_SOURCE_ADOPTION.md`.

## Sprint 5.1 — Player Feel
Implemented without changing `MaloController`, `Recorder` or `InteractionContext` domain behaviour:

- movement remains on Godot physical WASD positions, which correspond to WASD on QWERTY and ZQSD on AZERTY;
- `E` remains interaction;
- left mouse button is now an alternate context-interaction input;
- `R` remains hold-to-REC and release-to-STOP;
- `Space` is now the preferred PLAY-latest input;
- legacy `P` PLAY remains available during the prototype;
- the numeric keypad is not required;
- HUD hints teach the new controls;
- `docs/PLAYER_FEEL_INPUTS.md` documents the contract;
- `tests/static_validate_player_feel.py` validates the input architecture.

Left click currently acts on the interactable already selected by `InteractionContext`; it is deliberately not a point-and-click raycast yet. No unrestricted mouse-look has been added.

## Sprint 5.2 — Visual Slice
Implemented as a reversible presentation layer around the canonical Sprint 4 scene:

- `Christmas1982_VisualSlice.tscn` still instances `Christmas1982.tscn`; the canonical gameplay scene is unchanged;
- wall, floor, rug, sofa, wood, fireplace and Fisher Price materials are overridden only in the wrapper;
- additional period materials now include dark warm flooring, warm fireplace stone, painted cream trim and muted-red Christmas ornaments;
- fireplace, tree and fill lights receive a restrained presentation-only balance pass;
- large in-world debug labels over Fisher Price and Ronan are hidden in the Visual Slice while the contextual HUD remains active;
- the world Fisher Price receives a visual-only burgundy front panel so it reads closer to the intended beige/burgundy object language;
- `visual/period_1982_set_dressing.gd` adds visual-only skirting boards, a fireplace mantel, three sofa cushions and sparse tree ornaments;
- the set-dressing layer creates no collision shapes, Areas or CharacterBodies;
- `tests/static_validate_sprint5.py` now validates the 5.2 separation contract;
- `docs/SPRINT5_2_VISUAL_REVIEW.md` defines the mandatory A/B and gameplay regression review.

Sprint 5.2 remains **pending live Godot/MCP visual acceptance**. No claim is made yet that the new lighting or detail placement looks correct in-engine.

## Sprint 5.3 — Higgsfield 3D Asset Pipeline
Started in parallel as a single-object technical proof, without changing the canonical Godot scene.

- Higgsfield / 3D Jutsu project created: `BO_Sprint5_3_AssetPipeline`.
- Project ID: `be670f5b-c348-42a3-b025-85e4054d0373`.
- First catalog search uses `coffee table`.
- Test asset imported: `Coffee Table`, catalog asset ID `1e3a1161-ba81-4b72-a9fd-22ca654843a1`.
- Scene entity name: `BO_CoffeeTable_Test`.
- Higgsfield entity ID: `20f51259-b8db-4241-8a50-e4623b047d37`.
- Import settled at Higgsfield revision `1`, scene sequence `1`.
- A GLB export exists for revision `1`.
- `docs/HIGGSFIELD_3D_PIPELINE.md` records the round-trip acceptance contract.
- Godot-side reversible slot added at `visual/external_asset_slot.gd`.
- Isolated preview scene added at `scenes/piste_0/christmas_1982/CoffeeTableAssetPreview.tscn`.
- The preview currently uses an empty target envelope matching the existing coffee-table footprint and does **not** hard-reference a missing GLB.
- Reserved import path documented at `assets/3d/higgsfield/README.md`.
- `tests/static_validate_asset_pipeline.py` validates that the asset slot has no Recorder, interaction or collision dependency.

The table is **not approved as production art** yet. It exists only to validate Higgsfield -> GLB -> Godot -> visual review. No batch import should happen before this single object passes the complete round trip.

## Sprint 5.4 — Architecture / Cyclops planning
Prepared offline so Work can execute it immediately after 5.2/5.3 validation.

- `data/christmas1982_house_zones.json` defines the planning topology and indicative metre-scale dimensions for salon, corridor, kitchen glimpse, future kitchen, bedroom zone, bathroom, garden, tree cabin, gate and street edge.
- The salon remains the locked canonical anchor.
- Corridor and kitchen glimpse are explicitly non-playable in the first 5.4 pass.
- `docs/CHRISTMAS1982_SOUND_MAP.md` ties every future zone to meaningful recording, memory and character opportunities so the house expands by density rather than empty floor area.
- `docs/SPRINT5_4_ARCHITECTURE_EXECUTION.md` defines the exact Cyclops build order, A/B/C evidence, decision gate and stop conditions.
- `tests/static_validate_house_plan.py` validates the planning contract and protects the canonical blocking scope.
- `AGENTS.md` now contains a dedicated 5.4 architecture lock.

No Cyclops addon has been installed and no canonical scene geometry has been changed yet. This is preparation only until live Godot/MCP review is available.

## Material targets currently prepared
- warm cream wallpaper;
- dark varnished wood;
- muted brown/orange upholstery;
- muted brown carpet/rug;
- dark warm floor;
- warm fireplace stone;
- painted cream trim;
- muted-red tree ornaments;
- aged Fisher Price beige plastic;
- muted burgundy Fisher Price panel plastic.

## Explicitly not added
- inventory;
- save/load;
- dialogue tree;
- NPC navigation or open-world simulation;
- Radio Malo;
- MK2 mechanics;
- pitch, Sound-on-Sound or multitrack;
- combat, vehicles, GTA-style systems;
- final production character likenesses;
- mouse raycast selection;
- free 360-degree camera;
- numeric-keypad dependency;
- production-grade 3D prop replacement;
- traversable expansion beyond the salon.

## Acceptance contract
1. The Sprint 4 first-recording beat order remains FIND_FISHER -> RECORD_RONAN -> PLAY_RECORDING -> COMPLETE.
2. Malo can still reach the Fisher Price and RonanTest without collision regressions.
3. REC/STOP/PLAY behaviour remains owned by the existing Recorder system.
4. Spatial locks in `docs/CHRISTMAS1982_LAYOUT.md` and `docs/CHRISTMAS1982_BLOCKING.md` remain valid unless a specific visual change is documented.
5. Visual improvements remain separable from gameplay logic.
6. Any external addon is evaluated on a branch-safe, reversible basis and must not become a hard dependency before validation.
7. `tests/static_validate.py` must still report `0 failure(s)`.
8. `tests/static_validate_sprint5.py` must report `0 failure(s)`.
9. `tests/static_validate_player_feel.py` must report `0 failure(s)`.
10. `tests/static_validate_asset_pipeline.py` must report `0 failure(s)`.
11. `tests/static_validate_house_plan.py` must report `0 failure(s)`.
12. Godot headless acceptance tests must still pass when the runtime is available.
13. Real editor/MCP visual and input inspection is required before Sprint 5 can be considered accepted.
14. The first Higgsfield GLB must be validated in isolation before any second production-prop import.
15. Cyclops is adopted only if the A/B/C architecture spike improves iteration without adding runtime coupling.

## Next live-engine validation
When Godot / Work is available:

1. run `tests/static_validate.py`;
2. run `tests/static_validate_sprint5.py`;
3. run `tests/static_validate_player_feel.py`;
4. run `tests/static_validate_asset_pipeline.py`;
5. run `tests/static_validate_house_plan.py`;
6. run the existing headless Godot suite;
7. test movement on the available keyboard layout;
8. verify `E` and left click both take the Fisher Price when in interaction range;
9. verify hold/release `R` still creates the RonanTest clip;
10. verify `Space` and `P` both play the latest clip;
11. open canonical `Christmas1982.tscn` and capture the baseline camera view;
12. open `Christmas1982_VisualSlice.tscn` and capture the same view;
13. compare A/B using `docs/SPRINT5_2_VISUAL_REVIEW.md`;
14. verify the hidden world labels do not make Fisher/Ronan interactions unclear;
15. inspect skirting, mantel, cushions, ornaments and Fisher front panel for floating/intersection errors;
16. verify the new light balance keeps Malo, Ronan and Fisher readable;
17. if 5.2 passes, retrieve/import the revision-1 `BO_CoffeeTable_Test` GLB into `assets/3d/higgsfield/coffee_table_test.glb`;
18. assign the imported PackedScene only in `CoffeeTableAssetPreview.tscn` first;
19. compare the candidate against the target envelope for scale, orientation, materials and mesh complexity;
20. only after the coffee-table round trip passes, decide whether Higgsfield becomes the preferred prop-production route for Sprint 5;
21. if the visual slice remains stable, execute `docs/SPRINT5_4_ARCHITECTURE_EXECUTION.md` as an isolated Cyclops spike;
22. capture A/B/C evidence and make an explicit keep/discard decision for Cyclops.

## Current state
- Branch: `sprint-5`.
- Canonical gameplay architecture: preserved.
- Automated validation checkpoint (2026-09-06): 23 static validators and 7 Godot 4.7 headless suites pass from an empty engine cache; zero engine diagnostics in the final log.
- Player Feel 5.1 bindings: four automated input-event routes pass in canonical and Visual Slice scenes; manual keyboard/mouse feel and listening still pending.
- Visual Slice 5.2 implementation: runtime loading and structural separation pass; actual visual inspection and A/B captures still pending.
- Character preview: fixed label children preventing procedural geometry; both placeholders instantiate, visual/age readability still pending.
- Higgsfield 5.3 pipeline: Godot integration scaffold prepared; GLB still intentionally absent from the repository.
- Sprint 5.4 architecture: planning/data/test contract prepared; no live geometry changes yet.
- Gameplay mechanics added by 5.1/5.2/5.3/5.4 planning: none.
- Visual/input acceptance: pending live Godot/MCP inspection.
- `SPRINT 5 READY FOR ACCEPTANCE: NO` — graphical display/MCP unavailable in the validation session.
- Results, observed fixes and remaining gates: [2026-09-06 validation report](docs/SPRINT5_VALIDATION_REPORT_2026-09-06.md).
