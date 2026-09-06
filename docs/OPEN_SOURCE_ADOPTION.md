# Open-source adoption policy — Sprint 5

## Principle
External tools may accelerate BO_Ta_Vie, but the project must remain understandable, reversible and maintainable without turning the current prototype into a dependency stack.

## Priority candidates

### 1. Cyclops Level Builder
Purpose: accelerate architectural blocking, walls, openings, room expansion and future house layout.

Adoption rule:
- evaluate first as an editor productivity tool;
- do not rewrite gameplay nodes around it;
- export/bake geometry to ordinary Godot resources where practical;
- preserve existing blocking coordinates for Christmas1982 during the first evaluation.

Decision gate:
Adopt only if it reduces scene-building time while keeping the scene editable and tests stable.

### 2. Phantom Camera
Purpose: evaluate richer fixed/semi-fixed framing and authored camera transitions.

Adoption rule:
- `CinematicCamera` remains the BO-facing contract during evaluation;
- do not spread addon-specific calls through gameplay code;
- any integration should be wrapped or isolated behind a small adapter/presentation layer;
- no camera change may obscure the Fisher pickup or Ronan recording path.

Decision gate:
Adopt only if it creates a clear cinematic benefit over the existing camera with limited integration cost.

### 3. Material Maker
Purpose: author period-appropriate reusable PBR materials.

Adoption rule:
- treat it primarily as a content-authoring tool;
- exported materials/textures should remain standard assets consumable by Godot;
- keep texture resolution and memory budgets appropriate for the prototype.

Decision gate:
Adopt freely for authored materials if exported assets have compatible licensing and remain engine-independent enough to maintain.

### 4. Dialogue Manager
Purpose: future dialogue/conditional narrative layer.

Sprint 5 rule:
Do not integrate yet. Dialogue is out of Sprint 5 scope.

### 5. Godot State Charts
Purpose: possible future high-level narrative/device progression.

Sprint 5 rule:
Do not replace the existing `Recorder` STOP/REC/PLAY state machine. Reconsider only when MK2, Radio Malo or significantly more complex narrative state appears.

### 6. GOAT / other adventure templates
Purpose: architectural reference and pattern library.

Adoption rule:
- study patterns selectively;
- do not wholesale-copy the template into BO;
- audit code and asset licenses separately;
- prefer BO's existing interaction/recorder architecture when the concepts overlap.

## Licensing rule
Before importing code, textures, meshes, audio or other assets:
1. identify the exact license;
2. verify commercial-use compatibility;
3. record attribution obligations if any;
4. distinguish code license from demo/content asset licenses;
5. do not import assets with unclear provenance.

MIT/BSD/Apache-style code is preferred when technically suitable, but every dependency must still be reviewed individually.

## Dependency budget
Sprint 5 should introduce no more than one runtime addon at a time.

Editor-only/content-authoring tools may be evaluated independently because they do not necessarily become runtime dependencies.

## Reversibility contract
Every addon evaluation must be removable without breaking the core loop:

`Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY`

If removing an addon requires rewriting the Recorder, InteractionContext or core player logic, the integration is too invasive for Sprint 5.
