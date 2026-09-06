# Sprint 5.3 — Higgsfield 3D Asset Pipeline

## Goal
Establish a controlled asset pipeline from Higgsfield 3D Jutsu to Godot without making Higgsfield a runtime dependency of BO.

Godot remains the game engine and source of gameplay truth. Higgsfield is used as an asset-production workspace.

## Current Higgsfield project
- Project: `BO_Sprint5_3_AssetPipeline`
- Project ID: `be670f5b-c348-42a3-b025-85e4054d0373`
- Current committed revision: `1`
- Current scene sequence: `1`

## First pipeline test
A single catalog asset was imported as a reversible technical test:

- Source search: `coffee table`
- Catalog asset name: `Coffee Table`
- Catalog asset ID: `1e3a1161-ba81-4b72-a9fd-22ca654843a1`
- Scene entity name: `BO_CoffeeTable_Test`
- Higgsfield entity ID: `20f51259-b8db-4241-8a50-e4623b047d37`
- GLB export exists at revision 1.

This asset is not yet approved as production art. It exists only to validate the full round trip.

## Required validation order
1. Inspect the asset visually in Higgsfield / 3D Jutsu.
2. Check dimensions, origin, orientation, materials and mesh complexity.
3. Export/retrieve the committed GLB.
4. Import the GLB into a non-canonical Godot test location.
5. Confirm metre scale and orientation in Godot.
6. Confirm material compatibility under BO lighting.
7. Add a simple Godot collision proxy only if the asset is accepted.
8. Compare it against the current procedural coffee-table placeholder.
9. Keep or discard the asset without touching Recorder/gameplay code.

## Acceptance criteria
The pipeline is considered validated only if:

- GLB imports cleanly into Godot 4.7.x;
- scale is believable without destructive rescaling;
- material slots survive import or are easy to remap;
- mesh complexity is reasonable for this project;
- the asset can be replaced without changing gameplay logic;
- no Higgsfield runtime dependency is introduced.

## Scope rule
Do not batch-import furniture yet. One validated object must complete the entire Higgsfield -> GLB -> Godot -> visual review loop first.

## Next action in Work / Godot-MCP
After Sprint 5.2 A/B visual validation, import the revision-1 `BO_CoffeeTable_Test` GLB into an isolated Sprint 5 test path and compare it against `Set/CoffeeTablePlaceholder`.
