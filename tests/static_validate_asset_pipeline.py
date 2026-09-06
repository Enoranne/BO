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
preview = root / "scenes/piste_0/christmas_1982/CoffeeTableAssetPreview.tscn"
readme = root / "assets/3d/higgsfield/README.md"

ok(slot.exists(), "external asset slot exists")
ok(preview.exists(), "isolated coffee-table preview exists")
ok(readme.exists(), "Higgsfield import folder is documented")

if slot.exists():
    text = slot.read_text(encoding="utf-8")
    ok("class_name ExternalAssetSlot" in text, "ExternalAssetSlot class declared")
    ok("@export var asset_scene: PackedScene" in text, "asset scene remains optional")
    ok("Recorder" not in text and "InteractionContext" not in text, "asset slot has no gameplay dependency")
    ok("CollisionShape3D" not in text and "Area3D" not in text, "asset slot creates no collision/gameplay area")

if preview.exists():
    text = preview.read_text(encoding="utf-8")
    ok("external_asset_slot.gd" in text, "preview uses ExternalAssetSlot")
    ok("coffee_table_test.glb" not in text, "preview does not hard-reference an absent GLB")
    ok("2.15, 0.65, 1.08" in text, "preview keeps current coffee-table target envelope")

print(f"\nSprint 5.3 asset-pipeline static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
