# BO_Ta_Vie — Character Gesture Sequence Cards

## Status
Design only. These cards are implementation/animation references, not Sprint 5 scope expansion.

## Card format
Each sequence is described as:

`SETUP -> INTENTION -> CONTACT -> RESULT -> RELEASE`

The domain action remains authoritative. Animation presents the action.

---

# C01 — Malo takes the Fisher Price

## Purpose
Make the first object acquisition feel physical and emotionally important without turning it into a long cutscene.

## Setup
- Fisher visible/readable in gift area.
- Malo enters interaction range.
- Player chooses TAKE.

## Intention
Target: ~0.15–0.35 s.
- gaze lowers toward Fisher;
- small torso lean/reach preparation.

Do not force an automatic full-body turn if the existing alignment is already readable.

## Contact
Target: ~0.25–0.55 s.
- hand reaches handle/body;
- grip reads clearly;
- Fisher begins moving with hand.

## Result
Target: ~0.25–0.45 s.
- device lifts;
- carried visual becomes authoritative presentation;
- object settles near lower torso/hip.

## Release
- ordinary player control returns;
- carry pose remains;
- HUD/context advances toward Ronan.

## Audio sync
- optional small plastic/handle contact;
- no oversized magical pickup sting.

## Gameplay rule
Existing Fisher pickup state remains authoritative.
Animation must not create/own the pickup.

## Acceptance
- duration ideally under ~1.4 s;
- no obvious teleport between world and held Fisher;
- no hand passing through device in final production rig;
- Malo still reads six years old;
- player can understand that the device is now carried.

---

# C02 — Malo presses REC

## Purpose
Make recording physically legible and satisfying.

## Setup
- Fisher equipped;
- valid source/context according to gameplay rules;
- player presses/holds R.

## Intention
Target: ~0.05–0.15 s.
- tiny attention/hand preparation;
- no slow wind-up.

## Contact
Target: ~0.08–0.20 s.
- finger/hand depresses REC control;
- mechanical click aligns with visible contact.

## Result
- Recorder is already logically REC after valid input;
- REC visual/lamp responds;
- Malo settles into attentive hold.

## Release
- transition into `recording_hold` pose;
- movement remains according to gameplay contract.

## Audio sync
The click is part of tactile state confirmation.
No electronic confirmation beep.

## Acceptance
- perceived latency from input to response is very low;
- animation does not gate logical REC;
- button contact and click feel coincident;
- recording hold does not look like aiming a weapon.

---

# C03 — Malo releases REC / STOP

## Purpose
Make the end of a take readable without breaking responsiveness.

## Setup
- Recorder currently REC;
- player releases R.

## Contact
Target: ~0.08–0.20 s.
- quick hand release/button motion;
- STOP/transport click.

## Result
- Recorder creates clip according to existing logic;
- REC indication ends;
- Malo relaxes slightly.

## Release
Target total ~0.15–0.35 s.
- return toward carry pose;
- optional glance down to recorder.

## Acceptance
- STOP feels immediate;
- no animation lock delays clip creation;
- motion relaxation is subtle.

---

# C04 — Malo presses PLAY and listens

## Purpose
Make replay a small emotional event rather than only a UI state.

## Setup
- latest clip available;
- player presses Space/P according to current contract.

## Contact
- short button press;
- transport click.

## Result
- playback begins;
- Malo's movement/gesture becomes slightly quieter.

## Listening beat
Target: ~0.5–2.0 s of readable attention layered while playback continues.

Possible reactions later:
- small glance to recorder;
- tiny smile after Ronan laugh;
- head tilt at unexpected sound.

Do not hard-code emotional reaction to every clip.

## Release
- ordinary carry/idle returns naturally when playback ends or player moves.

## Acceptance
- playback remains player-controlled;
- listening pose never becomes a long forced cinematic state;
- replay looks different from REC.

---

# C05 — Recording hold / moving with Fisher

## Purpose
Make Malo look like a child concentrating on capturing sound.

## Base pose
- Fisher supported securely;
- recorder angled plausibly toward general source direction;
- shoulders remain natural;
- free arm not permanently rigid.

## Moving
- shorter/careful walk remains readable;
- device does not bounce excessively;
- upper-body recorder pose blends with locomotion.

## Attention
For salient source:
- head may orient partially;
- torso may bias slightly;
- no auto-navigation.

## Acceptance
- does not resemble firearm aiming;
- device has perceived weight;
- silhouette reads from locked/semi-fixed camera;
- animation permits gameplay movement.

---

# C06 — Ronan notices he is being recorded

## Purpose
First proof that family members perceive Malo's recorder.

## Trigger
Narrative/character layer observes relevant recording context.
Do not put this reaction in Recorder.

## Variant A — glance
~0.3–0.8 s.
- eyes/head glance to Fisher;
- return to prior activity.

## Variant B — performs
~1–4 s.
- notices recorder;
- leans/turns slightly;
- says/makes a sound intentionally.

## Variant C — avoids
- glance;
- subtle turn away/move.

## Variant D — spoils take
- deliberate noise/line/laugh;
- can create `RATÉ MAIS GARDER` material.

## Acceptance
- Ronan never becomes a generic alert-state NPC;
- reactions have cooldown/variation later;
- recording is not automatically cancelled.

---

# C07 — `MALO TU FAIS QUOI ?` reaction

## Purpose
Show a family interruption entering Malo's attention without stealing control.

## Trigger
Mother voice from house during future wind beat.

## Reaction
~0.3–0.9 s.
- head turns sharply toward source direction;
- shoulders may follow slightly;
- Fisher remains in current state;
- REC continues if player is still holding it.

## Narrative value
The interruption may improve the recording even if it spoils Malo's intended wind take.

## Acceptance
- no automatic STOP;
- no forced return to house;
- player can ignore call temporarily if beat permits;
- body language sells that Malo heard her.

---

# C08 — Gate latch/open

## Purpose
First post-prototype object interaction where gesture timing and captured transient matter together.

## Setup
- player near gate;
- OPEN selected;
- REC may already be active.

## Intention
- hand reaches latch;
- body aligns only as much as required.

## Contact
- latch sound aligns with hand action.

## Result
- gate enters OPENING;
- hinge squeak follows physical motion;
- capture system later records actual temporal interval.

## Release
- hand leaves gate;
- player regains movement.

## Acceptance
- animation remains presentation-only;
- gate state owner controls open/close;
- REC can coexist;
- missing interaction animation must not prevent gate operation in fallback/debug mode.

---

# C09 — Cassette review / `RATÉ MAIS GARDER`

## Purpose
Make archive judgement physical rather than menu-only.

## Setup
Future Sprint 6 review surface.

## Action
- pick cassette;
- glance/read label;
- optional replay;
- place into chosen physical box/pile.

## Gesture target
~1–3 s for a simple pick/place cycle.

## Emotional rule
Do not add triumphant reward animation for GOOD.
`RATÉ MAIS GARDER` should feel equally legitimate.

## Acceptance
- physical placement readable;
- no inventory-grid feel;
- annotation service, not animation, owns classification state.

---

# C10 — Father tends fireplace

## Purpose
Add quiet family life and visual rhythm.

## Sequence
- approach/lean;
- small tool/log/fireplace adjustment;
- pause/observe;
- return to ambient position.

## Duration
~1.5–4 s authored ambient routine.

## Rule
No quest significance required.
It is allowed to exist purely as family/world behaviour and sound context.

## Acceptance
- does not loop mechanically every few seconds;
- supports CALM pacing;
- remains independent from Recorder.
