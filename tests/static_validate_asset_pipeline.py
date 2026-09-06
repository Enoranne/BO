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

slot = root / "visual/external_asset_slot.gd"
preview_camera = root / "visual/asset_preview_camera.gd"
preview = root / "scenes/piste_0/christmas_1982/CoffeeTableAssetPreview.tscn"
readme = root / "assets/3d/higgsfield/README.md"

ok(slot.exists(), "external asset slot exists")
ok(preview_camera.exists(), "asset preview camera helper exists")
ok(preview.exists(), "isolated coffee-table preview exists")
ok(readme.exists(), "Higgsfield import folder is documented")

if slot.exists():
    text = slot.read_text(encoding="utf-8")
    ok("class_name ExternalAssetSlot" in text, "ExternalAssetSlot class declared")
    ok("@export var asset_scene: PackedScene" in text, "asset scene remains optional")
    ok("envelope_floor_aligned" in text, "target envelope supports floor alignment")
    ok("target_size.y * 0.5" in text, "target envelope is positioned on the preview floor")
    ok("Recorder" not in text and "InteractionContext" not in text, "asset slot has no gameplay dependency")
    ok("CollisionShape3D" not in text and "Area3D" not in text, "asset slot creates no collision/gameplay area")

if preview_camera.exists():
    text = preview_camera.read_text(encoding="utf-8")
    ok("extends Camera3D" in text, "preview helper is camera-only")
    ok("look_at" in text, "preview camera targets the asset slot")

if preview.exists():
    text = preview.read_text(encoding="utf-8")
    ok("external_asset_slot.gd" in text, "preview uses ExternalAssetSlot")
    ok("asset_preview_camera.gd" in text, "preview uses dedicated camera helper")
    ok("coffee_table_test.glb" not in text, "preview does not hard-reference an absent GLB")
    ok("2.15, 0.65, 1.08" in text, "preview keeps current coffee-table target envelope")
    ok('name="Floor"' in text, "preview has a floor reference plane")
    ok('name="Camera"' in text and "current = true" in text, "preview is directly runnable with an active camera")
    ok('name="KeyLight"' in text and 'name="WarmFill"' in text, "preview provides neutral inspection lighting")

print(f"\nSprint 5.3 asset-pipeline static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
