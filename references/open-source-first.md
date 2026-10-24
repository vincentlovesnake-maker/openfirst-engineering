# Open-Source-First Gate

## Trigger

Run for new features, technology selection, new dependencies, core refactors, framework replacement, AI or Agent expansion, open-source transformation, or likely duplicate implementation.

## Local capability first

Inspect, in order:

1. User-visible and hidden native features.
2. Existing modules, interfaces, background services, feature flags, routes, and commands.
3. Installed framework capabilities, packages, plugins, and version constraints.
4. Existing but disconnected UI, workflow, API, or data paths.
5. Configuration or adapter changes that could expose the capability.

Record each as AVAILABLE, PARTIAL, DISCONNECTED, UNUSABLE, or UNKNOWN with current-baseline evidence.

## External search

When authorized networking exists, prefer primary sources: official repository, package registry, release notes, security advisories, license text, and framework ecosystem documentation. Search GitHub or GitLab, Hugging Face when models matter, official plugins, and compatible Skills or tools.

If search is unavailable or prohibited, record SEARCH_UNAVAILABLE, list missing sources, and do not claim no solution exists.

Never run or install a candidate merely to inspect it. Review identity, source, release artifacts, install hooks, privileges, network and data access, and known advisories before execution authorization.

## Candidate evaluation

For every serious candidate record:

- capability match and missing functions;
- upstream identity, version or commit, releases, recent substantive activity;
- issue and PR responsiveness plus bus-factor signals;
- direct and transitive license, commercial or network-use obligations, provenance;
- advisories, dependency posture, install and update mechanism, signing or checksums;
- stack, API, data, and operating-system compatibility;
- offline, proxy, regional, and China-mainland feasibility when relevant;
- integration, migration, testing, rollback, operations, training, and maintenance cost;
- required privileges, telemetry, network access, and data exposure.

Stars, popularity, a polished README, or a recent commit alone are not acceptance evidence.

## Forced comparison

| Decision | Required proof |
|---|---|
| KEEP | Current behavior is adequate and change adds no net value |
| REUSE_NATIVE | Existing capability meets acceptance through configuration or exposure |
| INTEGRATE | External component has clear net benefit and acceptable obligations |
| IMPROVE | Bounded local repair is lower risk than replacement |
| REPLACE | Proven material deficiency and justified migration |
| MINIMAL_BUILD | No suitable native or external option meets the fixed requirement |
| DEFER | Value or evidence is insufficient now |
| REJECT | Security, license, compatibility, cost, or product constraints fail |

Use assets/open-source-comparison-template.md. State conditions, evidence, risks, total ownership cost, migration, and rollback.

## Emergency exception

Allow minimal containment before research only for active security, data-loss, availability, or compliance harm. Record why delay was unsafe, exact containment, expiration or review date, and deferred gate owner.
