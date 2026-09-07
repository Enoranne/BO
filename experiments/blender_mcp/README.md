# Blender MCP — controlled asset-normalization spike

## Decision principle

This spike measures improvement to the BO_Ta_Vie pipeline, not mere technical capability. **Value must exceed complexity.** A functioning tool is rejected if it increases iteration time, dependencies, maintenance, handoff difficulty, or regression risk without a compensating gain.

## Immutable baseline

- repository: `Enoranne/BO`
- branch: `spike/blender-mcp`
- baseline HEAD: `7d72ce8bab8dd7a90fc0aff01dc00a497412a750`
- baseline worktree: clean
- baseline diff stat: empty
- baseline validation: 23 static validators and 7 Godot headless suites pass
- protected-file manifest: `protected_files.sha256`

Run from repository root before and after every experiment:

```bash
sha256sum -c experiments/blender_mcp/protected_files.sha256
```

Any mismatch is a stop condition. Do not repair it automatically.

## Allowed scope

Only the existing Higgsfield coffee-table GLB may be used, or an explicitly labelled local proxy when that file is absent. The original is immutable. Blender sources and new exports belong under `experiments/blender_mcp/` or `assets/3d/experimental/`; use names such as `coffee_table_test_blender_normalized.glb`. No network asset, AI generation, character, animation, house model, gameplay, production material or canonical collision work is allowed.

No output may be referenced by `Christmas1982.tscn`. Godot testing is limited to an experimental copy of `CoffeeTableAssetPreview.tscn`.

## Tool and supply-chain inventory

| Component | Evaluated version | Source / licence | Relevant access |
| --- | --- | --- | --- |
| Work host | Linux 6.18.35, x86-64 | managed environment | unrestricted project filesystem; restricted network; no display/Xvfb |
| Godot | 4.7 stable, commit `5b4e0cb0f` | official Godot release | headless only |
| Blender | not installed | Blender Foundation, GPL | Blender MCP requires GUI or a virtual display |
| Blender MCP | 1.9.1 source at commit `c5f35d9cc54451d785ac4c00c48bf9e98a2e8db9` | `ahujasid/blender-mcp`, MIT, explicitly third-party | localhost socket 9876; arbitrary Blender Python by default; optional asset networks and telemetry |
| Python / uvx | 3.12.13 / available | Work runtime | MCP server package execution; not invoked for installation |
| Node / npm | 24.19.0 / 11.9.0 | Work runtime | not required by Blender MCP |

The source repository, maintainer (Siddharth Ahuja), MIT licence, current commit, recent activity, dependencies (`mcp`, `httpx`), installation method, filesystem/network reach and code-execution surface were inspected. The project has no GitHub releases; version 1.9.1 comes from `pyproject.toml` at the audited commit.

Blender MCP supports arbitrary Python execution by default, network asset providers, AI 3D services and optional telemetry. A future authorized retest must use `BLENDER_MCP_SAFE_MODE=1`, `DISABLE_TELEMETRY=true`, localhost only, no provider credentials, and no asset/network/generation tools. Safe Mode protects only the MCP path; the addon socket can still accept raw `execute_code` from another local process. These limitations prevent treating it as a security boundary.

No MCP package or Blender binary was installed: the addon explicitly refuses Blender background mode, and this Work environment has no GUI display or virtual display. Installing a large application could not make the required connection usable and would add unjustified friction.

## Coordinate-system and normalization contract

- Godot: right-handed, Y up, `-Z` forward, one unit interpreted as one metre.
- Blender: right-handed, Z up, `-Y` forward by Blender glTF convention.
- glTF/GLB uses metres; Blender's glTF importer/exporter performs axis conversion.
- target diagnostic envelope: approximately 1.05 × 0.55 × 0.38 m, not final art approval.
- source dimensions, object/data transforms, origin and orientation must be recorded before correction.
- apply only reproducible object transforms and export into a new file; never hide a scale compensation in Godot.

## Reproducible test procedure

Pinned retest only:

1. Install a recorded Blender version and Blender MCP 1.9.1 from audited commit `c5f35d9` in a graphical environment.
2. Start MCP with Safe Mode and telemetry disabled; verify addon/server versions and localhost connection.
3. Preserve `coffee_table_test.glb`; record its provenance as experimental and licence unresolved for production.
4. Import it into an isolated `.blend` source under `experiments/blender_mcp/`.
5. Record object count, dimensions, transforms, origins, axes, mesh/material/triangle counts and source GLB size.
6. Normalize only scale/orientation/origin/shading/material facts demonstrated necessary.
7. Save the `.blend` source and export a new normalized GLB.
8. Import A and B into an experimental Godot preview using identical camera/light/import settings; record warnings, import time, hierarchy, mesh/material/triangle counts and approximate draw-call/material complexity.
9. Make one minor origin or material correction in Blender, export B2, and verify stable Godot reimport and references.
10. Recheck protected hashes and full Sprint 5 validation.

