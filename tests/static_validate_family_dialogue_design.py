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

catalog_path = root / "data/family_bark_catalog_1982.json"
design_doc = root / "docs/FAMILY_DIALOGUE_BARKS_DESIGN.md"
architecture_doc = root / "docs/FAMILY_DIALOGUE_EVENT_ARCHITECTURE.md"
handoff_doc = root / "docs/WORK_DIALOGUE_HANDOFF.md"
recorder_path = root / "recorder/recorder.gd"
context_path = root / "interaction/interaction_context.gd"

for path, label in [
    (catalog_path, "family bark catalog exists"),
    (design_doc, "family dialogue design exists"),
    (architecture_doc, "family dialogue architecture exists"),
    (handoff_doc, "Work dialogue handoff exists"),
]:
    ok(path.exists(), label)

if catalog_path.exists():
    data = json.loads(catalog_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "family bark catalog remains design-only")
    ok(data.get("source_language") == "fr", "French remains canonical source-writing language")
    rules = data.get("design_rules", {})
    ok(rules.get("dialogue_tree_default") is False, "dialogue trees are not default")
    ok(rules.get("localized_text_is_identifier") is False, "localized text is never an identifier")
    ok(rules.get("recorder_owns_barks") is False, "Recorder does not own barks")
    ok(rules.get("interaction_context_owns_barks") is False, "InteractionContext does not own barks")
    ok(rules.get("free_guidance_removes_subtitles") is False, "FREE guidance does not disable subtitles")
    ok(rules.get("ordinary_barks_interruptible") is True, "ordinary barks remain interruptible")
    ok(rules.get("constant_chatter") is False, "constant chatter is rejected")

    entries = data.get("entries", [])
    keys = [entry.get("key") for entry in entries]
    ok(len(keys) == len(set(keys)), "bark localization/event keys are unique")
    required = {
        "family.ronan.rec_notice.01",
        "family.mother.wind_call.01",
        "family.mother.fridge.01",
        "family.father.fireplace.01",
        "radio_malo.ronan.praise.01",
    }
    ok(required.issubset(set(keys)), "signature family bark cases are represented")
    for entry in entries:
        ok(entry.get("family") in data.get("families", []), f"valid bark family: {entry.get('key')}")
        ok(entry.get("intensity") in data.get("intensities", []), f"valid bark intensity: {entry.get('key')}")
        ok(bool(entry.get("recording_relation")), f"recording relation documented: {entry.get('key')}")
        ok(bool(entry.get("repeat_policy")), f"repeat policy documented: {entry.get('key')}")

if design_doc.exists():
    text = design_doc.read_text(encoding="utf-8")
    for token in ["MALO, TU FAIS QUOI ?", "Radio Malo est complètement génial", "Canonical authored source", "constant chatter"]:
        ok(token in text, f"dialogue design documents: {token}")
    ok("Do not make Recorder wait for a bark to finish" in text, "barks cannot block Recorder")

if architecture_doc.exists():
    text = architecture_doc.read_text(encoding="utf-8")
    ok("events may cause speech; speech never owns the gameplay event" in text, "event ownership rule is explicit")
    ok("must **not** manually copy a bark into `RecordingClip`" in text, "temporal capture remains natural")
    ok("FREE guidance must not disable subtitles" in text, "subtitle accessibility stays independent")

if handoff_doc.exists():
    text = handoff_doc.read_text(encoding="utf-8")
    ok("Do **not** build a full dialogue-tree framework" in text, "Work is protected from dialogue overbuild")
    ok("Never manually inject bark audio into a `RecordingClip`" in text, "Work handoff preserves capture architecture")

for path, label in [(recorder_path, "Recorder"), (context_path, "InteractionContext")]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for forbidden in ["family_bark_catalog", "BarkSelector", "FamilyReactionDirector", "localization_key", "dialogue_tree"]:
            ok(forbidden not in text, f"{label} has no premature dialogue coupling: {forbidden}")

print(f"\nFamily dialogue design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
