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

profiles_path = root / "data/audio_memory_profiles_1982.json"
events_path = root / "data/p0_sound_event_design.json"
catalog_path = root / "data/sound_catalog_1982.json"
pipeline_doc = root / "docs/AUDIO_MEMORY_PIPELINE_1982.md"
temporal_doc = root / "docs/FUTURE_TEMPORAL_CAPTURE_ARCHITECTURE.md"
choreography_doc = root / "docs/P0_INTERACTION_SOUND_CHOREOGRAPHY.md"
adr_doc = root / "docs/ADR_001_TEMPORAL_AUDIO_CAPTURE.md"
recorder = root / "recorder/recorder.gd"

ok(profiles_path.exists(), "audio memory profile data exists")
ok(events_path.exists(), "P0 temporal sound-event map exists")
ok(catalog_path.exists(), "sound production catalog exists")
ok(pipeline_doc.exists(), "three-stage audio memory pipeline doc exists")
ok(temporal_doc.exists(), "future temporal capture architecture doc exists")
ok(choreography_doc.exists(), "P0 interaction/sound choreography doc exists")
ok(adr_doc.exists(), "temporal audio capture ADR exists")

catalog_ids = set()
if catalog_path.exists():
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    catalog_ids = {entry.get("id") for entry in catalog.get("entries", [])}
    required = [entry.get("id") for entry in catalog.get("entries", []) if entry.get("required_in_sprint5")]
    ok(required == ["ronan_test"], "sound catalog still has only ronan_test as required Sprint 5 recording")

if profiles_path.exists():
    data = json.loads(profiles_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "audio memory profiles remain design-only")
    profiles = data.get("profiles", {})
    ok(set(["world", "fisher_capture", "cassette_playback"]).issubset(profiles), "WORLD / FISHER_CAPTURE / CASSETTE_PLAYBACK profiles exist")
    rule = data.get("sprint5_rule", {})
    ok(rule.get("required_recording") == "ronan_test", "ronan_test remains the only required recording")
    ok(rule.get("implement_dsp_now") is False, "DSP implementation is explicitly deferred")
    ok(rule.get("new_required_recordings") is False, "audio design does not add Sprint 5 required recordings")
    treatments = data.get("p0_treatments", {})
    for sound_id in [
        "gate_squeak",
        "garden_wind_tree",
        "kitchen_fridge_hum",
        "fisher_button_mechanics",
        "fisher_transport_click",
        "fireplace_crackle",
        "street_moped_pass",
        "ronan_test",
    ]:
        ok(sound_id in treatments, f"P0 memory treatment exists: {sound_id}")
        ok(sound_id in catalog_ids, f"P0 memory treatment maps to sound catalog id: {sound_id}")

if events_path.exists():
    events = json.loads(events_path.read_text(encoding="utf-8"))
    ok(events.get("status") == "design_only", "P0 event behavior map remains design-only")
    event_items = events.get("events", [])
    event_ids = [event.get("sound_id") for event in event_items]
    ok(len(event_ids) == len(set(event_ids)), "P0 event map has no duplicate sound ids")
    for sound_id in event_ids:
        ok(sound_id in catalog_ids, f"P0 event maps to production catalog id: {sound_id}")
    valid_types = {"passive", "triggered", "moving", "device"}
    for event in event_items:
        ok(event.get("event_type") in valid_types, f"valid temporal event type: {event.get('sound_id')}")
    rules = events.get("global_rules", {})
    ok(rules.get("recording_quality_score") is False, "recordings are not numerically quality-scored")
    ok(rules.get("automatic_pristine_replacement") is False, "partial recordings are not replaced by pristine full events")
    ok(rules.get("partial_recordings_valid") is True, "partial recordings remain valid content")
    ok(rules.get("playback_feedback_into_capture_default") is False, "playback feedback is disabled by default in future design")

if pipeline_doc.exists():
    text = pipeline_doc.read_text(encoding="utf-8")
    ok("WORLD" in text and "FISHER CAPTURE" in text and "CASSETTE PLAYBACK" in text, "pipeline doc defines all three perceptual stages")
    ok("not measured hardware specifications" in text.lower(), "creative tuning values are not misrepresented as measured hardware specs")

if temporal_doc.exists():
    text = temporal_doc.read_text(encoding="utf-8")
    ok("Design only" in text, "temporal capture remains future design")
    ok("CaptureBackend" in text, "future capture seam preserves Recorder decoupling")
    ok("anti-feedback" in text.lower(), "future routing explicitly protects against accidental feedback")
    ok("Sprint 6 candidate" in text, "temporal capture implementation is deferred beyond Sprint 5")

if choreography_doc.exists():
    text = choreography_doc.read_text(encoding="utf-8")
    for token in ["Fisher Price", "Gate", "Wind", "Fridge", "Fireplace", "Moped"]:
        ok(token in text, f"P0 choreography covers {token}")
    ok("No score for recording quality" in text, "recording quality remains listen-first rather than scored")
    ok("composition" in text.lower(), "interaction + recordability composition rule is documented")

if adr_doc.exists():
    text = adr_doc.read_text(encoding="utf-8")
    ok("Status:** Proposed" in text, "temporal capture ADR is proposed rather than accepted/implemented")
    ok("dedicated recordable-world audio bus" in text.lower(), "ADR identifies bus-based temporal capture candidate")
    ok("Do not implement ADR-001" in text, "ADR contains explicit Sprint 5 implementation stop gate")

if recorder.exists():
    text = recorder.read_text(encoding="utf-8")
    ok("AudioEffectRecord" not in text and "CaptureBackend" not in text, "Sprint 5 Recorder has not been prematurely rewritten for temporal capture")

print(f"\nAudio-memory design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
