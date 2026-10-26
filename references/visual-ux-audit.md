# MODE-09 VISUAL_UX_AUDIT

Use this mode when the primary request is to inspect the actual rendered and interactive quality of a Web or desktop product. Permission is `READ_ONLY` or `TEST_IN_SANDBOX` when bounded test state is required.

## Required workflow

1. Freeze repository, commit, build or artifact, deployment identity, browser or desktop host, viewport or DPI, locale, role, account, route, data state, cache state, and permission.
2. Build a coverage matrix by role, route, page type, critical journey, state, viewport, and input method. Sample by risk; do not silently claim full coverage.
3. Operate the real rendered surface with an available browser or desktop tool. Source inspection alone cannot support a visual pass or defect conclusion.
4. Capture traceable screenshots and, when available, console messages, network requests, response status, timing, focus order, DOM geometry, accessibility output, and stored readback.
5. Review layout, typography, spacing, color, contrast, density, consistency, responsive behavior, feedback, forms, menus, dialogs, tables, pagination, filtering, loading, empty, error, permission, and recovery states.
6. Verify that actions affect the real business layer. A DOM change or success toast is not proof of request completion, persistence, authorization, state transition, export, or delivery.
7. Check cache, build assets, flags, deployment variant, service worker, and API-contract causes before classifying a symptom as a design defect.
8. Deduplicate symptoms under the smallest supported root cause and rank by user and delivery impact.

If the current application cannot start, authenticate, reach the page, obtain representative data, or capture the required state, return `UNVERIFIED` with the missing condition. Do not infer the rendered result from source.

## Finding evidence

Use the visual finding fields defined in [evidence-policy.md](evidence-policy.md). Allowed finding types are `VISUAL`, `LAYOUT`, `INTERACTION`, `ACCESSIBILITY`, `RESPONSIVE`, `BUSINESS_FLOW`, `DATA_BINDING`, `DEPLOYMENT_ASSET`, and `UNKNOWN`.

Pixel or geometry signals are clues. A detector result needs human or rules-based interpretation against the frozen product contract before it becomes a defect.

## Output and stop

Use [../assets/visual-audit-template.md](../assets/visual-audit-template.md). Stop after the frozen matrix is covered and findings are deduplicated. A page that meets the acceptance contract may conclude `NO_UI_CHANGE_NEEDED`; do not manufacture polish work.
