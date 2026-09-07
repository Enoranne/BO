# Pascal MCP — controlled authoring spike

## Decision principle

This spike measures improvement to the BO_Ta_Vie pipeline, not mere technical capability. **Value must exceed complexity.** A functioning tool is rejected if it adds disproportionate iteration time, dependencies, maintenance, handoff difficulty, or regression risk.

## Immutable baseline

- repository: `Enoranne/BO`
- branch: `spike/pascal-mcp`
- baseline HEAD: `7d72ce8bab8dd7a90fc0aff01dc00a497412a750`
- baseline worktree: clean
- baseline diff stat: empty
- baseline validation: 23 static validators and 7 Godot headless suites pass
- protected-file manifest: `protected_files.sha256`

Run from repository root before and after every experiment:

```bash
sha256sum -c experiments/pascal_mcp/protected_files.sha256
```

Any mismatch is a stop condition. Do not repair it automatically.

## Allowed scope

Only a salon shell, one opening and a short non-playable corridor segment may be authored. Optional fireplace and sofa proxies may be used for scale. No production decoration, gameplay, collisions, lighting, characters, audio, house expansion, or generated assets.

Outputs belong only under `experiments/pascal_mcp/` (and, if a neutral shared experimental asset is ever justified, `assets/3d/experimental/`). No experimental result may be referenced by the canonical scene.

## Tool and supply-chain inventory

| Component | Evaluated version | Source / licence | Relevant access |
| --- | --- | --- | --- |
| Work host | Linux 6.18.35, x86-64 | managed environment | unrestricted project filesystem; restricted network; no display |
| Godot | 4.7 stable, commit `5b4e0cb0f` | official Godot release | headless only |
| Pascal Editor | `1.0.0-beta.1`, commit `d92c0e652239c13ae35523c11ef973c796d816b2` | `pascalorg/editor`, MIT | browser/WebGPU editor; local files/database; optional network assets |
| Pascal MCP | `1.0.0-beta.1`, same commit | official `@pascal-app/mcp`, MIT | stdio or loopback HTTP; local SQLite; scene file reads; optional network vision inputs |
| Bun | 1.3.0 | official `oven-sh/bun` release | package/runtime filesystem and network during install |
| Node / npm | 24.19.0 / 11.9.0 | Work runtime | not used to substitute an unpinned Pascal runtime |
| Python | 3.12.13 | Work runtime | not required by Pascal MCP |

The source repository, maintainer (`Pascal Group Inc.`), MIT licence, recent release activity, lockfile, primary dependencies, installation method, transports and permissions were inspected before installation. Pascal MCP depends directly on the MCP SDK, Pascal core/lingo and Zod. Its documented persistent store defaults to `~/.pascal/data/pascal.db`; any future retest must instead set `PASCAL_DATA_DIR` to this experiment directory. Non-loopback HTTP is forbidden for this spike. No secrets are required or permitted.

The official Bun 1.3.0 Linux x64 archive was downloaded outside BO and matched release SHA-256 `60c39d92b8bd090627524c98b3012f0c08dc89024cfdaa7c9c98cb5fd4359376`. Dependency installation was attempted from the pinned Pascal lockfile with install scripts disabled and an external cache. Work blocked registry access; the attempt was stopped rather than requesting expanded network authority.

## Coordinate-system contract

- Pascal: right-handed, X/Z ground plane, Y up, metres, Euler rotations in radians.
- Godot: right-handed, X/Z ground plane, Y up, one unit interpreted as one metre.
- intended conversion: `1 Pascal metre = 1 Godot unit = 1 metre`, with no hidden scale compensation.
- wall-attached positions in Pascal are wall-local; viewport orientation is not source geometry orientation.
- any future exported GLB must be checked for forward-axis conversion, origin, applied transforms and stable reimport before adoption.

## Reproducible test procedure

Pinned retest only:

1. Use Pascal Editor/MCP `1.0.0-beta.1` from commit `d92c0e6` and Bun 1.3.0.
2. Set `PASCAL_DATA_DIR` inside `experiments/pascal_mcp/runtime-data/`.
3. Connect over stdio; never expose a non-loopback endpoint.
4. Create the 12 × 8 m salon shell at 3.6 m height from `data/christmas1982_house_zones.json`.
5. Add one opening and a 1.35 × 4.6 m corridor segment at 2.65 m height.
6. Inspect, measure, validate and save the editable Pascal JSON/SQLite source.
7. Export a new GLB, import it only in `PascalHousePreview.tscn`, and record import metrics.
8. Change one opening width, re-export and reimport without manual Godot edits.
9. Compare both iterations for timing, hierarchy, transforms, materials, mesh/material/triangle counts, warnings and predictable reference stability.
10. Recheck protected hashes and the complete Sprint 5 validation.

