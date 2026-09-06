# Christmas1982 — Material palette

This palette is a reusable visual foundation for the Sprint 5 vertical slice. Values are deliberately restrained and slightly aged; they are not final scanned period materials.

## Core palette

| Material | Intended use | Base character | Roughness target |
|---|---|---|---:|
| `wallpaper_cream` | salon walls / future corridor | warm cream-beige, low saturation | 0.88 |
| `wood_dark_varnished` | furniture / trim | deep warm brown, modest varnish | 0.58 |
| `upholstery_brown_orange` | sofa / fabric accents | muted burnt orange-brown | 0.94 |
| `carpet_muted_brown` | carpet/rug base | desaturated warm brown | 0.98 |
| `floor_dark_warm_brown` | salon floor | deep warm brown, non-glossy | 0.90 |
| `fireplace_stone_warm` | fireplace body / hearth | warm stone-brown | 0.96 |
| `painted_trim_cream` | skirting / painted trim | aged cream paint | 0.86 |
| `ornament_muted_red` | sparse Christmas decoration | muted warm red | 0.78 |
| `plastic_fisher_beige` | Fisher Price body / handle | aged warm beige plastic | 0.82 |
| `plastic_fisher_burgundy` | Fisher Price cassette panel / play button | deep muted burgundy | 0.80 |
| `plastic_fisher_window_dark` | cassette window | dark warm brown-black | 0.68 |
| `plastic_rec_red` | REC button accent | restrained red | 0.76 |

## Rendering rules
- Keep metallic at zero except for explicitly metallic props.
- Prefer high roughness to avoid modern glossy surfaces.
- Use texture/detail maps later; the first pass intentionally uses stable flat materials.
- Avoid pure black and pure white.
- Do not introduce cyan/teal accents into the main environmental palette.
- Practical-light warmth should come primarily from lighting, not by over-saturating every material.
- Hero-object accents such as REC red should remain small enough not to dominate the frame.

## Fisher Price visual hierarchy
The Sprint 5 placeholder should read at a glance as:

1. beige body / handle;
2. burgundy cassette-door area;
3. dark cassette window;
4. small muted-red REC control.

These are presentation cues only. Final brand-accurate industrial design is outside Sprint 5 and should be handled as an authored hero asset later.

## Integration order
1. Apply palette to the existing greybox with no gameplay geometry change.
2. Validate traversal and camera readability.
3. Introduce architectural detail and period props progressively.
4. Replace flat materials with authored Material Maker or asset-native PBR exports only after the palette is visually accepted.
