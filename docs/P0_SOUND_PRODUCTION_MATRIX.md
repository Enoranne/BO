# BO_Ta_Vie — P0 Sound Production Matrix

## Purpose
Turn the P0 sonic design into a concrete production plan before adding more audio files or implementing temporal capture.

This document is planning only. It does **not** expand Sprint 5 gameplay scope. `ronan_test` remains the only required recording source for Sprint 5 acceptance.

## Production rule
Do not build three permanent libraries for WORLD / FISHER CAPTURE / CASSETTE PLAYBACK.

Preferred model:

1. preserve one high-quality WORLD master family;
2. route/capture it through the future Fisher microphone path;
3. apply cassette playback coloration nondestructively;
4. render preview derivatives only when useful for approval.

This saves storage, avoids drift between duplicate assets, and keeps future MK2 behavior possible without re-authoring every source.

## Source preference
For identity-critical P0 sounds, prefer in this order:

1. original field recording;
2. original Foley recording;
3. licensed library with documented provenance;
4. procedural/synthetic layers for nonliteral support only;
5. AI-generated sound only as a reviewed fallback.

No Higgsfield audio generation is required for this plan.

## Master format
- WAV.
- 48 kHz.
- 24-bit where available.
- no destructive normalization of source masters.
- mono for tightly localised sources unless stereo information is meaningful.
- stereo for ambience beds or pass-bys where movement/space is intrinsic.

## Family matrix

| Family | Priority | Minimum | Ideal | Preferred source | Main production risk |
|---|---:|---:|---:|---|---|
| Ronan first recording | P0 | 3 | 5 | controlled/original voice | losing intelligibility after Fisher coloration |
| Fisher button mechanics | P0 | 8 | 12 | Foley / real mechanics | sounding like modern UI clicks |
| Fisher transport | P0 | 6 | 8 | Foley / cassette mechanics | states not distinguishable by ear |
| Fireplace | P0 | 2 beds + sweeteners | 4 assets+ | field/library | short obvious loops or oversized crackle |
| Gate | P0 | 6 | 10 | field recording | one pitch-shifted squeak reused everywhere |
| Garden wind/tree | P1 identity | 3 long states | 6 | field/library | constant storm-like bed |
| Fridge hum | P1 identity | 4 | 6 | period appliance/library | modern near-silent character or wrong compressor logic |
| Moped pass | P1 identity | 3 | 6 | field/period vehicle library | fake pass-by or wrong era engine character |

The machine-readable source of truth is `data/p0_sound_production_matrix.json`.

---

# 1. Ronan

## Minimum take family
- clear short phrase/laugh;
- more spontaneous off-axis take;
- quieter or slightly more distant take.

Ideal production adds two natural alternates rather than five copies of the same delivery.

## WORLD
Natural room placement. No baked cinematic reverb.

## FISHER CAPTURE
Mono, narrower bandwidth, proximity-sensitive, mild level compression. The onboarding take must remain forgiving.

## CASSETTE PLAYBACK
Add medium identity only after capture: hiss, speaker coloration, minor instability, transport framing.

## Acceptance
The player still understands the first recording after coloration.

---

# 2. Fisher Price mechanics

This family is critical because the recorder should communicate state **by sound**.

## Required identities
### REC
Heaviest physical action. Spring-loaded, committed, slightly more forceful than PLAY.

### STOP
Short, decisive, final.

### PLAY
Firm but lighter than REC.

### Release
Small physical return sounds with controlled variation.

Minimum target: two variants for REC, STOP and PLAY plus two generic release variations.

## Transport family
Separate button mechanics from internal cassette transport:
- REC transport engage;
- REC disengage;
- PLAY engage;
- PLAY disengage;
- motor start;
- motor stop.

The button and mechanism may overlap temporally in-game, but the masters should remain separable for tuning.

## Acceptance
With the screen hidden, a player should usually know whether Malo just started recording, stopped, or started playback.

---

# 3. Fireplace

## Recommended construction
Use two restrained long beds and sparse one-shot sweeteners.

Do **not** make a five-second loop with obvious repetition.

Useful layers:
- bed A — calm;
- bed B — slightly more active;
- small pop;
- ember shift.

## WORLD
Warm, low-level domestic anchor. It should support silence rather than fill it.

## FISHER CAPTURE
Closer microphone position reveals crackle. Distance loses detail. Peaks compress slightly.

## CASSETTE PLAYBACK
Fine crackle becomes softer/grainier and can merge gently with tape noise.

