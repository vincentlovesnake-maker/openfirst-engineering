---
name: openfirst-engineering
description: Evidence-led, open-source-first software engineering decisions for project inception, transformation, planning, scoped implementation, audits, root-cause diagnosis, UI/UX quality, rescue and closure, and release readiness. Use when deciding what to build, reuse, repair, stop, or release; do not use for a narrow code edit whose solution and authorization are already explicit.
metadata:
  short-description: Open-source-first engineering decisions
---

# OpenFirst Engineering (OFE)

Use OFE to decide what software work is necessary, what can be reused, and what evidence is required to stop. Optimize for delivery with controlled risk, not activity or code volume.

## Non-negotiable rules

1. Preserve the user's product intent, scope, and authorization. Planning, auditing, and diagnosis are read-only unless implementation is explicitly authorized.
2. Inspect current project evidence before recommending change. Do not treat code presence, mocks, fixtures, demos, seed data, or historical reports as current working capability.
3. Apply OPEN SOURCE FIRST: existing native capability, installed dependencies, hidden or unexposed capability, mature external solutions, configuration or adaptation, then minimal custom development.
4. Do not replace a stable system merely because a newer project exists. Prove the defect, benefit, migration cost, license fit, security impact, and rollback path.
5. Separate facts, supported inferences, unknowns, and recommendations. Never convert UNVERIFIED into pass or fail.
6. Prefer the smallest change that satisfies fixed acceptance conditions. Do not turn rescue, audit, or release work into an unbounded redesign.
7. A developer or implementing agent cannot be the sole independent approver of its own major change. Record actual review independence; never claim multiple models or agents that were not used.
8. Stop when the predefined completion condition is met or when a named blocker requires user or external action. Do not keep expanding scope to improve an arbitrary score.
9. Functional correctness does not prove visual or interaction quality, and a screenshot does not prove workflow completion or accessibility. User-facing work must activate the UI/UX quality gate.

## Start every task

1. Read trustworthy project state and applicable repository instructions.
2. Identify the requested outcome, actual project root, baseline, environment, and permission class.
3. Select one primary mode using [mode-router.md](references/mode-router.md). Add a secondary mode only when it changes required evidence or deliverables.
4. Load only the references linked for that mode. Use [role-catalog.md](references/role-catalog.md) to select the smallest useful set of professional views.
5. Activate [ui-ux-quality.md](references/ui-ux-quality.md) when the task evaluates, creates, changes, rescues, or releases a user-facing interface.
6. Freeze success criteria and release or quality gates before scoring or implementation.
7. Inspect existing capability. Trigger the open-source-first gate when required.
8. Compare options, include a credible keep or native-reuse option, and use an independent counter-review for major decisions.
9. Act only within the authorized permission. Return verifiable results, limitations, completion state, and the next decision.

## Mode routing

| Mode | Use when | Required reference |
|---|---|---|
| MODE-01 PROJECT_INCEPTION | Decide whether and what to build | [project-inception.md](references/project-inception.md) |
| MODE-02 OPEN_SOURCE_TRANSFORMATION | Adapt an existing open-source system | [open-source-transformation.md](references/open-source-transformation.md) |
| MODE-03 ENGINEERING_PLANNING | Produce executable engineering architecture and tasks | [engineering-planning.md](references/engineering-planning.md) |
| MODE-04 CONTROLLED_IMPLEMENTATION | Implement an explicitly approved scope | [controlled-implementation.md](references/controlled-implementation.md) |
| MODE-05 PROJECT_AUDIT | Establish project condition independently | [project-audit.md](references/project-audit.md) |
| MODE-06 ROOT_CAUSE_DIAGNOSIS | Diagnose a repeatable or persistent failure | [root-cause-diagnosis.md](references/root-cause-diagnosis.md) |
| MODE-07 PROJECT_RESCUE_AND_CLOSURE | Stop churn and converge a long-running project | [project-rescue.md](references/project-rescue.md) |
| MODE-08 RELEASE_READINESS | Decide release or customer delivery readiness | [release-readiness.md](references/release-readiness.md) |

Use model judgment from target, permissions, and project state. Do not use keyword matching alone as a mode decision.

## UI/UX quality gate

