# Work Handoff — Guidance, Assistance and Story/Archive Modes

## Decision summary
Do not implement BO as separate Easy / Medium / Hard campaigns.

Use **one Story Mode** with the same narrative content for everyone, plus a player-adjustable guidance profile:

- `GUIDED`
- `NATURAL` — default
- `FREE`

A separate future `ARCHIVE MODE` may allow revisiting eras, replaying or re-recording memories and experimenting without replacing Story Mode.

## What changes by guidance profile
Only presentation/support variables:
- explicitness of objectives;
- prompt frequency;
- hint escalation;
- sound-source emphasis;
- optional visual emphasis;
- timing tolerance where appropriate.

## What must not change
- story content;
- memory beats;
- endings;
- narrative rewards;
- character relationships;
- save compatibility;
- quality or value of recordings.

## Player control
Guidance must be changeable during play without restarting or losing progress.

A player may temporarily switch from FREE to GUIDED for one beat, then return to NATURAL.

## Default
`NATURAL`.

## Assistance architecture
Treat guidance as a **presentation/accessibility observer** of narrative state.

Do not:
- duplicate beat logic three times;
- put guidance state inside `Recorder`;
- create difficulty-specific recording assets;
- punish players for using more guidance;
- gate endings or achievements behind FREE mode.

## Failure/recovery
Use soft failure:
- partial recordings may be kept;
- optional opportunities may recur naturally;
- mandatory beats provide retry opportunities;
- hints escalate progressively;
- never default to `MISSION FAILED`.

See:
- `docs/GUIDANCE_ASSISTANCE_MODES.md`
- `data/guidance_profiles.json`
- `docs/MICRO_QUEST_FAILURE_RECOVERY.md`
- `data/assistance_recovery_rules.json`

## Implementation gate
Design only while Sprint 5 remains unvalidated live.
Do not implement before explicit authorisation after Sprint 5 acceptance.
