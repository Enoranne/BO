# Sprint 5 — Cyclops Level Builder spike

## Objective
Evaluate Cyclops Level Builder as an **authoring accelerator**, not as a required runtime dependency.

The spike is successful only if it lets us build and revise believable domestic architecture faster while preserving the existing Christmas1982 gameplay and blocking contracts.

## Non-negotiable rules
- Work on `sprint-5` or a temporary child branch only.
- Do not replace the canonical `Christmas1982.tscn` before visual validation.
- Do not move `Blocking/MaloStart`, `FisherPickupBeat`, `RonanRecordBeat`, `RonanStand` or `CameraStart`.
- Do not change Recorder, InteractionContext, MaloController or Christmas1982Director logic.
- Do not add navigation, inventory, save/load, dialogue or MK2 mechanics.
- Cyclops-generated geometry must remain replaceable by normal Godot meshes / GLTF later.

## First spike task
Rebuild only the **architectural shell** around the current salon:

1. floor volume;
2. back wall;
3. side walls;
4. wall thickness / room corners;
5. one doorway suggesting the corridor;
6. simple trim / skirting if fast;
7. optional shallow kitchen glimpse beyond the doorway.

Do not rebuild furniture in the first pass.

## Visual target
The room should stop reading as an isolated rectangular test box and begin reading as a real late-1970s / early-1980s family interior.

Required improvements:
- believable wall thickness;
- visible doorway / circulation logic;
- more natural architectural proportions;
- stronger depth from the locked camera;
- no obstruction of the Fisher Price or Ronan path.

## Comparison protocol
Create screenshots from the same camera position for:

- A — canonical Sprint 4 greybox;
- B — Sprint 5 material wrapper;
- C — Cyclops architectural shell + Sprint 5 materials.

Compare:
- spatial readability;
- period credibility;
- cinematic depth;
- gameplay legibility;
- editing speed;
- fragility / maintenance cost.

## Acceptance
Cyclops is adopted only if all are true:

1. The room is clearly faster to iterate than hand-editing primitive meshes.
2. Generated geometry behaves correctly in Godot 4.7.x.
3. Existing traversal remains intact.
4. Camera composition remains valid.
5. Geometry can be converted/exported to ordinary Godot-friendly assets.
6. Removing the addon does not destroy the production scene after conversion.

If any of these fail, keep the current native-Godot architecture and treat the experiment as informational.

## Astra / Codex instruction
When live Godot MCP access is available:

1. call MCP status first;
2. open the existing scene and inspect the tree before editing;
3. duplicate or instance the scene for the experiment;
4. install/enable Cyclops only after verifying compatibility;
5. build the architectural shell only;
6. run static and headless contracts;
7. capture visual evidence from the locked camera;
8. stop before expanding gameplay.
