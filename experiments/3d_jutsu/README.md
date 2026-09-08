# Spike — 3D Jutsu -> GLB -> Godot

## Purpose
Test the shortest viable environment pipeline for BO before adding Blender or Pascal.

Decision principle: `VALUE > COMPLEXITY`.

## Isolation contract
- Branch: `spike/3d-jutsu-godot`
- Canonical gameplay scene is read-only for this spike.
- No Recorder, MaloController, InteractionContext, objective, collision or camera ownership changes.
- No Blender/Pascal dependency in the direct-import test.
- No new Higgsfield generation is required for this test.

## Candidate inspected before import
Expected file: `assets/3d/experimental/childrens_bedroom_3d_jutsu.glb`

The supplied candidate is a real structured GLB, not the earlier empty export. Pre-import inspection found approximately:
- 255 KB file size;
- 164 nodes;
- 152 meshes;
- 26 materials;
- 8 textures/images;
- 2 cameras;
- 5,146 vertices;
- 4,644 triangles;
- semantic object names including room floor/ceiling, walls, Malo/Ronan beds, door, wardrobe, corridor, books and toys.

These counts are technical observations, not production approval.

## First Godot test
Open:

`res://experiments/3d_jutsu/ChildrensBedroom3DJutsuPreview.tscn`

The preview loader deliberately uses `ResourceLoader.exists()` so the branch remains loadable before the binary GLB is copied locally.

Review only:
1. Does the GLB import without errors?
2. Does the scene appear at plausible metre scale?
3. Are walls/floor/beds/door/corridor recognisable?
4. Are materials/textures present and correctly assigned?
5. Is geometry orientation sane?
6. Is the hierarchy still semantically structured in Godot?
7. Are there obvious pivot/origin problems?
8. Does the scene remain light enough for a narrative-game environment?
9. Does reimport remain stable after reopening Godot?

## Decision gate
- **ADOPT DIRECT** — GLB -> Godot is clean enough; Blender is optional repair/finishing only.
- **REWORK** — useful scene, but scale/orientation/material/pivot cleanup is needed; test Blender next.
- **REJECT** — direct import creates more problems than value.

Do not integrate the bedroom into `Christmas1982.tscn` during this spike.
