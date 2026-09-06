# Sprint 5+ — 1982 asset backlog

## Purpose
Prioritise production art for BO so every imported/generated asset improves the playable Christmas1982 slice or prepares a clearly identified next zone.

This is an art-production backlog, not permission to batch-generate assets. Higgsfield generation/import remains opt-in and must respect credit constraints.

## Asset quality rules
Every candidate should be checked for:

- believable metre scale;
- clean orientation and origin;
- reasonable mesh density for its screen importance;
- portable PBR materials where possible;
- no required runtime plugin;
- easy replacement in Godot;
- licensing/provenance recorded when sourced externally;
- period credibility for late 1970s / early 1980s France;
- no unnecessary contemporary design language.

Triangle counts below are **review ranges, not hard budgets**. Silhouette and import cleanliness matter more than arbitrary numbers.

## P0 — Christmas1982 hero/readability assets
These directly affect the first 2–3 playable minutes.

### Coffee table
Current state: procedural placeholder + Higgsfield GLB technical candidate.

Target:
- low rectangular domestic table;
- dark warm wood / veneer;
- rounded or softened edges preferred over ultra-modern sharp minimalism;
- candidate review range: ~2k–15k triangles.

Acceptance: must read better than `Set/CoffeeTablePlaceholder` from the locked camera.

### Sofa
Target:
- 1970s/early-80s family sofa;
- brown / burnt-orange upholstery;
- soft, lived-in proportions;
- cushions separable if possible;
- candidate review range: ~5k–25k triangles.

### Fireplace surround / mantel
Target:
- warm stone/brick/plaster domestic fireplace;
- visually anchors back-left corner;
- should support practical fire glow rather than become a hero object itself.

### Christmas tree
Target:
- believable natural silhouette;
- sparse period decorations;
- avoid glossy commercial showroom look;
- ornaments should remain secondary to Fisher/Malo/Ronan readability.

### Fisher Price recorder proxy
Target:
- beige body + muted burgundy cassette-door language;
- readable handle and cassette window;
- generic/non-branded production version preferred unless legal/art direction later explicitly approves trademarked detail;
- hero-object mesh can be denser than ordinary props.

Important: this asset must never own Recorder logic. It replaces presentation only.

### Rug / carpet
Target:
- muted brown/orange period textile;
- enough surface variation to stop the floor feeling flat;
- no extreme high-frequency pattern that competes with characters.

## P1 — salon depth / domestic credibility

### Floor or table lamp
Warm practical light source; period shade and base.

### Sideboard / low cabinet
Useful for wall depth and future cassette/record storage.

### Curtains / window treatment
Only after window architecture is defined. Heavy warm textile is preferable to modern blinds.

### Gift boxes / wrapping
Varied silhouettes, period-appropriate muted wrapping rather than saturated modern graphics.

### Small domestic clutter set
Books, ashtray-free neutral décor, bowl, family-photo frames without identifiable real people, magazines/newspapers with non-readable placeholder print.

## P2 — kitchen glimpse
Only produce after the 5.4 doorway/kitchen-glimpse shell is accepted.

### Refrigerator
Period silhouette, off-white/cream, mechanically plausible door and handle.

### Kitchen cabinetry
Warm laminate/wood tones; modular so Work can resize the room without remodelling everything.

### Coffee maker / kettle
High sonic-value prop for future recording mechanics.

### Table + chairs
Simple family kitchen furniture, not design-showroom pieces.

### Sink / tap / dishes
Useful both visually and later acoustically.

## P3 — bedroom / creative identity
Produce only after interior topology is stable.

- construction bricks / toys;
- cassette cases;
- cassette storage boxes;
- school desk / writing surface;
- pencil/paper clutter;
- turntable / record player if retained in final narrative continuity;
- record sleeves with original/generic artwork;
- books;
- tape-repair tools and simple stationery.

## P4 — garden / exterior micro-hub

- swing / portique;
- large tree;
- improvised treehouse/cabin pieces;
- metal gate;
- garden chairs / simple outdoor clutter;
- gravel/grass/leaf material set;
- neighbour/street boundary elements.

## Hero-vs-background rule
Before spending production time or credits, classify the candidate:

- **Hero** — player handles it or narrative focuses on it: Fisher, later MK2.
- **Gameplay landmark** — player repeatedly navigates/records near it: gate, fridge, tree/cabin.
- **Set anchor** — defines a room composition: sofa, fireplace, kitchen cabinetry.
- **Background** — fills credibility only: minor décor and clutter.

Use highest visual fidelity only for Hero and major Gameplay Landmark assets.

## Source strategy
Preferred order per asset:

1. reuse/improve native Godot placeholder if it already reads well enough;
2. evaluate a clean existing catalog/CC0/open-source asset with recorded licence;
3. use Higgsfield 3D Jutsu/catalog if it materially improves speed/quality and credit impact is understood;
4. custom model only when the asset is truly distinctive to BO.

## Sprint 5 discipline
Do not turn this backlog into a shopping list. The current proof order remains:

1. validate 5.2 Visual Slice;
2. validate one coffee-table GLB round trip;
3. validate 5.4 architectural shell;
4. then choose the next **one** P0 asset with the highest visual impact.
