import bpy
from pathlib import Path

# Run from Blender's Scripting workspace after opening any empty .blend.
# The script expects the BO repository to be the current working directory,
# or edit REPO_ROOT below to the local BO checkout path.

REPO_ROOT = Path.cwd()
INPUT_GLB = REPO_ROOT / "assets/3d/experimental/childrens_bedroom_3d_jutsu.glb"
OUTPUT_GLB = REPO_ROOT / "assets/3d/experimental/childrens_bedroom_3d_jutsu_clean.glb"

RESET_LOCAL_TRANSFORMS = {
    "CAR_rally_body", "CAR_rally_cab", "CAR_rally_wheel",
    "CAR_white_body", "CAR_white_cab", "CAR_white_wheel",
    "CURT_L1", "CURT_L2", "CURT_L3",
    "CURT_R1", "CURT_R2", "CURT_R3",
    "LACE_1", "LACE_2",
    "DSK_lamp_head",
    "VIN_0", "VIN_1", "VIN_2",
}


def clear_scene() -> None:
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.meshes, bpy.data.curves, bpy.data.cameras, bpy.data.lights):
        for block in list(datablocks):
            if block.users == 0:
                datablocks.remove(block)


def import_glb() -> None:
    if not INPUT_GLB.exists():
        raise FileNotFoundError(f"Input GLB not found: {INPUT_GLB}")
    bpy.ops.import_scene.gltf(filepath=str(INPUT_GLB))


def reset_known_bad_transforms() -> list[str]:
    fixed = []
    missing = []
    for name in sorted(RESET_LOCAL_TRANSFORMS):
        obj = bpy.data.objects.get(name)
        if obj is None:
            missing.append(name)
            continue
        obj.location = (0.0, 0.0, 0.0)
        obj.rotation_mode = 'QUATERNION'
        obj.rotation_quaternion = (1.0, 0.0, 0.0, 0.0)
        obj.scale = (1.0, 1.0, 1.0)
        fixed.append(name)
    print("Fixed local transforms:", fixed)
    if missing:
        print("WARNING — expected objects not found:", missing)
    return fixed


def remove_imported_camera_light_ownership() -> None:
    # Godot owns gameplay camera and preview lighting. Keep meshes/materials only.
    for obj in list(bpy.data.objects):
        if obj.type in {'CAMERA', 'LIGHT'}:
            bpy.data.objects.remove(obj, do_unlink=True)

    # Remove imported animation clips, including CAM_MaloRonan.
    for action in list(bpy.data.actions):
        bpy.data.actions.remove(action)


def print_scene_summary() -> None:
    meshes = [o for o in bpy.data.objects if o.type == 'MESH']
    print(f"Mesh objects: {len(meshes)}")
    for name in sorted(RESET_LOCAL_TRANSFORMS):
        obj = bpy.data.objects.get(name)
        if obj is not None:
            print(name, "location=", tuple(round(v, 4) for v in obj.location),
                  "rotation=", tuple(round(v, 4) for v in obj.rotation_quaternion),
                  "scale=", tuple(round(v, 4) for v in obj.scale))


def export_glb() -> None:
    bpy.ops.export_scene.gltf(
        filepath=str(OUTPUT_GLB),
        export_format='GLB',
        export_apply=False,
        export_animations=False,
        export_cameras=False,
        export_lights=False,
    )
    print(f"Exported cleaned candidate: {OUTPUT_GLB}")


def main() -> None:
    clear_scene()
    import_glb()
    reset_known_bad_transforms()
    remove_imported_camera_light_ownership()
    print_scene_summary()
    export_glb()


if __name__ == "__main__":
    main()
