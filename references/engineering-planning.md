# MODE-03 Engineering Planning

## Goal
Turn approved outcomes into executable architecture and engineering tasks without silently implementing them.

## Procedure
1. Confirm functional and non-functional requirements plus explicit exclusions.
2. Inspect the existing architecture and capability map.
3. Run the open-source-first gate for each material new capability or dependency.
4. Define system boundaries, trust boundaries, data ownership, interfaces, error semantics, observability, migration, and rollback.
5. Select the smallest architecture consistent with expected scale and operations.
6. Split tasks by dependency and owner role. Every task includes root rationale, scope, interfaces, risks, acceptance, rollback, and definition of done.
7. Freeze quality gates and integration sequence before work begins.
8. Counter-review high-impact choices and record rejected alternatives.

## Outputs
Use assets/project-plan-template.md and assets/implementation-task-template.md. The plan must distinguish decisions already approved from assumptions requiring approval.

## Stop condition
Tasks are independently executable and testable, dependencies are explicit, no unresolved decision blocks the first approved tranche, and implementation permission remains unchanged.
