# BO_Ta_Vie — Sprint 5

Godot 4.7.x prototype for **PISTE 0 — Christmas1982**.

## Current scope

The only implemented gameplay loop remains:

`Malo → Fisher Price → REC → capture RonanTest → STOP → PLAY`

Sprint 5 improves **player feel, visual presentation, external-asset integration scaffolding and house-architecture planning** without broadening the gameplay loop.

No inventory, save system, dialogue tree, NPC navigation, Radio Malo, MK2 mechanics, pitch, Sound-on-Sound or multitrack is implemented.

## Controls — Sprint 5.1

- **WASD on QWERTY / ZQSD on AZERTY** — move Malo (physical key cluster)
- **E or left mouse button** — context interaction / take Fisher Price when prompted
- **Hold R** — record the nearest recordable source
- **Release R** — stop and create a `RecordingClip`
- **Space** — play latest recording
- **P** — legacy PLAY shortcut kept during the prototype
- Numeric keypad is **not required**

Left mouse currently triggers the interactable already selected by `InteractionContext`; it is not a point-and-click raycast system. The cinematic camera is still fixed/semi-fixed rather than a free GTA-style camera.

## Architecture

- `Interactable` — generic interaction contract with priority and enable/disable.
- `InteractionContext` — owns proximity selection for interactables and recordable sources.
- `RecordableSource` — generic in-world audio source with metadata.
- `RecordingClip` — independent `Resource` containing source, duration, timestamp, metadata and stream.
- `Recorder` — device-agnostic STOP / REC / PLAY state machine.
- `FisherPrice` — first recorder device shell with PLACED / EQUIPPED / ACTIVE states.
- `MaloController` — movement and player-intent orchestration; it does not scan the world itself.
- `PlaceholderHumanoid3D` — procedural temporary character rig used by Malo and Ronan.
- `FisherPriceVisual` — carried device placeholder observing the real Recorder state.
- `Christmas1982Director` — presentation-only first-recording beat observer; it does not own Recorder logic.
- `CinematicCamera` — fixed/semi-fixed framing with deliberately limited follow around Malo's spawn anchor.
- `HUD` — signal-driven presentation only; it does not own gameplay state.

The recorder exposes capability descriptors (`track_count`, `supports_pitch`, `supports_sound_on_sound`) so a future Philips D6920 MK2 can extend the device profile without changing Malo or the interaction contract. These future mechanics are deliberately not implemented yet.

## Sprint 5.2 — Visual Slice

The canonical gameplay scene remains:

`res://scenes/piste_0/christmas_1982/Christmas1982.tscn`

A reversible presentation wrapper is available at:

`res://scenes/piste_0/christmas_1982/Christmas1982_VisualSlice.tscn`

It instances the canonical scene and adds presentation-only changes:

- period 1982 material overrides;
- warmer wall/floor/furniture palette;
- Fisher Price beige/burgundy visual language;
- restrained fireplace/tree/fill-light balance;
- visual-only skirting, mantel, sofa cushions and tree ornaments;
- removal of large floating debug labels in the Visual Slice while retaining contextual HUD guidance.

The Visual Slice has **not yet received live Godot/MCP visual acceptance**. Compare canonical A versus Visual Slice B using `docs/SPRINT5_2_VISUAL_REVIEW.md`.

## Sprint 5.3 — Higgsfield 3D pipeline

Higgsfield / 3D Jutsu is treated as an **asset-production workspace**, never as a runtime dependency.

Current proof-of-pipeline:

- project `BO_Sprint5_3_AssetPipeline`;
- one coffee-table catalog asset imported and committed as Higgsfield revision 1;
- GLB export exists;
- Godot-side reversible asset slot: `visual/external_asset_slot.gd`;
- isolated preview: `scenes/piste_0/christmas_1982/CoffeeTableAssetPreview.tscn`;
- intended repository import path: `assets/3d/higgsfield/coffee_table_test.glb`.

The GLB is intentionally not referenced by the canonical scene until isolated Godot validation passes. See `docs/HIGGSFIELD_3D_PIPELINE.md`.

## Sprint 5.4 — compact house / Cyclops preparation

The goal is a dense narrative **micro-hub**, not an open world.

Planning assets:

- `data/christmas1982_house_zones.json` — room topology and indicative dimensions;
- `docs/CHRISTMAS1982_HOUSE_EXPANSION.md` — expansion strategy;
- `docs/CHRISTMAS1982_SOUND_MAP.md` — future sonic value of every room;
- `docs/CYCLOPS_SPRINT5_SPIKE.md` — Cyclops evaluation rules;
- `docs/SPRINT5_4_ARCHITECTURE_EXECUTION.md` — exact live-engine build order and stop conditions.

The salon remains the canonical anchor. The first Cyclops pass may add only architectural shell, one doorway, corridor depth and a shallow kitchen glimpse. It must not add new objectives or move existing blocking markers.

## Christmas1982 canonical blocking

The existing scene establishes:

- fireplace at back-left;
- sofa at back-center;
- Christmas tree at back-right;
- gifts near the tree;
- rug and coffee table in the center;
- Malo entering from the camera/front side;
- Fisher Price associated with the gift area;
- Ronan positioned for the first-recording path;
- warm fireplace/tree practical lighting;
- explicit blocking markers for Malo start, Fisher pickup, Ronan record position and camera start.

Spatial lock: [`docs/CHRISTMAS1982_LAYOUT.md`](docs/CHRISTMAS1982_LAYOUT.md)  
Blocking lock: [`docs/CHRISTMAS1982_BLOCKING.md`](docs/CHRISTMAS1982_BLOCKING.md)  
Presentation lock: [`docs/FIRST_RECORDING_PRESENTATION.md`](docs/FIRST_RECORDING_PRESENTATION.md)

## Validation

Preferred Sprint 5 validation command:

```bash
bash tests/run_sprint5_validation.sh
```

It runs:

- original static contract;
- Sprint 5 visual contract;
- Player Feel input contract;
- external-asset pipeline contract;
- house-planning contract;
- Godot headless tests automatically when a Godot binary is available.

Individual Godot headless suite:

```bash
./tests/run_headless.sh
```

Open the prototype:

```bash
godot --path . --editor
```

See [`SPRINT5_STATUS.md`](SPRINT5_STATUS.md) for the authoritative current acceptance state.

## Codex / Astra + yanhuifair Godot-MCP

The repository is prepared for the `@yanhuifair/godot-mcp` MCP server.

Full setup: [`MCP_SETUP.md`](MCP_SETUP.md)

macOS/Linux helper:

```bash
./scripts/setup_godot_mcp.sh
```

Windows PowerShell helper:

```powershell
./scripts/setup_godot_mcp.ps1
```

Codex registration used by the helpers:

```bash
codex mcp add godot-mcp -- npx -y @yanhuifair/godot-mcp -p .
```

Codex/Astra repository rules live in [`AGENTS.md`](AGENTS.md).
