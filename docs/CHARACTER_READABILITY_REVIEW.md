# Sprint 5.2 — Malo / Ronan readability review

## Purpose
Evaluate the current procedural placeholders as **blocking/readability tools**, not as final character art.

Open:

`res://scenes/piste_0/christmas_1982/CharacterReadabilityPreview.tscn`

The scene presents Malo and Ronan side by side with the same current proportions and colours used by Christmas1982.

## Questions to answer in Work / Godot

### 1. Age / hierarchy read
- Does Malo immediately read as the younger child?
- Does Ronan read as the older brother without looking adult-sized?
- Is the current 1.45 vs 1.68 stature difference believable in the game camera language?

### 2. Silhouette read
- Can the two characters be distinguished at medium distance without labels?
- Do head/torso/limb proportions feel too toy-like, too blocky or acceptable for the current prototype stage?
- Does the facing marker/nose provide enough directionality?

### 3. Colour separation
- Malo: warm ochre/brown family.
- Ronan: muted blue/charcoal family.

The two should remain distinguishable under warm tungsten lighting. If Ronan's blue collapses to grey or Malo blends into the sofa/walls, adjust presentation colours before changing geometry.

### 4. Movement readability
The preview disables gait for comparison. In Christmas1982, verify separately that Malo's procedural walk does not look comical enough to undermine the narrative tone.

### 5. Camera-scale read
From the canonical cinematic camera:
- Malo must remain visible against rug/floor;
- Ronan must remain visible near the recording position;
- neither should require an outline shader or floating name label in the production presentation.

## Decision ladder
Make changes in this order only:

1. lighting / background separation;
2. clothing colours;
3. silhouette proportions;
4. procedural mesh refinement;
5. only then replacement with authored character assets.

Do not jump directly to final characters before confirming the gameplay scale and camera composition.

## Acceptance for Sprint 5
The placeholders are acceptable for Sprint 5 if:

- Malo/Ronan are instantly distinguishable;
- their relative age/height reads correctly;
- they remain legible in the Visual Slice lighting;
- no debug label is necessary during normal play;
- their temporary nature does not block evaluation of Fisher/Recorder gameplay.

Final likeness, facial animation, clothing detail and production rigging are explicitly outside Sprint 5.
