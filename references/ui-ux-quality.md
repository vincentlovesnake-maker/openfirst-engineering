# UI/UX Quality Gate

## Purpose

Provide evidence-led constraints for auditing, planning, implementing, rescuing, or releasing user-facing interfaces without turning one complaint into an unbounded redesign.

`UI_UX_QUALITY_GATE` is a companion to MODE-01 through MODE-08, not a separate lifecycle mode.

## Activation

Activate the gate when work affects or judges:

- visual hierarchy, layout, typography, color, density, or product presentation;
- forms, navigation, workflows, dashboards, editors, administration, onboarding, or empty states;
- responsive, mobile, desktop, embedded WebView, zoom, or high-DPI behavior;
- loading, success, validation, failure, timeout, permission, destructive action, or recovery behavior;
- keyboard, focus, semantics, assistive use, localization layout, motion, or user-facing performance.

Do not activate it for backend-only or infrastructure-only work unless a user-visible contract changes. Record `NOT_APPLICABLE` rather than silently omitting the decision for a release that contains a user interface.

## Freeze the interface contract

Before scoring, redesign, or implementation, identify:

- repository, commit, build, route or screen, data, account or permission, and environment;
- surface type: marketing, task or workbench, content or reading, or immersive experience;
- target users, usage context, top tasks, success endpoints, and destructive or high-risk actions;
- incumbent product and design constraints, native platform conventions, component system, and brand requirements;
- representative journeys, relevant states, input methods, viewports, devices, zoom or DPI, locales, and reduced-motion needs;
- exact permission, in-scope surfaces, protected business behavior, exclusions, and propagation boundary.

If the baseline cannot be identified, report `BLOCKED` or `UNVERIFIED`; do not combine screenshots or findings from different builds as one current interface.

## Evidence order

1. Inspect incumbent product truth: real components, design tokens, routes, data states, and nearby patterns.
2. Review actual rendered evidence from surfaces and journeys before deterministic detectors when possible, so automated findings do not anchor the design critique.
3. Run deterministic checks for geometry, accessibility, console or network failures, performance, and source ownership.
4. Merge duplicate symptoms under the smallest supported root cause.
5. Compare before and after only on equivalent build, data, viewport, locale, and permission conditions.

Source inspection is E2 evidence. A named screenshot is E1 unless identity and state are traceable. Repeatable browser geometry or interaction checks are normally E3; isolated end-to-end journey evidence may reach E4. Production or customer outcome requires E5 and authorization.

## Minimum coverage matrix

Choose representative coverage proportional to risk, but do not omit a relevant failure class merely to obtain a pass.

| Dimension | Required questions |
|---|---|
| Users | Can a first-time user, frequent operator, and affected reviewer or administrator complete their relevant tasks? |
| Journeys | Is the goal, entry, primary decision, submission, success endpoint, and recovery path observable? |
| Data | Do empty, single, dense, long-text, long-token, zero, unmeasured, and unconfigured states remain truthful and usable? |
| System states | Are loading, success, validation, server or network failure, timeout, permission denial, retry, and destructive confirmation handled? |
| Presentation | Are hierarchy, typography, spacing, color, contrast, surfaces, icons, density, and product specificity coherent? |
| Viewports | Do the approved desktop, laptop, tablet, mobile, embedded, zoom, or DPI targets avoid clipping, overlap, and inaccessible actions? |
| Input | Can applicable mouse, touch, keyboard, and assistive workflows reach, operate, escape, and recover? |
| Language | Do localization, fallback text, long labels, dates, numbers, and error copy preserve meaning and layout? |

## Root-cause taxonomy

Use one canonical root finding where possible:

- `UI-RC-01` design-token or style ownership conflict;
- `UI-RC-02` cascade, selector, or page-override conflict;
- `UI-RC-03` DOM or component structure incompatible with real data or states;
- `UI-RC-04` hierarchy, typography, spacing, color, density, or surface imbalance;
- `UI-RC-05` unclear task priority, action hierarchy, navigation, or information architecture;
- `UI-RC-06` missing feedback, state preservation, error recovery, or destructive protection;
- `UI-RC-07` mechanical scaling, stacking, clipping, or device adaptation failure;
- `UI-RC-08` keyboard, focus, semantics, contrast, motion, or assistive-use failure;
- `UI-RC-09` design artifact, demo content, or visual contract diverges from real product behavior;
- `UI-RC-10` duplicated page-level implementation or missing reusable component contract;
- `UI-RC-11` latency, layout shift, blocking work, or resource behavior harms interaction;
- `UI-RC-12` unknown cause requiring narrower reproduction.

Do not use “looks cheap,” “not modern,” or a detector warning as a root cause. Record observation, affected journey, evidence, causal mechanism, smallest repair boundary, and retest.

## Severity