The editable Pascal scene must remain the architectural authoring source; Blender, if separately adopted, owns cleanup sources; Godot owns runtime scenes; GitHub owns versioned project state. No external tool may own indispensable gameplay data.

## Mandatory round-trip and adoption gates

The first export is insufficient. Adoption requires a successful second edit/export/import, a reproducible source, predictable reimport, acceptable mesh/material complexity, no runtime dependency, and faster or more editable architecture than current Godot primitives. Collision generation is evaluated only as potential; canonical collisions are never generated or replaced during this spike.

Visual comparisons must use the same camera, lighting and framing. Import settings must be versioned/documented; no irreproducible manual Godot changes are allowed. The pipeline must remain credible after ten reexports.

## Current controlled result

- connection: **FAIL** — no Pascal MCP tool is exposed to this Work session; isolated dependency resolution was blocked by registry policy.
- authoring: **FAIL / NOT EXECUTED**.
- export: **FAIL** — the evaluated MCP explicitly returns `not_implemented` for `export_glb`; rendered geometry requires the browser Three.js/WebGPU path.
- Godot import: **FAIL / NOT REACHED**.
- round-trip: **FAIL / NOT POSSIBLE IN THIS ENVIRONMENT**.
- time to first useful result: **not reached**; audit plus bounded installation attempt stopped well inside the 60–90 minute budget.
- time to second iteration: **not available**.
- friction: **HIGH**.
- collision generation potential: **ACCEPTABLE but unverified**; semantic wall/opening data exists, while derived geometry is not generated headlessly.
- Godot import/performance metrics: not available because no GLB was produced.
- new paid actions: none.
- new external assets: none.
- asset provenance: no asset used; the Higgsfield coffee table was not retrieved.

## Detailed score

| Criterion | Score /10 | Evidence |
| --- | ---: | --- |
| Installation / MCP | 3 | pinned source and runtime identifiable; connection blocked |
| Architecture speed | 4 | promising high-level tools, not timed live |
| Precision | 7 | explicit metres, dimensions and typed schemas |
| Agent modification | 7 | walls, openings, measurement, undo and validation exposed |
| Scene graph quality | 7 | semantic editable nodes and JSON source |
| Export | 1 | MCP GLB export is a documented stub |
| Godot interoperability | 2 | compatible target format exists only through browser editor |
| Reversibility | 8 | isolated JSON/database design and no runtime requirement |
| Maintainability | 5 | beta tool plus split MCP/browser export path |

Weighted inputs: BO value 4, iteration speed 4, Godot interoperability 2, MCP reliability 3, reversibility 8, maintenance 5.

**PASCAL WEIGHTED SCORE: 4.0/10**

**VERDICT: REJECT for the current BO pipeline.** Retest only after Pascal exposes a reliable MCP-accessible GLB export or Work supplies a browser/editor bridge that can be automated and reproduced.

## Cleanup and follow-up

No addon, Pascal runtime dependency, scene or asset is referenced by BO. Removing `experiments/pascal_mcp/` leaves the canonical project unchanged. Follow-up candidates, not implementation work: watch for headless GLB export; retest stable 1.x rather than silently changing versions; benchmark one opening-width second iteration when export becomes available.

NEW WORK SESSION CAN REPRODUCE PIPELINE: **NO** (current environment cannot complete it)

EXPERIMENTAL DEPENDENCY LEAK: **NONE**

SAFE TO INTEGRATE PASCAL INTO BO PIPELINE: **NO**

CANONICAL GAMEPLAY MODIFIED: **NO**

## Final report fields

- BASELINE HEAD: `7d72ce8bab8dd7a90fc0aff01dc00a497412a750`
- FINAL HEAD: recorded in the branch handoff after this report is committed
- PROTECTED FILE HASHES: **IDENTICAL**
- PASCAL TIME TO FIRST RESULT: **NOT REACHED** (bounded install/connection attempt stopped after about one minute of dependency resolution; full audit remained within budget)
- PASCAL ROUND-TRIP: **FAIL**
- GODOT IMPORT WARNINGS: **N/A — no experimental GLB produced**
- EXPERIMENTAL DEPENDENCY LEAK: **NO**
- NEW PAID ACTIONS: **NONE**
- NEW EXTERNAL ASSETS: **NONE**
- PIPELINE REPRODUCIBLE: **NO**
- FOLLOW-UP CANDIDATES: MCP-accessible GLB export; pinned graphical editor bridge; opening-width A/B round-trip benchmark
