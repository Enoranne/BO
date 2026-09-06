# Christmas1982 — First Recording Presentation Lock

Sprint 4 does not add a new gameplay system. It makes the existing loop readable on screen.

## Beat order

1. **FIND_FISHER** — HUD objective: `Find the Fisher Price`.
2. **RECORD_RONAN** — triggered only after Malo equips the Fisher Price.
3. **PLAY_RECORDING** — triggered only when a clip from `ronan_test` is created.
4. **COMPLETE** — triggered after that clip enters PLAY and returns to STOP.

## Device readability

- The world Fisher Price disappears after pickup as before.
- A simple carried Fisher Price placeholder appears on Malo.
- The carried device binds to the same `Recorder` instance that owns STOP / REC / PLAY.
- Its red REC lamp is visible only while Recorder state is `REC`.
- No inventory slot, equipment menu, or second device system is introduced.

## Ownership rules

- `MaloController` owns player intent and equips the Recorder.
- `FisherPriceVisual` is presentation only and observes Recorder state.
- `Christmas1982Director` observes existing signals and advances only the first-recording presentation beat.
- `HUD` renders the objective; it does not decide progression.

This keeps the path open for a future MK2 device profile without hard-coding MK2 mechanics into Malo or the scene director.
