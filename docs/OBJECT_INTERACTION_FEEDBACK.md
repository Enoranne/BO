# BO_Ta_Vie — Object Interaction Feedback Contract

## Status
Design only. Future interaction-quality contract.

## Goal
Every meaningful physical interaction should be readable before, during and after the action without depending on a large HUD message.

## The 4-step feedback rule
For authored interactions, evaluate four moments:

1. **INVITATION** — why might the player try this?
2. **COMMIT** — did the input register?
3. **PHYSICAL RESULT** — what changed in the world?
4. **MEMORY RESULT** — did the action create or alter something worth hearing/remembering?

Not every interaction needs a memory result, but every interaction needs a clear physical result.

---

# Feedback channels

## Motion
Preferred first feedback for physical objects.

Examples:
- gate rotates;
- fridge door opens;
- Fisher button depresses;
- tap handle moves.

Motion should start quickly enough that input feels acknowledged.

## Sound
Core BO feedback channel.

Use object-specific mechanical/material sound rather than generic UI confirmation.

Examples:
- latch click;
- transport clunk;
- seal release;
- water start;
- cassette case snap.

Avoid synthetic `success` chimes for ordinary interactions.

## Light/state
Useful when physically plausible.

Examples:
- Fisher REC lamp;
- fridge interior light;
- television power state later.

Do not turn every interactable into a glowing object.

## Character reaction
Use selectively.

Examples:
- Mother glances after repeated fridge openings;
- Ronan reacts to REC;
- Father looks toward unusual sound.

Character reaction is narrative feedback, not required for every action.

## HUD
Last support layer.

HUD should communicate:
- available semantic action;
- current Recorder state;
- temporary explicit hint in GUIDED mode.

HUD should not compensate permanently for unreadable physical design.

---

# Timing feel

These are provisional feel targets, not engine-locked constants.

## Immediate input acknowledgement
Visible/audio response should usually begin within roughly 0.05–0.15 s after input for direct button/toggle actions.

## Mechanical follow-through
A door/gate/fridge may take roughly 0.4–1.2 s to reach a readable state depending on weight and style.

## Device controls
Fisher transport actions should feel chunky but responsive. Avoid long animation locks before the Recorder state changes.

The domain state transition and presentation animation must not drift into contradictory states.

---

# Interruptibility

Short domestic interactions should generally not trap Malo in long unskippable animations.

Preferred:
- brief authored hand/body gesture later;
- object animation continues independently where safe;
- player regains movement quickly.

Avoid:
- 3-second canned open-door animation for every door;
- camera takeover for ordinary object manipulation;
- repeated forced close-ups.

Cinematic emphasis should be reserved for major memory/device moments.

---

# Failed interaction feedback

If an interaction cannot occur:
- no generic error buzzer;
- prefer no action + subtle contextual explanation only if needed;
- distinguish `not in range`, `state does not allow`, and `beat not available` at the presentation layer when debugging;
- production UI should avoid exposing implementation language.

Examples:
- already-open gate: semantic action becomes `Close gate` rather than failing `Open gate`;
- Fisher already equipped: placed pickup is no longer offered;
- unavailable future room: architecture should make boundary believable rather than show `LOCKED QUEST 4`.

---

# Recording interaction feedback

BO has two overlapping interaction loops:

1. manipulating the world;
2. recording what happens.

These must remain legible simultaneously.

Example gate while REC:
- player presses REC -> Fisher state/transport feedback;
- player opens gate -> gate motion + latch + squeak;
- Recorder keeps recording without stealing control;
- player releases REC -> STOP feedback;
- later playback reveals actual captured timing.

Do not pause world interaction merely because Recorder is in REC unless a genuine hardware limitation is intentionally designed.

---

# Object-specific minimum feedback

## Fisher Price
Minimum:
- button/transport motion or credible state indication;
- mechanical clack;
- REC lamp for REC;
- carried/world visibility state;
- compact Recorder state feedback.

## Gate
Minimum:
- handle/latch implication;
- rotation;
- latch + hinge sound;
- clear open/closed silhouette.

## Fridge
Minimum:
- door rotation;
- seal sound;
- interior light;
- hum perspective/state change.

## Tap
Minimum:
- handle motion;
- water starts/stops visibly;
- water audio follows state;
- bathroom room response later.

## Cassette review
Minimum later:
- physical selection/placement;
- cassette handling sound;
- playback action;
- annotation/box state readable without spreadsheet UI.

---

# Guidance interaction

## GUIDED
May add:
- earlier prompt;
- stronger local audio emphasis;
- short hint after repeated confusion;
- slightly broader timing windows.

## NATURAL
Physical feedback + contextual prompt at normal range.

## FREE
Physical feedback remains identical; interpretive UI is reduced.

Never reduce physical feedback in FREE mode. FREE means less explanation, not worse usability.

---

# Accessibility note

Future accessibility options may independently provide:
- stronger interactable contrast;
- subtitle/sound-caption support;
- larger prompts;
- hold/toggle alternatives;
- reduced timing pressure.

Do not force these needs into the narrative guidance profile. `GUIDED / NATURAL / FREE` and accessibility are related but separate concepts.

---

# Work acceptance questions

For every new object interaction, Work should answer:

1. Can a first-time player plausibly guess the action from the world?
2. Does input receive immediate acknowledgement?
3. Does the object's physical state visibly change?
4. Is there object/material-specific sound feedback?
5. Does the prompt reflect the current state?
6. Can the interaction coexist with REC?
7. Does guidance alter explanation rather than game content?
8. Is the object still understandable with HUD hidden?
9. Is any failed attempt recoverable without a `MISSION FAILED` state?
10. Has the canonical Fisher/Ronan loop remained intact?
