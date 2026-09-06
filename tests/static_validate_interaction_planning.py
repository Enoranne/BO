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

interactable = root / "interaction/interactable.gd"
context = root / "interaction/interaction_context.gd"
recordable = root / "interaction/recordable_source.gd"
doc = root / "docs/INTERACTION_TAXONOMY.md"

for path, label in [
    (interactable, "Interactable contract"),
    (context, "InteractionContext"),
    (recordable, "RecordableSource contract"),
    (doc, "interaction taxonomy"),
]:
    ok(path.exists(), f"{label} exists")

if interactable.exists():
    text = interactable.read_text(encoding="utf-8")
    ok("extends Area3D" in text and "class_name Interactable" in text, "Interactable remains generic Area3D contract")
    for token in ["Recorder", "RecordingClip", "RecordableSource", "Inventory"]:
        ok(token not in text, f"Interactable remains decoupled from {token}")

if recordable.exists():
    text = recordable.read_text(encoding="utf-8")
    ok("extends Area3D" in text and "class_name RecordableSource" in text, "RecordableSource remains independent Area3D contract")
    ok("source_metadata" in text, "RecordableSource retains future-safe metadata")
    ok("interaction_prompt" not in text and "interact(" not in text, "RecordableSource does not absorb Interactable semantics")

if context.exists():
    text = context.read_text(encoding="utf-8")
    ok("_choose_interactable" in text, "InteractionContext selects interactables generically")
    ok("_choose_recordable_source" in text, "InteractionContext selects recordable sources independently")
    ok("interaction_priority" in text and "recording_priority" in text, "interaction and recording priorities remain separate")

if doc.exists():
    text = doc.read_text(encoding="utf-8")
    for concept in [
        "Toggle / hinge",
        "Momentary action",
        "Continuous / held action",
        "Passive source",
        "Triggered source",
        "Continuous source",
        "gate open/close + squeak",
        "fridge open/close + hum/seal",
        "tap on/off + running water",
    ]:
        ok(concept in text, f"interaction planning covers: {concept}")
    ok("Do not generalise this into an inventory system" in text, "planning explicitly blocks premature inventory")

print(f"\nSprint 5 interaction-planning static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
