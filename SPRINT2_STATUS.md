# Sprint 2 — Christmas1982 visual greybox

## Goal

Turn `Christmas1982` from a sparse test floor into a readable 3D/2.5D cinematic greybox while preserving the Sprint 1 recorder loop exactly.

## Implemented

- Three visible room walls plus invisible front collision boundary.
- Warm floor and late-70s/early-80s placeholder wall palette.
- Central rug.
- Sofa placeholder with collision.
- Fireplace placeholder with hearth, emissive fire opening, collision and warm practical light.
- Coffee table placeholder with collision.
- Stylized placeholder Christmas tree with collision.
- Gift pile marking the Christmas-morning focal area.
- Malo/Ronan/Fisher placeholder materials differentiated for readability.
- Second warm practical light near the tree plus restrained directional fill.
- Fisher Price repositioned into the gift composition.
- RonanTest repositioned for the intended first-recording route.
- Camera framing tightened to 46 degrees FOV.
- Cinematic camera follow corrected to use displacement from Malo's spawn anchor rather than world-origin coordinates.
- Static TSCN validation expanded to verify every ExtResource/SubResource reference and `load_steps` count.
- Headless visual-contract test added for required set nodes, opening route distances and cinematic camera state.

## Explicitly not implemented

- Production models or textures.
- Character animation.
- Final lighting/color grading.
- Camera cuts or multiple camera zones.
- New dialogue.
- MK2 mechanics.
- Save/inventory/Radio Malo.
- Any gameplay outside the existing Fisher Price loop.

## Validation

`python tests/static_validate.py` -> **0 failures**.

Godot engine parse/runtime validation remains pending until Godot 4.7.x or the Godot-MCP bridge is available in the execution environment.

## Sprint 2 runtime acceptance test

1. Open `Christmas1982`.
2. Confirm Malo starts inside the room and cannot cross visible/invisible room boundaries.
3. Confirm sofa, fireplace, coffee table and tree block Malo appropriately.
4. Confirm the opening camera frame contains Malo plus clear visual orientation toward fireplace/tree/gifts.
5. Walk Malo to the Fisher Price and pick it up with `E`.
6. Approach RonanTest.
7. Hold `R`, release to STOP, then press `P`.
8. Confirm the Sprint 1 gameplay contract remains intact.
9. Confirm there are no parser, scene-tree, physics or audio errors.
