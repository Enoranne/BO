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

catalog_path = root / "data/p0_affordance_catalog.json"
language_doc = root / "docs/PHYSICAL_AFFORDANCE_LANGUAGE.md"
feedback_doc = root / "docs/OBJECT_INTERACTION_FEEDBACK.md"
handoff_doc = root / "docs/WORK_AFFORDANCE_HANDOFF.md"
taxonomy_doc = root / "docs/INTERACTION_TAXONOMY.md"
interactable_path = root / "interaction/interactable.gd"
context_path = root / "interaction/interaction_context.gd"
recorder_path = root / "recorder/recorder.gd"

for path, label in [
    (catalog_path, "affordance catalog exists"),
    (language_doc, "physical affordance language exists"),
    (feedback_doc, "interaction feedback contract exists"),
    (handoff_doc, "Work affordance handoff exists"),
    (taxonomy_doc, "interaction taxonomy exists"),
]:
    ok(path.exists(), label)

if catalog_path.exists():
    data = json.loads(catalog_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "affordance catalog remains design-only")
    rules = data.get("design_rules", {})
    ok(rules.get("world_cue_before_prompt") is True, "world cue precedes prompt")
    ok(rules.get("persistent_outline_default") is False, "persistent outlines are not default")
    ok(rules.get("quest_marker_default") is False, "quest markers are not default")
    ok(rules.get("recordable_does_not_imply_interactable") is True, "recordability stays separate from interaction")
    ok(rules.get("interactable_does_not_imply_inventory") is True, "interaction does not imply inventory")
    ok(rules.get("current_required_interaction") == "take_fisher_price", "current required interaction stays Fisher pickup")

    objects = {item.get("id"): item for item in data.get("objects", [])}
    for object_id in [
        "fisher_price",
        "garden_gate",
        "kitchen_fridge",
        "bathroom_tap",
        "cassette_boxes",
        "fireplace",
        "moped_pass",
    ]:
        ok(object_id in objects, f"affordance object exists: {object_id}")

    if "fireplace" in objects:
        ok(objects["fireplace"].get("verbs") == [], "fireplace proves meaningful sources need not be interactable")
        ok(objects["fireplace"].get("recordable_relationship") == "passive_source", "fireplace remains a passive source")

    if "garden_gate" in objects:
        gate = objects["garden_gate"]
        ok(set(["OPEN", "CLOSE"]).issubset(gate.get("verbs", [])), "gate uses OPEN/CLOSE verbs")
        ok(gate.get("recordable_relationship") == "triggered_temporal_source", "gate remains temporal sound candidate")
        ok(gate.get("implementation_phase") == "post_sprint5_after_temporal_capture", "gate implementation stays gated")

    if "kitchen_fridge" in objects:
        fridge = objects["kitchen_fridge"]
        ok(fridge.get("recordable_relationship") == "passive_plus_triggered_source", "fridge combines passive and triggered audio")

    if "bathroom_tap" in objects:
        tap = objects["bathroom_tap"]
        ok(tap.get("recordable_relationship") == "continuous_state_source", "tap is reserved for sustained-source experiment")

    for object_id, item in objects.items():
        guidance = item.get("guidance", {})
        ok(set(["GUIDED", "NATURAL", "FREE"]).issubset(guidance), f"all guidance profiles specified for {object_id}")

if language_doc.exists():
    text = language_doc.read_text(encoding="utf-8")
    for token in ["A0", "A1", "A2", "A3", "TAKE", "OPEN / CLOSE", "PRESS", "TURN ON / TURN OFF"]:
        ok(token in text, f"affordance language covers {token}")
    ok("No universal highlight language" in text, "default outline/marker language is explicitly rejected")
    ok("The best interaction is one the player understands before reading the prompt" in text, "world-first affordance thesis is explicit")

if feedback_doc.exists():
    text = feedback_doc.read_text(encoding="utf-8")
    for token in ["INVITATION", "COMMIT", "PHYSICAL RESULT", "MEMORY RESULT"]:
        ok(token in text, f"feedback contract covers stage: {token}")
    ok("FREE means less explanation, not worse usability" in text, "FREE guidance retains physical usability")
    ok("Can the interaction coexist with REC?" in text, "REC coexistence is an acceptance question")

if handoff_doc.exists():
    text = handoff_doc.read_text(encoding="utf-8")
    ok("Do not infer a requirement to implement every object" in text, "Work is protected from catalog-as-scope expansion")
    ok("implement garden gate as first real post-prototype sound-memory interaction" in text, "gate rollout recommendation is documented")

for path, label in [
    (interactable_path, "Interactable"),
    (context_path, "InteractionContext"),
    (recorder_path, "Recorder"),
]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for forbidden in ["garden_gate", "kitchen_fridge", "bathroom_tap", "affordance_level", "GUIDED", "NATURAL", "FREE"]:
            ok(forbidden not in text, f"{label} has no premature affordance-specific coupling: {forbidden}")

print(f"\nPhysical affordance design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
