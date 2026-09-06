#!/usr/bin/env bash
set -euo pipefail

if [[ ! -f project.godot ]]; then
  echo "ERROR: run this script from the BO_Ta_Vie project root (project.godot not found)." >&2
  exit 1
fi

command -v node >/dev/null 2>&1 || { echo "ERROR: Node.js 18+ is required." >&2; exit 1; }
command -v npx >/dev/null 2>&1 || { echo "ERROR: npx is required." >&2; exit 1; }
command -v codex >/dev/null 2>&1 || { echo "ERROR: Codex CLI is not installed or not on PATH." >&2; exit 1; }

NODE_MAJOR="$(node -p 'process.versions.node.split(".")[0]')"
if (( NODE_MAJOR < 18 )); then
  echo "ERROR: Node.js 18+ is required; found $(node -v)." >&2
  exit 1
fi

echo "Installing/enabling yanhuifair Godot-MCP editor plugin..."
npx -y @yanhuifair/godot-mcp --enable-plugin -p .

echo "Registering Godot-MCP with Codex..."
if codex mcp list 2>/dev/null | grep -q 'godot-mcp'; then
  echo "godot-mcp is already registered in Codex; leaving the existing entry in place."
else
  codex mcp add godot-mcp -- npx -y @yanhuifair/godot-mcp -p .
fi

echo
echo "Verification:"
npx -y @yanhuifair/godot-mcp --version
codex mcp list

echo
echo "Next: open this project in Godot, then run:"
echo '  codex exec "Run get_status. Then validate the project and list all scenes. Do not modify anything."'
