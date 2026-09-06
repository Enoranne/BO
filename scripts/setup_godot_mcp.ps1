$ErrorActionPreference = "Stop"

if (-not (Test-Path "project.godot")) {
    throw "Run this script from the BO_Ta_Vie project root (project.godot not found)."
}

foreach ($cmd in @("node", "npx", "codex")) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        throw "$cmd is not installed or not available on PATH."
    }
}

$major = [int](node -p 'process.versions.node.split(".")[0]')
if ($major -lt 18) {
    throw "Node.js 18+ is required."
}

Write-Host "Installing/enabling yanhuifair Godot-MCP editor plugin..."
npx -y @yanhuifair/godot-mcp --enable-plugin -p .

Write-Host "Registering Godot-MCP with Codex..."
$list = (codex mcp list 2>$null | Out-String)
if ($list -match "godot-mcp") {
    Write-Host "godot-mcp is already registered in Codex; leaving the existing entry in place."
} else {
    codex mcp add godot-mcp -- npx -y @yanhuifair/godot-mcp -p .
}

Write-Host "`nVerification:"
npx -y @yanhuifair/godot-mcp --version
codex mcp list

Write-Host "`nNext: open this project in Godot, then run:"
Write-Host 'codex exec "Run get_status. Then validate the project and list all scenes. Do not modify anything."'
