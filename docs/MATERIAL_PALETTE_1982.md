# Christmas1982 — Material palette

This palette is a reusable visual foundation for the Sprint 5 vertical slice. Values are deliberately restrained and slightly aged; they are not final scanned period materials.

## Core palette

| Material | Intended use | Base character | Roughness target |
|---|---|---|---:|
| `wallpaper_cream` | salon walls / future corridor | warm cream-beige, low saturation | 0.88 |
| `wood_dark_varnished` | furniture / trim | deep warm brown, modest varnish | 0.58 |
| `upholstery_brown_orange` | sofa / fabric accents | muted burnt orange-brown | 0.94 |
| `carpet_muted_brown` | carpet/rug base | desaturated warm brown | 0.98 |
| `plastic_fisher_beige` | Fisher Price body | aged warm beige plastic | 0.82 |
| `plastic_fisher_burgundy` | Fisher Price cassette panel | deep muted burgundy | 0.80 |

## Rendering rules
- Keep metallic at zero except for explicitly metallic props.
- Prefer high roughness to avoid modern glossy surfaces.
- Use texture/detail maps later; the first pass intentionally uses stable flat materials.
- Avoid pure black and pure white.
- Do not introduce cyan/teal accents into the main environmental palette.
- Practical-light warmth should come primarily from lighting, not by over-saturating every material.

## Integration order
1. Apply palette to the existing greybox with no geometry change.
2. Validate traversal and camera readability.
3. Introduce architectural detail and period props progressively.
4. Replace flat materials with authored Material Maker exports only after the palette is visually accepted.
