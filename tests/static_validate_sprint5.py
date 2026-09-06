from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
errors = []


def ok(condition: bool, message: str) -> None:
    if condition:
        print("PASS:", message)
    else:
        print("FAIL:", message)
        errors.append(message)


base_scene = root / "scenes/piste_0/christmas_1982/Christmas1982.tscn"
visual_scene = root / "scenes/piste_0/christmas_1982/Christmas1982_VisualSlice.tscn"
visual_pass = root / "visual/period_1982_visual_pass.gd"
set_dressing = root / "visual/period_1982_set_dressing.gd"

ok(base_scene.exists(), "Sprint 4 canonical Christmas1982 scene still exists")
ok(visual_scene.exists(), "Sprint 5 visual-slice wrapper scene exists")
ok(visual_pass.exists(), "Sprint 5 period visual pass exists")
ok(set_dressing.exists(), "Sprint 5.2 visual-only set dressing exists")

materials = [
    "materials/period_1982/wallpaper_cream.tres",
    "materials/period_1982/wood_dark_varnished.tres",
    "materials/period_1982/upholstery_brown_orange.tres",
    "materials/period_1982/carpet_muted_brown.tres",
    "materials/period_1982/plastic_fisher_beige.tres",
    "materials/period_1982/plastic_fisher_burgundy.tres",
    "materials/period_1982/floor_dark_warm_brown.tres",
    "materials/period_1982/fireplace_stone_warm.tres",
    "materials/period_1982/painted_trim_cream.tres",
    "materials/period_1982/ornament_muted_red.tres",
]
for rel in materials:
    ok((root / rel).exists(), f"Sprint 5 material exists: {rel}")

if visual_scene.exists():
    text = visual_scene.read_text(encoding="utf-8")
    ok("Christmas1982.tscn" in text, "visual slice instances canonical Christmas1982")
    ok("period_1982_visual_pass.gd" in text, "visual slice loads Period1982VisualPass")
    ok("period_1982_set_dressing.gd" in text, "visual slice loads Period1982SetDressing")
    ok(text.count('root_path = NodePath("../Base")') == 2, "both presentation passes target the wrapper Base instance")
    ok("position =" not in text and "rotation" not in text, "wrapper itself does not override spatial blocking")

if visual_pass.exists():
    text = visual_pass.read_text(encoding="utf-8")
    for rel in materials[:8]:
        ok(rel in text, f"visual pass references material when expected: {rel}")
    for path in [
        "Set/Floor/Mesh",
        "Set/BackWall/Mesh",
        "Set/LeftWall/Mesh",
        "Set/RightWall/Mesh",
        "Set/RugPlaceholder",
        "Set/SofaPlaceholder/Seat",
        "Set/CoffeeTablePlaceholder/Top",
        "Set/FireplacePlaceholder/Main",
        "FisherPrice/Visual",
        "Malo/HeldRecorderVisual/Body",
        "Lighting/FireGlow",
        "Lighting/TreeLamp",
        "Lighting/SoftFill",
    ]:
        ok(path in text, f"visual pass contains expected target path: {path}")
    ok("material_override" in text, "visual pass applies MeshInstance3D material overrides")
    ok("CollisionShape3D" not in text, "visual pass does not modify collision shapes")
    for forbidden in ["start_recording(", "stop_recording(", "play_latest(", "RecordingClip", "Recorder.State", "equipped_recorder"]:
        ok(forbidden not in text, f"visual pass does not contain gameplay token: {forbidden}")

if set_dressing.exists():
    text = set_dressing.read_text(encoding="utf-8")
    for rel in [
        "materials/period_1982/painted_trim_cream.tres",
        "materials/period_1982/wood_dark_varnished.tres",
        "materials/period_1982/upholstery_brown_orange.tres",
        "materials/period_1982/ornament_muted_red.tres",
    ]:
        ok(rel in text, f"set dressing references {rel}")
    for token in ["CollisionShape3D", "CharacterBody3D", "Area3D", "Blocking/", "start_recording(", "stop_recording("]:
        ok(token not in text, f"set dressing remains presentation-only: no {token}")
    ok('layer.name = "VisualSetDressing"' in text, "set dressing is isolated under its own visual layer")
    ok("BoxMesh.new()" in text and "SphereMesh.new()" in text, "set dressing creates visual meshes only")

print(f"\nSprint 5 static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
