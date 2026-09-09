# Beckett MCP spike — Sprint 5

## Decision

**VERDICT: REJECT FOR ACTIVE SPRINT 5 INTEGRATION / RETAIN AS FALLBACK**

Principle: **VALUE > COMPLEXITY**.

Beckett is technically credible and compatible with Godot 4.7, but it does not currently provide enough unique value to justify adding a second Godot MCP/runtime addon beside the project-standard `@yanhuifair/godot-mcp` stack.

## Candidate reviewed

- project: `beckettlab/beckett-godot-mcp`
- edition evaluated: Lite / MIT
- reviewed release: `v1.15.0`
- Godot target: 4.7
- architecture: MCP server embedded in Godot as an `EditorPlugin`, no Node.js/Python sidecar

## What Beckett does well

- zero-sidecar MCP server inside the Godot editor;
- no Node.js or Python process required for the MCP bridge;
- inspect -> author -> run -> see workflow;
- live runtime observation, screenshots, remote tree/node inspection, logs and performance;
- loopback-local transport;
- v1.15.0 adds export-safety measures so the editor addon is stripped from normal game exports except for a guarded stub.

## Comparison with the BO canonical Godot MCP

BO already standardises agent work around `@yanhuifair/godot-mcp` in `AGENTS.md`.

That stack already supplies the capabilities BO currently needs:

- large file/editor tool surface;
- `search_tools` discovery and `get_status` diagnostics;
- scene/script/resource editing;
- live editor inspection;
- runtime tree/node inspection;
- runtime input injection;
- screenshots;
- pause/freeze/resume;
- deterministic frame stepping;
- undoable editor mutations;
- compatibility with Codex and other MCP clients.

For BO, Beckett Lite therefore duplicates most high-value capabilities rather than filling a critical gap.

## Dependency and architecture cost

Beckett is not just an external CLI. Enabling it adds an editor plugin and registers a `BeckettRuntime` autoload for runtime observation.

Even though v1.15.0 improved export safety, adopting Beckett would still mean maintaining a second Godot editor/runtime integration, another port/configuration surface and another tool vocabulary for agents.

That conflicts with the current Sprint 5 dependency budget and increases handoff/debug ambiguity: an agent failure could originate from Beckett, `godot-mcp`, Godot itself, or their interaction.

## Why no installation was performed

The purpose of the spike is to decide whether Beckett improves BO, not merely prove that it can launch.

Installing it would add project/plugin state before a unique use case has been identified. Because the available feature set already shows heavy overlap with the canonical MCP, the value gate fails before installation is justified.

No gameplay, scene, `project.godot`, autoload or addon file is changed by this spike.

## Conditions for reconsideration

Re-evaluate Beckett only if one of these becomes true:

1. `@yanhuifair/godot-mcp` proves materially unstable on the production Mac workflow;
2. Node.js/sidecar management becomes a recurring source of friction;
3. Beckett gains a BO-critical capability that the canonical MCP cannot provide;
4. the project intentionally replaces the canonical MCP rather than running two overlapping MCP stacks;
5. a future Beckett edition offers autonomous playtesting that is clearly superior to the existing runtime + gdUnit4 validation path at acceptable cost.

## If reconsidered

Do not run both MCP stacks by default.

Use a separate spike branch and compare one concrete BO task end-to-end, for example:

`open Christmas1982 -> run -> move Malo -> take Fisher -> hold REC on Ronan -> STOP -> PLAY -> inspect runtime state -> capture screenshot`.

Measure:

- setup friction;
- execution reliability;
- number of repair/retry steps;
- observability;
- testability;
- token/tool overhead;
- reversibility;
- effect on local project state.

Only replace the canonical MCP if Beckett wins that comparison materially.

## Final status

- Beckett quality: **PASS**
- Godot 4.7 compatibility: **PASS (upstream-supported)**
- licensing for Lite: **PASS (MIT)**
- unique value for current BO Sprint 5: **INSUFFICIENT**
- dependency-budget fit: **FAIL if added alongside current MCP**
- installation into BO now: **NO**
- fallback candidate: **YES**

**BECKETT SPRINT 5: REJECT ACTIVE INTEGRATION / KEEP AS FALLBACK**
