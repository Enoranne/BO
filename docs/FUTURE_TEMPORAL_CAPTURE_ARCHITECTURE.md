# BO_Ta_Vie — Future temporal audio capture architecture

## Status

**Design only. Do not implement during Sprint 5 validation.**

This document exists because the current `Recorder` correctly validates the first prototype beat but represents recording as a reference to one existing `RecordableSource.audio_stream`.

That is sufficient for `ronan_test`.

It is not sufficient for the long-term BO fantasy:

> Malo presses REC, the world continues happening, he opens a gate, wind changes, someone speaks in the distance, then he stops and the cassette contains what actually happened during that interval.

## Current prototype contract to preserve

Current Sprint 4/5 behaviour:

- `Recorder.start_recording(source)` receives one `RecordableSource`;
- REC duration is measured;
- on STOP, a `RecordingClip` is created;
- its `stream` is currently the source's existing stream;
- `RecordingClip` stays directly playable;
- Recorder owns STOP / REC / PLAY state;
- `InteractionContext` owns source selection;
- Malo owns player intent.

The future capture system must extend this architecture, not replace those ownership boundaries.

---

# Why temporal capture matters

A static-stream model encourages this pattern:

`find sound icon -> press record -> receive predefined clip`

BO should eventually support:

`notice something -> choose when to press REC -> let events unfold -> stop when Malo feels he has something`

This permits:

- partial recordings;
- late starts;
- accidental voices;
- overlapping sounds;
- waiting for the right gust;
- recording the gate at different speeds;
- hearing a moped before seeing it;
- discovering that mundane machines become musical material.

Imperfect timing is content, not failure.

---

# Preferred future direction: bus-based temporal capture

Godot 4 provides audio buses and `AudioEffectRecord`, which can record sound passing through a bus into an `AudioStreamWAV` without requiring a physical microphone.

A future BO prototype should evaluate this before inventing a custom sample mixer.

## Conceptual bus layout

Suggested design names only:

- `Master` — final audible game mix;
- `RecordableWorld` — world sounds eligible to enter Malo's recording;
- `NonRecordableWorld` — music / presentation sounds that should never become part of a cassette;
- `RecorderPlayback` — cassette playback; must never feed the capture bus;
- optional future `RecorderMechanics` — diegetic button / motor mechanics if separation becomes useful.

## Critical anti-feedback rule

`RecorderPlayback` must never be captured back into `RecordableWorld` by default.

Otherwise PLAY while another recording path is active could create accidental digital feedback or recursive self-recording that the game has not explicitly designed.

Sound-on-Sound, when the MK2 eventually arrives, must be a deliberate capability rather than an accidental routing bug.

---

# Proposed future CaptureBackend seam

Do not make `Recorder` know low-level bus APIs directly if avoidable.

Long-term seam:

`Recorder -> CaptureBackend -> Audio bus / recording implementation`

Possible responsibilities for a future backend:

- `begin_capture(device_profile, context)`;
- `get_elapsed_seconds()`;
- `end_capture() -> AudioStream`;
- optional capture metadata;
- cancel / cleanup;
- validation that recording resources are ready.

The current static source behaviour can remain available as a prototype/test backend.

A future temporal backend can produce a real recorded `AudioStreamWAV`.

This keeps the Recorder FSM device-agnostic.

---

# Processing strategy

## Do not make the world lo-fi

World sources remain clean enough to represent physical reality.

The recording transformation belongs to the device/memory pipeline.

## First low-risk prototype

A future first temporal-capture experiment can prioritize correctness over perfect Fisher simulation:

1. capture eligible world audio over the actual REC interval;
2. store the resulting stream in `RecordingClip`;
3. preserve `device_id` and capture metadata;
4. route playback through a Fisher playback profile;
5. only then add more advanced microphone coloration.

This already proves the essential design difference: the clip contains the event timing chosen by the player.

## Device coloration

Creative targets live in:

- `docs/AUDIO_MEMORY_PIPELINE_1982.md`;
- `data/audio_memory_profiles_1982.json`.

Avoid destructively baking every effect into source files.

Device evolution should eventually be possible through profiles:

- Fisher Price;
- Philips D6920 MK2;
- later recording/editing capabilities.

---

# Recordability model

Not every audible sound must be recordable.

Three useful categories:

### A — Recordable environment

Examples:

- Ronan;
- fireplace;
- fridge;
- wind;
- gate;
- moped;
- household handling sounds.

### B — Diegetic device mechanics

Examples:

- REC button;
- STOP clack;
- cassette transport;
- speaker playback.

These are audible to the player but should not automatically become collectible sources.

### C — Non-recordable presentation

Examples:

- non-diegetic score;
- menu sounds;
- debug cues;
- UI acknowledgement sounds.

These should never leak into Malo's cassette unless a specific narrative exception is designed.

---

# Spatial capture principle

Future temporal capture should preserve the consequence of where Malo stands.

Desired result:

- close source -> clearer / stronger;
- far source -> more environment and lower relative source level;
- behind architecture -> appropriate attenuation / room relationship when the audio system supports it;
- moving source -> changing level/timbre over the recorded interval.

Do not turn this into a numerical microphone-aim minigame.

The player should learn by listening.

---

# Recording fragments are valid

Examples:

- Malo catches only the last half of a moped pass;
- he starts REC after the gate latch and captures only the squeak;
- Mother begins talking just before he releases R;
- the best gust happens at the end of an otherwise quiet wind recording.

These should produce valid clips.

Do not silently replace them with the full pristine source event.

---

# Metadata later worth preserving

A future temporal capture can add metadata without changing `RecordingClip.stream` playback compatibility:

- `capture_device_id`;
- `capture_profile_version`;
- `capture_zone`;
- `capture_position`;
- `capture_duration`;
- `dominant_source_ids` if cheaply available;
- overload / clipping hint;
- contextual narrative tags;
- source event timestamps only if needed for later editing mechanics.

Do not add future MK2 fields prematurely.

---

# Migration path

## Sprint 5

Keep current static-stream recording.

Goal: validate the playable first memory, Visual Slice and architecture.

## Sprint 6 candidate

Build one isolated temporal-capture proof using two or three sources only:

- Ronan voice;
- fireplace bed;
- one triggered sound such as a gate proxy.

Acceptance:

- player chooses REC start/stop;
- overlapping eligible sounds are captured over that interval;
- resulting clip remains a normal `RecordingClip`;
- playback does not feed back into capture;
- old static Recorder tests remain possible.

## Later

Add device profiles, richer microphone coloration, dynamic room acoustics and MK2 capabilities only after temporal capture itself is stable.

---

# Architectural invariant

The long-term mechanic must still read conceptually as:

`Malo intent -> Recorder FSM -> CaptureBackend -> RecordingClip`

and not:

`every world object implements its own recorder logic`.

That invariant protects BO's modular architecture as the sonic system becomes more ambitious.