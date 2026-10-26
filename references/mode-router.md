# Mode Router

Choose one primary mode from the requested decision, not from incidental words. A secondary mode is allowed only when it adds distinct evidence or authorization requirements.

## Decision table

| User intent | Primary mode | Typical permission | Mandatory companion |
|---|---|---|---|
| Decide whether a product should exist | MODE-01 | PLAN_ONLY | Open-source gate; UI/UX gate when interface assumptions affect viability |
| Preserve and adapt an upstream project | MODE-02 | READ_ONLY or PLAN_ONLY | Open-source gate, license review, and UI/UX gate for user-facing adaptation |
| Turn approved requirements into architecture and tasks | MODE-03 | PLAN_ONLY | Open-source gate for new choices; UI/UX gate for interface scope |
| Make approved code or configuration changes | MODE-04 | IMPLEMENT_SCOPED | Baseline, tests, risk-based review, and UI/UX gate when interface behavior changes |
| Establish current project condition | MODE-05 | READ_ONLY | Evidence policy and UI/UX gate when auditing user-facing surfaces |
| Explain a concrete recurring failure | MODE-06 | READ_ONLY then TEST_IN_SANDBOX | Reproduction hierarchy and UI/UX gate for interface failures |
| End churn and converge delivery | MODE-07 | READ_ONLY or PLAN_ONLY | Frozen exit conditions and UI/UX gate when interface churn is material |
| Decide whether a candidate can ship | MODE-08 | READ_ONLY or RELEASE_PREPARATION | Release gates and UI/UX gate for user-facing candidates |
| Inspect actual rendered pages and interactions for visual or UX defects | MODE-09 | READ_ONLY or TEST_IN_SANDBOX | UI/UX gate, visual evidence schema, actual browser or desktop operation |
| Plan or implement an approved reference design against real routes and data | MODE-10 | PLAN_ONLY; IMPLEMENT_SCOPED only when explicitly authorized | UI/UX gate, design-system inventory, open-source gate when adding or replacing dependencies |
| Compare UI before and after a change under equivalent conditions | MODE-11 | TEST_IN_SANDBOX | UI/UX gate, frozen baseline identity, screenshot and functional review |
| Accept or reject complete user journeys as real users | MODE-12 | TEST_IN_SANDBOX or RELEASE_PREPARATION | UI/UX gate, business readback, role isolation, real-versus-mock disclosure |

## Cross-cutting UI/UX gate

Activate `UI_UX_QUALITY_GATE` whenever the decision concerns how a user-facing surface looks, behaves, responds, communicates state, adapts across devices, or supports keyboard and assistive use. For MODE-09 through MODE-12 it is mandatory. Read [ui-ux-quality.md](ui-ux-quality.md).

Do not activate it for backend-only, infrastructure-only, or non-visual data work unless the change alters a user-visible contract. The gate may be `NOT_APPLICABLE`, but that conclusion must be explicit for a release that includes a user interface.

## Tie breakers

1. An approved, bounded implementation is MODE-04 even if investigation is needed.
2. Asking why a failure occurs is MODE-06; cataloging the whole product is MODE-05.
3. A long-running project''s convergence problem is MODE-07, not a fresh full audit.
4. A release decision is MODE-08 even when it uses audit evidence.
5. Missing source or environment limits evidence but does not change the mode.
6. Contradictory goals require a decision record or clarification before implementation.
7. A new user instruction can reroute the task; do not mechanically keep the old mode.
8. A source-only UI review remains MODE-05 with limited evidence; MODE-09 requires actual rendered operation or an explicit UNVERIFIED result.
9. MODE-10 defaults to PLAN_ONLY. A reference image or request to match it is not implementation authorization.
10. MODE-11 requires equivalent before and after conditions; otherwise classify the comparison as UNVERIFIED or non-equivalent evidence.
11. MODE-12 requires business persistence, readback, and role or boundary checks; a visible success message alone is insufficient.

## Review depth

- Light: one module, reversible, low impact. One lead role and one review view.
- Standard: cross-module or user-facing. Product, architecture, and QA or delivery views.
- Deep: security, money, customer data, core architecture, release, or rescue. Independent counter-review and explicit gates.

Do not activate all roles by default. Do not use a keyword classifier as the final decision.
