# BO_Ta_Vie — Character Animation Architecture

## Status
Design only. Future integration contract.

## Goal
Add authored character motion without moving gameplay ownership into animation code.

## Ownership model

### MaloController owns
- movement intent;
- actual character-body locomotion;
- interaction input routing;
- Recorder input routing;
- gameplay permission to move/interact.

It must not own detailed animation clips or animation-specific state names.

### Recorder owns
- STOP / REC / PLAY domain state;
- recording/playback validity;
- clip creation.

It must not wait for animation events to decide whether recording logically starts or stops.

### FisherPrice / device presentation owns
- placed/equipped/active presentation;
- carried device visual state;
- visual/audio reaction to Recorder state.

### Future CharacterAnimationPresenter owns
- mapping gameplay signals/state into animation intents;
- locomotion blend values;
- gesture requests;
- short interaction animation presentation;
- safe fallback when a requested animation is unavailable.

It observes domain systems. It does not replace them.

### Narrative/director layer owns
- authored reaction requests;
- attention targets for specific beats;
- family reaction variants;
- short staging windows.

It does not write Recorder state directly.

## Recommended future seam

```text
MaloController / Recorder / Interactable / NarrativeDirector
             | signals / read-only state
             v
    CharacterAnimationPresenter
             |
             v
    AnimationTree / AnimationPlayer / rig
```

Production rig details stay behind the presenter.

## Why this seam
It allows:
- placeholder rig now;
- authored rig later;
- AnimationTree replacement without rewriting gameplay;
- different character rigs sharing high-level intents;
- animation failures to degrade visually instead of breaking interaction logic.

## High-level animation intents
Use semantic intents, not raw clip names in gameplay systems.

Candidate intent vocabulary:
- `LOCOMOTION`
- `IDLE`
- `LISTEN`
- `PICKUP_FISHER`
- `CARRY_RECORDER`
- `PRESS_REC`
- `RECORDING_HOLD`
- `PRESS_STOP`
- `PRESS_PLAY`
- `NOTICE_SOURCE`
- `REACTION_SHORT`
- `OPEN_HINGE`
- `HANDLE_CASSETTE`

The presenter may map these to different implementation-specific clips/trees per rig.

## Event timing rule
Gameplay is authoritative.

For button actions:
1. player input is accepted by domain logic;
2. Recorder/object changes logical state;
3. animation and sound present that state with minimal latency;
4. contact timing is aligned visually/audio-wise as closely as practical.

Do not delay real REC until an animation notify unless a later interaction is explicitly designed as a committed cinematic action.

This prevents low frame rate, missing clips or animation interruption from breaking recorder logic.

## Interaction anchors
For physical interactions later, an object may expose presentation anchors such as:
- hand target;
- stand target;
- facing target;
- interaction height.

Use these as optional presentation aids.

Do not make `InteractionContext` depend on animation anchors.

## IK policy
First authored rig may use lightweight hand/arm IK for:
- Fisher handle/button contact;
- gate latch;
- fridge handle;
- cassette placement.

IK is enhancement, not a prerequisite for gameplay validity.

Fallback must remain acceptable without IK.

## Attention system
Future attention should be a small presentation service with:
- target;
- strength;
- max angle;
- duration;
- priority;
- release/blend time.

Priorities might be:
1. authored narrative reaction;
2. current recording source when explicitly relevant;
3. interacting object;
4. nearby salient sound;
5. neutral forward/locomotion attention.

Do not continuously select nearest Interactable as gaze target.

## Locomotion
Keep controller-authoritative movement.

Presenter reads:
- horizontal speed;
- movement direction;
- equipped state;
- optionally acceleration/deceleration.

First blend can remain simple:
- idle;
- walk;
- recorder-carry idle/walk later.

Do not build run/sprint/crouch/combat locomotion without narrative need.

## Turn handling
At fixed/semi-fixed camera angles, facing readability matters.

Candidate approach:
- body orientation follows intended movement/facing using existing controller rules;
- animation adds turn anticipation only after live testing;
- short attention head-turns must not rotate navigation direction.

## Gesture concurrency
Need explicit rules so gestures do not fight.

Examples:
- locomotion + recorder carry: allowed;
- locomotion + mild head attention: allowed;
- REC press + locomotion: may briefly constrain upper body only;
- pickup Fisher + full locomotion: usually blocked for short pickup window;
- major narrative performance + locomotion: authored per beat.

## Interruptibility classes

### Immediate
Can be interrupted freely.
Examples: idle, attention, listening.

### Soft-commit
Very short interaction should finish if possible but can fail gracefully.
Examples: REC/STOP/PLAY press.

### Commit
Short physical manipulation where interruption risks visual nonsense.
Examples: Fisher pickup, gate latch, cassette placement.

### Narrative lock
Rare authored performance.
Use only when explicitly justified.

## Placeholder integration rule
Do not convert primitive `PlaceholderHumanoid3D` into a fake production skeleton.

If a live test before authored rigs is useful, add only isolated presentation hooks such as:
- recorder carry proxy offset;
- mild arm pose;
- attention/facing proxy;
- locomotion timing parameters.

Keep those changes reversible.

## Production rig requirements
When commissioning/importing Malo/Ronan rigs:
- metre scale;
- stable skeleton hierarchy;
- clean rest pose;
- readable hands/fingers for device work;
- deforming shoulders/elbows suitable for recorder carry;
- head/neck bones suitable for mild look-at;
- root orientation documented;
- animation retargeting path documented;
- no gameplay dependency on vendor-specific skeleton names.

## Testing order
1. locomotion silhouette in CharacterReadabilityPreview;
2. idle/listening stillness;
3. Fisher carry pose;
4. REC/STOP/PLAY upper-body timing;
5. pickup Fisher;
6. Ronan reaction variant;
7. family ambient routine;
8. later object interactions.

## Failure policy
If an animation is missing:
- preserve gameplay;
- fall back to neutral/carry pose;
- log/debug missing presentation intent;
- never reject a valid Recorder action solely because animation data is unavailable.

## Explicitly not now
- Gameplay Ability System equivalent;
- giant hierarchical state machine;
- animation-driven Recorder state;
- animation-driven quest progression;
- motion matching;
- full procedural IK suite;
- ragdoll;
- combat layers;
- parkour/climbing.
