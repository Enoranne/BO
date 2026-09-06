# Work Handoff — PISTE 0 Physical Affordances

## Status
Design prepared. Do not implement until the relevant sprint/beat is authorised.

## Read first
1. `docs/PHYSICAL_AFFORDANCE_LANGUAGE.md`
2. `data/p0_affordance_catalog.json`
3. `docs/OBJECT_INTERACTION_FEEDBACK.md`
4. `docs/INTERACTION_TAXONOMY.md`

Do not infer a requirement to implement every object.

## Core decision
BO uses a small physical verb vocabulary and world-first affordances.

Preferred verbs:
- TAKE;
- OPEN / CLOSE;
- PRESS;
- TURN ON / TURN OFF;
- REVIEW later.

Listening is primarily perceptual, not a generic `LISTEN` button.

## Architecture lock
Preserve composition:

```text
ObjectRoot
├── presentation / collision
├── Interactable or object-specific interaction component
└── RecordableSource when the object genuinely produces capturable sound
```

Do not:
- make every `RecordableSource` interactable;
- make every `Interactable` a collectible;
- put narrative beat IDs into `InteractionContext`;
- put guidance logic into `Recorder`;
- create a universal inventory or inspect system merely for these objects.

## Affordance priority
World signals before UI:
1. silhouette / handle / physical form;
2. placement;
3. motion/state;
4. sound;
5. character attention;
6. framing/light;
7. contextual prompt.

Default presentation must not rely on glowing outlines, exclamation marks or permanent markers.

## Guidance profiles
Same object and same interaction in all profiles.

- `GUIDED`: earlier prompts / clearer hint escalation / optional broader tolerance.
- `NATURAL`: world cue first, prompt when actionable.
- `FREE`: same physical feedback, less interpretation.

FREE must never mean poor usability or missing physical feedback.

## First implementation order after current prototype
Do not implement this order until Sprint 5 has live acceptance.

Recommended sequence:
1. validate current Fisher affordance/feedback live;
2. implement one ordinary authored hinge/toggle prototype;
3. after temporal capture is proven, implement garden gate as first real post-prototype sound-memory interaction;
4. then fridge;
5. tap only later as first sustained-source state object.

## Gate acceptance target
The gate is the first major proof because it should demonstrate:
- understandable handle/latch geometry;
- OPEN/CLOSE state;
- object motion;
- latch + hinge sound;
- coexistence with active REC;
- actual transient timing captured later;
- soft retry if player misses it;
- guidance profile affects explanation only.

## Debug vs production
During implementation Work may expose debug state labels or collision/interaction ranges.
Before production acceptance, validate the interaction with those debug overlays disabled.

## Do not implement now
- physics grabbing;
- interaction wheel;
- generic inventory;
- universal inspection camera;
- dialogue-choice interactions;
- NPC navigation coupling;
- all doors at once;
- all household props at once;
- MK2 control surface;
- Archive Mode UI.

## Validation
Use `tests/static_validate_affordance_design.py` once present in the branch, plus the existing Sprint 5 validation command.
