# BO — Domestic Interaction Taxonomy

## Purpose
Prepare future household interactions without expanding Sprint 5 gameplay or coupling the existing Recorder loop to object-specific code.

The current architecture already provides two intentionally separate contracts:

- `Interactable` — player action / prompt / priority;
- `RecordableSource` — sound capture source / metadata / priority.

Keep them separate.

## Core composition rule
A household object that is both manipulable and recordable should normally be composed as:

```text
ObjectRoot (Node3D)
├── Visual / collision
├── InteractionArea (Interactable or specialised subclass)
├── SoundSource (RecordableSource)
└── Audio / animation presentation helpers
```

Do **not** force `RecordableSource` to inherit from `Interactable`, or vice versa, merely because one prop needs both behaviours.

This avoids multiple-inheritance pressure and keeps Recorder logic independent from doors, taps, cupboards, toys, etc.

## Interaction archetypes

### A. Take / collect-equipment
Current example: Fisher Price.

Characteristics:
- typically one meaningful interaction in a scene;
- interaction disables or changes state after success;
- may equip a capability rather than enter a generic inventory.

Examples:
- Fisher Price;
- future MK2 acquisition.

Sprint 5 rule: do not generalise this into an inventory system.

### B. Toggle / hinge
State alternates between two readable physical states.

Examples:
- room door open/close;
- cupboard door;
- fridge door;
- garden gate;
- French door.

Prompt should reflect current state:
- `Open fridge`
- `Close fridge`

The object owns its physical state. HUD does not.

### C. Momentary action
A short action triggers presentation/audio and returns naturally.

Examples:
- press cassette button;
- light switch;
- flush;
- doorbell;
- tap a toy;
- knock on a surface.

Avoid unnecessary persistent state when the physical action does not need one.

### D. Continuous / held action — later only
Player sustains an action while input remains held.

Potential examples:
- running tap;
- winding / mechanical toy;
- holding a microphone close to a source in a later system.

Do not implement a generic hold framework in Sprint 5. Add only when a real interaction requires it.

### E. Multi-state domestic prop — later
More than two states with meaningful presentation.

Examples:
- television off / channel / volume state;
- cassette deck STOP / REC / PLAY;
- future MK2 controls.

Use a dedicated state owner for the prop. Do not overload generic `Interactable` with device-specific state machines.

### F. Inspect / observe — later if needed
Non-manipulative close attention.

Examples:
- cassette label;
- handwritten sound list;
- photograph;
- record sleeve.

Do not add an inspect-camera system until actual authored content justifies it.

## Recordable sound relationship
Interaction and sound capture can happen in several patterns.

### Passive source
Sound exists without player manipulating the object.

Examples:
- refrigerator hum;
- fireplace;
- Ronan voice;
- wind.

Use `RecordableSource` without requiring an `Interactable`.

### Triggered source
Interaction creates a short sound that can be recorded.

Examples:
- gate squeak;
- cupboard close;
- fridge seal;
- door latch.

Preferred architecture:
- Interactable/object state triggers audio presentation;
- sibling/child `RecordableSource` exposes the appropriate capture stream/metadata;
- Recorder remains unaware of the object's state machine.

### Continuous source
Object state enables a sustained recordable sound.

Examples:
- running tap;
- refrigerator compressor cycle;
- television.

Preferred architecture:
- object owns on/off state;
- RecordableSource's enabled/stream presentation follows object state through a small adapter/presentation script;
- InteractionContext still selects the source generically.

## Priority policy
Current `InteractionContext` resolves priority first, then distance.

Recommended provisional interaction priority bands:

- `100+` — critical onboarding / explicit current beat, used sparingly;
- `50–99` — strong contextual action close to player;
- `10–49` — ordinary domestic interaction;
- `0–9` — low-priority optional interaction;
- negative — intentionally de-emphasised fallback.

Do not solve poor scene layout by continuously increasing priorities. Spatial readability should remain primary.

Recordable-source priority should follow the same philosophy independently.

## Prompt language
Keep prompts short, physical and verb-led.

Preferred:
- `Take Fisher Price`
- `Open fridge`
- `Close gate`
- `Turn tap on`
- `Turn tap off`
- `Press play`

Avoid:
- lore sentences;
- controller-specific text embedded inside object prompts;
- duplicated `[E]` / key names inside `Interactable` strings.

The HUD owns how the action binding is communicated (`E / click`, etc.). The object owns only the semantic verb phrase.

## Sound metadata
Future `RecordableSource.source_metadata` can carry non-gameplay descriptive tags such as:

- zone;
- object category;
- material;
- memory association;
- indoor/outdoor;
- family member;
- source variant.

Do not make progression logic depend on arbitrary metadata keys until a dedicated system is designed.

## First future implementation candidates
After Sprint 5 acceptance, the best low-risk domestic interaction tests are:

1. **gate open/close + squeak** — iconic and mechanically simple;
2. **fridge open/close + hum/seal** — combines state and passive/triggered sound;
3. **tap on/off + running water** — first continuous-source experiment.

Implement only one archetype at a time and preserve the validated Ronan recording loop.

## Explicitly deferred
- inventory framework;
- interaction wheel;
- item combining;
- physics grabbing;
- generic inspect mode;
- scripted quest triggers inside Interactable;
- NPC conversation system;
- door/navigation AI coupling;
- MK2 control surface.
