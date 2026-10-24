# Project State Record

Maintain one authoritative record per project or product line. It prevents repeated investigation without allowing stale evidence to masquerade as current truth.

Required fields:

- project ID and product boundary;
- repository or worktree, branch, commit, dirty-state identity, build and deploy identity;
- current goal and active mode or permission;
- confirmed implementation and verified results;
- canonical blockers and accepted non-blocking risks;
- approved decisions with evidence and expiry;
- unfinished tasks with owners and dependencies;
- rejected options and reasons;
- historical issues with current status;
- next-phase entry and completion conditions.

Before reusing a result, compare baseline, relevant configuration, schema, dependencies, environment, and acceptance criterion. Revalidate only what changed or is critical. Never scan unrelated project directories by default.

Use assets/project-state-template.md.
