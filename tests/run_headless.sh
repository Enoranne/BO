#!/usr/bin/env bash
set -euo pipefail
GODOT_BIN="${GODOT_BIN:-godot}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
# Fresh checkouts have no global-class cache or imported audio yet.
"$PYTHON_BIN" tests/run_godot_checked.py "$GODOT_BIN" --headless --path . --editor --import
"$PYTHON_BIN" tests/run_godot_checked.py "$GODOT_BIN" --headless --path . -s res://tests/test_recorder.gd
"$PYTHON_BIN" tests/run_godot_checked.py "$GODOT_BIN" --headless --path . -s res://tests/test_gameplay_contract.gd
"$PYTHON_BIN" tests/run_godot_checked.py "$GODOT_BIN" --headless --path . -s res://tests/test_visual_contract.gd
"$PYTHON_BIN" tests/run_godot_checked.py "$GODOT_BIN" --headless --path . -s res://tests/test_blocking_contract.gd
"$PYTHON_BIN" tests/run_godot_checked.py "$GODOT_BIN" --headless --path . -s res://tests/test_presentation_contract.gd
"$PYTHON_BIN" tests/run_godot_checked.py "$GODOT_BIN" --headless --path . -s res://tests/test_sprint5_scene_contract.gd
"$PYTHON_BIN" tests/run_godot_checked.py "$GODOT_BIN" --headless --path . -s res://tests/test_player_input_contract.gd
