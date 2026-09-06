# yanhuifair/Godot-MCP + Codex setup

This project is prepared to use **yanhuifair/Godot-MCP** with Codex/Astra.

## Requirements

- Godot 4.x
- Node.js 18+
- Codex CLI
- Internet access for the first `npx` download

## 1. Open a terminal in this project root

The current directory must contain `project.godot`.

## 2. Install/enable the Godot editor plugin

```bash
npx -y @yanhuifair/godot-mcp --enable-plugin -p .
```

This should create `addons/godot-mcp/` and enable the plugin in `project.godot`.

## 3. Register the MCP server in Codex

```bash
codex mcp add godot-mcp -- npx -y @yanhuifair/godot-mcp -p .
```

The `--` is important: everything after it is the command Codex will spawn for the MCP server.

Verify:

```bash
codex mcp list
```

## 4. Open BO_Ta_Vie in Godot

Keep the project open so the MCP editor bridge can connect.

## 5. First Codex smoke test — inspection only

From the project root:

```bash
codex exec "Run get_status. Then validate the project and list all scenes. Do not modify anything."
```

Expected result: the server reports its tool set, the project is detected, and `Christmas1982` is listed.

## 6. First live-editor test

After Godot is open:

```text
Run get_status. Confirm the editor bridge is reachable. Read Christmas1982, inspect its scene tree, then run the scene and take a screenshot. Do not change any files.
```

## 7. Sprint 0 repair/validation prompt

Once the inspection succeeds:

```text
Use godot-mcp for this project. First call get_status and use search_tools before choosing any MCP tool.

Validate the existing Sprint 0 without adding features. Preserve the strict scope:
Malo -> Fisher Price -> REC -> RonanTest -> STOP -> PLAY.

Tasks:
1. Validate project references and all GDScript syntax.
2. Read Christmas1982 before editing anything.
3. Run the scene.
4. Exercise the gameplay loop using runtime input where possible.
5. Inspect runtime errors and the live scene tree.
6. Take screenshots at STOP, REC and PLAY states.
7. Correct only bugs that prevent or visibly break this loop.
8. Re-run validation after every correction.
9. Do not add MK2, pitch, Sound-on-Sound, multitrack, inventory, menus or final art.
10. Finish with a concise test report: PASS/FAIL per step and files changed.
```

## Optional safety mode

For the very first exploration of an unfamiliar version of the project, the MCP server can be run in read-only mode. The normal Codex registration above is intentionally writable because this repository is already isolated under Git, but use read-only if you want an inspection-only session.

## Notes

- `AGENTS.md` contains the permanent rules Codex/Astra should follow in this repository.
- Always launch Codex from the project root when using `-p .`.
- If Godot is not auto-detected, set `GODOT_PATH` in Codex MCP configuration to the Godot executable.
