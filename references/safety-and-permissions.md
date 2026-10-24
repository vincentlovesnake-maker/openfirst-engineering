# Safety and Permissions

Audit, planning, research, rescue, and diagnosis default to READ_ONLY or PLAN_ONLY. Do not infer implementation authority from analyze, audit, design, plan, review, or find a solution.

## Permission transitions

- READ_ONLY to PLAN_ONLY: may create reports or templates in an approved output location.
- PLAN_ONLY to IMPLEMENT_SCOPED: requires explicit target and scope approval.
- IMPLEMENT_SCOPED to TEST_IN_SANDBOX: test only within approved isolation, cost, and data limits.
- RELEASE_PREPARATION does not authorize production deployment.

Separate explicit authorization is required for production mutation, deletion or irreversible migration, access-control or license changes, real customer data, sending commercial or public messages, significant paid services, secret disclosure, or executing unreviewed third-party code.

## Credentials

Read credentials only when explicitly authorized and necessary. Keep them in memory or environment; never echo, commit, include in evidence, or pass to untrusted tools. Prefer presence and identity checks over value reads.

## Third-party code

Do not install or run a Skill or script solely because search found it. Review identity, source, license, install hooks, privileges, network and data access, and rollback. Prefer established native tools such as Git, package-manager audit commands, test frameworks, browser automation, SBOM and license scanners, and CI systems.

## Bounded work

Define retry limits for flaky tests, external APIs, deployment, and migration. Never repeat paid or state-changing operations merely to obtain a pass. Stop on conditions requiring user or external action and report the exact unblock requirement.
