# BO_Ta_Vie — Recording System Evolution by Era

## Purpose
Keep future recorder mechanics narratively progressive instead of exposing a fully featured audio workstation from the beginning.

This document is roadmap/design only.

## Principle
The recording system should mature because **Malo matures** and because his equipment changes.

The UI, organisation and creative possibilities should evolve with him.

---

# Era 1 — Fisher Price / age ~6

## Player fantasy
Discovery.

Malo realises that sound can be captured and replayed.

## Core verbs
- hear;
- approach;
- REC;
- STOP;
- PLAY;
- listen again;
- keep;
- retry.

## Archive language
Physical and crude:
- `CASSETTES`;
- `BIEN`;
- `RATÉS MAIS GARDER`;
- optional `À REFAIRE`.

## Titles
Short, concrete, child-like.

Examples:
- `RONAN`
- `PORTAIL`
- `VENT`
- `BRUIT BIZARRE`

## Mechanical limits
- one simple track concept;
- no pitch;
- no Sound-on-Sound;
- no multitrack;
- no detailed waveform editing;
- no advanced library UI.

## Emotional function
Recording is magical because replay itself is new.

---

# Era 2 — Philips D6920 MK2 / age ~8–10

## Player fantasy
Experimentation.

Malo no longer only captures sounds. He starts trying to **change** them and understand the machine.

## New verbs candidates
- pitch/speed experimentation;
- track/channel awareness where technically/narratively appropriate;
- Sound-on-Sound;
- re-recording;
- layered experiments;
- tape repair;
- deliberate level mistakes;
- comparing versions.

Exact hardware-faithful capabilities must be validated before implementation; do not assume every feature from narrative shorthand maps literally to the device.

## Archive language
More systematic:
- tape numbers;
- sound lists;
- experiment notes;
- versions;
- source/derivative relationships;
- `BIEN` / `RATÉS MAIS GARDER` still persist.

## Titles
Still personal but more purposeful.

Examples:
- `PORTAIL LENT`
- `RONAN AIGU`
- `VENT + VOIX`
- `ESSAI 3`

## Data evolution
The raw recording remains immutable where possible.

Transformations should create derivative relationships rather than silently overwrite history.

Potential model:
`source recording -> transformation recipe -> derived recording/version`

## Emotional function
Malo learns that memory can be manipulated, not just preserved.

---

# Era 3 — Radio Malo

## Player fantasy
Composition and performance.

The private archive becomes material for something made for others.

## New verbs candidates
- select clips;
- sequence fragments;
- create jingles;
- insert voice links;
- reuse old recordings;
- build a programme;
- play/show the result.

## Archive language
Working studio rather than collection:
- selects;
- intros;
- jingles;
- beds;
- voice;
- weird sounds;
- programme order.

## Important continuity
The old six-year-old labels remain visible/history-preserving where relevant.

A sophisticated later use must not retroactively rename the childhood source.

Example:
`ENCORE PORTAIL` may become a metallic rhythm in Radio Malo while retaining its original child title in provenance.

## Emotional function
Memory becomes creative material.

---

# Era 4 — Later/adult perspective if used

## Player fantasy
Reinterpretation.

Old recordings outlive the circumstances in which they were made.

## Potential verbs
- replay;
- compare eras;
- revisit associations;
- hear original + transformed versions;
- encounter narrative callbacks.

## Emotional function
The archive becomes evidence of people, places and selves that changed.

---

# Cross-era invariants

## 1. Raw provenance matters
Never lose the relationship to the original capture.

## 2. Child labels are historical artefacts
Later systems may add metadata but should not erase early titles/judgements.

## 3. No universal quality score
What counts as “good” changes with Malo's purpose.

## 4. Mistakes survive
`RATÉ MAIS GARDER` remains structurally important across eras.

## 5. Capability follows device + age
Do not expose MK2/Radio Malo mechanics during Fisher gameplay.

## 6. Complexity must be earned
Every new interface concept should correspond to Malo learning a new creative habit.

## Suggested roadmap relationship
- Sprint 5: Fisher onboarding + visual slice only.
- Sprint 6: persistent recordings + child annotation/physical review proof.
- Sprint 7: family/dialogue/world density may grow.
- later: temporal multi-source capture hardened.
- later MK2 sprint: transformations/versions.
- later Radio Malo sprint: composition workflow.

Sprint numbering after 6 remains subject to production priorities; the conceptual order matters more than the exact number.
