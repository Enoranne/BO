# Christmas1982 — Character Art Direction

## Purpose
Define the production-facing visual target for Malo and Ronan before replacing the procedural `PlaceholderHumanoid3D` rigs.

This document does not authorize a final character replacement during Sprint 5. It exists so future modelling / Higgsfield / Blender / Godot work shares the same target.

## Shared visual rules
- France, Christmas 1982.
- Naturalistic family clothing; no costume-shop nostalgia.
- Warm, slightly muted palette compatible with tungsten / Kodak 500T-inspired grading.
- No modern streetwear silhouettes, synthetic neon accents, oversized contemporary sneakers or current hairstyles.
- Characters must remain readable under the fixed/semi-fixed salon camera at medium distance.
- Realistic human proportions with a lightly authored narrative-game stylisation; avoid bobble-head/cartoon proportions.
- Clothing and hair should respond well to warm practical lighting and deep brown shadows.

## Malo — age 6

### Narrative read
Curious, observant, inventive, physically smaller than the world around him. The player should read **attention and curiosity** before heroism.

### Body / silhouette
- target apparent height: ~1.15–1.22 m;
- child proportions, relatively larger head than Ronan but still realistic;
- narrow shoulders;
- short arms/legs appropriate to age;
- slightly compact silhouette that contrasts with furniture and the Fisher Price;
- hands must remain readable enough to carry / manipulate the recorder later.

### Face / hair
- expressive eyes and brows more important than facial micro-detail;
- warm fair/medium skin range compatible with existing visual target;
- medium/dark brown hair;
- practical early-80s child haircut, slightly imperfect rather than styled;
- no adult facial sharpness.

### Clothing direction
Primary target:
- warm rust / ochre / brown knit or long-sleeve top;
- muted brown trousers / corduroy-like read;
- dark simple indoor shoes / slippers or socks depending final scene choice.

Material language:
- wool/cotton/corduroy;
- high roughness;
- no glossy technical fabric.

### Animation/personality notes for later
- gaze frequently drawn to objects rather than camera;
- recorder carried with concentration;
- small hesitation before pressing controls;
- quick curiosity movements balanced by quiet listening moments.

## Ronan — older brother

### Narrative read
Clearly the older brother before the player knows his name. More physically assured, slightly more socially aware, and visually distinct from Malo.

### Age / scale relationship
Current prototype uses a strong stature gap. Production target should preserve a believable sibling difference.

Suggested apparent target:
- age: roughly 9–11 for Christmas1982 unless narrative continuity later locks a more precise age;
- height: ~1.35–1.48 m;
- visibly taller and longer-limbed than Malo;
- narrower head-to-body ratio than Malo.

Do not finalise exact age/height from this planning document alone if the film/novel continuity later gives a stronger canonical value.

### Face / hair
- family resemblance to Malo without making them twins;
- slightly more defined face;
- dark brown hair;
- more controlled expression;
- visually plausible as the brother relatives might perceive as the conventionally more handsome child, but keep the distinction subtle and naturalistic rather than idealised.

### Clothing direction
Primary target:
- muted blue-grey / petrol-blue knit or shirt layer;
- charcoal / dark brown trousers;
- restrained warm accents if needed to integrate with salon palette.

This cool-neutral clothing difference gives Ronan immediate silhouette separation from Malo without introducing teal grading.

## Malo vs Ronan readability test
From the locked Christmas1982 camera, a player should identify them without labels through:

1. height;
2. body proportions;
3. clothing colour family;
4. stance / animation;
5. blocking.

Face detail is secondary at this camera distance.

## LOD / technical target for first authored characters
Until performance profiling exists, favour moderate complexity:

- one skinned body mesh per character where practical;
- separate hair allowed;
- small number of material slots;
- 2K textures are more than sufficient for the first vertical slice;
- prioritise silhouette, deformation and face over hidden clothing micro-detail;
- retain clean origins / metre scale / Godot-compatible skeleton naming.

## Replacement protocol
When authored characters become available:

1. open `CharacterReadabilityPreview.tscn`;
2. compare placeholder vs candidate at identical camera distance;
3. validate apparent age and sibling hierarchy;
4. validate warm-light response;
5. validate silhouette from back / three-quarter view because the player often sees Malo from third person;
6. only then test the candidate inside `Christmas1982_VisualSlice.tscn`;
7. do not modify MaloController or interaction logic to accommodate art assets.

## Do not solve yet
- facial performance system;
- dialogue lip sync;
- production hair simulation;
- cloth simulation;
- full animation state machine;
- NPC AI;
- final likeness lock.