The editable `.blend` file is the cleanup source; Godot owns runtime import/scenes; GitHub owns versioned project state. No Blender dependency is permitted at runtime and no indispensable gameplay data may live in Blender.

## Mandatory round-trip and adoption gates

Adoption requires both the first normalization and a second controlled export, a real gain over manual cleanup, stable Godot reimports, original preservation, reproducible source and acceptable complexity. Visual A/B must use the same camera, lighting and framing. No irreproducible manual Godot adjustment is allowed; the workflow must remain stable across ten reexports.

## Current controlled result

- connection: **FAIL** — no Blender MCP tool is exposed; no graphical Blender runtime is available.
- import: **FAIL / NOT EXECUTED** — the existing coffee-table GLB is not present locally.
- normalization: **FAIL / NOT EXECUTED**.
- export GLB: **FAIL / NOT EXECUTED**.
- Godot import: **FAIL / NOT REACHED**.
- second export / round-trip: **FAIL / NOT REACHED**.
- time to first useful result: **not reached**; environment gate identified well inside the 60–90 minute budget.
- time to second iteration: **not available**.
- friction: **HIGH in this Work environment**.
- Godot import warnings and performance metrics: not available because no GLB was imported.
- new paid actions: none.
- new external assets: none.
- coffee-table provenance: Higgsfield technical candidate only; file absent and production rights unresolved.

## Detailed score

| Criterion | Score /10 | Evidence |
| --- | ---: | --- |
| Installation / MCP | 1 | GUI requirement cannot be met here |
| Inspection | 0 | no connection or source GLB |
| Scale correction | 0 | not executed |
| Transform correction | 0 | not executed |
| Materials | 0 | not executed |
| Optimization | 0 | not executed |
| GLB export | 0 | not executed |
| Godot interoperability | 6 | standard glTF path is supported in principle, unverified here |
| Reversibility | 7 | separate `.blend` and output GLB can preserve the original |

Weighted inputs: BO value 5, GLB quality 0, iteration speed 0, Godot interoperability 6, MCP reliability 1, reversibility/maintenance 7.

**BLENDER WEIGHTED SCORE: 3.0/10**

**VERDICT: RETEST** in a graphical, pinned Blender environment with the existing GLB. This result does not reject Blender as an asset tool; it rejects claiming MCP value from this session.

## Cleanup and follow-up

No addon, Blender runtime dependency, `.blend`, scene or asset is referenced by BO. Removing `experiments/blender_mcp/` leaves the canonical project unchanged. Follow-up candidates, not implementation work: supply a display-capable Blender host; retrieve the already-existing Higgsfield revision only after its earlier visual gate; record production licence/provenance; execute A/B/B2 with Safe Mode and telemetry disabled.

NEW WORK SESSION CAN REPRODUCE PIPELINE: **NO** (required runtime and input asset are absent)

EXPERIMENTAL DEPENDENCY LEAK: **NONE**

SAFE TO INTEGRATE BLENDER INTO BO PIPELINE: **NO**

CANONICAL GAMEPLAY MODIFIED: **NO**

## Final report fields

- BASELINE HEAD: `7d72ce8bab8dd7a90fc0aff01dc00a497412a750`
- FINAL HEAD: recorded in the branch handoff after this report is committed
- PROTECTED FILE HASHES: **IDENTICAL**
- BLENDER TIME TO FIRST RESULT: **NOT REACHED** (GUI/runtime and source-asset gates identified immediately; no disproportionate installation attempted)
- BLENDER ROUND-TRIP: **FAIL**
- GODOT IMPORT WARNINGS: **N/A — no experimental GLB imported**
- EXPERIMENTAL DEPENDENCY LEAK: **NO**
- NEW PAID ACTIONS: **NONE**
- NEW EXTERNAL ASSETS: **NONE**
- PIPELINE REPRODUCIBLE: **NO**
- FOLLOW-UP CANDIDATES: pinned graphical Blender host; existing coffee-table revision retrieval; provenance review; A/B/B2 Safe Mode benchmark
