#!/usr/bin/env bash
set -euo pipefail
GODOT_BIN="${GODOT_BIN:-godot}"
"$GODOT_BIN" --headless --path . -s res://tests/test_recorder.gd
"$GODOT_BIN" --headless --path . -s res://tests/test_gameplay_contract.gd
"$GODOT_BIN" --headless --path . -s res://tests/test_visual_contract.gd
"$GODOT_BIN" --headless --path . -s res://tests/test_blocking_contract.gd
