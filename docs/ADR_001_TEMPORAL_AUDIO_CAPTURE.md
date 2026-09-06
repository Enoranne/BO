# ADR-001 — Temporal audio capture for BO

- **Status:** Proposed — validate after Sprint 5 live acceptance
- **Scope:** Future Sprint 6+ audio architecture
- **Decision owner:** BO_Ta_Vie project
- **Does this change Sprint 5 gameplay?** No

## Context

The current Recorder prototype stores the `AudioStream` supplied by the selected `RecordableSource`.

That intentionally keeps the first loop simple:

`Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY`

Long-term BO needs recordings to preserve **what actually happened between REC and STOP**.

Examples:

- gate opened during a recording;
- fireplace continuing under Ronan's voice;
- wind gust arriving late;
- fridge hum plus door opening;
- only the tail of a moped pass because Malo pressed REC too late.

Replacing those moments with complete predefined clips would undermine the central fantasy.

## Decision

The first post-Sprint-5 temporal-capture prototype should evaluate a **dedicated recordable-world audio bus captured over the real REC interval**, using Godot's bus recording facilities before considering a custom audio-mixing implementation.

The existing Recorder FSM remains the state owner.

Low-level recording should sit behind a future composition seam conceptually described as `CaptureBackend`.

`RecordingClip` should continue to expose a directly playable `AudioStream` so existing playback ownership remains simple.

## Proposed conceptual flow

`World audio event(s)`

→ eligible recordable routing

→ `RecordableWorld` bus

→ temporal capture backend while Recorder is REC

→ recorded `AudioStream`

→ `RecordingClip`

→ `RecorderPlayback` bus

→ device-specific Fisher playback treatment

## Why this direction

### Captures timing rather than catalogue identity

The clip represents the player's REC interval, not merely the ID of a discovered source.

### Naturally permits overlap

Ronan, fireplace and a distant household sound can coexist in one captured moment.

### Preserves mistakes

Late starts and early stops remain meaningful.

### Compatible with current `RecordingClip`

A rendered/captured audio stream can still populate the existing `stream` property.

### Device evolution remains possible

Capture/playback profiles can be associated with `device_id` without making Malo or world objects device-specific.

## Critical routing rule

Playback from the recorder must **not** feed the normal recordable-world capture bus.

This avoids accidental feedback and prevents Sound-on-Sound from existing before it is intentionally introduced as a later device capability.

## Interaction architecture rule

World objects do not implement Recorder state.

A gate may expose:

- an `Interactable` role for open/close;
- world audio events for latch/hinge;
- recordable routing for those events.

It must not call `Recorder.start_recording()` or construct `RecordingClip` itself.

## First proof scope

After Sprint 5 is accepted, build the smallest meaningful temporal-capture proof:

1. Ronan voice event;
2. fireplace passive ambience;
3. one triggered gate proxy sound.

The proof passes if:

- player controls exact REC start and STOP time;
- a triggered event occurring inside that interval is present;
- passive ambience can overlap it;
- an event before REC is absent;
- an event after STOP is absent;
- the result is stored as a normal playable `RecordingClip`;
- playback never loops into capture;
- existing Recorder static tests remain viable or receive a compatible test backend.

## Deferred from the first proof

- perfect microphone simulation;
- physical microphone input;
- waveform editing;
- pitch;
- Sound-on-Sound;
- multitrack;
- save/load of long audio libraries;
- automatic source recognition;
- quality scoring;
- AI audio generation at runtime.

## Alternatives considered

### Alternative A — keep one predefined clip per source

**Advantage:** extremely simple.

**Rejected as long-term architecture because:**

- ignores player timing;
- cannot naturally capture overlap;
- makes gate/wind/moped interactions feel like collectibles;
- weakens BO's core differentiator.

The approach remains useful for static unit tests and the current Ronan prototype.

### Alternative B — event recipe only

Store event IDs/timestamps and rebuild the recording during PLAY rather than storing captured audio.

**Advantages:**

- compact data;
- deterministic;
- potentially editable later.

**Risks:**

- playback can diverge from what the player originally heard;
- overlapping spatial/room behaviour must be reconstructed;
- becomes a bespoke sequencer prematurely.

Possible later use for editing mechanics, but not preferred for the first temporal-capture proof.

### Alternative C — custom PCM mixer immediately

**Advantage:** maximum control.

**Rejected for first proof because:**

- high engineering cost;
- easy to overbuild;
- unnecessary before validating the design value of temporal capture.

### Alternative D — record the entire Master bus

**Advantage:** trivial representation of everything heard.

**Rejected because:**

- UI / score / non-diegetic audio could leak into cassettes;
- recorder playback could feed itself;
- weak separation between world truth and recordable reality.

A dedicated eligible-source path is preferable.

## Consequences

### Positive

- BO recordings can become genuine moments rather than pickups;
- architecture remains compatible with device progression;
- interaction and recording stay decoupled;
- future Sound-on-Sound can be introduced deliberately.

### Costs / risks

- audio routing becomes part of gameplay architecture;
- memory usage for recorded streams must eventually be budgeted;
- long recordings will need limits or storage policy;
- Godot runtime behaviour must be profiled on target hardware;
- bus/effect ordering must be verified experimentally rather than assumed.

## Related project documents

- `docs/AUDIO_MEMORY_PIPELINE_1982.md`
- `data/audio_memory_profiles_1982.json`
- `docs/P0_INTERACTION_SOUND_CHOREOGRAPHY.md`
- `docs/INTERACTION_TAXONOMY.md`
- `docs/SOUND_BIBLE_1982.md`
- `docs/FUTURE_TEMPORAL_CAPTURE_ARCHITECTURE.md`

## Decision gate

Do **not** implement ADR-001 merely because it exists.

First complete live Sprint 5 validation.

Then evaluate the minimal three-source proof in isolation.

If temporal capture does not feel materially better than the static-source prototype, stop and reassess before broad integration.