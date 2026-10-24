# MODE-02 Open-Source Transformation

## Goal
Preserve useful upstream behavior while planning the smallest justified adaptation.

## Baseline
Record upstream URL, fork or vendor identity, commit or release, license, local changes, build and deployment identity, and available permissions. If source is missing, produce limited planning and mark source-level claims UNVERIFIED.

## Procedure
1. Run a source-level native capability inventory, including disabled, hidden, or disconnected features.
2. Map requested retain, remove, expose, adapt, and new capabilities.
3. Review architecture, extension points, update path, contribution model, and license obligations.
4. Run the open-source-first gate for desktop wrappers, plugins, integrations, AI features, or replacement proposals.
5. For user-facing adaptation, activate [ui-ux-quality.md](ui-ux-quality.md), preserve useful upstream interaction behavior and platform conventions, and identify the smallest shell or component changes needed for the target environment.
6. Compare configuration, adapter, plugin, sidecar, wrapper, maintained fork, and bounded local change.
7. Define upstream synchronization, migration, testing, packaging, update, rollback, and attribution obligations.
8. Reject changes that unnecessarily sever upstream compatibility.

## Required acceptance
For desktop packaging include install, first start, normal start, close, background lifecycle, data location, upgrade, rollback, uninstall, permissions, offline behavior, signing, and platform support. Do not claim these pass without execution evidence.

## Stop condition
A transformation route, change boundary, upstream strategy, license posture, and verification plan are fixed.
