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

schema_path = root / "data/cassette_memory_schema.json"
titles_path = root / "data/child_recording_title_rules.json"
examples_path = root / "data/cassette_memory_examples.json"
design_doc = root / "docs/CASSETTE_LIBRARY_DESIGN.md"
ux_doc = root / "docs/CASSETTE_PHYSICAL_UX.md"
sprint6_doc = root / "docs/SPRINT6_RECORDING_MEMORY_PLAN.md"
clip_path = root / "recorder/recording_clip.gd"
recorder_path = root / "recorder/recorder.gd"

for path, label in [
    (schema_path, "cassette memory schema exists"),
    (titles_path, "child title rules exist"),
    (examples_path, "cassette memory examples exist"),
    (design_doc, "cassette library design doc exists"),
    (ux_doc, "physical cassette UX doc exists"),
    (sprint6_doc, "Sprint 6 recording-memory plan exists"),
]:
    ok(path.exists(), label)

if schema_path.exists():
    data = json.loads(schema_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "cassette schema remains design-only")
    rules = data.get("design_rules", {})
    ok(rules.get("recording_quality_score") is False, "no recording quality score")
    ok(rules.get("mandatory_title_before_playback") is False, "title not required before playback")
    ok(rules.get("destructive_delete_default") is False, "destructive deletion is not default")
    ok(rules.get("favourite_equals_good") is False, "favourite remains distinct from GOOD")
    ok(rules.get("physical_metaphor_first") is True, "physical metaphor is preferred")
    ok(rules.get("sprint5_implementation") is False, "cassette library is not a Sprint 5 implementation")
    states = set(data.get("memory_annotation", {}).get("keep_state", []))
    for state in ["UNREVIEWED", "GOOD", "FAILED_KEEP", "RETRY", "IMPORTANT"]:
        ok(state in states, f"memory keep state exists: {state}")
    boxes = {box.get("id") for box in data.get("early_childhood_boxes", [])}
    ok({"cassettes", "good", "failed_keep"}.issubset(boxes), "core childhood boxes exist")

if titles_path.exists():
    data = json.loads(titles_path.read_text(encoding="utf-8"))
    rules = data.get("rules", {})
    ok(rules.get("mandatory_before_playback") is False, "child title remains optional")
    ok(rules.get("stable_id_is_separate") is True, "display title is separate from stable id")
    examples_text = json.dumps(data.get("examples", []), ensure_ascii=False)
    for token in ["RONAN", "PORTAIL", "VENT"]:
        ok(token in examples_text, f"child-title examples cover {token}")

if examples_path.exists():
    data = json.loads(examples_path.read_text(encoding="utf-8"))
    examples = data.get("examples", [])
    states = {item.get("annotation", {}).get("keep_state") for item in examples}
    ok("GOOD" in states, "examples include a GOOD take")
    ok("FAILED_KEEP" in states, "examples include RATÉ MAIS GARDER behavior")
    ok("RETRY" in states, "examples include retry without deletion")

if design_doc.exists():
    text = design_doc.read_text(encoding="utf-8")
    ok("RATÉS MAIS GARDER" in text, "canonical failed-but-kept language is documented")
    ok("There is no global score" in text, "library design rejects global quality scoring")
    ok("Spotify/iTunes-style" in text, "modern media-library anti-pattern is documented")

if ux_doc.exists():
    text = ux_doc.read_text(encoding="utf-8")
    ok("in the world" in text, "physical cassette UX is world-first")
    ok("2 to 5 recordings" in text, "first review proof stays deliberately small")
    ok("RATÉS MAIS GARDER" in text, "physical failed-but-kept moment is represented")

if sprint6_doc.exists():
    text = sprint6_doc.read_text(encoding="utf-8")
    ok("Do not start this sprint until Sprint 5 is live-engine validated" in text, "Sprint 6 implementation is gated by Sprint 5 validation")
    ok("stable recording ids" in text, "Sprint 6 plan requires stable recording identity")
    ok("no quality score" in text.lower(), "Sprint 6 plan preserves no-score philosophy")

if clip_path.exists():
    text = clip_path.read_text(encoding="utf-8")
    for forbidden in ["keep_state", "favourite", "box_id", "child_note"]:
        ok(forbidden not in text, f"RecordingClip is not prematurely coupled to editorial field: {forbidden}")

if recorder_path.exists():
    text = recorder_path.read_text(encoding="utf-8")
    for forbidden in ["CassetteLibrary", "MemoryAnnotation", "FAILED_KEEP", "favourite"]:
        ok(forbidden not in text, f"Recorder is not prematurely coupled to cassette library: {forbidden}")

print(f"\nCassette memory design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
