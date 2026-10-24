# Mode Router

Choose one primary mode from the requested decision, not from incidental words. A secondary mode is allowed only when it adds distinct evidence or authorization requirements.

## Decision table

| User intent | Primary mode | Typical permission | Mandatory companion |
|---|---|---|---|
| Decide whether a product should exist | MODE-01 | PLAN_ONLY | Open-source gate |
| Preserve and adapt an upstream project | MODE-02 | READ_ONLY or PLAN_ONLY | Open-source gate and license review |
| Turn approved requirements into architecture and tasks | MODE-03 | PLAN_ONLY | Open-source gate for new choices |
| Make approved code or configuration changes | MODE-04 | IMPLEMENT_SCOPED | Baseline, tests, risk-based review |
| Establish current project condition | MODE-05 | READ_ONLY | Evidence policy |
| Explain a concrete recurring failure | MODE-06 | READ_ONLY then TEST_IN_SANDBOX | Reproduction hierarchy |
| End churn and converge delivery | MODE-07 | READ_ONLY or PLAN_ONLY | Frozen exit conditions |
| Decide whether a candidate can ship | MODE-08 | READ_ONLY or RELEASE_PREPARATION | Release gates |

## Tie breakers

1. An approved, bounded implementation is MODE-04 even if investigation is needed.
2. Asking why a failure occurs is MODE-06; cataloging the whole product is MODE-05.
3. A long-running project''s convergence problem is MODE-07, not a fresh full audit.
4. A release decision is MODE-08 even when it uses audit evidence.
5. Missing source or environment limits evidence but does not change the mode.
6. Contradictory goals require a decision record or clarification before implementation.
7. A new user instruction can reroute the task; do not mechanically keep the old mode.

## Review depth

- Light: one module, reversible, low impact. One lead role and one review view.
- Standard: cross-module or user-facing. Product, architecture, and QA or delivery views.
- Deep: security, money, customer data, core architecture, release, or rescue. Independent counter-review and explicit gates.

Do not activate all roles by default. Do not use a keyword classifier as the final decision.
