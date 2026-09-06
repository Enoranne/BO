# BO_Ta_Vie — PISTE 0 Narrative Gameplay Beats

## Status
**DESIGN ONLY.**

This document turns known PISTE 0 memories into playable narrative beats without authorising new Sprint 5 mechanics.

The current implemented loop remains:

`Malo -> Fisher Price -> REC RonanTest -> STOP -> PLAY`

## Design thesis
PISTE 0 should not feel like a chain of quests. The player should feel that Malo is **noticing, following, recording and keeping moments**.

A good BO beat therefore works through:

1. an attractor already present in the world — sound, movement, light, character, object;
2. curiosity rather than an explicit waypoint;
3. one or two understandable actions;
4. an optional recording opportunity when appropriate;
5. a soft exit back into exploration;
6. possible later meaning through the cassette-memory system.

## Anti-quest rules
- No minimap objective markers.
- No permanent quest tracker.
- No XP, rarity or collectible score.
- No `MISSION PASSED` / `FAILED` language.
- Missing a non-critical sound must not block story progression.
- If a sound can naturally recur, let the world produce another opportunity.
- If a one-off moment is missed, the narrative may continue and the absence itself may be meaningful.
- A technically imperfect recording can still be emotionally valuable.
- The player should often discover the next interesting thing by **hearing it before seeing it**.

## Beat grammar
Each beat should preferably follow:

`NOTICE -> APPROACH -> LISTEN/ACT -> OPTIONAL REC -> REACT -> RELEASE`

Not every beat needs every step.

### NOTICE
The world makes itself interesting.

### APPROACH
The player closes distance because of curiosity, not because a waypoint says so.

### LISTEN / ACT
The player hears the source, interacts with an object, or watches a character action.

### OPTIONAL REC
If Malo has a recorder and the moment is recordable, the player may capture it.

### REACT
A character, sound, object or Malo's later annotation gives the moment meaning.

### RELEASE
Control returns quickly. The game does not freeze for a reward panel.

---

# Memory beats

## MB00 — Christmas 1982 / First Fisher Price
**Role:** canonical onboarding; only mandatory PISTE 0 recording beat currently implemented.

**Attractor:** presents, family attention, Fisher Price physical object.

**Player path:**
1. move Malo;
2. notice/take Fisher Price;
3. approach Ronan;
4. hold REC;
5. release to STOP;
6. PLAY the take.

**Capture:** `ronan_test`.

**Failure policy:** forgiving. This beat teaches the system and must not punish distance/timing harshly.

**Exit:** playback itself completes the learning loop; no reward screen.

**Future memory seed:** first successful self-made recording.

**Implementation:** Sprint 4/5 canonical loop.

---

## MB01 — Fisher mechanics fascination
**Role:** make the recorder itself a toy before it becomes a tool.

**Attractor:** chunky button clacks, moving cassette window, motor sound.

**Player activity:** press/play/stop, inspect, repeat.

**Capture:** no separate collectible required. These are device sounds framing other recordings.

**Optional micro-behaviour:** Malo may press a control again simply because it sounds satisfying.

**Failure policy:** none.

**Memory value:** establishes tactile identity of the Fisher Price.

**Implementation:** sound/presentation layer after Sprint 5 validation.

---

## MB02 — Portail / `BONJOUR`
**Role:** first iconic outdoor sound hunt and social-world glimpse.

**Attractor:** metallic gate squeak from outside/edge of garden, neighbour presence.

**Player path:** follow squeak -> approach gate -> interact/open/close -> hear or trigger neighbour `BONJOUR` beat -> optionally record.

**Capture possibilities:**
- latch only;
- squeak only;
- full latch + squeak + `BONJOUR`;
- accidental partial take.

**Preferred design:** do not tell the player which version is "correct".

**Failure policy:** gate can be operated again; neighbour line should not become an infinite vending-machine bark.

**Memory seed:** a mundane sound becomes a signature landmark.

**Future callback:** a later gate recording can carry an unexpected family voice in the background.

**Implementation:** candidate Sprint 6.4+ once temporal capture exists.

---

## MB03 — Wind / `MALO TU FAIS QUOI ?`
**Role:** teach waiting, listening and imperfect outdoor recording.

