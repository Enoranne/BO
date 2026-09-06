# BO_Ta_Vie — Character Gesture Language

## Status
Design only. This document does not authorise a production animation state machine during Sprint 5.

## Goal
Make Malo, Ronan and the family read as people before they become high-fidelity characters.

Animation should communicate:
- age;
- attention;
- intention;
- relationships;
- recorder state;
- small emotional shifts;
- household life.

The target is not animation quantity. It is **readable authored behaviour**.

## Core principle
For BO, animation should often answer:

> What is this person paying attention to right now?

A six-year-old Malo should not move like a scaled-down adult player avatar.

## Layer model

### L0 — Locomotion
Body movement required to navigate.

Examples:
- idle;
- walk;
- start/stop;
- turn;
- small direction correction.

### L1 — Attention
Small gestures that show perception without changing gameplay state.

Examples:
- head turn toward a sound;
- glance to Fisher;
- glance to Ronan;
- listening stillness;
- brief look back toward Mother calling.

### L2 — Object interaction
Authored gestures tied to a physical action.

Examples:
- reach Fisher;
- lift Fisher;
- press REC;
- release/STOP gesture;
- press PLAY;
- open gate;
- open fridge;
- handle cassette.

### L3 — Character reaction
Short behaviour expressing relationship or consequence.

Examples:
- Ronan notices REC light;
- Ronan leans toward recorder;
- Mother looks over after repeated fridge opening;
- Father glances up from fireplace;
- Malo freezes when caught.

### L4 — Narrative performance
Rare authored moments with stronger staging.

Examples:
- horse persistence beat;
- tape repair concentration;
- first Radio Malo performance;
- major device transition.

Do not solve L4 before the basic locomotion/interaction language is convincing.

## Malo — movement identity

### Age read
Malo is six.

Desired qualities:
- shorter stride;
- slightly quicker cadence than an adult;
- small over-corrections when stopping;
- curiosity can pull torso/head before feet fully follow;
- moments of complete stillness when listening;
- object manipulation shows concentration rather than expertise.

Avoid:
- tactical/game-avatar crouch posture;
- confident adult shoulder-led locomotion;
- constant exaggerated child bounce;
- cartoon flailing.

### Idle
Primary idle should be quiet.

Subtle ingredients:
- small weight shift;
- occasional head movement;
- hands not perfectly frozen;
- attention events layered only when context justifies them.

The idle must support silence. Do not make Malo continuously fidget because the animation system is afraid of stillness.

### Walk
Desired read:
- compact stride;
- believable six-year-old balance;
- arms relaxed;
- mild speed-dependent swing;
- foot placement should not skate.

Recorder-equipped locomotion later:
- Fisher changes arm posture;
- gait becomes slightly more guarded;
- free arm may still balance naturally;
- recorder should feel like an object with weight, not glued to the chest.

## Recorder pose language

### Carry
Default Fisher carry should be recognisable from the locked third-person camera.

Candidate pose:
- one hand primarily supports handle/body;
- device sits near lower torso/hip rather than permanently raised to face;
- second hand remains available unless interaction/recording requires it.

### Prepare to record
Very short intention gesture:
- attention shifts toward source;
- recorder rises slightly;
- free hand approaches REC control;
- no long cinematic lockout.

### REC press
The press must visually coincide closely with the mechanical click.

Desired:
- small finger/hand compression;
- recorder reacts minimally to the force;
- optional tiny body stilling immediately after engagement.

### Recording hold
Malo becomes more attentive, not frozen by an animation pose.

He may:
- angle torso toward source;
- hold device more carefully;
- move slowly if gameplay permits;
- glance between source and recorder.

### STOP
Release should be readable and fast.

After STOP:
- small relaxation;
- optional glance to recorder;
- player regains ordinary movement immediately.

### PLAY
Press → short anticipation → listening reaction.

Playback listening should often reduce motion rather than add gesture.

## Attention / listening grammar

### Sound noticed
Use a hierarchy:
1. eyes/head first;
2. upper torso second if source remains salient;
3. feet/whole body only if player chooses to move.

Do not steal player control with full-body auto-turns for ordinary sounds.

### Strong family interruption
Example: `MALO TU FAIS QUOI ?`

Possible authored reaction:
- brief head snap toward house;
- tiny shoulder response;
- recorder remains where player left it;
- no forced walk/cutscene unless narrative beat explicitly requires one.

## Ronan — movement identity
Ronan should read older before facial detail.

Desired qualities:
- longer stride;
- more stable stance;
- less frequent balance correction;
- more socially conscious body language;
- can deliberately perform for or avoid Malo's recorder.

### Ronan notices recording
Useful variants:
- quick glance at Fisher;
- knowing half-smile;
- turn away;
- step closer and perform;
- deliberately spoil take;
- suspicious look if Malo follows him.

Do not make every detection trigger the same reaction.

## Mother
Movement is practical and task-led.

Desired:
- purposeful household crossings;
- hands often occupied;
- reactions can begin with a glance before dialogue;
- repeated Malo behaviour may move from ignore → acknowledge → intervene.

## Father
Movement is quieter and less reactive.

Desired:
- deliberate gestures;
- fireplace/object routines;
- observation before intervention;
- small affectionate looks can carry narrative weight.

## Eye-line / head-look policy
Use procedural/look-at assistance cautiously.

Good uses:
- short attention toward nearby source;
- family member acknowledgement;
- recorder glance after STOP.

Bad uses:
- head constantly tracking nearest interactable;
- eyes snapping between targets;
- player avatar automatically looking at every quest-relevant object.

Attention must feel authored, not like an NPC targeting system.

## Root motion policy
Do not require root motion for the first implementation.

Preferred first pass:
- gameplay movement remains owned by existing controller;
- locomotion animation visually follows velocity;
- authored interaction animations are short and local;
- use controlled alignment/interaction anchors only when needed.

Re-evaluate root motion for specific narrative performances later.

## Interaction lockouts
Keep them short.

Candidate budgets:
- button press: ~0.15–0.35 s;
- pick-up Fisher: ~0.7–1.4 s;
- simple hinge interaction: ~0.4–0.9 s;
- cassette handling/review: ~1–3 s depending context.

These are targets, not hard engine constants.

Never make ordinary object interaction feel like a mini-cutscene.

## Blend philosophy
Prefer:
- locomotion base;
- upper-body/object overlay where rig permits;
- small additive attention gestures;
- short authored reactions.

Avoid building one giant monolithic animation graph before real assets/rigs exist.

## Placeholder phase
The current `PlaceholderHumanoid3D` remains a procedural proxy.

Do not force detailed production animation into its primitive mesh hierarchy.

Useful placeholder tests only:
- locomotion rhythm;
- idle amount;
- direction/facing readability;
- simple recorder carry proxy;
- timing of interaction beats.

## Production acceptance questions
For each gesture ask:
1. Can I understand the intention without text?
2. Does Malo still look six?
3. Does the gesture preserve player responsiveness?
4. Does sound line up with contact/action?
5. Does the animation improve storytelling rather than merely add movement?
6. Does it remain readable from the actual game camera?

## Explicitly deferred
- facial capture;
- full lip sync;
- motion matching;
- complex IK stack;
- cloth/hair simulation;
- full-body procedural locomotion;
- NPC combat/navigation animation;
- giant AnimationTree architecture before authored rigs exist.
