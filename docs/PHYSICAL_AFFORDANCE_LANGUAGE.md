# BO_Ta_Vie — Physical Affordance Language

## Status
Design only. No new interaction implementation is authorised during Sprint 5.

## Goal
Make important objects understandable through their physical presence before the HUD explains them.

BO should not feel like a room full of invisible interaction hotspots. The player should usually understand that an object may matter because of one or more of these cues:

1. **shape / silhouette**;
2. **material and wear**;
3. **placement**;
4. **motion / state**;
5. **sound**;
6. **character attention**;
7. **light / framing**;
8. **contextual prompt** — last resort, not first language.

The interaction system may remain proximity-based. The world itself must carry most of the semantic load.

---

# Affordance layers

## A0 — ambient readability
The object is visible and believable but not calling for interaction.

Examples:
- sofa;
- lamp;
- decorative books;
- ordinary dishes.

No prompt should appear merely because the player passes nearby.

## A1 — suggestive
The object has a reason to attract curiosity but does not demand action.

Possible cues:
- recognisable handle;
- moving hinge;
- audible hum;
- unusual wear;
- family member glancing at it;
- sound source spatialisation.

Examples:
- fridge hum;
- gate squeak heard from garden;
- cassette boxes on a shelf.

## A2 — actionable
The object is close enough and in a valid state for an immediate action.

At this point a contextual prompt may appear depending on guidance profile.

Examples:
- `Take Fisher Price`;
- `Open gate`;
- `Open fridge`;
- `Turn tap on`.

## A3 — beat-relevant
The object is currently important to a narrative or sound beat.

Use stronger but still diegetic emphasis:
- sound repetition;
- character glance/movement;
- slight lighting/composition advantage;
- animation/state change;
- earlier contextual prompt in GUIDED mode.

Do not add glowing outlines by default.

---

# Primary player verbs

Keep the verb vocabulary small.

## TAKE
Acquire/equip a meaningful device.

Current canonical use:
- Fisher Price.

Future:
- MK2 transition.

Do not generalise TAKE into a universal inventory pickup.

## OPEN / CLOSE
Physical hinge/toggle.

Examples:
- gate;
- fridge;
- door;
- cupboard.

Opening and closing should produce different physical/sound consequences when appropriate.

## PRESS
Momentary device control.

Examples:
- Fisher REC / STOP / PLAY;
- later MK2 controls.

A press must feel tactile through animation + mechanical sound, not only UI feedback.

## TURN ON / TURN OFF
Persistent source state.

Examples:
- tap;
- television later;
- lamp if narratively useful.

## LISTEN / NOTICE
Usually not a literal button.

BO should let listening happen through player attention, position and playback rather than a generic `LISTEN` action on every source.

## REVIEW
Future physical cassette-memory action.

Prefer world-space cassette/box interaction before a full-screen media library.

## INSPECT
Deferred.

Do not add a universal inspection-camera mode until actual authored objects justify it.

---

# Prompt hierarchy

Prompts should clarify an already plausible action rather than reveal a completely hidden possibility.

Preferred semantic prompts:
- `Take Fisher Price`
- `Open gate`
- `Close gate`
- `Open fridge`
- `Close fridge`
- `Turn tap on`
- `Turn tap off`

Do not put control bindings inside object-owned prompt strings.
The HUD owns `E`, click, controller icon, etc.

---

# Guidance profiles and affordance visibility

## GUIDED
- prompt may appear earlier within interaction range;
- beat-relevant object may receive stronger sound repetition or composition support;
- short explicit hint permitted after confusion;
- timing tolerance may be wider.

## NATURAL — default
- world cue first;
- prompt only when close/actionable;
- no persistent marker;
- ordinary timing tolerance.

## FREE
- strongest reliance on world cues;
- prompt delayed until very close or after deliberate proximity;
- no interpretive objective text by default;
- same object states and same underlying interactions.

The guidance mode must never change which objects fundamentally exist or which memories are narratively valuable.

---

# Interaction feedback stack

A successful physical action should normally communicate through at least two channels.

Examples:

### Gate opens
1. hand/object motion;
2. hinge/latch sound;
3. changed silhouette/open path.

