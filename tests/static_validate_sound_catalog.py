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

catalog_path = root / "data/sound_catalog_1982.json"
bible_path = root / "docs/SOUND_BIBLE_1982.md"
map_path = root / "docs/CHRISTMAS1982_SOUND_MAP.md"

ok(catalog_path.exists(), "sound production catalog exists")
ok(bible_path.exists(), "1982 sound bible exists")
ok(map_path.exists(), "spatial sound opportunity map exists")

if catalog_path.exists():
    data = json.loads(catalog_path.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    ids = [entry.get("id") for entry in entries]
    ok(data.get("canonical_required_recording") == "ronan_test", "canonical required recording remains ronan_test")
    ok(len(entries) >= 10, "catalog contains a useful first production backlog")
    ok(len(ids) == len(set(ids)), "sound IDs are unique")
    required = [entry.get("id") for entry in entries if entry.get("required_in_sprint5")]
    ok(required == ["ronan_test"], "Sprint 5 still requires only the Ronan onboarding recording")
    for entry in entries:
        ok(entry.get("priority") in {"P0", "P1", "P2"}, f"valid priority: {entry.get('id')}")
        ok(bool(entry.get("zone")), f"zone declared: {entry.get('id')}")
        ok(bool(entry.get("filename_stem")), f"filename stem declared: {entry.get('id')}")
        duration = entry.get("target_duration_s", [])
        ok(isinstance(duration, list) and len(duration) == 2 and duration[0] > 0 and duration[1] >= duration[0], f"valid duration target: {entry.get('id')}")

if bible_path.exists():
    text = bible_path.read_text(encoding="utf-8")
    ok("48 kHz" in text and "24-bit" in text, "source master audio targets are documented")
    ok("Only `ronan_test` is required" in text, "sound bible preserves Sprint 5 scope")
    ok("what the player hears in the world" in text, "future world/capture/playback distinction is documented without implementation")

print(f"\nSprint 5 sound-catalog static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
