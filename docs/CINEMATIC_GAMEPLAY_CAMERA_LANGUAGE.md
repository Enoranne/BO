# BO_Ta_Vie — Cinematic Gameplay Camera Language

## Status
Design only beyond the existing Christmas1982 camera.

## Thesis
BO should feel **cinematically framed, not camera-controlled by the player**.

The camera supports memory, space, sound and character blocking while preserving reliable movement and interaction.

Do not evolve the project into unrestricted third-person mouse-look merely because the world expands.

## Existing baseline
Christmas1982 already uses a fixed/semi-fixed camera with deliberately limited follow around an anchor.

Preserve that principle as the reference.

## Camera grammar

### C0 — Anchored tableau
Mostly fixed composition with tiny bounded follow.

Best for:
- salon;
- family group scenes;
- reflective cassette review;
- authored domestic compositions.

Purpose:
- strong mise-en-scène;
- stable spatial memory;
- readable family relationships.

### C1 — Soft follow frame
Fixed authored camera with modest bounded translation/look-at support.

Best for:
- slightly wider playable room;
- moving between two nearby interaction clusters.

Purpose:
- preserve authored composition without losing Malo near frame edge.

### C2 — Threshold handoff
Transition between two authored camera anchors when Malo crosses a meaningful doorway/zone threshold.

Best for:
- salon → corridor;
- corridor → kitchen;
- interior → garden.

The handoff should feel motivated by architecture, not by arbitrary trigger volumes.

### C3 — Beat emphasis
Temporary, restrained framing adjustment for a meaningful event.

Examples:
- Fisher pickup;
- first playback reaction;
- important family interruption;
- later cassette review.

Rule: gameplay remains authoritative. Do not lock movement for a decorative camera move unless the beat explicitly becomes a cutscene.

### C4 — Listening composition
Frame intentionally leaves visual space toward an off-screen/approaching sound source.

Examples:
- garden wind;
- moped approaching street edge;
- Mother voice from doorway.

Purpose:
- use composition to make sound spatially meaningful.

### C5 — Exterior spatial frame
Broader authored frame for garden/gate/tree area with more lateral tolerance than salon.

Still not free orbit.

## Transition vocabulary
Prefer a small set:

### CUT
Use when spatial relationship is obvious and immediate readability improves.

Good for:
- doorway crossing with strong continuity;
- switching sides of a compact zone when player direction remains clear.

### SHORT BLEND
~0.25–0.8 s target range, subject to playtest.

Use when:
- two anchors are close;
- a hard cut feels jarring;
- motion continuity matters.

### AUTHORED MOVE
Rare, short camera move tied to a real beat.

Do not use continuous cinematic rails during ordinary navigation.

## Camera handoff rules
A zone transition should preserve:
- player screen-direction where practical;
- visible destination/exit cue;
- control continuity;
- interaction readability;
- no sudden reversal that makes the player walk backward accidentally.

Never cut simply because a trigger was crossed if the resulting frame is worse.

## Salon
Primary language: C0/C1.

The salon is the visual and emotional anchor.

Camera should preserve:
- fireplace back-left;
- sofa/family field;
- tree/gifts back-right;
- Fisher pickup readability;
- Ronan record position;
- enough foreground floor for Malo movement.

Do not constantly reframe every interaction.

## Corridor
Primary language: C2 + narrow C1.

Goals:
- imply house depth;
- keep corridor from feeling like a free-roaming hallway game;
- use doorways as compositional frames;
- allow distant family voices to lead navigation.

## Kitchen
Primary language: C0/C1.

Potential key composition:
- fridge readable in one plane;
- Mother working/crossing in another;
- garden/French-door relation visible when possible.

This supports fridge comedy and garden transition without UI arrows.

## Garden
Primary language: C5 + C4.

Goals:
- give Malo more breathing room;
- retain visual anchor to house;
- tree/portique/gate should form readable landmarks;
- allow sound sources to exist beyond frame edge.

Do not solve exterior scale by adding unrestricted camera rotation.

## Gate / street edge
Primary language: C4/C5.

For gate `BONJOUR`:
- gate and latch readable;
- enough negative space beyond gate to suggest neighbour/street;
- camera should not spoil every approaching event by showing it too early.

For moped:
- player can hear approach before full visual confirmation;
- composition may reserve street-edge space;
- missing the perfect capture remains possible.

## Recorder relationship
Camera must not zoom or snap automatically every time REC starts.

REC is a player capability, not a cinematic event by itself.

Beat directors may request a temporary composition only when narratively justified.

Do not put camera control inside `Recorder`.

## Interaction relationship
Camera may improve affordance visibility but must not become the only way an object is discoverable.

Avoid:
- auto-centering every interactable;
- camera magnetism that fights movement;
- hiding usable objects behind foreground geometry without compensation.

## Character relationship
Malo should remain readable as a small child in the domestic environment.

Use framing to preserve:
- scale contrast with furniture/adults;
- hand/recorder readability during key actions;
- Ronan/Malo sibling hierarchy.

## Occlusion policy
Future authored zones should review:
- wall/furniture occlusion;
- foreground objects hiding Malo;
- doorway clipping;
- camera collision only if genuinely needed.

Do not immediately add a complex dynamic camera-collision system. Prefer better authored anchors/geometry first.

## Reduced motion accessibility
Future `reduced_camera_motion` may:
- prefer CUT over long blend/move;
- reduce beat-emphasis travel;
- reduce camera lag where it causes discomfort.

It must not alter story content or camera availability.

## Phantom Camera decision
An addon may only be adopted if it materially simplifies authored anchor blending/handoffs while preserving this contract.

Do not adopt it simply to add more camera features.

## First future camera proof
After Sprint 5 acceptance and house shell readiness:

1. retain current salon camera as A;
2. create one corridor anchor B;
3. cross a single salon/corridor threshold;
4. compare CUT vs short blend;
5. confirm movement direction remains intuitive;
6. confirm REC can continue through transition;
7. confirm no camera logic enters Recorder/MaloController;
8. only then consider kitchen/garden anchors.

## Anti-patterns
- unrestricted 360 mouse-look;
- constant shoulder camera;
- automatic zoom on every interaction;
- camera cut every few steps;
- long rail moves during ordinary control;
- objective-marking camera pans;
- camera logic embedded in domain systems;
- addon-specific gameplay dependencies.