## Acceptance
Ronan remains clearly dominant during onboarding.

---

# 4. Gate

This should become one of BO's recurring **sonic landmarks**.

## Minimum family
- latch open;
- slow squeak A;
- slow squeak B;
- faster squeak;
- controlled close;
- latch close.

Later optional variations:
- harder close/slam;
- wind-driven movement;
- hand contact / painted metal scrape.

## WORLD
The hinge must have a memorable tonal identity.

## FISHER CAPTURE
Orientation and distance matter substantially. A thin/off-axis recording can still be valuable if recognisable.

## CASSETTE PLAYBACK
Preserve the tonal contour. Bandwidth loss should make it feel more fragile, not erase its identity.

## Critical gameplay implication
If Malo presses REC after the latch/opening transient, those earlier sounds are absent from the recording. Temporal causality is part of the mechanic.

---

# 5. Garden wind/tree

## Minimum family
Use long natural states rather than conventional short loops:
- calm leaf movement;
- medium branch movement;
- gusty sequence with natural rise/fall.

Later: isolated gust sweeteners.

## WORLD
Irregular, with quiet gaps. No permanent storm bed.

## FISHER CAPTURE
Moderate wind buffeting can occur when exposed directly to a gust. It should feel like a child's imperfect field recording, not audio failure.

## CASSETTE PLAYBACK
Fine leaf detail becomes softer broadband texture while the gust envelope remains readable.

## Acceptance
The future Mother call (`MALO TU FAIS QUOI ?`) can remain intelligible through the environment.

---

# 6. Fridge

## Minimum family
- compressor steady state A;
- compressor steady state B;
- compressor start;
- compressor stop.

Do not randomly crossfade those four files without state logic: a compressor has a temporal cycle.

## WORLD
Clearly older domestic machine character, but low enough to sit under conversation.

## FISHER CAPTURE
Low-mid content survives strongly; deep low end and upper mechanical detail reduce.

## CASSETTE PLAYBACK
Fridge drone and tape hiss can partially merge. That ambiguity is useful because the player may wonder what belongs to the room and what belongs to the medium.

---

# 7. Moped

## Minimum family
- close residential pass;
- medium pass;
- distant pass.

Prefer genuinely distinct passes rather than reversing/mirroring one recording.

## WORLD
Small, period-appropriate two-stroke moped. Modest residential speed. Convincing approach → pass → recede arc.

## FISHER CAPTURE
Timing is the mechanic. Starting REC late can capture only the receding tail.

## CASSETTE PLAYBACK
Motion/Doppler remains recognisable while low-frequency authority and engine detail are reduced.

## Acceptance
The sound expands the perceived world without implying any vehicle gameplay.

---

# Folder plan

Proposed future source-master layout:

```text
audio/
  masters/
    characters/ronan/
    devices/fisher/
    ambience/salon/
    ambience/garden/
    appliances/kitchen/
    props/gate/
    vehicles/street/
  previews/
```

Do not move `audio/ronan_test.wav` yet. It is a canonical Sprint 5 dependency and should remain stable until Work validates a migration.

## Preview derivatives
For creative approval, temporary files may later use:
- `_fisher_preview.wav`
- `_cassette_preview.wav`

They belong under `audio/previews/` and are **not** source-of-truth assets.

# Acquisition batches

## Batch A — needed first after Sprint 5 acceptance
1. Fisher REC/STOP/PLAY mechanics.
2. Fisher transport/motor.
3. Ronan alternate source takes.
4. Fireplace bed.

These improve the existing salon and recorder loop directly.

## Batch B — first micro-hub expansion
1. Gate family.
2. Garden wind states.
3. Fridge compressor family.

## Batch C — wider-world implication
1. Moped passes.
2. corridor / kitchen density sounds from the broader sound catalog.

# Quality gate
Before a sound family is marked production-ready:

1. provenance/licence is known;
2. dry master exists;
3. naming matches the catalog;
4. variation count is sufficient for its event class;
5. no destructive Fisher/cassette coloration is baked into the master;
6. it has been heard in context, not only solo;
7. for identity-critical sounds, WORLD → CAPTURE → PLAYBACK remains recognisable;
8. the family does not introduce a new Sprint 5 gameplay requirement.

# Cost discipline
Do not spend credits merely to fill this matrix.

A generated sound is justified only when:
- original recording is impractical;
- a suitable licensed source is unavailable or inferior;
- provenance can be recorded;
- the generated result passes the same in-context review as any other asset.