**Attractor:** rising wind in leaves before the player reaches the tree/garden area.

**Player path:** hear gust -> choose position -> optionally start REC -> wait for gust -> Mother's distant call may enter the take.

**Capture possibilities:**
- too early: mostly quiet air;
- good gust;
- wind overload/rough capture;
- call from Mother layered into the recording.

**Failure policy:** no quality score. Wind naturally returns in changing intensity.

**Memory seed:** the "mistake" of recording family bleed can become more valuable than the target sound.

**Implementation:** later garden playable phase.

---

## MB04 — Fridge / Mother
**Role:** comic domestic beat with a strong machine sound underneath.

**Attractor:** compressor hum and kitchen activity bleeding through corridor before kitchen is fully playable.

**Player path:** follow hum -> inspect fridge / hover near Mother -> interact when kitchen becomes playable -> optionally record hum or door action.

**Comedy principle:** the joke comes from Malo's obsessive attention to the wrong/boring sound while an adult is doing something ordinary around him.

**Capture possibilities:**
- compressor hum;
- door seal/open-close;
- Mother speaking over the attempt;
- cutlery/dishes bleeding in.

**Failure policy:** refrigerator cycles naturally; no reset button.

**Memory seed:** domestic machinery becomes part of childhood acoustics.

**Implementation:** later kitchen gameplay.

---

## MB05 — Ronan, suspect
**Role:** sibling play / mock detective structure.

**Attractor:** Ronan moving away, suspicious off-screen noise, or a missing/changed object.

**Player fantasy:** Malo treats Ronan like the suspect in an investigation because recording lets him collect "evidence".

**Player actions:** follow, listen from doorway, record snippets, compare what Malo thinks happened with what actually happened.

**Important:** do not build a detective evidence-board system. The comedy is imaginative role-play, not a mystery UI.

**Capture:** Ronan voice, door, footsteps, small object noise.

**Failure policy:** the scene remains funny even without a recording.

**Memory seed:** recording becomes a way Malo reframes family life into stories.

**Implementation:** post-Sprint 6 dialogue/character-life phase.

---

## MB06 — Mobylette pass-by
**Role:** make the street feel larger than the playable map.

**Attractor:** distant two-stroke engine approaching before the vehicle is visible.

**Player path:** hear approach -> run/position near boundary -> optionally start REC -> vehicle crosses the acoustic field -> fades away.

**Capture possibilities:**
- only approach;
- clean pass;
- only tail;
- gate/wind/voice overlapping.

**Failure policy:** do not instantly respawn the same moped. Another pass can occur later under world timing.

**Memory seed:** childhood fascination with catching something transient.

**Implementation:** street-edge phase, no controllable vehicle.

---

## MB07 — `Radio Malo est complètement génial`
**Role:** early transition from recording to performance/broadcast identity.

**Attractor:** Malo has accumulated a few sounds and begins speaking *to* the recorder rather than merely capturing the world.

**Player fantasy:** assemble or perform a tiny homemade "radio" moment using voice, a found sound and a jingle-like idea.

**Important scope rule:** early Radio Malo should begin as **play-acting and sequencing**, not a DAW or multitrack editor.

**Possible structure:**
1. Malo announces something;
2. a recorded sound plays;
3. Ronan reacts;
4. phrase `Radio Malo est complètement génial` becomes a recurring identity marker.

**Memory seed:** shift from documentation to authorship.

**Implementation:** later than basic cassette memory; before full MK2 creative tooling if narratively appropriate.

---

## MB08 — Édition spéciale biscuits
**Role:** comic example of Malo inventing a broadcast because ordinary life feels newsworthy.

**Attractor:** biscuits / kitchen event / family comment.

**Player fantasy:** turn a trivial domestic event into an "édition spéciale".

**Player actions:** notice event -> optionally record a short report -> seek a reaction or ambient insert.

**Failure policy:** no correct script and no dialogue grading.

**Memory seed:** Malo's creativity is not only technical; he narrativises the everyday.

**Implementation:** after simple Radio Malo performance grammar exists.

---

## MB09 — Studio enfant / boxes and lists
**Role:** externalise Malo's growing creative system physically in the bedroom.

**Attractor:** cassette boxes, handwritten labels, paper lists such as `BRUIT PORTE / PORTAIL / VENT`.

