# MODE-12 END_TO_END_UAT

Use this mode to accept or reject complete business journeys as representative users. Permission is `TEST_IN_SANDBOX` or `RELEASE_PREPARATION`; production or real-customer mutation still requires separate authorization.

## Acceptance coverage

For each critical journey, verify applicable:

- login, session expiry, logout, and role or tenant authorization;
- route discovery, navigation, deep links, back or cancel behavior;
- form validation, submission, duplicate submission, retry, and idempotency;
- request result, persistence, reload or independent readback, audit trail, and business state transition;
- loading, empty, success, validation, server failure, network failure, timeout, permission denial, and recovery;
- export, download, notification, handoff, or other promised delivery outcome;
- multi-role and multi-tenant isolation, including negative tests;
- desktop lifecycle when applicable: install, launch, close, restart, update, offline behavior, and uninstall;
- truthful distinction among real AI or Agent execution, tool calls, retrieval, simulation, mock, fixture, seed, cached, and preloaded results.

## Evidence rules

A success message or HTTP 2xx is not business completion. Correlate UI action, network or service result, stored state, subsequent read, downstream status, and user-visible outcome. Record the baseline, role, test data lineage, environment, timestamps or correlation identity, and cleanup or rollback.

Mark unavailable journeys `UNVERIFIED` with the exact missing account, environment, integration, data, permission, or tool. Do not count an unexecuted case as passed or failed.

Use [../assets/end-to-end-uat-template.md](../assets/end-to-end-uat-template.md). A UAT pass does not by itself authorize release; MODE-08 owns the release decision.
