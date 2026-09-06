from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []


def ok(condition: bool, message: str) -> None:
    if condition:
        print(f"PASS: {message}")
    else:
        print(f"FAIL: {message}")
        errors.append(message)


project = (root / "project.godot").read_text(encoding="utf-8")
hud = (root / "ui/hud.gd").read_text(encoding="utf-8")
malo = (root / "characters/malo/malo.gd").read_text(encoding="utf-8")

# Preserve the abstract input architecture.
ok('Input.get_vector("move_left", "move_right", "move_forward", "move_back")' in malo,
   "Malo movement still uses abstract input actions")
ok('event.is_action_pressed("interact")' in malo,
   "Malo interaction still uses the interact action")
ok('event.is_action_pressed("play_recording")' in malo,
   "Malo playback still uses the play_recording action")
ok('event.is_action_pressed("record")' in malo and 'event.is_action_released("record")' in malo,
   "REC remains hold-to-record / release-to-stop")

# Physical movement cluster: W/A/S/D physical positions map naturally to Z/Q/S/D on AZERTY.
for code, name in [(87, "forward physical key"), (83, "back physical key"), (65, "left physical key"), (68, "right physical key")]:
    ok(f'physical_keycode":{code}' in project, f"{name} remains declared")

# Sprint 5.1 alternates.
interact_match = re.search(r'interact=\{(.*?)\n\}', project, re.S)
play_match = re.search(r'play_recording=\{(.*?)\n\}', project, re.S)
ok(interact_match is not None and 'InputEventMouseButton' in interact_match.group(1) and 'button_index":1' in interact_match.group(1),
   "left mouse button is an alternate interact binding")
ok(play_match is not None and 'physical_keycode":32' in play_match.group(1),
   "Space is an alternate playback binding")
ok(play_match is not None and 'physical_keycode":80' in play_match.group(1),
   "legacy P playback binding remains available")

# HUD should teach the new controls.
ok('E / Left click' in hud, "HUD teaches mouse interaction")
ok('Space / P' in hud, "HUD teaches Space playback while preserving P")

# No numpad dependency should be introduced.
ok('KP_' not in project and 'KEY_KP' not in project and 'numpad' not in project.lower(),
   "core controls do not depend on the numeric keypad")

print(f"\nPlayer-feel static validation complete: {len(errors)} failure(s).")
sys.exit(1 if errors else 0)
