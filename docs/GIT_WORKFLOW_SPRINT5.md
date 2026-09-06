# BO_Ta_Vie — Git Workflow for Sprint 5

## Current repository state
- Repository: `Enoranne/BO`
- Default GitHub branch: `main`
- Active development branch: `sprint-5`
- Sprint 5 base: Sprint 4 commit `41e0cfd8ec1682a7b056c343828094405911e42d`

## Core rule
**Do not resume BO development from `main`.**

Work/Codex must use the current `sprint-5` HEAD as the handoff state unless explicitly instructed otherwise.

## Why the history is granular
Sprint 5 has been prepared through many small GitHub API writes while live Work/Godot was unavailable.

This produces a large number of small, reversible commits.

That is acceptable during active preparation because:
- each change is isolated;
- rollback is easy;
- file ownership/intent remains clear;
- canonical gameplay files have been protected.

The commit count is **not** a request to review every commit chronologically.

## Work/Codex session rule
On resume:
1. checkout/fetch `sprint-5`;
2. verify HEAD/current branch;
3. read `README.md`, `SPRINT5_STATUS.md`, `AGENTS.md` and the relevant compact handoff only;
4. run `bash tests/run_sprint5_validation.sh`;
5. continue from current files;
6. do not replay or reimplement historical commits.

## Never do automatically
- reset `sprint-5` to `main`;
- recreate Sprint 1–4;
- force-push or rebase the shared branch merely to make history prettier;
- squash the active branch while Work is still validating it;
- copy only selected Sprint 5 files onto a new branch and accidentally omit contracts/data;
- treat `main` as more canonical merely because GitHub marks it default.

## Checkpoint strategy
Before substantial live-engine work, create a clear checkpoint commit after validation if there are local changes.

Suggested semantic checkpoint message:

`Sprint 5: pre-Work offline-preparation checkpoint`

Do not manufacture a no-op commit if the current HEAD is already clean and fully pushed.

## Merge strategy later
Once Sprint 5 is genuinely accepted:
1. ensure static and headless tests pass;
2. capture live visual/input evidence;
3. update `SPRINT5_STATUS.md` to accepted state;
4. create/review a PR from `sprint-5` toward the intended integration branch;
5. prefer a **squash merge** if the goal is a readable main history, because Sprint 5 contains many micro-commits;
6. preserve the original `sprint-5` branch until post-merge verification is complete.

A squash merge is a publication/history-cleanliness choice, not a reason to rewrite the working branch during development.

## What should appear in the eventual PR summary
- Sprint 5.1 Player Feel;
- Sprint 5.2 Visual Slice;
- Sprint 5.3 Higgsfield 3D integration scaffold;
- Sprint 5.4 architecture/Cyclops preparation;
- offline hardening/design contracts;
- validation evidence;
- explicit statement that core Recorder/InteractionContext/MaloController ownership was preserved;
- deferred Sprint 6+ design documents marked as non-implementation.

## Branch naming for future implementation
Do not create future sprint branches prematurely.

After Sprint 5 acceptance, possible next implementation branch:
- `sprint-6`

It should branch from the **accepted Sprint 5 integration point**, not from old `main` or old Sprint 4.

## Git hygiene principle
The repository should optimise for:
1. recoverability during active development;
2. clear ownership/contracts;
3. validated checkpoints;
4. readable integration history at merge time.

Do not optimise for a pretty commit graph at the cost of losing prepared work or breaking the active handoff.
