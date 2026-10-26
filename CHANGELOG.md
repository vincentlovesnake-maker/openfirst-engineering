# Changelog

All notable changes to OpenFirst Engineering are documented in this file.

The project follows semantic versioning for tagged public releases.

## 1.2.0 - 2026-10-27

### Added

- `MODE-09 VISUAL_UX_AUDIT`, `MODE-10 DESIGN_REFERENCE_IMPLEMENTATION`, `MODE-11 VISUAL_REGRESSION`, and `MODE-12 END_TO_END_UAT` with explicit permission, evidence, stop, and handoff boundaries.
- Mode-specific references, role routing using the existing 81-role catalog, and templates for visual audit, reference implementation, regression, and UAT.
- Extended visual finding schema for route, role, viewport, browser or host, screenshots, expected and actual behavior, root-cause evidence, smallest change scope, and regression acceptance.
- Optional isolated Playwright runtime probe and repeatable fixtures covering a healthy page, overflow, UI-only fake success, reference mapping, shared-component regression, unreachable environments, and cache or asset identity changes.
- Environment-specific visual tooling guidance that discloses unavailable automated accessibility and desktop validation.

### Changed

- Expanded structured output validation and behavioral routing from eight to twelve modes while preserving compatibility for existing findings and reports.
- Kept `UI_UX_QUALITY_GATE` as the shared quality floor across lifecycle and specialized visual modes.

## 1.1.1 - 2026-10-25

### Changed

- Rewrote Skill discovery metadata to expose project audit, open-source transformation, root-cause diagnosis, UI/UX quality, project rescue, and release-readiness capabilities without turning the Skill into a generic catch-all.
- Reworked the English and Chinese README opening sections around concrete high-intent use cases and natural search language for people, GitHub search, and AI retrieval.
- Strengthened agent-facing metadata and default invocation context so automatic discovery can match the Skill to the decisions it actually supports.

## 1.1.0 - 2026-10-25

### Added

- Cross-cutting `UI_UX_QUALITY_GATE` for user-facing work without adding a conflicting ninth lifecycle mode.
- Rendered journey, state, viewport, input-method, localization, responsive, accessibility, and recovery evidence requirements.
- Canonical UI/UX root-cause taxonomy, severity rules, implementation constraints, acceptance decisions, and stop conditions.
- Dedicated UI/UX assessment template and a behavioral fixture for visually weak but functionally passing interfaces.
- Structured output validation that keeps functional, visual, interaction, and accessibility results independent.

### Changed

- Planning, implementation, audit, root-cause, rescue, release, quality-gate, README, template, and agent metadata guidance now activate the UI/UX companion gate when applicable.

## 1.0.1 - 2026-10-25

### Fixed

- Replaced shell-dependent Python wildcard compilation with `compileall` so
  the documented command and CI work consistently on Windows, Linux, and macOS.

## 1.0.0 - 2026-10-25

### Added

- Eight engineering decision and delivery modes.
- Mandatory open-source-first gate for high-duplication-risk work.
- Evidence levels, controlled status vocabulary, and finding records.
- Permission classes and mutation safety boundaries.
- Quality, release, rollback, rescue, and stop-condition guidance.
- Eighty-one professional responsibility contracts across four role packs.
- Templates for planning, implementation, open-source comparison, audit,
  release, durable project state, and rescue work.
- Read-only project inventory and structured-output validation scripts.
- Unit, integrity, scenario, behavioral, and cross-platform CI tests.
- English and Simplified Chinese project documentation.
