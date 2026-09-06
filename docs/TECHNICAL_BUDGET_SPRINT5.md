# Sprint 5 — Provisional Technical Budget

## Purpose
Prevent visual upgrades and imported/generated assets from becoming disproportionately heavy before BO has real performance profiling.

These are **guardrails, not final optimisation targets**. Live Godot profiling may revise them.

## General target
The Christmas1982 vertical slice should stay deliberately light enough to iterate quickly on ordinary development hardware.

Optimisation priorities:
1. stable frame pacing;
2. fast scene load / import iteration;
3. clean asset replacement;
4. visual readability;
5. only then micro-detail.

## Character budget — first authored pass
Per character target:
- visible body + clothing + hair: roughly 25k–60k triangles preferred;
- hard warning above ~100k triangles before profiling;
- 1–3 primary material slots preferred;
- 2K texture set sufficient for vertical slice;
- normal/roughness maps only where they visibly improve the locked-camera result;
- no real-time cloth/hair simulation in Sprint 5.

Malo and Ronan should spend geometry on silhouette, hands and face before hidden clothing detail.

## Hero prop — Fisher Price
Preferred first-pass target:
- ~5k–25k triangles;
- 2–4 material roles max: beige body, burgundy control face, dark/transparent window, small indicator/accent;
- 1K–2K textures sufficient;
- no geometry for invisible internal cassette mechanisms unless later close-ups justify it.

Because the Fisher Price is carried and narratively central, it may exceed ordinary prop budget if live review proves the detail visible.

## Large furniture / architectural props
Sofa, fireplace, table:
- ~3k–30k triangles each depending silhouette complexity;
- prefer 1–3 material slots;
- 1K–2K textures;
- simple Godot collision proxies rather than mesh collision where possible.

## Secondary props
Gifts, dishes, toys, books, cassette cases:
- typically hundreds to low thousands of triangles;
- atlas/reuse materials where practical;
- repeated objects should prefer instancing/shared meshes;
- no unique 2K/4K material set for every small prop.

## Christmas tree
The tree can become expensive quickly.

Sprint 5 target:
- favour a moderate authored mesh or grouped branch cards/geometry;
- avoid per-needle geometry;
- use lightweight repeated ornaments;
- lights are visual accents, not dozens of shadow-casting real lights;
- only a small number of actual light sources should illuminate the room.

## Texture budget
Default hierarchy:
- hero character / hero recorder: up to 2K where useful;
- large furniture: 1K–2K;
- medium props: 1K;
- small props: 512–1K / atlases;
- 4K requires a demonstrated locked-camera need.

## Materials
Prefer:
- portable PBR;
- restrained shader complexity;
- shared material roles;
- high roughness appropriate to aged domestic surfaces.

Avoid during Sprint 5:
- layered procedural runtime materials merely for micro-detail;
- expensive transparency on large overlapping surfaces;
- many unique shader variants;
- imported Blender-only shader networks that do not survive GLB.

## Lighting budget
Christmas1982 currently relies on a small motivated hierarchy:
- fireplace practical/key;
- tree practical;
- soft fill.

Rule:
- preserve a small number of meaningful real lights;
- decorative tree bulbs do not each become shadow-casting OmniLight3D nodes;
- prefer emissive appearance / baked-looking decorative detail for many tiny bulbs;
- profile shadows before adding more shadowed lights.

## Audio budget
The project is sound-centric, but that does not require all sounds to be resident simultaneously.

Initial guidelines:
- mono where spatial source character permits;
- stereo for room tones / deliberately wide ambience;
- lossless WAV source masters may be retained outside runtime packaging strategy;
- runtime import/compression choice should be made in Godot after listening tests;
- loop points must be clean for ambience;
- avoid dozens of always-playing AudioStreamPlayer3D nodes before the zone becomes playable.

## Higgsfield / external asset intake gate
Before any imported asset becomes production-approved, record:
- dimensions;
- triangle/vertex count;
- material count;
- texture count and maximum resolution;
- animation/skeleton presence if applicable;
- provenance / license status;
- Godot import result;
- whether simpler authored geometry would achieve the same locked-camera result.

## Performance review points
Work/Godot should establish real measurements after:
1. Visual Slice 5.2 opens successfully;
2. first authored/imported prop is placed;
3. first authored character candidate is placed;
4. Cyclops shell is tested;
5. first dense kitchen/garden area becomes playable.

Until then, these budgets favour conservative iteration over premature high-detail production.
