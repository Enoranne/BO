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

preview = root / "scenes/piste_0/christmas_1982/CharacterReadabilityPreview.tscn"
review = root / "docs/CHARACTER_READABILITY_REVIEW.md"
humanoid = root / "characters/common/placeholder_humanoid.gd"
camera = root / "visual/asset_preview_camera.gd"

ok(preview.exists(), "character readability preview exists")
ok(review.exists(), "character readability review protocol exists")
ok(humanoid.exists(), "placeholder humanoid source exists")
ok(camera.exists(), "preview camera helper exists")

if preview.exists():
    text = preview.read_text(encoding="utf-8")
    ok("placeholder_humanoid.gd" in text, "preview reuses canonical placeholder implementation")
    ok('name="MaloPreview"' in text and 'name="RonanPreview"' in text, "preview contains both character candidates")
    ok("stature = 1.45" in text, "Malo preview keeps canonical stature")
    ok("stature = 1.68" in text, "Ronan preview keeps canonical stature")
    ok('name="Camera"' in text and "current = true" in text, "character preview is directly runnable")
    ok("CollisionShape3D" not in text and "CharacterBody3D" not in text, "character preview is presentation-only")
    ok("Recorder" not in text and "InteractionContext" not in text, "character preview has no gameplay dependency")

if review.exists():
    text = review.read_text(encoding="utf-8")
    for needle in ["Age / hierarchy read", "Silhouette read", "Colour separation", "Decision ladder"]:
        ok(needle in text, f"readability review covers: {needle}")
    ok("Final likeness" in text, "review keeps final character art out of Sprint 5")

print(f"\nCharacter-preview static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
