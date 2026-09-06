# Christmas1982 — P0 Asset Briefs

## Purpose
Define what the highest-priority visual assets must accomplish before any modelling or Higgsfield generation is approved.

Priority rule: an asset earns P0 status only if it is highly visible, narratively important, or critical to the first-recording path.

## 1. Fisher Price recorder — highest priority

### Narrative role
The object that starts Malo's relationship with sound. It must read as **special, tactile and child-scaled** without looking like a generic prop box.

### Visual target
- aged warm beige plastic body;
- deep burgundy cassette/control face;
- clear cassette window;
- chunky child-friendly transport controls;
- carry handle;
- modest wear and moulded-plastic seams;
- no pristine modern product-render gloss.

### Approximate first-pass envelope
Use the existing prototype envelope as a gameplay reference, not as a product-accurate final measurement:
- width ~0.85 m in current placeholder is intentionally oversized for readability and will likely need reduction after real asset validation;
- production candidate must be checked against Malo's six-year-old hands/body and against the locked camera.

### Functional requirements
- separate visual areas for beige body, burgundy panel/window and REC indicator where possible;
- origin sensible for placement and carrying;
- orientation obvious;
- can be instanced as world prop and carried prop without changing Recorder logic;
- no built-in gameplay scripts.

### Acceptance
Must be immediately recognisable as Malo's recorder from the locked camera before labels appear.

## 2. Sofa

### Narrative role
Primary family-room anchor and major colour mass in the frame.

### Visual target
- late-70s / early-80s family sofa;
- brown / burnt-orange upholstery;
- practical, slightly bulky proportions;
- fabric, not glossy leather unless later references justify it;
- lived-in rather than showroom-perfect;
- three cushions acceptable but avoid excessive decorative styling.

### Approximate envelope
Current placeholder:
- width ~3.3 m;
- depth ~1.1–1.25 m;
- visual back height roughly 1.15 m above local base.

A production sofa can be modestly smaller, but the locked composition must retain the same visual mass.

### Functional requirements
- collision can remain a simple proxy;
- player does not need to sit during Sprint 5;
- material slots should remain few and stable.

## 3. Fireplace

### Narrative role
Dominant warm practical and spatial landmark. It grounds the Christmas family-memory identity.

### Visual target
- plausible French domestic fireplace / surround for the period;
- warm stone, brick or plaster/stone combination;
- dark firebox opening;
- mantel shelf with enough depth for later small props;
- no luxury château language unless later visual references demand it.

### Approximate envelope
Current main block:
- width ~2.35 m;
- height ~2.25 m;
- depth ~0.62 m;
- hearth extends to ~2.8 m width.

### Functional requirements
- separate fire opening from surround;
- simple collision proxy sufficient;
- lighting remains owned by Godot, not embedded in the mesh.

## 4. Christmas tree

### Narrative role
Secondary visual anchor opposite the fireplace and source of warm domestic sparkle.

### Visual target
- natural tree rather than perfect modern cone;
- modest family decoration;
- sparse warm incandescent-style string-light feeling;
- muted red / cream / simple ornaments;
- slightly uneven branches improve authenticity.

### Approximate envelope
Current placeholder visual height ~2.9 m including collision volume. Production target may be around 2.1–2.5 m depending camera review.

### Functional requirements
- trunk/foliage can be separate;
- ornaments/lights can remain separate lightweight instances;
- no expensive foliage simulation required;
- collision should be simple and conservative.

## 5. Coffee table

### Narrative role
Central foreground depth cue and first Higgsfield round-trip test.

### Current target envelope
- width: 2.15 m;
- height: 0.65 m;
- depth: 1.08 m.

These dimensions derive from the current placeholder and exist to compare scale; they are not sacred production dimensions.

### Visual target
- dark warm varnished wood;
- simple late-70s / early-80s domestic design;
- avoid contemporary Scandinavian minimalism if it reads too modern;
- broad enough to remain a strong composition element.

### Pipeline rule
`BO_CoffeeTable_Test` from Higgsfield is only a technical candidate. Do not approve it until:
- dimensions are inspected;
- material compatibility is checked;
- provenance/licensing status is acceptable;
- it looks period-correct in Godot.

## 6. Gift pile / wrapping

### Narrative role
Guides the eye toward the Fisher Price and sells Christmas without text.

### Visual target
- period-plausible paper;
- muted red, cream, brown/kraft and restrained patterned options;
- ribbons optional;
- several box sizes and imperfect wrapping;
- no glossy contemporary luxury packaging.

### Functional requirements
- mostly static;
- no individual collision needed for Sprint 5;
- one or two later interaction-ready gift props may be separated if narrative use appears.

## Shared technical rules
For P0 props:

- metre scale;
- Y-up / Godot-friendly import orientation;
- clean origin;
- portable PBR materials;
- low material-slot count;
- no runtime dependency on authoring software;
- collision authored separately in Godot unless the source mesh provides a clearly suitable simple proxy;
- no hidden gameplay logic embedded in imported scenes;
- source/provenance/license status recorded before production approval.

## Production order
1. Fisher Price
2. sofa
3. fireplace
4. Christmas tree
5. coffee table candidate validation
6. gift pile

The order may change only after live camera review demonstrates a different screen-impact priority.
