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

beats_path = root / "data/piste0_narrative_beats.json"
deps_path = root / "data/piste0_beat_dependencies.json"
beats_doc = root / "docs/PISTE0_NARRATIVE_GAMEPLAY_BEATS.md"
structure_doc = root / "docs/PISTE0_PLAYABLE_STRUCTURE.md"
rollout_doc = root / "docs/PISTE0_IMPLEMENTATION_ROLLOUT.md"
recorder_path = root / "recorder/recorder.gd"
interaction_path = root / "interaction/interaction_context.gd"

ok(beats_path.exists(), "PISTE 0 narrative beat data exists")
ok(deps_path.exists(), "PISTE 0 beat dependency map exists")
ok(beats_doc.exists(), "PISTE 0 narrative beat design doc exists")
ok(structure_doc.exists(), "PISTE 0 playable-structure doc exists")
ok(rollout_doc.exists(), "PISTE 0 implementation-rollout doc exists")

beat_ids = set()
if beats_path.exists():
    data = json.loads(beats_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "PISTE 0 narrative beats remain design-only")
    rules = data.get("design_rules", {})
    ok(rules.get("quest_log") is False, "no quest-log design")
    ok(rules.get("waypoint_default") is False, "waypoints are not the default guidance")
    ok(rules.get("quality_score") is False, "recording quality is not scored")
    ok(rules.get("collect_all_requirement") is False, "no collect-all progression gate")
    ok(rules.get("mission_failed_language") is False, "no mission-failed language")
    ok(rules.get("sound_first_guidance") is True, "sound-first guidance is preserved")
    ok(rules.get("only_current_required_recording") == "ronan_test", "ronan_test remains the only current required recording")

    beats = data.get("beats", [])
    beat_ids = {beat.get("id") for beat in beats}
    required_ids = {
        "MB00_first_fisher",
        "MB02_gate_bonjour",
        "MB03_wind_mother_call",
        "MB04_fridge_mother",
        "MB05_ronan_suspect",
        "MB06_moped_pass",
        "MB07_radio_malo_genesis",
        "MB08_biscuit_special",
        "MB09_child_studio_boxes",
        "MB10_always_take_laugh",
        "MB11_horse_persistence",
        "MB12_tv_bricolage",
        "MB13_gull_patience",
        "MB14_tape_repair",
    }
    ok(required_ids.issubset(beat_ids), "known PISTE 0 signature beats are represented")

    mandatory = [beat for beat in beats if beat.get("criticality") == "mandatory_onboarding"]
    ok(len(mandatory) == 1, "only one mandatory onboarding beat exists")
    if mandatory:
        ok(mandatory[0].get("id") == "MB00_first_fisher", "mandatory onboarding remains first Fisher/Ronan beat")
        ok(mandatory[0].get("recording_source") == "ronan_test", "mandatory onboarding still records RonanTest")
        ok(mandatory[0].get("implementation") == "sprint4_sprint5_existing", "only existing onboarding is marked as current implementation")

if deps_path.exists():
    deps = json.loads(deps_path.read_text(encoding="utf-8"))
    ok(deps.get("status") == "design_only", "beat dependency map remains design-only")
    dep_beats = deps.get("beats", [])
    dep_ids = {item.get("id") for item in dep_beats}
    if beat_ids:
        ok(beat_ids == dep_ids, "dependency map covers exactly the narrative beat set")
    safe_now = [item.get("id") for item in dep_beats if item.get("safe_to_implement_now") is True]
    ok(safe_now == ["MB00_first_fisher"], "only existing first-Fisher beat is safe to implement now")
    gate = next((item for item in dep_beats if item.get("id") == "MB02_gate_bonjour"), None)
    ok(gate is not None, "gate beat dependency entry exists")
    if gate is not None:
        requirements = set(gate.get("requires", []))
        ok({"temporal_capture", "garden_playable"}.issubset(requirements), "gate proof waits for temporal capture and garden access")
    ok("one new systemic dependency at a time" in deps.get("rollout_rule", ""), "rollout rule limits simultaneous systemic risk")

if beats_doc.exists():
    text = beats_doc.read_text(encoding="utf-8")
    for token in ["BONJOUR", "MALO TU FAIS QUOI", "Radio Malo est complètement génial", "RATÉS MAIS GARDER", "Toujours prendre le rire"]:
        ok(token in text, f"narrative design covers signature PISTE 0 element: {token}")
    ok("No minimap objective markers" in text, "anti-quest marker rule is documented")
    ok("MISSION PASSED" in text and "FAILED" in text, "mission-language anti-pattern is documented")

if structure_doc.exists():
    text = structure_doc.read_text(encoding="utf-8")
    for phase in [
        "Christmas 1982 / Discovery",
        "The house becomes audible",
        "Garden / Sound hunting",
        "Malo starts organising",
        "Recording becomes storytelling",
        "Persistence / Experimentation",
        "MK2 transition",
        "Radio Malo",
    ]:
        ok(phase in text, f"playable structure includes phase: {phase}")
    ok("Do not expose a completion percentage for sounds" in text, "no sound-completion percentage")

if rollout_doc.exists():
    text = rollout_doc.read_text(encoding="utf-8")
    for token in [
        "Ronan archive",
        "physical review",
        "temporal capture test",
        "Gate",
        "Wind",
        "Fridge",
        "Radio Malo",
        "MK2",
    ]:
        ok(token in text, f"rollout includes staged proof: {token}")
    ok("Why gate first" in text, "gate is explicitly justified as first new signature beat")
    ok("No DAW" in text, "early Radio Malo rollout explicitly avoids a DAW")
    ok("Do not immediately build the garden" in text, "temporal capture is proven in isolation before world expansion")

for path, label in [(recorder_path, "Recorder"), (interaction_path, "InteractionContext")]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for forbidden in ["Quest", "Mission", "MB02_gate_bonjour", "Radio Malo", "collect_all"]:
            ok(forbidden not in text, f"{label} has no premature narrative-beat coupling: {forbidden}")

print(f"\nPISTE 0 narrative design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
