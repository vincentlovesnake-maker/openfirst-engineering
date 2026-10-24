# MODE-04 Controlled Implementation

## Entry criteria
Explicit authorization identifies the target, scope, repository or environment, and acceptable side effects. A planning request alone does not satisfy entry.

## Procedure
1. Freeze baseline, worktree status, acceptance, permission, and rollback.
2. Read applicable repository instructions and inspect nearby implementation patterns.
3. Confirm reuse or open-source gate decisions; do not reopen settled choices without new evidence.
4. For user-facing changes, activate [ui-ux-quality.md](ui-ux-quality.md), preserve the frozen interface contract, and implement the approved pilot or component family without unrelated redesign.
5. Make the smallest coherent change. Preserve unrelated edits, data, configuration, and stable behavior.
6. Test in the approved environment. Start narrow, then expand with blast radius.
7. Record actual commands, exit status, artifacts, rendered evidence, and unverified paths.
8. Obtain independent review proportional to risk; the implementer cannot be sole approver of a major change.
9. Stop at the fixed scope. New findings become separate decisions unless they block acceptance.

## Required output
Changed files or components, behavior change, tests and results, risk or compatibility notes, rollback, unresolved items, and completion state. For user-facing changes, separately report functional, visual, interaction, and accessibility results plus the pilot propagation decision.

## Failure handling
After uncertain writes, inspect actual state before retrying. Do not weaken assertions, permissions, security, or data checks to obtain a pass.