**Player activity:** review a very small set of recordings and physically classify them.

**Core boxes:**
- `CASSETTES`
- `BIEN`
- `RATÉS MAIS GARDER`

**Important:** no spreadsheet-style inventory UI.

**Micro-objective:** choose what Malo wants to keep, retry or revisit.

**Memory seed:** failed takes gain personal value.

**Implementation:** Sprint 6 physical cassette-memory surface.

---

## MB10 — `Toujours prendre le rire`
**Role:** establish one of Malo's personal creative rules.

**Attractor:** spontaneous laughter during or immediately after an intended recording.

**Design behaviour:** if laughter overlaps a take, the system must not classify it as contamination. The player can decide to keep the recording because of the laugh.

**Possible presentation:** a handwritten note or later annotation, not a tutorial popup.

**Memory seed:** teaches the player that human accidents matter more than technical cleanliness.

**Implementation:** emerges naturally from temporal capture + cassette annotation; no separate mechanic required.

---

## MB11 — Cheval / persistence
**Role:** show Malo's persistence when a result does not satisfy him.

**Attractor:** an observational moment with a sound/action that is difficult to capture as imagined.

**Player path:** attempt -> listen -> decide it is not what Malo wanted -> reposition/retry -> perhaps still keep earlier failed take.

**Important:** the lesson is not "repeat until score = 100%". It is that Malo personally chooses to try again.

**Memory seed:** creativity as stubborn experimentation.

**Implementation:** use when an appropriate horse/observational sequence exists in the playable chronology; do not force a horse mechanic into Sprint 5/6.

---

## MB12 — Television bricolage montage
**Role:** early editing instinct before formal editing tools.

**Attractor:** television image/sound and Malo's desire to recontextualise it.

**Player fantasy:** combine timing, playback and live commentary rather than operate a timeline editor.

**Presentation style:** fast, playful, handmade, Gondry-like resourcefulness.

**Memory seed:** Malo discovers that meaning changes through juxtaposition.

**Implementation:** later creative-tool phase; not Sprint 6 base archive.

---

## MB13 — Mouette / hard-to-catch exterior sound
**Role:** reward attention to distant and unpredictable sources.

**Attractor:** one or two distant calls with uncertain repetition.

**Player activity:** stop moving, listen, decide whether to wait/record.

**Failure policy:** the bird does not become a farmable icon. Some sessions may yield silence or a partial sound.

**Memory seed:** patience and the pleasure of a rare accidental capture.

**Implementation:** later outdoor sound ecology.

---

## MB14 — Tape repair
**Role:** material relationship to recorded memory.

**Attractor:** damaged/chewed tape after enough cassette use exists in the narrative.

**Player fantasy:** preserve something worth keeping rather than repair generic durability.

**Important:** not a crafting system. This is a specific intimate maintenance beat.

**Memory seed:** recordings are physical and fragile.

**Implementation:** later cassette/MK2 era, after archive value is established.

---

# Mandatory vs optional structure

## Mandatory spine
Keep very small:
- acquire Fisher Price;
- make first Ronan recording;
- listen back;
- later major device/era transitions when required by story.

## Optional discovery field
Most PISTE 0 memories should be optional or semi-optional:
- gate;
- wind;
- fridge;
- moped;
- gull;
- incidental laughs;
- alternative takes;
- domestic sound details.

The player should never need to "collect 7/10 childhood sounds" to unlock the next scene.

# Soft guidance hierarchy
When the game wants to suggest a beat, prefer this order:

1. sound cue;
2. character glance/movement;
3. lighting/composition;
4. object animation;
5. short contextual prompt only when interaction is ambiguous;
6. explicit objective text only for onboarding or accessibility fallback.

# Revisit rule
A location becomes more interesting over time when:
- a new person is present;
- a new device capability changes what Malo can do;
- a familiar sound occurs under a new context;
- an old recording gains a memory association;
- an earlier `RATÉ MAIS GARDER` becomes narratively meaningful.

Do not repopulate old rooms with arbitrary collectibles.

# Implementation gate
This document does not authorise any of these beats during Sprint 5 beyond MB00 and presentation improvements already in scope.

Sprint 6 should first prove temporal recording + cassette-memory review on a tiny scale before any broad content rollout.
