# BO_Ta_Vie — Animation Production Backlog

## Status
Planning only. Do not batch-produce animations before live character/rig validation.

## Objective
Spend animation effort where it changes perceived quality and narrative readability most.

The first vertical slice does not need a large animation library. It needs a **small set of convincing, camera-readable motions**.

## Batch A — Current Christmas1982 vertical slice
Highest return on effort.

### A1 — Malo locomotion
Need:
- idle;
- walk cycle;
- start/stop treatment if needed after live test;
- simple turn readability.

Acceptance:
- reads as six years old;
- no foot skating from production camera;
- no adult tactical posture;
- responsive under current controller.

### A2 — Fisher carry
Need:
- carry idle;
- carry walk adaptation.

Acceptance:
- device has weight;
- silhouette clear;
- not weapon-like;
- no severe hand/body clipping.

### A3 — Fisher interaction trio
Need:
- press REC;
- STOP/release;
- press PLAY.

Can initially share hand/upper-body structure with timing variants.

Acceptance:
- tactile sound/contact sync;
- very low latency;
- no gameplay gating.

### A4 — Fisher pickup
Need:
- reach;
- grasp;
- lift/settle.

Acceptance:
- no obvious world-to-held teleport;
- under ~1.4 s target unless live staging proves otherwise.

### A5 — Listening attention
Need:
- subtle head/upper-body listening layer.

Acceptance:
- stillness remains possible;
- no constant target tracking.

### A6 — Ronan simple idle
Need:
- stable older-sibling idle.

Acceptance:
- visually distinct from Malo by stance/cadence, not only height.

### A7 — Ronan notices REC
Need at least one short glance reaction.

Acceptance:
- does not cancel recording;
- reads from current camera.

### A8 — Family quiet ambient gesture
Preferred first candidate:
- Father tends fireplace.

Purpose:
- prove the house can feel alive without quest significance.

## Batch A stop gate
Do not start Batch B until:
- authored/proxy rig route is stable;
- A1–A7 are readable in-game;
- no animation architecture regression affects Recorder or interaction;
- frame/time cost is acceptable;
- camera does not hide all the gesture work.

---

## Batch B — First living micro-hub
Only after Sprint 5 acceptance and first post-prototype systems.

Candidates:
- gate latch/open/close;
- Malo notice sound;
- `MALO TU FAIS QUOI ?` reaction;
- Mother fridge glance;
- Mother fridge intervention;
- Ronan perform-for-recorder;
- Ronan spoil-take;
- cassette pick/place;
- basic door/fridge handle interaction.

Batch B should be driven by implemented beats, not animation completionism.

---

## Batch C — Later PISTE 0 authored performance
Examples:
- horse persistence;
- TV bricolage;
- tape repair;
- Radio Malo presenting/performing;
- MK2 manipulation;
- family crowd micro-performance;
- gull waiting patience.

These deserve more authored timing and character detail.

Do not produce before the corresponding gameplay/narrative beats are locked.

---

## Reuse policy
Reuse is encouraged where physical semantics match.

Good reuse:
- generic small button-press base adapted to REC/PLAY/STOP;
- simple hinge/handle reach base adapted to gate/fridge;
- head-attention layer reused with different targets/strengths.

Bad reuse:
- same exaggerated reaction for every family event;
- same gait for Malo and Ronan;
- turning every object interaction into identical reach-and-click.

## Animation source policy
Before accepting any external animation asset:
- record source/provenance/license;
- validate skeleton compatibility;
- validate retarget quality;
- judge camera readability;
- avoid vendor-specific gameplay coupling.

Do not select an animation merely because it exists in a library.

## Production review captures
For each Batch A animation, capture:
1. side/three-quarter preview in `CharacterReadabilityPreview`;
2. actual locked/semi-fixed game camera;
3. with Fisher where relevant;
4. debug overlay off;
5. before/after or placeholder/candidate comparison.

## Success criterion
If Batch A succeeds, the player should perceive:
- Malo as a six-year-old child rather than a moving pawn;
- Fisher as a physical object;
- REC/STOP/PLAY as embodied actions;
- Ronan as a person who notices Malo;
- the salon as a place inhabited by a family.

That perceptual gain matters more than raw animation count.
