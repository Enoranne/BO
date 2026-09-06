# BO_Ta_Vie — Cassette Library / Memory Shelf Design

## Purpose
Define how Malo's recordings become a persistent memory language without turning BO into a conventional inventory screen.

This is **Sprint 6 design preparation only**. Sprint 5 still requires only the existing `Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY` loop.

## Core fantasy
Malo is not collecting audio files.

He is building a private archive of moments he decided were worth keeping.

The cassette library should feel like a child's evolving system of order:

- imprecise;
- tactile;
- personal;
- sometimes funny;
- sometimes obsessive;
- emotionally meaningful long before it is technically organised.

The interface language should eventually inherit from real physical cassette handling, handwritten labels, piles, boxes and improvised categories rather than a modern media-library UI.

## Design principles

### 1. Every recording is valid
There is no global score for recording quality.

A technically poor recording may be emotionally valuable.

Examples:
- Ronan is too far away but laughs unexpectedly;
- the gate squeak clips slightly but Mother calls Malo in the background;
- the wind overwhelms the intended subject but creates a beautiful accident;
- a recording starts too late yet preserves a fragment Malo likes.

The game should never automatically discard such material.

### 2. Failure is editorial, not mechanical
Use labels such as:

- `BIEN`
- `RATÉ MAIS GARDER`
- `À REFAIRE`
- `IMPORTANT`
- `DRÔLE`
- `BIZARRE`

These are Malo's judgements, not system ratings.

The canonical childhood phrase `RATÉS MAIS GARDER` is a core identity marker and should eventually appear physically in the world.

### 3. The archive should emerge progressively
At six years old, Malo should not behave like a database administrator.

Early organisation can be crude:
- unnamed cassette;
- object or person label;
- one-word handwritten note;
- box/pile assignment.

Later eras can introduce richer systems:
- numbered tapes;
- sound lists;
- categories;
- favourites;
- experiments;
- edits;
- MK2-specific transformations;
- Radio Malo preparation.

### 4. Metadata exists for the game, not for the child
The internal data model may know:
- timestamp;
- era;
- zone;
- source ids;
- device;
- duration;
- nearby characters;
- capture conditions;
- derived transformations.

The player should see only what makes sense for Malo at that age.

### 5. Listening is the primary management action
Before rename, tagging or categorisation, the key action is:

`PLAY`

The player should be able to listen and decide what a recording means.

## Proposed library hierarchy

### Layer A — Tape
A physical or conceptual cassette container.

Fields later may include:
- cassette id;
- era;
- recorder/device family;
- side A / side B;
- maximum duration if physical simulation is introduced;
- handwritten label;
- visual wear;
- creation context.

Sprint 6 should not require full tape-capacity simulation unless it proves narratively valuable.

### Layer B — Recording
Backed by the existing `RecordingClip` concept.

One recording represents one REC -> STOP interval.

It may contain:
- a dominant intended source;
- accidental secondary sources;
- silence;
- mistakes;
- environmental context.

### Layer C — Memory annotation
A separate editorial layer owned by Malo/player, not by the audio source.

Examples:
- Malo's spontaneous title;
- keep state;
- favourite;
- handwritten note;
- category/box;
- emotional tag;
- later transformation history.

This should remain separable from raw `RecordingClip` so the recording can exist before Malo has named or classified it.

## Proposed keep states

### `UNREVIEWED`
Fresh recording. Malo has not listened back yet.

### `KEEP`
Worth retaining.

### `GOOD`
Malo actively likes the result.

### `FAILED_KEEP`
`RATÉ MAIS GARDER`.

The recording failed its original intention but contains something worth preserving.

### `RETRY`
Malo wants another attempt. The old take is not necessarily deleted.

### `IMPORTANT`
Narrative/emotional importance. This must not become a quest-item icon by default.

### `ARCHIVED`
Later organisational state for material no longer in the active working pile.

## Deletion rule
Default recommendation: **avoid permanent destructive deletion in early childhood gameplay**.

A child may put a cassette aside, overwrite later by mistake, lose it, or classify it as bad. A clean desktop-style Delete command would weaken the material fiction.

If deletion/overwrite enters the game later, it should be tied to the physical recording medium and create meaningful consequences.

## Naming language

Early Malo titles should favour concrete observation over polished metadata.

Examples:
- `RONAN`
- `PORTAIL`
- `VENT`
- `PORTE`
- `MAMAN CUISINE`
- `BRUIT BIZARRE`
- `RIRE RONAN`
- `MOBYLETTE`
- `ENCORE PORTAIL`
- `VENT FORT`

Later Malo can become more systematic.

Do not auto-title every recording with a perfect semantic description. That would remove authorship from the character.

## Auto-suggestion vs player naming
Recommended Sprint 6 approach:

1. system creates a private technical id;
2. a lightweight proposed child-title may be generated from dominant source/context;
3. player may accept, edit or ignore it;
4. no naming is required before playback;
5. repeated sources can naturally become `PORTAIL 2`, `ENCORE PORTAIL`, etc., depending on age/style rules.

## Favourites
A favourite is not the same as `GOOD`.

Malo may favourite:
- a technically poor laugh;
- a strange noise;
- a failed experiment;
- an emotionally important voice.

This distinction is important to BO's tone.

## Memory associations
A recording may eventually link to one or more memory associations:

- person;
- place;
- object;
- era;
- event;
- later narrative callback.

These links should emerge through play and story, not all appear as database tags on first capture.

## Physical presentation concepts
Potential later presentation modes, in preferred order:

1. cassette itself + handwritten label;
2. physical box/pile in Malo's room;
3. simple playback surface when examining a cassette;
4. optional abstract memory view only after the physical metaphor is established.

Avoid a permanent full-screen Spotify/iTunes-style library.

## Boxes / piles
Canonical childhood organisation candidates:

- `CASSETTES`
- `BIEN`
- `RATÉS MAIS GARDER`

These can begin as literal physical boxes.

A fourth temporary pile can be useful:
- `À REFAIRE`

Do not expose too many categories at six years old.

## Emotional design rule
The library succeeds if the player occasionally prefers a recording because of **what accidentally happened inside it**, not because the UI told them it was rare or high quality.

## Sprint 5 lock
Do not implement:
- cassette inventory;
- save/load persistence;
- tape capacity;
- tagging UI;
- deletion;
- auto-transcription;
- memory scoring;
- favourite UI;
- box-management mechanics.

All of the above is design preparation for Sprint 6+.
