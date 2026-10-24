# MODE-05 Project Audit

## Goal
Establish the current project''s actual condition and decision-relevant risks without automatic remediation.

## Phases
1. Freeze repositories, commits, dirty state, environments, builds, deployments, data stores, objectives, permissions, and exclusions.
2. Inventory backend, frontend, APIs, data, integrations, AI, deployment, operations, documentation, and commercial flows.
3. Test whether UI, service, data, and external outcomes connect; file or route existence is not completion.
4. Review architecture, code, security, privacy, license and supply chain, tests, reliability, delivery, cost, and project governance using selected roles.
5. Run authorized isolated end-to-end checks across normal, failure, repeat, permission, recovery, and boundary cases.
6. Run the open-source gate only where replacement or duplicate-development risk is material.
7. Deduplicate findings, preserve disputes, and score only after weights and gates are frozen.
8. Produce an explicit release or investment decision, not report volume.

## Status
Use CONFIRMED, RISK, UNVERIFIED, PASSED, NOT_IMPLEMENTED, OUT_OF_SCOPE, RESOLVED, DISPUTED.

## Boundary
Audit is READ_ONLY by default. Missing runtime or source limits conclusions; it does not justify invented defects or passes.

Use assets/audit-report-template.md.
