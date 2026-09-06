from pathlib import Path
import re
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

ok(base_scene.exists(), "Sprint 4 canonical Christmas1982 scene still exists")
ok(visual_scene.exists(), "Sprint 5 visual-slice wrapper scene exists")
ok(visual_pass.exists(), "Sprint 5 period visual pass exists")

materials = [
    "materials/period_1982/wallpaper_cream.tres",
    "materials/period_1982/wood_dark_varnished.tres",
    "materials/period_1982/upholstery_brown_orange.tres",
    "materials/period_1982/carpet_muted_brown.tres",
    "materials/period_1982/plastic_fisher_beige.tres",
    "materials/period_1982/plastic_fisher_burgundy.tres",
]
for rel in materials:
    ok((root / rel).exists(), f"Sprint 5 material exists: {rel}")

if visual_scene.exists():
    text = visual_scene.read_text(encoding="utf-8")
    ok("Christmas1982.tscn" in text, "visual slice instances canonical Christmas1982")
    ok("period_1982_visual_pass.gd" in text, "visual slice loads Period1982VisualPass")
    ok('root_path = NodePath("../Base")' in text, "visual pass targets the wrapper Base instance")
    ok("position =" not in text and "rotation" not in text, "wrapper does not override spatial blocking")

if visual_pass.exists():
    text = visual_pass.read_text(encoding="utf-8")
    for rel in materials:
        ok(rel in text, f"visual pass references {rel}")
    for path in [
        "Set/BackWall/Mesh",
        "Set/LeftWall/Mesh",
        "Set/RightWall/Mesh",
        "Set/RugPlaceholder",
        "Set/SofaPlaceholder/Seat",
        "Set/CoffeeTablePlaceholder/Top",
        "FisherPrice/Visual",
        "Malo/HeldRecorderVisual/Body",
    ]:
        ok(path in text, f"visual pass contains expected target path: {path}")
    ok("material_override" in text, "visual pass only needs MeshInstance3D material overrides")
    ok("global_position" not in text and "position =" not in text, "visual pass does not move gameplay nodes")
    ok("CollisionShape3D" not in text, "visual pass does not modify collision shapes")
    ok("Recorder" not in text and "RecordingClip" not in text, "visual pass does not own recorder gameplay")

print(f"\nSprint 5 static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
