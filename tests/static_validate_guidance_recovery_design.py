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

profiles_path = root / "data/guidance_profiles.json"
rules_path = root / "data/assistance_recovery_rules.json"
guidance_doc = root / "docs/GUIDANCE_ASSISTANCE_MODES.md"
recovery_doc = root / "docs/MICRO_QUEST_FAILURE_RECOVERY.md"
recorder_path = root / "recorder/recorder.gd"

for path, label in [
    (profiles_path, "guidance profiles exist"),
    (rules_path, "assistance recovery rules exist"),
    (guidance_doc, "guidance modes doc exists"),
    (recovery_doc, "failure/recovery doc exists"),
]:
    ok(path.exists(), label)

if profiles_path.exists():
    data = json.loads(profiles_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "guidance design remains design-only")
    ok(data.get("default_profile") == "NATURAL", "NATURAL is the default guidance profile")
    ok(data.get("same_campaign_content") is True, "guidance profiles share one campaign")
    ok(data.get("changeable_during_play") is True, "guidance can change during play")
    profiles = data.get("profiles", {})
    ok({"GUIDED", "NATURAL", "FREE"}.issubset(profiles), "all three guidance profiles exist")
    invariants = data.get("invariants", {})
    for key in ["same_story", "same_memory_beats", "same_endings", "same_rewards", "no_progress_penalty_for_guidance"]:
        ok(invariants.get(key) is True, f"guidance invariant holds: {key}")

if rules_path.exists():
    data = json.loads(rules_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "recovery rules remain design-only")
    principles = data.get("principles", {})
    ok(principles.get("mission_failed_language") is False, "no mission-failed language")
    ok(principles.get("frame_perfect_timing_required") is False, "no frame-perfect timing requirement")
    ok(principles.get("optional_beats_block_progression") is False, "optional beats do not block progression")
    ok(principles.get("poor_recording_equals_game_failure") is False, "poor recordings are not game failure")
    ok(principles.get("recorder_owns_story_failure") is False, "Recorder does not own narrative failure")
    ladder = data.get("hint_ladder", [])
    ok([item.get("level") for item in ladder] == [0, 1, 2, 3, 4], "hint ladder is ordered 0 through 4")
    ok(data.get("current_mandatory_beat") == "MB00_first_fisher", "current mandatory beat remains Fisher/Ronan onboarding")

if guidance_doc.exists():
    text = guidance_doc.read_text(encoding="utf-8")
    for token in ["GUIDED", "NATURAL", "FREE", "ARCHIVE MODE", "Default profile: `NATURAL`"]:
        ok(token in text, f"guidance document includes: {token}")
    ok("same story content" in text.lower(), "guidance doc preserves identical story content")

if recovery_doc.exists():
    text = recovery_doc.read_text(encoding="utf-8")
    for token in ["interesting failure", "soft retry", "adaptive assistance", "Hint 4"]:
        ok(token in text, f"recovery document includes: {token}")
    ok("Never default to `MISSION FAILED`" in text, "recovery doc explicitly rejects mission-failed framing")

if recorder_path.exists():
    text = recorder_path.read_text(encoding="utf-8")
    for forbidden in ["GUIDED", "NATURAL", "FREE", "Hint 4", "MISSION FAILED", "failed_attempts"]:
        ok(forbidden not in text, f"Recorder is not coupled to assistance logic: {forbidden}")

print(f"\nGuidance/recovery design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
