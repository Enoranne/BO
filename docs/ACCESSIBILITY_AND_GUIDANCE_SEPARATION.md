# BO_Ta_Vie — Accessibility vs Guidance

## Status
Design only. Future settings contract.

## Core decision
**Accessibility settings and guidance profile are separate axes.**

A player choosing `FREE` guidance is asking for less interpretation/help from the game, not fewer accessibility tools.

Never make accessibility a reward for choosing GUIDED or a penalty for choosing FREE.

## Guidance axis
Prepared profiles:
- GUIDED;
- NATURAL — default;
- FREE.

Guidance may alter:
- objective explicitness;
- prompt frequency;
- hint escalation;
- optional diegetic emphasis;
- timing tolerance where appropriate.

Guidance must not disable:
- subtitles;
- subtitle speaker labels;
- text scaling;
- control remapping later;
- hearing-support cues;
- visual REC state feedback;
- accessibility contrast options.

## Subtitle settings — future
Recommended independent options:
- subtitles: ON/OFF;
- speaker labels: ON/OFF;
- text size: SMALL / MEDIUM / LARGE;
- background: NONE / SOFT / STRONG;
- off-screen speaker indication: OFF / SUBTLE / ON;

Default proposal:
- subtitles ON for spoken narrative/family lines until user changes it;
- speaker labels ON for off-screen family speech;
- MEDIUM text;
- SOFT background.

Exact defaults should be playtested.

## Hearing-support cues
BO is sound-centric, so hearing accessibility needs special care without turning every sound into a quest marker.

Possible future options:
- subtle directional indicator for narratively important transient sounds;
- short semantic captions for critical non-speech sounds (`[portail grince]`, `[mobylette approche]`);
- stronger REC-state visual feedback;
- optional waveform/activity cue while recording;
- replay transcript/semantic annotation only for authored critical material if needed.

Do not caption every ambience by default.

FREE guidance may still use these accessibility cues if the player enables them.

## Visual accessibility
Future considerations:
- UI text scale;
- stronger prompt contrast;
- non-colour-only REC/STOP/PLAY distinction;
- avoid relying only on red/green state coding;
- adjustable camera motion/reduced motion if cinematic transitions later become stronger.

## Motor/accessibility considerations
Future options may include:
- remappable actions;
- hold/toggle alternative for REC if needed;
- interaction input redundancy preserved (`E` / left click currently);
- broader timing tolerance independent from narrative guidance when accessibility requires it.

Do not change Recorder semantics until actual implementation is scoped and tested.

## Cognitive load
The design already helps by:
- small verb vocabulary;
- context-first prompts;
- no giant quest tracker;
- short family barks;
- physical object states;
- progressive hinting.

Future optional support may include:
- replay last hint;
- show current intent briefly;
- pause-safe reminder after long absence.

Do not force these into FREE mode unless player enables them.

## Archive Mode
Future Archive Mode may be especially useful as a low-pressure revisit space, but it is not an accessibility substitute.

Accessibility settings must apply consistently in Story Mode and Archive Mode.

## Localization relationship
Subtitle settings operate on localization keys/content, not literal gameplay IDs.

Source dialogue may be French while UI/subtitles are localized independently.

## Work rule
When implementing settings later:
- store guidance and accessibility separately;
- do not branch narrative content by accessibility state;
- do not put accessibility settings inside Recorder or individual interactables;
- accessibility presentation should observe public state/events.
