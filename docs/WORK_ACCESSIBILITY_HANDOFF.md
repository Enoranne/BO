# Work Handoff — Accessibility vs Guidance

## Status
Design prepared. Do not implement settings UI during Sprint 5 live acceptance unless explicitly authorised.

## Core decision
Accessibility and guidance are independent.

Guidance profiles:
- GUIDED
- NATURAL
- FREE

Accessibility options may remain enabled in any profile.

FREE must not disable:
- subtitles;
- speaker labels;
- text scaling;
- hearing-support cues;
- stronger REC-state feedback;
- future remapping/accessibility input options.

## Source files
- `docs/ACCESSIBILITY_AND_GUIDANCE_SEPARATION.md`
- `data/accessibility_settings_contract.json`
- `docs/GUIDANCE_ASSISTANCE_MODES.md`
- `docs/WORK_GUIDANCE_HANDOFF.md`

## First later implementation priority
When settings work is explicitly authorised, prefer:
1. subtitles ON/OFF;
2. speaker labels;
3. subtitle size/background;
4. UI text scale;
5. only then sound-direction/hearing-support experiments.

Do not start by redesigning Recorder input semantics.

## Sound-centric accessibility principle
BO depends heavily on listening, but accessibility must not turn every sound into an objective icon.

Use optional cues for critical authored sounds rather than constant captioning of all ambience.

## Architecture lock
Store guidance and accessibility separately.
Do not put accessibility state inside:
- `Recorder`;
- `Interactable`;
- `InteractionContext`;
- individual narrative beat data as branching content.

Presentation layers observe public state/events.

## No reward penalty
Never gate endings, achievements, memory value or story content based on accessibility options.

## Validation
Use `tests/static_validate_accessibility_design.py` once present, plus the Sprint 5 validation suite.
