# MODE-08 Release Readiness

## Goal
Decide whether a frozen candidate can be released or delivered to the named audience and environment.

## Required gates
1. Candidate identity: commit, dirty state, build, artifact hashes, deployment configuration, database or migration version.
2. Critical business flows: normal, failure, duplicate, permission, recovery, and boundary behavior.
3. Security and privacy: open critical findings, secrets, authn and authz, data handling, dependencies, incident controls.
4. License and supply chain: obligations, notices, provenance, SBOM or dependency inventory, artifact source.
5. Installation or deployment: prerequisites, clean install, upgrade, rollback, uninstall or teardown, operator steps.
6. Reliability: monitoring, alerts, backup and restore, capacity assumptions, queues and scheduled work.
7. Customer delivery: scope, acceptance, support, known issues, training or runbook, commercial promises.
8. Independent approval for high-impact unresolved risks.

## Decision
- GO: every mandatory gate passes on the frozen candidate.
- CONDITIONAL_GO: no uncontrolled blocker; named controls, owners, deadlines, and customer impact are accepted.
- NO_GO: a mandatory gate fails or remains critically unverified.
- DEFER: evidence or decision authority is unavailable.

A high average score cannot override a failed mandatory gate.

Use assets/release-checklist-template.md.
