# Spike — Blender cleanup for 3D Jutsu bedroom

## Goal
Determine whether Blender adds enough value to justify a narrow cleanup step between 3D Jutsu and Godot.

Decision rule: `VALUE > COMPLEXITY`.

## Branch
`spike/blender-cleanup`

## Input
`assets/3d/experimental/childrens_bedroom_3d_jutsu.glb`

## Output
`assets/3d/experimental/childrens_bedroom_3d_jutsu_clean.glb`

## Scope
This spike is deliberately surgical. It may:
- correct obviously duplicated node transforms/pivots on known misplaced props;
- remove imported cameras and animation so Godot keeps camera ownership;
- remove imported lights from the exported candidate so Godot preview lighting remains authoritative;
- preserve the room, ceiling, walls, furniture, props, materials, textures and semantic object names;
- export a fresh GLB for A/B comparison in the existing Godot preview.

It must NOT:
- remodel the room;
- replace furniture;
- retopologise everything;
- merge the whole scene into one opaque mesh;
- change gameplay scenes or Recorder/Malo systems;
- add Blender as a runtime dependency.

## Known transform suspects from raw GLB inspection
The following node transforms are likely duplicated on top of already world-positioned mesh vertices:
- `CAR_rally_body`, `CAR_rally_cab`, `CAR_rally_wheel`
- `CAR_white_body`, `CAR_white_cab`, `CAR_white_wheel`
- `CURT_L1`, `CURT_L2`, `CURT_L3`
- `CURT_R1`, `CURT_R2`, `CURT_R3`
- `LACE_1`, `LACE_2`
- `DSK_lamp_head`
- `VIN_0`, `VIN_1`, `VIN_2`

The cleanup script resets only these local transforms and leaves all other geometry untouched.

## A/B acceptance
Compare the direct import and cleaned import in Godot.

PASS if:
1. misplaced curtain/lace/vinyl/car/lamp objects return to plausible positions;
2. room scale and main furniture remain unchanged;
3. materials/textures still import;
4. no new Godot import errors appear;
5. camera/lighting are easier to control in Godot;
6. the cleanup can be reproduced in a few minutes.

Verdict:
- `ADOPT BLENDER CLEANUP` if the A/B gain is clear and the step remains reproducible;
- `RETEST` if some transforms improve but collateral damage appears;
- `REJECT BLENDER` if it adds complexity without a material improvement.
