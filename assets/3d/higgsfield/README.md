# Higgsfield 3D imports — Sprint 5.3

This folder is reserved for validated GLB assets exported from the BO Higgsfield 3D Jutsu project.

## First candidate
Expected working filename after Work/Godot-MCP retrieves the approved revision-1 export:

`coffee_table_test.glb`

Do not add the binary until the Sprint 5.2 visual slice has been reviewed in Godot and the 3D asset has been visually inspected.

## Integration rule
The first GLB must be tested through:

`scenes/piste_0/christmas_1982/CoffeeTableAssetPreview.tscn`

Assign the imported PackedScene to `AssetSlot.asset_scene`. The slot's target envelope matches the current procedural coffee-table collision envelope: approximately `2.15 x 0.65 x 1.08 m`.

The preview scene intentionally contains no gameplay, Recorder, interaction, or collision dependency. If the candidate is rejected, remove the asset assignment and the project returns to the empty target envelope.

## Production acceptance
Before replacing any visible placeholder in Christmas1982:

1. confirm orientation and metre scale;
2. inspect material import under BO's warm lighting;
3. compare silhouette against the existing table;
4. verify reasonable mesh complexity;
5. create collision separately in Godot only after visual acceptance;
6. never make gameplay logic depend on a Higgsfield asset path.
