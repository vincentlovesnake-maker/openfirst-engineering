# MODE-10 DESIGN_REFERENCE_IMPLEMENTATION

Use this mode when a screenshot, design file, prototype, or explicit visual standard must be mapped to a real product. Default permission is `PLAN_ONLY`. Move to `IMPLEMENT_SCOPED` only when the user explicitly authorizes named routes, components, and files.

## Investigate before proposing change

1. Freeze the current build, target routes, roles, states, viewports, data sources, API contracts, and reference identity.
2. Inspect the incumbent design system, tokens, component library, icons, typography, layouts, interaction modules, and nearby reusable patterns.
3. Decompose the reference into pages, components, states, layout rules, color, type, spacing, radius, shadow, iconography, tables, charts, navigation, and responsive behavior.
4. Separate decorative material from functional controls and business information. Identify reference elements that have no current product meaning.
5. Map each retained element to a real route, component owner, permission, data source, state transition, and failure or empty state.
6. Apply the open-source-first gate before adding or replacing a framework, component library, charting package, icon set, font, animation runtime, or screenshot tool.
7. Define a representative pilot, protected business behavior, propagation boundary, acceptance, rollback, and stop condition.

## Implementation rules

- Do not use static screenshots, fake pages, hard-coded success, fixtures, or invented data as proof of implementation.
- Preserve authentication, authorization, state machines, persistence, telemetry, API contracts, and real data lineage unless separately authorized.
- Prefer existing tokens and components; introduce the smallest new contract that solves repeated gaps.
- Implement one bounded representative surface before propagating shared changes.
- Verify functional, visual, interaction, responsive, and accessibility results separately.

When authorization is only planning, provide a file and component impact map, tasks, dependencies, acceptance conditions, rollback, and explicit non-authorized implementation scope. Use [../assets/design-reference-implementation-template.md](../assets/design-reference-implementation-template.md).
