# BO — Higgsfield Credit Safety Policy

## Purpose
Use Higgsfield as a useful production tool without silently spending the user's credits or batch-generating assets before the pipeline is validated.

## Default rule
**Read first. Generate/import only after the user has been informed when an action may consume credits or has unclear billing behaviour.**

## Read-only actions — normally safe to perform without a new approval
Examples:
- inspect current balance;
- list existing 3D Jutsu projects;
- read an existing project/revision;
- search the curated 3D catalog;
- inspect existing generation history when explicitly useful;
- retrieve metadata for an already-created asset/revision;
- retrieve an already-existing GLB/Blend download reference;
- inspect model constraints/cost information without submitting generation.

These actions should not be presented as proof that a mutation/generation is free.

## Mutation / generation actions — warn first
Before performing any of the following, tell the user what will be attempted and that it may consume credits if the tool does not provide a reliable zero-cost guarantee:

- image generation;
- video generation;
- audio/TTS generation;
- 3D generation;
- catalog asset import into a 3D Jutsu project when billing behaviour is not explicitly known;
- creation of multiple 3D project variants;
- batch generations;
- regeneration / upscaling / enhancement jobs;
- any workflow that submits a new Higgsfield generation job.

If a cost-preflight tool exists for the requested generation type, use it when practical before submission.

## Batch rule
Do not batch-produce BO props merely because a model/pipeline is available.

Required order:
1. one candidate;
2. inspect result;
3. validate Godot import / scale / performance / rights;
4. decide whether the pipeline is worth continuing;
5. only then consider another production candidate.

## Current exception/history
A single coffee-table catalog asset was imported into `BO_Sprint5_3_AssetPipeline` as the first technical round-trip test. The user later reported that their Higgsfield credit balance appeared unchanged.

This observation does **not** establish that all future 3D imports or generations are free.

## Credit-awareness requirement
Whenever a new Higgsfield job is proposed, prefer to state:
- what is being generated/imported;
- why it is needed now;
- whether cost is known, estimated or unknown;
- whether a cheaper/read-only alternative exists.

## Production principle
Godot remains the game runtime/source of gameplay truth. Higgsfield is an optional production pipeline. A credit-spending action must have a concrete expected benefit to BO's current production stage.
