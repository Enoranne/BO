# BO_Ta_Vie — Recorder sonic grammar

## Purpose

Define a small, repeatable set of diegetic sounds that makes the Fisher Price understandable by ear.

The recorder is not just a prop. Its mechanical sounds are equivalent to verbs:

- REC;
- STOP;
- PLAY;
- capture active;
- playback active;
- clip complete.

The player should not need a synthetic UI beep to know what the device just did.

This document is design-only during Sprint 5.

---

# Principle: physical before digital

Feedback priority:

1. device mechanic;
2. visible device response;
3. minimal HUD support;
4. synthetic UI sound only if a usability problem remains.

For example, pressing REC should first feel like a physical button/transport action, not like clicking a menu.

---

# Fisher state signatures

## STOP — resting state

No continuous confirmation tone.

Possible character:

- low-level physical silence;
- optional tiny device handling noise only when Malo moves/raises it later;
- no electronic idle hum invented purely for UI readability.

STOP is neutral.

## REC press

Target sequence:

`tactile press -> transport engagement -> capture begins`

Creative timing target:

- primary clack: immediate;
- secondary transport response: within roughly 30–100 ms;
- REC lamp: visually immediate;
- no long confirmation animation.

The exact timing must be tuned live in Godot.

## REC active

Do not play a loud looping 'recording noise' as a UI substitute.

If device self-noise is audible in world presentation, keep it restrained.

The strongest ongoing indication should be:

- red REC lamp;
- player's held R input;
- minimal timer/state if HUD is visible.

## STOP / release R

Target sequence:

`transport release -> REC lamp off -> clip sealed`

The mechanical STOP sound should be more neutral than REC.

A subtle temporary `Recorded` HUD message may remain, but there should be no achievement jingle.

## PLAY press

Target sequence:

`PLAY clack -> very short physical lead-in -> cassette/speaker content`

Creative lead-in target:

- approximately 80–180 ms starting point;
- enough to feel physical;
- not enough to make every playback sluggish.

## PLAY active

The captured stream should feel like it comes from the physical recorder/speaker.

Avoid presenting cassette playback as pristine full-bandwidth non-spatial UI audio.

## Playback end

Possible sequence:

`recorded content tail -> tiny hiss/room gap -> transport returns to STOP`

Do not overuse large tape-stop effects.

---

# Live mechanics vs recorded content

This distinction matters.

## Live device mechanics

Sounds the player hears because Malo operates the Fisher:

- REC clack;
- STOP release;
- PLAY clack;
- handling / transport movement.

These are **not normal RecordableSource collectibles**.

## Recorded device bleed

Later, for authenticity, a capture profile may optionally include very small mechanical bleed at the head of a recording.

For example:

- tiny physical bump at recording start;
- low cassette/self-noise floor;
- handling transient if Malo moves the device.

This is part of the **device capture profile**, not a separate world sound icon.

Do not implement it during Sprint 5 simply because the concept exists.

---

# Clip head design

A future Fisher recording should not necessarily start with mathematically perfect zero-time content.

Possible subtle head character:

1. REC actuation / micro-bump;
2. extremely short tape/self-noise lead;
3. world content enters immediately enough to preserve player timing.

Important: do not hide a player's late REC press by adding artificial pre-roll from before the input.

If the gate latch happened before REC, it remains absent.

---

# Clip tail design

A future clip tail may contain:

- last captured world sample;
- tiny noise tail;
- no fabricated content after STOP.

The live STOP button sound can occur outside the stored recording if that is how the final implementation behaves.

The core rule is temporal honesty.

---

# Distinguishing REC / STOP / PLAY

The three transport actions should be recognisable even when the player is not looking at the HUD.

Suggested differentiation:

### REC

- strongest tactile commitment;
- slightly heavier mechanical action;
- associated with red lamp.

### STOP

- short release / disengage;
- dry and neutral;
- no emotional flourish.

### PLAY

- related family of mechanism sound, but distinct engagement signature;
- followed quickly by playback speaker character.

Do not make them three unrelated sci-fi UI sounds.

---

# Error/rejection feedback

Current prototype can reject actions such as REC without a recorder or PLAY with no clip.

Production-facing feedback should prefer:

- restrained HUD text;
- absence of successful mechanical state change;
- optional small physical unsuccessful action only if useful.

Avoid harsh error buzzers unless testing proves the player is confused.

---

# Device evolution

The Fisher grammar establishes the baseline.

Later devices should feel related but mechanically different.

## Fisher Price

- chunky;
- tactile;
- simple;
- limited;
- child-friendly physicality.

## Philips D6920 MK2 later

Potential future contrast:

- more precise switches/buttons;
- more serious transport character;
- clearer operational feedback;
- richer playback;
- later pitch / Sound-on-Sound / track capabilities.

The player should hear technological progression before opening any specification screen.

---

# Acceptance questions for live audio pass

When real device sounds are available, test:

1. Can a player identify REC with eyes off HUD?
2. Is STOP clearly different from PLAY?
3. Does repeated REC/STOP remain satisfying rather than annoying?
4. Is playback lead-in short enough to preserve flow?
5. Does cassette playback feel physical rather than like menu audio?
6. Does the device communicate without synthetic beeps?
7. Are mechanics subtle enough not to dominate Ronan's first playback?

If yes, the recorder is beginning to function as an instrument rather than just a control scheme.