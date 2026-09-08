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

hud = root / "ui/hud.gd"
hud_pass = root / "visual/period_1982_hud_pass.gd"
visual_scene = root / "scenes/piste_0/christmas_1982/Christmas1982_VisualSlice.tscn"
doc = root / "docs/HUD_UX_SPRINT5.md"

for path, label in [
    (hud, "HUD script"),
    (hud_pass, "Visual Slice HUD pass"),
    (visual_scene, "Visual Slice scene"),
    (doc, "HUD UX contract"),
]:
    ok(path.exists(), f"{label} exists")

if hud.exists():
    text = hud.read_text(encoding="utf-8")
    # Canonical defaults must preserve the development HUD unless the wrapper opts in.
    ok('@export var objective_prefix := "OBJECTIVE  "' in text, "canonical objective prefix remains default")
    ok("@export var compact_hints := false" in text, "canonical compact hints remain disabled")
    ok("@export var teach_legacy_play_key := true" in text, "canonical HUD still teaches legacy P")
    ok("@export var minimal_context_hints := false" in text, "canonical minimal hints remain disabled")
    ok("@export var state_color_emphasis := false" in text, "canonical state colour emphasis remains disabled")

    for wording in [
        "Release R  Stop",
        "Playing…",
        "Space  Play",
        "Hold R  Record",
        "Find a sound",
    ]:
        ok(wording in text, f"context-first wording exists: {wording}")

    ok("_has_clip" in text, "HUD tracks presentation-only clip availability for hint priority")
    ok("_current_state" in text, "HUD tracks presentation-only Recorder state for hint priority")
    ok("refresh_presentation" in text, "HUD exposes presentation refresh without gameplay ownership")
    ok("recorder.recording_time_changed.connect(_render_time)" in text,
       "HUD renders elapsed REC time from Recorder presentation signal")
    ok("recorder.playback_time_changed.connect(_render_time)" in text,
       "HUD renders elapsed PLAY time from Recorder presentation signal")

if hud_pass.exists():
    text = hud_pass.read_text(encoding="utf-8")
    for setting, expected in [
        ('hud.set("objective_prefix", "")', "objective prefix removed"),
        ('hud.set("compact_hints", true)', "compact hints enabled"),
        ('hud.set("teach_legacy_play_key", false)', "P hidden from Visual Slice teaching"),
        ('hud.set("minimal_context_hints", true)', "single context hint enabled"),
        ('hud.set("state_color_emphasis", true)', "state colour emphasis enabled"),
    ]:
        ok(setting in text, expected)
    ok('hud.call("refresh_presentation")' in text, "HUD presentation is refreshed after wrapper preferences")
    for forbidden in ["start_recording(", "stop_recording(", "play_latest(", "InputMap", "InteractionContext", "RecordingClip"]:
        ok(forbidden not in text, f"HUD pass has no gameplay ownership token: {forbidden}")

if visual_scene.exists():
    text = visual_scene.read_text(encoding="utf-8")
    ok("period_1982_hud_pass.gd" in text, "Visual Slice loads HUD presentation pass")
    ok('root_path = NodePath("../Base")' in text, "presentation passes target the canonical Base instance")

print(f"\nSprint 5 HUD UX static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
