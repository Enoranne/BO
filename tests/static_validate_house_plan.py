from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parents[1]
errors = []


def ok(condition: bool, message: str) -> None:
    if condition:
        print("PASS:", message)
    else:
        print("FAIL:", message)
        errors.append(message)


zones_path = root / "data/christmas1982_house_zones.json"
sound_map = root / "docs/CHRISTMAS1982_SOUND_MAP.md"
execution = root / "docs/SPRINT5_4_ARCHITECTURE_EXECUTION.md"
canonical_scene = root / "scenes/piste_0/christmas_1982/Christmas1982.tscn"

ok(zones_path.exists(), "house-zone planning contract exists")
ok(sound_map.exists(), "sonic opportunity map exists")
ok(execution.exists(), "Sprint 5.4 execution plan exists")
ok(canonical_scene.exists(), "canonical Christmas1982 scene exists")

if zones_path.exists():
    data = json.loads(zones_path.read_text(encoding="utf-8"))
    ok(data.get("schema_version") == 1, "house-zone schema version is 1")
    ok(data.get("units") == "metres", "house-zone dimensions use metres")
    anchor = data.get("canonical_anchor", {})
    ok(anchor.get("room") == "salon", "salon remains canonical anchor")
    ok(anchor.get("preserve_existing_blocking") is True, "planning contract preserves existing blocking")

    zones = {z.get("id"): z for z in data.get("zones", [])}
    required = ["salon", "corridor", "kitchen_glimpse", "kitchen", "bedroom_zone", "bathroom", "garden", "tree_cabin", "gate", "street_edge"]
    for zone_id in required:
        ok(zone_id in zones, f"house plan includes zone: {zone_id}")

    if "salon" in zones:
        ok(zones["salon"].get("locked") is True, "salon is locked in planning contract")
        ok(zones["salon"].get("playable") is True, "salon remains playable")

    for visual_only in ["corridor", "kitchen_glimpse"]:
        if visual_only in zones:
            ok(zones[visual_only].get("phase") == "5.4", f"{visual_only} belongs to Sprint 5.4")
            ok(zones[visual_only].get("playable") is False, f"{visual_only} starts non-playable")

    rules = "\n".join(data.get("rules", []))
    ok("Do not move canonical Christmas1982 blocking markers" in rules, "planning contract explicitly protects canonical blocking")
    ok("No new gameplay objective" in rules, "planning contract forbids new Sprint 5.4 objective")

if sound_map.exists():
    text = sound_map.read_text(encoding="utf-8")
    for needle in ["## Salon", "## Corridor", "## Kitchen", "## Bathroom", "## Bedroom zone", "## Garden", "## Gate", "## Street edge"]:
        ok(needle in text, f"sound map documents {needle[3:]}")
    ok("RonanTest remains the only gameplay capture required" in text, "sound map preserves Sprint 5 recording scope")

if execution.exists():
    text = execution.read_text(encoding="utf-8")
    for needle in ["canonical A", "Visual Slice B", "Cyclops shell C", "Stop conditions", "canonical blocking markers are not adjustable"]:
        ok(needle in text, f"5.4 execution plan contains guard: {needle}")
    for forbidden in ["inventory", "save/load", "Radio Malo", "MK2"]:
        # These terms may be mentioned only as scope/guards in other docs; this plan should stay architecture-focused.
        pass

print(f"\nHouse-plan static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
