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

model_path = root / "data/family_behavior_beats_1982.json"
doc_path = root / "docs/FAMILY_LIVING_WORLD_DESIGN.md"
recorder_path = root / "recorder/recorder.gd"
interaction_path = root / "interaction/interaction_context.gd"

ok(model_path.exists(), "family living-world design data exists")
ok(doc_path.exists(), "family living-world design doc exists")

if model_path.exists():
    data = json.loads(model_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "family behaviour remains design-only")
    ok(data.get("simulation_model") == "lightweight_authored_behaviour", "lightweight authored behaviour is preferred")
    ok(data.get("full_npc_navigation_required") is False, "full NPC navigation is not required")
    chars = set(data.get("characters", {}))
    ok({"ronan", "mother", "father"}.issubset(chars), "Ronan, Mother and Father behaviour roles exist")
    categories = set(data.get("behaviour_categories", []))
    ok({"AMBIENT", "REACTIVE", "INTERRUPTIVE", "COLLABORATIVE", "CALLBACK"}.issubset(categories), "all family behaviour categories exist")
    invariants = data.get("invariants", {})
    ok(invariants.get("family_are_quest_dispensers") is False, "family are not quest dispensers")
    ok(invariants.get("interruptions_are_punishment") is False, "interruptions are not punishment")
    ok(invariants.get("recorder_owns_family_behaviour") is False, "Recorder does not own family behaviour")
    ok(invariants.get("sprint5_implementation") is False, "family AI is not a Sprint 5 implementation")

if doc_path.exists():
    text = doc_path.read_text(encoding="utf-8")
    for token in ["Ronan", "Mother", "Father", "Interruptions as content", "Repeat-action design"]:
        ok(token in text, f"family design document includes: {token}")
    ok("Do not start with free roaming AI" in text, "family design rejects premature roaming AI")

for path, label in [(recorder_path, "Recorder"), (interaction_path, "InteractionContext")]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for forbidden in ["mother_fridge", "ronan_reacts", "family_behaviour", "INTERRUPTIVE", "CALLBACK"]:
            ok(forbidden not in text, f"{label} is not coupled to family behaviour: {forbidden}")

print(f"\nFamily living-world design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
