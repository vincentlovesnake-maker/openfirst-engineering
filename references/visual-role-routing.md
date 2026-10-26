# Visual and UAT Role Routing

Use the smallest set that changes the decision. These are existing OFE responsibility views; this reference creates no new roles, preserves the 81-role contract, and makes no claim of separate people or models.

| Mode | Lead | Independent review | Supporting views | Required separation |
|---|---|---|---|---|
| MODE-09 VISUAL_UX_AUDIT | QA-02 or UX-01 | A11Y-01 and QA-05 for material findings | UI-01, FE-01, UX-02, QA-03, QA-04, DESK-01 when native | The person or pass that formed the visual conclusion must not be the sole approver of a release blocker. |
| MODE-10 DESIGN_REFERENCE_IMPLEMENTATION | UI-01 | UX-01 or CODE-REV-01 | FE-01, FULL-01, PRD-02, PRD-03, OSS-01, A11Y-01 | Separate reference interpretation from implementation acceptance. |
| MODE-11 VISUAL_REGRESSION | QA-03 | QA-05 or UI-01 | FE-01, BUILD-01, CONF-01, A11Y-01 | Baseline updates require review independent from the change author. |
| MODE-12 END_TO_END_UAT | QA-04 | PRD-03 and QA-05 | FULL-01, REL-04, DESK-01, UX-01, relevant security or data owner | The implementer cannot be the only business acceptance authority. |

Use `ROLE_SEPARATED_SELF_REVIEW` when real independent delegation is unavailable. Do not multiply the same screenshot, trace, or tester opinion into independent evidence.

## Routing additions

- Use OSS-01 when a design system, component library, browser tool, desktop automation dependency, screenshot-diff library, or test framework is introduced or replaced.
- Use BUILD-01 or CONF-01 when visual differences may be caused by asset hashing, cache headers, build variants, feature flags, CDN behavior, or environment configuration.
- Use PRD-02 and PRD-03 when the reference design changes task priority, workflow meaning, business status, acceptance criteria, or customer promise.
- Use DESK-01 when native windows, WebView behavior, DPI, installer state, operating-system chrome, or desktop lifecycle affects the evidence.
