# BO_Ta_Vie — Physical Cassette UX

## Purpose
Define how recording review should feel physically before any full-screen library UI is considered.

This is Sprint 6+ design preparation. It does not modify Sprint 5 gameplay.

## Core rule
The cassette archive should first exist **in the world**, not in a pause menu.

Malo should appear to be organising objects, not browsing database rows.

## Earliest viable review space
Preferred first implementation:

- a small surface in Malo's room, or temporary equivalent if the bedroom is not yet playable;
- one cassette or compact stack representing recent recordings;
- three visible physical boxes/piles:
  - `CASSETTES`;
  - `BIEN`;
  - `RATÉS MAIS GARDER`;
- optional `À REFAIRE` pile only after the basic metaphor is clear.

## Interaction rhythm

### Approach
Malo approaches the review surface.

No giant prompt should appear from across the room.

### Focus
Context interaction reveals the current cassette/take.

### Primary action
`PLAY` remains the most important action.

### Secondary action
After listening, simple editorial choices become available:
- keep as ordinary cassette;
- move to `BIEN`;
- move to `RATÉS MAIS GARDER`;
- optionally `À REFAIRE`.

### Optional title
Title may be added before or after classification.

Never block playback because a title is missing.

## Visual language

### Cassette
Should communicate:
- handwritten label area;
- slight plastic wear;
- side indicator;
- no polished digital card aesthetic.

### Boxes
Simple domestic cardboard/plastic storage is preferable to floating UI panels.

Handwriting should look improvised rather than like a decorative font treatment.

### Information hierarchy
Visible first:
1. cassette/take identity;
2. play state;
3. child title if one exists;
4. box placement.

Hidden or secondary:
- exact technical timestamp;
- source ids;
- metadata fields;
- internal file names.

## Review capacity
Do not show dozens of recordings simultaneously in the first prototype.

Recommended proof:
- 2 to 5 recordings visible/reviewable;
- enough to demonstrate comparison and personal judgement;
- small enough to preserve tactile intimacy.

## Controller/input compatibility
Future UX should remain action-based:
- context interact to examine/place;
- Space/PLAY to listen;
- directional/simple selection only when needed.

Do not design around precise mouse dragging as a requirement.

Mouse may provide an alternate action, but keyboard/controller parity should remain feasible.

## Animation priorities
For the first physical proof, prioritize:
- cassette appears/gets selected;
- simple hand/place implication;
- playback state feedback;
- box/pile change.

Do not require full hand IK or sophisticated finger animation before validating the metaphor.

## Audio feedback
The review surface should itself have tactile sonic identity:
- cassette case click;
- cassette plastic handling;
- light box/cardboard movement;
- Fisher transport click if playback uses the recorder.

UI beeps should not replace these sounds.

## Failed-but-kept moment
A signature early experience should demonstrate the philosophy:

1. player records something imperfect;
2. playback reveals an accidental detail;
3. player chooses `RATÉS MAIS GARDER`;
4. cassette is physically placed in the corresponding box;
5. nothing awards points or calls it a rare collectible.

The emotional reward is ownership of the mistake.

## Future evolution by era

### Age ~6 / Fisher Price
- crude boxes;
- short titles;
- physical piles;
- simple good/bad/keep judgements.

### Age ~8–10 / MK2
Possible evolution:
- cassette numbering;
- more systematic labels;
- experiment notes;
- sound lists;
- transformed versions;
- source/derivative relationships.

### Radio Malo era
The archive can become production material:
- selects;
- edited fragments;
- jingles;
- programme building.

The UI may become more structured only because Malo himself has become more structured.

## Anti-patterns
Avoid:
- inventory grid with item rarity;
- waveform browser as the default childhood interface;
- star ratings;
- completion percentage for every sound in the world;
- auto-generated perfect titles;
- permanent minimap markers for recording targets;
- instant magical sorting without Malo/player action.

## Accessibility note
The physical metaphor must not hide functionality from players who need clearer UI.

Later accessibility mode may provide:
- explicit text labels;
- stronger focus states;
- transcript/support where appropriate;
- simplified classification controls.

Accessibility assistance should expose the same underlying actions rather than replace the fiction with a separate progression system.
