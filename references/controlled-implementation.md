# MODE-04 Controlled Implementation

## Entry criteria
Explicit authorization identifies the target, scope, repository or environment, and acceptable side effects. A planning request alone does not satisfy entry.

## Procedure
1. Freeze baseline, worktree status, acceptance, permission, and rollback.
2. Read applicable repository instructions and inspect nearby implementation patterns.
3. Confirm reuse or open-source gate decisions; do not reopen settled choices without new evidence.
4. Make the smallest coherent change. Preserve unrelated edits, data, configuration, and stable behavior.
5. Test in the approved environment. Start narrow, then expand with blast radius.
6. Record actual commands, exit status, artifacts, and unverified paths.
7. Obtain independent review proportional to risk; the implementer cannot be sole approver of a major change.
8. Stop at the fixed scope. New findings become separate decisions unless they block acceptance.

## Required output
Changed files or components, behavior change, tests and results, risk or compatibility notes, rollback, unresolved items, and completion state.

## Failure handling
After uncertain writes, inspect actual state before retrying. Do not weaken assertions, permissions, security, or data checks to obtain a pass.
