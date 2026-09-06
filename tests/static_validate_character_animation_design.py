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

catalog_path = root / "data/character_gesture_catalog_1982.json"
language_doc = root / "docs/CHARACTER_GESTURE_LANGUAGE.md"
architecture_doc = root / "docs/CHARACTER_ANIMATION_ARCHITECTURE.md"
sequence_doc = root / "docs/CHARACTER_GESTURE_SEQUENCE_CARDS.md"
handoff_doc = root / "docs/WORK_CHARACTER_ANIMATION_HANDOFF.md"
placeholder_path = root / "characters/common/placeholder_humanoid.gd"
controller_path = root / "player/malo_controller.gd"
recorder_path = root / "recorder/recorder.gd"

for path, label in [
    (catalog_path, "character gesture catalog exists"),
    (language_doc, "character gesture language exists"),
    (architecture_doc, "character animation architecture exists"),
    (sequence_doc, "character gesture sequence cards exist"),
    (handoff_doc, "Work character animation handoff exists"),
]:
    ok(path.exists(), label)

if catalog_path.exists():
    data = json.loads(catalog_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "character gesture catalog remains design-only")
    rules = data.get("design_rules", {})
    ok(rules.get("controller_owns_locomotion") is True, "controller remains locomotion owner")
    ok(rules.get("root_motion_required") is False, "root motion is not required")
    ok(rules.get("attention_should_not_steal_control") is True, "attention may not steal control")
    ok(rules.get("sound_sync_required_for_contact_actions") is True, "contact gestures require audio sync")
    ok(rules.get("placeholder_is_not_final_rig") is True, "placeholder remains temporary")
    ok(rules.get("animation_tree_required_now") is False, "large AnimationTree is not required now")
    ok(rules.get("sprint5_new_animation_system") is False, "Sprint 5 has no authorised new animation system")

    gestures = {item.get("id"): item for item in data.get("gestures", [])}
    for gesture_id in [
        "malo_idle_listening",
        "malo_walk_child",
        "malo_pickup_fisher",
        "malo_carry_fisher",
        "malo_press_rec",
        "malo_recording_hold",
        "malo_stop_recording",
        "malo_press_play_listen",
        "ronan_notice_rec_glance",
        "mother_fridge_glance",
        "father_fireplace_adjust",
    ]:
        ok(gesture_id in gestures, f"gesture exists: {gesture_id}")

    for gesture_id in ["malo_press_rec", "malo_stop_recording", "malo_press_play_listen"]:
        if gesture_id in gestures:
            ok(gestures[gesture_id].get("priority") == "P0", f"current recorder gesture is P0: {gesture_id}")

if language_doc.exists():
    text = language_doc.read_text(encoding="utf-8")
    ok("L0 — Locomotion" in text, "gesture language defines locomotion layer")
    ok("L1 — Attention" in text, "gesture language defines attention layer")
    ok("L2 — Object interaction" in text, "gesture language defines object-interaction layer")
    ok("A six-year-old Malo should not move like a scaled-down adult player avatar" in text, "Malo age-specific motion principle is explicit")
    ok("Do not require root motion" in text, "root-motion policy is explicit")

if architecture_doc.exists():
    text = architecture_doc.read_text(encoding="utf-8")
    ok("Gameplay is authoritative" in text, "animation architecture keeps gameplay authoritative")
    ok("CharacterAnimationPresenter" in text, "future presenter seam is documented")
    ok("Do not make `InteractionContext` depend on animation anchors" in text, "animation anchors remain presentation-only")
    ok("never reject a valid Recorder action solely because animation data is unavailable" in text, "animation failure cannot break recorder gameplay")

if sequence_doc.exists():
    text = sequence_doc.read_text(encoding="utf-8")
    for token in ["Malo takes the Fisher Price", "Malo presses REC", "Malo releases REC / STOP", "Malo presses PLAY and listens", "Ronan notices he is being recorded"]:
        ok(token in text, f"critical sequence card exists: {token}")
    ok("animation does not gate logical REC" in text, "REC sequence preserves Recorder authority")
    ok("no automatic STOP" in text, "Mother-call reaction preserves active recording")

if handoff_doc.exists():
    text = handoff_doc.read_text(encoding="utf-8")
    ok("Gameplay owns logic. Animation owns presentation." in text, "Work handoff states ownership rule")
    ok("Do not turn the primitive placeholder into a fake final animation rig" in text, "Work avoids overbuilding placeholder")
    ok("Do not require root motion in the first pass" in text, "Work handoff keeps controller-authoritative locomotion")

if placeholder_path.exists():
    text = placeholder_path.read_text(encoding="utf-8")
    ok("AnimationTree" not in text and "AnimationPlayer" not in text, "placeholder has not been prematurely converted to production animation graph")
    ok("CharacterAnimationPresenter" not in text, "placeholder has no premature presenter coupling")

for path, label in [(controller_path, "MaloController"), (recorder_path, "Recorder")]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for forbidden in ["CharacterAnimationPresenter", "PRESS_REC", "PICKUP_FISHER", "AnimationTree", "animation_finished"]:
            ok(forbidden not in text, f"{label} has no premature animation coupling: {forbidden}")

print(f"\nCharacter animation design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
