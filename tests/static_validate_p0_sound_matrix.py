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

matrix_path = root / "data/p0_sound_production_matrix.json"
catalog_path = root / "data/sound_catalog_1982.json"
manifest_path = root / "audio/audio_manifest.json"
ronan_path = root / "audio/ronan_test.wav"
doc_path = root / "docs/P0_SOUND_PRODUCTION_MATRIX.md"

ok(matrix_path.exists(), "P0 sound production matrix exists")
ok(catalog_path.exists(), "sound catalog exists")
ok(manifest_path.exists(), "audio provenance manifest exists")
ok(ronan_path.exists(), "canonical Sprint 5 ronan_test.wav remains in place")
ok(doc_path.exists(), "P0 sound production matrix documentation exists")

if matrix_path.exists() and catalog_path.exists():
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    families = {entry["id"]: entry for entry in matrix.get("families", [])}
    catalog_ids = {entry["id"] for entry in catalog.get("entries", [])}

    required = {
        "ronan_test",
        "fisher_button_mechanics",
        "fisher_transport_click",
        "fireplace_crackle",
        "gate_squeak",
        "garden_wind_tree",
        "kitchen_fridge_hum",
        "street_moped_pass",
    }
    ok(required.issubset(families.keys()), "all identity-critical production families exist")
    ok(required.issubset(catalog_ids), "all production families map to the canonical sound catalog")

    rule = matrix.get("sprint5_rule", {})
    ok(rule.get("required_gameplay_source") == "ronan_test", "ronan_test remains the only required gameplay source")
    ok(rule.get("new_audio_files_required_now") is False, "matrix does not require new Sprint 5 audio files")
    ok(rule.get("temporal_capture_required_now") is False, "matrix does not require temporal capture in Sprint 5")
    ok(rule.get("higgsfield_generation_required_now") is False, "matrix does not require Higgsfield generation")

    for family_id, family in families.items():
        minimum = family.get("minimum_variations", 0)
        ideal = family.get("ideal_variations", 0)
        targets = family.get("target_files", [])
        ok(minimum > 0, f"{family_id}: minimum variation count is positive")
        ok(ideal >= minimum, f"{family_id}: ideal variation count is not below minimum")
        ok(len(targets) > 0, f"{family_id}: at least one target filename is planned")
        ok(all(path.endswith(".wav") for path in targets), f"{family_id}: target masters are WAV")
        ok("capture_design" in family and "playback_design" in family, f"{family_id}: WORLD/CAPTURE/PLAYBACK production intent is explicit")

if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assets = manifest.get("assets", [])
    current = [a for a in assets if a.get("id") == "ronan_test_current"]
    ok(len(current) == 1, "audio manifest contains one canonical ronan_test entry")
    if current:
        entry = current[0]
        ok(entry.get("path") == "audio/ronan_test.wav", "ronan manifest path remains canonical")
        ok(entry.get("sprint5_required") is True, "ronan manifest entry remains Sprint 5 required")
        ok(entry.get("production_approved") is False, "prototype Ronan audio is not mislabelled as final production audio")

if doc_path.exists():
    text = doc_path.read_text(encoding="utf-8")
    ok("Do not move `audio/ronan_test.wav` yet" in text, "documentation protects current Ronan dependency")
    ok("Do not build three permanent libraries" in text, "documentation preserves nondestructive WORLD/CAPTURE/PLAYBACK strategy")
    ok("No Higgsfield audio generation is required" in text, "documentation preserves credit discipline")

print(f"\nP0 sound production matrix validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