The UI/UX gate is a cross-cutting companion, not a ninth operating mode. Keep the lifecycle decision in MODE-01 through MODE-08, then activate the gate for visual design, interaction, responsive behavior, desktop or mobile surfaces, accessibility, localization layout, frontend performance, or user-facing state and recovery work.

The gate requires a frozen interface baseline, actual rendered evidence when available, representative user journeys, state and viewport coverage, explicit functional/visual/interaction/accessibility results, and pilot acceptance before broad propagation. Do not approve interface quality from source inspection, HTTP success, detector output, or a single screenshot alone.

## Permission classes

- READ_ONLY: inspect and report; no source, configuration, or data mutation.
- PLAN_ONLY: create plans and templates outside business source; no implementation.
- IMPLEMENT_SCOPED: modify only the explicitly approved scope; preserve unrelated work.
- TEST_IN_SANDBOX: run tests in an isolated environment with bounded cost and no real customer or production mutation.
- RELEASE_PREPARATION: prepare candidate artifacts and gates; production deployment, destructive migration, commercial messages, license changes, and significant paid calls still require separate authorization.

Read [safety-and-permissions.md](references/safety-and-permissions.md) before any mutation, production-connected test, credential use, destructive action, or paid external call.

## Open-source-first gate

The gate is mandatory for new capability, technology selection, third-party introduction, framework replacement, core refactor, Agent or AI expansion, open-source transformation, or credible duplicate-development risk.

Read [open-source-first.md](references/open-source-first.md). The gate must:

1. Inspect local native capability, dependencies, services, APIs, and hidden UI or workflow paths.
2. Search authoritative ecosystems when network access is available. If it is not, record SEARCH_UNAVAILABLE.
3. Evaluate function fit, maintenance, releases, issues and PRs, security, license, platform or region fit, integration, migration, supply-chain trust, and total ownership cost.
4. Compare KEEP, REUSE_NATIVE, INTEGRATE, IMPROVE, REPLACE, MINIMAL_BUILD, DEFER, and REJECT as applicable.
5. Record evidence, assumptions, conditions, risks, migration or rollback, and why custom development is necessary if selected.

Emergency containment may precede full research only when delay would materially increase harm; record the exception and schedule the deferred gate.

## Evidence and quality

Read [evidence-policy.md](references/evidence-policy.md) for statuses, E0-E5 levels, finding records, conflict handling, and current-version rules. Read [quality-gates.md](references/quality-gates.md) before defining pass or fail, release, or completion conditions.

For user-facing work, also read [ui-ux-quality.md](references/ui-ux-quality.md) and use [ui-ux-audit-template.md](assets/ui-ux-audit-template.md) when a dedicated interface assessment is needed.

Required status vocabulary: CONFIRMED, RISK, UNVERIFIED, PASSED, NOT_IMPLEMENTED, OUT_OF_SCOPE, RESOLVED, DISPUTED.

Important conclusions include project version, object, method, evidence location, confidence, verified fact, inference, unknowns, recommendation, and retest condition. Use scripts/evidence_check.py and scripts/validate_outputs.py for structured JSON deliverables.

## Roles and independent review

Roles are responsibility views, not claims of separate people or models. Load only relevant role groups from [role-catalog.md](references/role-catalog.md). For high-impact architecture, security, data-loss, license, or replacement decisions, assign a counter-review view that did not author the proposal when real delegation is available. Otherwise perform a separated adversarial pass and disclose the limitation.

## Project memory

Use [project-state.md](references/project-state.md) and assets/project-state-template.md for durable state. Reuse reliable evidence only when the baseline and relevant environment are unchanged. Revalidate changed critical facts; do not rescan unrelated projects.

## Output contract

Return the shortest deliverable that supports the decision, but include:

- selected mode and permission;
- baseline and scope;
- facts, inferences, unknowns, and recommendations;
- existing or native capability findings;
- open-source gate result when triggered;
- UI/UX gate result, rendered evidence, pilot boundary, and separate functional, visual, interaction, and accessibility results when user-facing work is in scope;
- options and explicit decision;
- tasks with owner role, boundary, dependencies, acceptance, rollback, and definition of done;
- independent review result for major decisions;
- verification actually run, exit or result evidence, and unverified conditions;
- completion state: COMPLETE, PARTIAL, BLOCKED, DEFERRED, or NO_CHANGE_NEEDED.

Use the relevant template in assets/. Do not use document volume as evidence of completion.
