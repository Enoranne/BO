# BO_Ta_Vie — Recording Memory Callbacks

## Purpose
Define how old recordings may gain new meaning later in the story without turning recordings into conventional quest collectibles.

This is future design preparation. No callback system is implemented in Sprint 5.

## Core idea
A recording does not have one fixed meaning at capture time.

The same clip may be:
- funny when Malo is six;
- embarrassing a few years later;
- precious after a family change;
- creatively useful when building Radio Malo;
- emotionally devastating or comforting as an adult.

BO should allow recordings to **accumulate meaning across time**.

## Separation of concerns

### Raw recording
What was actually captured.

### Malo annotation
What Malo thought of it at that point in his life.

### Narrative association
What the story later reveals or attaches to it.

Do not overwrite old annotations when a later meaning appears.

Example:
- Age 6 title: `RONAN`
- Age 6 judgement: `BIEN`
- Later association: `LAST_NORMAL_CHRISTMAS` or another story-specific context

The old child label remains intact.

## Callback types

### 1. Person callback
A familiar voice reappears later.

Examples:
- Ronan laugh;
- Mother calling from another room;
- Father speaking off-axis.

The emotional shift comes from context, not UI rarity.

### 2. Place callback
A sound recalls a location.

Examples:
- gate squeak;
- bathroom resonance;
- bedroom floorboard;
- garden wind.

### 3. Object callback
A material/mechanical sound returns.

Examples:
- Fisher transport;
- cassette case click;
- MK2 button;
- old fridge compressor.

### 4. Accidental callback
A background detail that seemed irrelevant becomes meaningful later.

This is one of BO's strongest potential systems.

Example:
Malo records the gate but accidentally captures Mother calling in the distance. Years later, the voice—not the gate—is why the recording matters.

### 5. Creative callback
An old recording becomes raw material for a later creation.

Examples:
- gate rhythm used in Radio Malo;
- family voice fragment in a montage;
- wind used as texture;
- Fisher mechanism used as a jingle transition.

## Trigger philosophy
Callbacks should not all fire as pop-up notifications.

Preferred mechanisms:
- player voluntarily replays an old cassette;
- story scene causes Malo to remember a related sound;
- an old recording becomes visible on a desk/shelf;
- later device workflow suggests an old sound as creative material;
- environmental sound resembles an archived recording.

Avoid:
- `NEW MEMORY UNLOCKED!` banners;
- automatic collectible completion rewards;
- map icons for every callback;
- forced exposition immediately after each capture.

## Memory association data
A future narrative-association record may contain:
- recording id;
- association id;
- association type;
- era introduced;
- reveal condition;
- optional narrative weight;
- optional linked person/place/object/event;
- whether it is player-discovered or story-forced.

This data should remain separate from `RecordingClip`.

## Discovery states
Potential future states:

### `DORMANT`
Association exists narratively but is not yet available/relevant.

### `AVAILABLE`
Context allows the association to be discovered.

### `DISCOVERED`
Player/story has surfaced it.

### `REVISITED`
Player listened again after discovery.

Do not equate `DISCOVERED` with completion percentage.

## Adult Malo / framing potential
If the game later uses adult Malo voice-over or framing, old recordings can become anchors for narration.

Important rule:
adult interpretation should not erase childhood interpretation.

The contrast between the two is the point.

## Example lifecycle — Gate

### Age 6
Capture:
`ENCORE PORTAIL`

Judgement:
`RATÉ MAIS GARDER`

Reason:
Malo missed part of the squeak.

### Later childhood
Creative use:
Malo notices the metallic rhythm and uses it in a home-made programme/jingle.

### Adult framing
Emotional use:
The distant family voice in the same recording becomes more important than the gate.

One raw clip, three meanings.

## Example lifecycle — Ronan

### First recording
`RONAN` → `BIEN` → favourite.

### Later sibling context
The recording becomes a marker of their relationship at that age.

### Later story
A laugh or phrase may trigger a callback without altering the original cassette label.

## Design test
A callback system is successful if the player can truthfully say:

> “I kept this for one reason, but now it matters for another.”

That sentence captures the intended memory mechanic better than a collectible counter.

## Sprint 5 / Sprint 6 boundary
Sprint 5: no callback system.

Early Sprint 6: recording identity + annotations only.

Callbacks should be implemented only after recording persistence and review are stable.
