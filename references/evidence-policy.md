# Evidence Policy

## Classification

- Fact: directly observed on the frozen baseline.
- Inference: conclusion supported by named facts and reasoning.
- Unknown: not verified, unavailable, or outside permission.
- Recommendation: proposed action, never current state.

## Status vocabulary

CONFIRMED, RISK, UNVERIFIED, PASSED, NOT_IMPLEMENTED, OUT_OF_SCOPE, RESOLVED, DISPUTED.

UNVERIFIED is neither pass nor defect. PASSED requires an applicable assertion, current baseline, actual execution or equivalent direct proof, and recorded result. RESOLVED requires retest against the resolution criteria.

## Evidence levels

- E0: unsupported statement.
- E1: claim, filename, README, screenshot, or weak indirect signal.
- E2: current static code, configuration, or schema evidence with a traceable location.
- E3: repeatable local test, build, or analysis with command or tool result and exit status.
- E4: isolated end-to-end, deployment, migration, recovery, performance, or security validation tied to the baseline.
- E5: verified production, customer, or business outcome with identity, time, lineage, and authorization.

Higher is not automatically better; evidence must be relevant.

## Finding record

Each material finding needs:

- unique ID, module or domain, finder role, status, severity, confidence;
- baseline and environment;
- object, method, evidence level, and location;
- verified fact, inference, and unknowns;
- reproduction or static proof;
- impact and affected scope;
- root cause or ROOT_CAUSE_UNKNOWN;
- smallest control or fix;
- independent retest criterion;
- duplicate link or dispute record when applicable.

Do not count one root cause repeatedly across departments. Link secondary impacts to the canonical finding.

## Current-version rule

Historical evidence is context, not current pass evidence, unless identity, relevant hashes or configuration, environment, and acceptance criteria remain equivalent. Stale evidence is historical, not failed.

## Conflict and independence

Preserve both evidence sets for disputed conclusions. Decide by relevance, reproducibility, and source authority, not vote count. Disclose when review is only a separated self-review rather than a separate agent or person.

Use scripts/evidence_check.py to validate structured finding records.

## Visual and interaction finding extension

For MODE-09 through MODE-12, or whenever a material issue is based on rendered or interactive evidence, add:

- project version or commit, route or screen, user role, viewport or DPI, browser or desktop host;
- reference design or `NOT_APPLICABLE`, actual screenshot or capture identity, and reproduction steps;
- expected and actual result;
- finding type: `VISUAL`, `LAYOUT`, `INTERACTION`, `ACCESSIBILITY`, `RESPONSIVE`, `BUSINESS_FLOW`, `DATA_BINDING`, `DEPLOYMENT_ASSET`, or `UNKNOWN`;
- root-cause evidence, smallest change scope, and regression acceptance condition.

A visual finding without an actual current capture is normally UNVERIFIED. An inaccessible environment is an UNVERIFIED coverage item, not proof that a defect exists. Cache, build, asset, service-worker, or deployment identity differences must be investigated before assigning a design root cause.