- `P0`: data loss, unsafe or irreversible action, security or privacy exposure, or a mandatory journey inaccessible to the intended audience.
- `P1`: core journey blocked, essential action unavailable, severe layout or state failure, or no viable recovery.
- `P2`: substantial friction, unclear action hierarchy, material inconsistency, poor responsive behavior, weak feedback, or visibly unprofessional presentation.
- `P3`: local polish, copy, alignment, motion, or noncritical consistency issue.

Severity reflects user and delivery impact, not the number of affected selectors or screenshots.

## Open-source and native-first interface decisions

Before adding a framework, design system, component library, icon pack, font package, or interaction runtime:

1. inspect the current design system, platform controls, installed dependencies, hidden components, and existing interaction modules;
2. determine whether configuration, extraction, adaptation, or a bounded component contract solves the problem;
3. run the open-source-first gate when a third party or replacement is material;
4. compare bundle, accessibility, maintenance, license, migration, theming, localization, testability, and rollback costs;
5. justify custom implementation only after native and mature options fail the frozen acceptance conditions.

## Implementation constraints

- Preserve explicit product intent, factual content, business behavior, permissions, and native platform expectations.
- Do not redesign the whole product from one screenshot or one broken page.
- Do not hide or delete real capability to make a surface appear clean.
- Do not use a framework replacement to avoid diagnosing component ownership, CSS, state, or information architecture.
- Do not add another global stylesheet, token source, or design system without resolving ownership and migration.
- Do not use site-wide scaling to repair responsive or high-DPI defects.
- Do not accumulate broad selectors, page-specific copies, or `!important` as the primary architecture.
- Do not add cards, gradients, shadows, animation, or decorative media to disguise weak hierarchy or workflow design.
- Do not treat demo data, mocks, placeholder success, or static prototypes as a working product state.
- Prefer a shell and component contract, then validate one or two representative journeys before propagation by component family.
- Keep UI changes separate from backend, database, permission, billing, or state-machine changes unless those changes are explicitly approved and necessary.

## Accessibility floor

Use the applicable standard and platform guidance. Unless a stricter approved contract applies:

- normal text contrast is at least 4.5:1 and large text at least 3:1, subject to documented exceptions;
- meaningful non-text boundaries and focus indicators have sufficient contrast;
- keyboard focus is visible, ordered, not trapped, and not obscured;
- custom controls expose correct semantics, names, states, and keyboard behavior;
- pointer targets meet the applicable minimum; prefer at least 44 by 44 CSS pixels for primary touch controls, while documented inline or spacing exceptions may use the standard minimum;
- zoom, text resize, long content, localization, and reduced motion do not remove essential information or action access;
- color, hover, animation, or position alone does not carry required meaning.

Automated scans support but do not replace manual keyboard, focus, screen-reader, zoom, and visual review.

## Acceptance gates

Freeze measurable gates before implementation. A representative acceptance set includes:

- no open P0 or P1 in the approved journeys;
- no unintended horizontal overflow, zero-width content, overlap, clipping, unreachable action, or unreadable wrapping at target conditions;
- a clear primary action, distinguishable secondary and destructive actions, and no misleading disabled or success state;
- immediate or appropriately progressive feedback for submitted work, loading, completion, failure, timeout, and retry;
- user input and context preserved after recoverable failure;
- empty and permission states explain cause, impact, and next available action without inventing capability;
- keyboard completion of applicable core journeys, visible focus, predictable escape and return, and no focus trap;
- truthful data and status language across UI, service, and stored result;
- no new unexpected console errors, failed requests, layout shifts, or material performance regression;
- functional, visual, interaction, and accessibility results recorded separately;
- pilot acceptance before wider propagation.

## Decisions

Use one explicit result:

- `UI_QUALITY_ACCEPTANCE_READY`: approved scope passes functional, visual, interaction, and accessibility gates on the frozen baseline;
- `UI_QUALITY_PARTIAL`: useful progress exists, but named noncritical work or evidence remains;
- `UI_QUALITY_BLOCKED`: required baseline, environment, evidence, authority, or dependency is unavailable;
- `UI_QUALITY_REJECTED`: a mandatory gate fails or the proposed approach creates unacceptable risk;
- `NO_UI_CHANGE_NEEDED`: current interface satisfies the frozen requirement with adequate evidence;
- `NOT_APPLICABLE`: the task has no user-facing effect.

`UI_QUALITY_ACCEPTANCE_READY` does not grant production deployment permission.

## Required output

Include primary mode and permission, interface baseline, surface type, users and journeys, states, viewports and input methods, rendered and deterministic evidence, canonical findings, separate functional/visual/interaction/accessibility results, open-source or native-reuse decision when triggered, pilot and propagation boundary, unresolved conditions, decision, rollback, and retest criteria.

Use [../assets/ui-ux-audit-template.md](../assets/ui-ux-audit-template.md) for a dedicated assessment.

## Stop conditions

Stop the affected work when the baseline is not unique, representative rendering cannot be obtained, the requested appearance requires falsifying or hiding product behavior, the repair requires an unapproved business or data change, a framework or design-system replacement has not passed the open-source gate, or the pilot still fails manual visual or journey review after bounded repair.
