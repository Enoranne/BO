# BO_Ta_Vie — Sprint 4

Godot 4.7.x prototype for **PISTE 0 — Christmas1982**.

## Scope

The only implemented gameplay loop remains:

`Malo → Fisher Price → REC → capture RonanTest → STOP → PLAY`

Sprint 4 adds **first-recording presentation feedback** on top of the Sprint 3 blocking: a carried Fisher Price visual, real REC lamp feedback, and a presentation-only objective beat. It does not add a new gameplay loop.

No inventory, save system, dialogue tree, NPC navigation, Radio Malo, MK2 mechanics, pitch, Sound-on-Sound or multitrack is implemented.

## Controls

- **WASD** — move Malo
- **E** — interact / take Fisher Price when prompted
- **Hold R** — record the nearest recordable source
- **Release R** — stop and create a `RecordingClip`
- **P** — play latest recording

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

## Christmas1982 greybox + blocking

The scene establishes the first intended composition with placeholder-only geometry:

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

Static validation:

```bash
python tests/static_validate.py
```

Authoritative Godot headless tests, with Godot 4.7.x available on PATH:

```bash
./tests/run_headless.sh
```

Open the prototype:

```bash
godot --path . --editor
```

See [`SPRINT4_STATUS.md`](SPRINT4_STATUS.md) for the current acceptance checklist.

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
