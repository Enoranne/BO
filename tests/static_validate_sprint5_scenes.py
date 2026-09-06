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


scenes = [
    root / "scenes/piste_0/christmas_1982/Christmas1982_VisualSlice.tscn",
    root / "scenes/piste_0/christmas_1982/CoffeeTableAssetPreview.tscn",
    root / "scenes/piste_0/christmas_1982/CharacterReadabilityPreview.tscn",
]

for scene in scenes:
    ok(scene.exists(), f"scene exists: {scene.name}")
    if not scene.exists():
        continue

    text = scene.read_text(encoding="utf-8")
    header = re.search(r'^\[gd_scene load_steps=(\d+) format=3\]$', text, re.M)
    ok(header is not None, f"{scene.name} declares Godot format=3 and load_steps")

    ext_ids = set(re.findall(r'^\[ext_resource .* id="([^"]+)"\]$', text, re.M))
    sub_ids = set(re.findall(r'^\[sub_resource .* id="([^"]+)"\]$', text, re.M))

    if header is not None:
        expected = len(ext_ids) + len(sub_ids) + 1
        ok(int(header.group(1)) == expected, f"{scene.name} load_steps matches resources ({expected})")

    for ref in re.findall(r'ExtResource\("([^"]+)"\)', text):
        ok(ref in ext_ids, f"{scene.name} ExtResource resolves: {ref}")

    for ref in re.findall(r'SubResource\("([^"]+)"\)', text):
        ok(ref in sub_ids, f"{scene.name} SubResource resolves: {ref}")

    for rel in re.findall(r'path="res://([^"]+)"', text):
        ok((root / rel).exists(), f"{scene.name} resource path exists: {rel}")

print(f"\nSprint 5 scene-resource validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
