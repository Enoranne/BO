# Christmas1982 — Visual Vertical Slice Contract

## Purpose
Sprint 5 improves presentation quality without changing the validated gameplay loop. The salon remains the canonical first playable memory.

## Art direction
The visual target is a believable French family interior at Christmas 1982, not a generic retro game room.

Key traits:
- late-1970s / early-1980s domestic architecture and furniture;
- warm tungsten practical lighting;
- amber / burnt-orange palette;
- deep chocolate-brown shadows;
- restrained saturation;
- warm skin and wood tones;
- soft cinematic contrast;
- subtle filmic texture rather than glossy game-engine surfaces;
- readable composition from fixed/semi-fixed cinematic cameras.

## Spatial lock
Preserve the existing composition unless a specific revision is documented:
- fireplace back-left;
- sofa back-center;
- Christmas tree back-right;
- gifts right-center;
- rug and coffee table center;
- Malo starts camera/front side;
- Fisher Price remains associated with the gift area;
- Ronan remains reachable on the first-recording path.

## Visual hierarchy
The player should read the scene in this order:
1. Christmas morning / family warmth.
2. Malo.
3. Fisher Price as the object of desire.
4. Ronan as the first recordable human target.
5. Fireplace/tree practicals as atmosphere rather than gameplay indicators.

## Material palette
Create reusable materials or placeholders for:
- dark varnished wood;
- warm beige/cream painted plaster;
- period wallpaper with restrained geometric/floral motif;
- brown/orange upholstery;
- muted carpet/rug fibres;
- burgundy / beige Fisher Price plastics;
- gift paper/cardboard;
- brass/metal fireplace details;
- slightly aged glass and plastic.

Avoid:
- modern minimalist surfaces;
- excessive metallic/specular response;
- teal/orange blockbuster grading;
- overly clean showroom interiors;
- generic fantasy or US-suburban visual cues when a French domestic cue is available.

## Lighting contract
- Fireplace: dominant warm practical from back-left, soft flicker acceptable.
- Christmas tree: localized warm decorative lights, not a second sun.
- Ambient fill: enough to preserve navigation and facial/silhouette readability.
- No harsh white overhead lighting unless later justified narratively.
- Maintain consistent exposure through the REC/PLAY interaction path.

## Character placeholder target
Malo and Ronan remain temporary assets in Sprint 5, but they should become more readable in silhouette, scale, clothing blocks and age difference.

Do not lock final faces or likenesses yet.

## Cinematography
The existing `CinematicCamera` contract remains authoritative. A third-party camera addon may be tested only if it preserves:
- fixed/semi-fixed authored framing;
- restricted follow around Malo;
- predictable transitions;
- stable gameplay visibility;
- compatibility with blocking markers.

## Completion criterion
Sprint 5 is successful when a short capture of the unchanged first-recording loop looks intentional enough to communicate the game's identity without explanatory text.
