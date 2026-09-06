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

model_path = root / "data/piste0_pacing_model.json"
doc_path = root / "docs/PISTE0_PACING_RHYTHM.md"
recorder_path = root / "recorder/recorder.gd"
interaction_path = root / "interaction/interaction_context.gd"

ok(model_path.exists(), "PISTE 0 pacing model exists")
ok(doc_path.exists(), "PISTE 0 pacing document exists")

if model_path.exists():
    data = json.loads(model_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "pacing model remains design-only")
    ok(data.get("rhythm_unit") == ["NOTICE", "WANT", "TRY", "RESULT", "REPLAY_OR_REACTION", "RELEASE"], "core rhythm unit is preserved")
    bands = set(data.get("bands", {}))
    ok({"CALM", "PLAYFUL", "FOCUSED", "CHAOTIC", "REFLECTIVE"}.issubset(bands), "all pacing bands exist")
    rules = data.get("rules", {})
    ok(rules.get("max_similar_beats_in_row") == 2, "similar beat run is limited")
    ok(rules.get("classification_after_every_recording") is False, "classification is not forced after every recording")
    ok(rules.get("fill_all_silence") is False, "silence remains allowed")
    ok(rules.get("stack_timing_challenges") is False, "timing challenges are not stacked")
    invariants = data.get("invariants", {})
    ok(invariants.get("guidance_changes_clarity_not_authored_rhythm") is True, "guidance does not rewrite pacing identity")
    ok(invariants.get("recorder_owns_pacing") is False, "Recorder does not own pacing")
    ok(invariants.get("interaction_context_owns_pacing") is False, "InteractionContext does not own pacing")

if doc_path.exists():
    text = doc_path.read_text(encoding="utf-8")
    for token in ["NOTICE -> WANT -> TRY -> RESULT -> REPLAY/REACTION -> RELEASE", "Anti-boredom rules", "Anti-fatigue rules", "Archive Mode"]:
        ok(token in text, f"pacing document includes: {token}")
    ok("five passive ambience discoveries in a row" in text, "pacing doc rejects passive repetition")

for path, label in [(recorder_path, "Recorder"), (interaction_path, "InteractionContext")]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for forbidden in ["CALM", "PLAYFUL", "FOCUSED", "CHAOTIC", "REFLECTIVE", "NOTICE", "WANT"]:
            ok(forbidden not in text, f"{label} is not coupled to pacing metadata: {forbidden}")

print(f"\nPISTE 0 pacing design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