### Fisher REC starts
1. physical button travel / device state;
2. transport click;
3. REC lamp;
4. optional compact HUD state.

### Fridge opens
1. door rotation;
2. seal release;
3. interior light / acoustic change;
4. hum becomes spatially clearer.

Avoid actions where the only feedback is a text label changing.

---

# Pre-action, action, consequence

Important BO interactions should be thought of as a short physical sentence:

`PRE-CUE -> ACTION -> PHYSICAL CONSEQUENCE -> SONIC CONSEQUENCE -> OPTIONAL MEMORY CONSEQUENCE`

Example — gate:
- PRE-CUE: distant squeak / visible handle;
- ACTION: open;
- PHYSICAL: gate rotates;
- SONIC: latch + hinge squeak;
- MEMORY: if REC was active, the actual transient becomes part of the recording.

This is preferable to an abstract `collect gate sound` command.

---

# No universal highlight language

Do not default to:
- glowing yellow outlines;
- pulsing icons over every prop;
- floating exclamation marks;
- permanent interaction dots;
- minimap markers.

A subtle accessibility highlight option may be considered later, but it must be opt-in and separate from the default art direction.

---

# Object state readability

An object should visually communicate whether repeating the same verb still makes sense.

Examples:
- open gate -> prompt becomes `Close gate`;
- running tap -> prompt becomes `Turn tap off`;
- Fisher equipped -> world Fisher no longer behaves as a placed pickup;
- cassette already reviewed -> physical placement/label reflects its annotation state later.

The object owns this state. The HUD reflects it.

---

# Distance bands

These are design concepts, not fixed engine constants.

## PERCEPTUAL
Player can hear/see the object but cannot act yet.

Purpose: anticipation and navigation.

## CONTEXTUAL
Player is close enough for the object to become a candidate in `InteractionContext`.

Purpose: action availability.

## INTIMATE
Very close positioning may expose extra tactile detail or stronger sound perspective.

Purpose: reward curiosity without requiring a new inspect system.

Do not create three separate interaction frameworks for these bands. They are presentation/readability rules.

---

# Priority objects

## Fisher Price
Affordance identity:
- chunky beige/burgundy object;
- large mechanical controls;
- gift placement;
- tactile button sounds;
- REC light;
- carried state after pickup.

Core verbs:
- TAKE;
- PRESS through dedicated Recorder controls.

Sprint 5 status:
- TAKE and Recorder controls already exist at prototype level;
- visual/tactile treatment still requires live validation.

## Gate
Affordance identity:
- visible handle/latch;
- recognisable hinge geometry;
- distinctive squeak;
- partial view beyond garden.

Core verbs:
- OPEN / CLOSE.

Narrative value:
- first recommended temporal-capture micro-quest after current prototype.

## Fridge
Affordance identity:
- handle;
- compressor hum;
- interior light when open;
- Mother nearby/contextual reactions.

Core verbs:
- OPEN / CLOSE.

Narrative value:
- experimentation + comic escalation.

## Tap
Affordance identity:
- handle/knob;
- water source;
- bathroom acoustic resonance.

Core verbs:
- TURN ON / TURN OFF.

Narrative value:
- first sustained recordable-source state experiment.

## Cassette / cassette box
Affordance identity:
- label;
- handwritten marks;
- physical pile/box placement;
- plastic handling sounds.

Core verbs later:
- REVIEW / PLAY / CLASSIFY through a physical memory surface.

Do not make every loose cassette a generic pickup collectible.

## Fireplace
Affordance identity:
- light flicker;
- crackle;
- Father's routine;
- warmth/composition.

Core default verb:
- none for Malo initially.

Important lesson:
A meaningful sound source does not need to be interactable.

---

# Implementation philosophy for Work

When an affordance is implemented later:
1. preserve generic `Interactable` / `RecordableSource` contracts;
2. create object-specific state only where the physical prop truly needs it;
3. make presentation react to state;
4. keep guidance as an observer/presentation layer;
5. keep narrative beat IDs outside `Recorder` and `InteractionContext`;
6. validate the interaction without HUD first where possible;
7. add HUD support only after physical readability exists.

The best interaction is one the player understands before reading the prompt.
