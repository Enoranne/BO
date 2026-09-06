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

contract_path = root / "data/accessibility_settings_contract.json"
design_doc = root / "docs/ACCESSIBILITY_AND_GUIDANCE_SEPARATION.md"
handoff_doc = root / "docs/WORK_ACCESSIBILITY_HANDOFF.md"
recorder_path = root / "recorder/recorder.gd"
interactable_path = root / "interaction/interactable.gd"
context_path = root / "interaction/interaction_context.gd"

for path, label in [
    (contract_path, "accessibility settings contract exists"),
    (design_doc, "accessibility/guidance separation doc exists"),
    (handoff_doc, "Work accessibility handoff exists"),
]:
    ok(path.exists(), label)

if contract_path.exists():
    data = json.loads(contract_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "accessibility contract remains design-only")
    ok(data.get("independent_from_guidance") is True, "accessibility is independent from guidance")
    settings = data.get("settings", {})
    for setting in [
        "subtitles",
        "speaker_labels",
        "subtitle_size",
        "subtitle_background",
        "ui_text_scale",
        "rec_input_mode",
    ]:
        ok(setting in settings, f"accessibility setting exists: {setting}")
    invariants = data.get("invariants", {})
    ok(invariants.get("free_guidance_can_use_subtitles") is True, "FREE can use subtitles")
    ok(invariants.get("free_guidance_can_use_hearing_support") is True, "FREE can use hearing support")
    ok(invariants.get("accessibility_changes_story_content") is False, "accessibility does not branch story")
    ok(invariants.get("accessibility_changes_recording_value") is False, "accessibility does not change recording value")
    ok(invariants.get("accessibility_owned_by_recorder") is False, "Recorder does not own accessibility")
    ok(invariants.get("accessibility_owned_by_interactable") is False, "Interactable does not own accessibility")

if design_doc.exists():
    text = design_doc.read_text(encoding="utf-8")
    ok("Accessibility settings and guidance profile are separate axes" in text, "separate-axis principle is explicit")
    ok("FREE guidance may still use these accessibility cues" in text, "FREE hearing support is explicit")
    ok("Do not caption every ambience by default" in text, "sound captions remain selective")
    ok("non-colour-only REC/STOP/PLAY distinction" in text, "REC state cannot rely on colour alone")

if handoff_doc.exists():
    text = handoff_doc.read_text(encoding="utf-8")
    ok("Accessibility and guidance are independent" in text, "Work handoff states separation")
    ok("Never gate endings, achievements, memory value or story content" in text, "no accessibility penalty")

for path, label in [
    (recorder_path, "Recorder"),
    (interactable_path, "Interactable"),
    (context_path, "InteractionContext"),
]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for forbidden in ["subtitle_size", "speaker_labels", "critical_sound_captions", "accessibility_settings_contract"]:
            ok(forbidden not in text, f"{label} has no premature accessibility coupling: {forbidden}")

print(f"\nAccessibility design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
