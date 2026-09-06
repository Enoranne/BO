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

profile_path = root / "data/camera_zone_profiles_1982.json"
design_doc = root / "docs/CINEMATIC_GAMEPLAY_CAMERA_LANGUAGE.md"
handoff_doc = root / "docs/WORK_CAMERA_HANDOFF.md"
camera_path = root / "scenes/piste_0/christmas_1982/cinematic_camera.gd"
recorder_path = root / "recorder/recorder.gd"
controller_path = root / "characters/malo/malo.gd"

for path, label in [
    (profile_path, "camera zone profile exists"),
    (design_doc, "cinematic gameplay camera language exists"),
    (handoff_doc, "Work camera handoff exists"),
    (camera_path, "existing cinematic camera exists"),
]:
    ok(path.exists(), label)

if profile_path.exists():
    data = json.loads(profile_path.read_text(encoding="utf-8"))
    ok(data.get("status") == "design_only", "future camera zones remain design-only")
    baseline = data.get("baseline", {})
    ok(baseline.get("free_mouse_look") is False, "free mouse-look remains rejected")
    ok(baseline.get("recorder_owns_camera") is False, "Recorder does not own camera")
    ok(baseline.get("malo_controller_owns_camera") is False, "Malo controller does not own cinematic camera")
    modes = data.get("camera_modes", {})
    for mode in ["C0", "C1", "C2", "C3", "C4", "C5"]:
        ok(mode in modes, f"camera grammar includes {mode}")
    zones = {zone.get("id"): zone for zone in data.get("zones", [])}
    for zone_id in ["salon", "corridor", "kitchen", "garden", "gate_street_edge"]:
        ok(zone_id in zones, f"camera zone exists: {zone_id}")
    rules = data.get("transition_rules", {})
    ok(rules.get("preserve_player_control") is True, "camera transitions preserve player control")
    ok(rules.get("rec_can_continue_through_transition") is True, "REC may continue through camera transitions")
    ok(rules.get("auto_zoom_on_rec") is False, "REC does not auto-zoom camera")
    ok(rules.get("auto_center_every_interactable") is False, "camera does not auto-center every interactable")

if camera_path.exists():
    text = camera_path.read_text(encoding="utf-8")
    ok("max_offset" in text, "existing camera keeps bounded offset contract")
    ok("follow_x" in text and "follow_z" in text, "existing camera remains soft-follow based")

if design_doc.exists():
    text = design_doc.read_text(encoding="utf-8")
    ok("not camera-controlled by the player" in text, "cinematic framing thesis is explicit")
    ok("Camera must not zoom or snap automatically every time REC starts" in text, "REC/camera separation is explicit")
    ok("Do not evolve the project into unrestricted third-person mouse-look" in text, "free camera anti-pattern is explicit")
    ok("reduced_camera_motion" in text, "reduced camera motion accessibility is documented")

if handoff_doc.exists():
    text = handoff_doc.read_text(encoding="utf-8")
    ok("Do not convert to unrestricted 360 mouse-look" in text, "Work handoff preserves authored camera")
    ok("verify active REC continues across the transition" in text, "Work proof includes REC continuity")

for path, label in [(recorder_path, "Recorder"), (controller_path, "Malo")]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for forbidden in ["camera_zone_profiles", "CinematicCameraDirector", "camera_anchor_id", "PhantomCamera"]:
            ok(forbidden not in text, f"{label} has no premature cinematic-camera coupling: {forbidden}")

print(f"\nCamera design static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
