#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"
GODOT_BIN="${GODOT_BIN:-godot}"

printf '\n=== BO Sprint 5 static validation ===\n'
"$PYTHON_BIN" tests/static_validate.py
"$PYTHON_BIN" tests/static_validate_sprint5.py
"$PYTHON_BIN" tests/static_validate_player_feel.py
"$PYTHON_BIN" tests/static_validate_asset_pipeline.py
"$PYTHON_BIN" tests/static_validate_house_plan.py
"$PYTHON_BIN" tests/static_validate_character_preview.py
"$PYTHON_BIN" tests/static_validate_sprint5_scenes.py
"$PYTHON_BIN" tests/static_validate_sound_catalog.py
"$PYTHON_BIN" tests/static_validate_hud_ux.py
"$PYTHON_BIN" tests/static_validate_interaction_planning.py
"$PYTHON_BIN" tests/static_validate_audio_memory_design.py
"$PYTHON_BIN" tests/static_validate_p0_sound_matrix.py
"$PYTHON_BIN" tests/static_validate_p0_sound_acquisition.py
"$PYTHON_BIN" tests/static_validate_cassette_memory_design.py
"$PYTHON_BIN" tests/static_validate_piste0_narrative_design.py
"$PYTHON_BIN" tests/static_validate_guidance_recovery_design.py
"$PYTHON_BIN" tests/static_validate_piste0_pacing_design.py
"$PYTHON_BIN" tests/static_validate_family_living_world_design.py

printf '\n=== BO Sprint 5 Godot headless contracts ===\n'
if command -v "$GODOT_BIN" >/dev/null 2>&1; then
  GODOT_BIN="$GODOT_BIN" bash tests/run_headless.sh
else
  printf 'SKIP: Godot binary not found (%s). Static validation passed; run headless tests in Work/Godot.\n' "$GODOT_BIN"
fi

printf '\n=== BO Sprint 5 validation complete ===\n'
