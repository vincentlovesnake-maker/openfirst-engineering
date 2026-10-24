<div align="center">

# OpenFirst Engineering

**Evidence-led, open-source-first engineering decisions for AI coding agents.**

[![Tests](https://github.com/vincentlovesnake-maker/openfirst-engineering/actions/workflows/tests.yml/badge.svg)](https://github.com/vincentlovesnake-maker/openfirst-engineering/actions/workflows/tests.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB.svg)](https://www.python.org/)
[![Skill](https://img.shields.io/badge/agent-SKILL.md-111827.svg)](SKILL.md)

[English](README.md) | [简体中文](README.zh-CN.md)

</div>

OpenFirst Engineering (OFE) is a reusable engineering skill for agents that
must decide **what to build, reuse, repair, stop, or release**. It turns broad
software requests into bounded decisions backed by current project evidence,
open-source research, explicit permissions, objective quality gates, rollback,
and verifiable completion conditions.

OFE optimizes for delivery with controlled risk, not activity, document volume,
or code generation volume.

## Why OFE exists

AI coding agents can move quickly, but speed alone does not answer the hardest
engineering questions:

- Does the requested capability already exist but remain hidden or disconnected?
- Is a maintained open-source solution safer than another custom subsystem?
- Is the current defect proven, or inferred from stale reports and mocks?
- Is a rewrite justified by benefit, license, migration cost, and rollback?
- What evidence is strong enough to call a task complete or a release ready?
- When should the agent stop instead of expanding the scope?

OFE makes those questions part of the workflow before large changes are made.

## Core capabilities

| Capability | What OFE adds |
|---|---|
| Project-state inspection | Separates current code and runtime evidence from demos, fixtures, mocks, and historical claims |
| Open-source-first selection | Checks native capability, dependencies, hidden paths, mature external solutions, adaptation, and only then minimal custom development |
| Mode routing | Selects one primary workflow based on the actual decision, not keyword matching |
| Permission control | Keeps planning and audits read-only unless implementation is explicitly authorized |
| Evidence discipline | Distinguishes facts, supported inferences, unknowns, recommendations, and disputed conclusions |
| Quality gates | Defines observable correctness, security, reliability, delivery, license, and commercial conditions |
| Minimal-change planning | Prefers the smallest justified change that preserves stable behavior and upstream compatibility |
| Release and rescue closure | Defines rollback, retest, ownership, stop conditions, and unresolved risk without manufacturing success |
| Professional review views | Provides 81 compact responsibility contracts without pretending they are separate people or agents |
| Structured validation | Includes local scripts for inventory, finding validation, and decision-report validation |

## Eight operating modes

| Mode | Use it to decide | Typical result |
|---|---|---|
| `MODE-01 PROJECT_INCEPTION` | Whether a product or capability should exist | Build, integrate, defer, or reject decision |
| `MODE-02 OPEN_SOURCE_TRANSFORMATION` | How to adapt an existing open-source system | Upstream-preserving transformation route |
| `MODE-03 ENGINEERING_PLANNING` | How an approved outcome becomes executable work | Architecture, boundaries, tasks, gates, rollback |
| `MODE-04 CONTROLLED_IMPLEMENTATION` | How to implement an explicitly approved scope | Bounded change with current-baseline verification |
| `MODE-05 PROJECT_AUDIT` | What condition a project is actually in | Evidence-backed findings and limitations |
| `MODE-06 ROOT_CAUSE_DIAGNOSIS` | Why a concrete failure persists | Reproduction, causal chain, smallest control, retest |
| `MODE-07 PROJECT_RESCUE_AND_CLOSURE` | How to stop churn and converge delivery | Frozen exit conditions and closure plan |
| `MODE-08 RELEASE_READINESS` | Whether a candidate can ship | Go, conditional go, no-go, or defer evidence |

The router selects a mode from the requested decision, project state, and
authorization. Missing source reduces confidence; it does not silently change
the task into implementation.

## Open-source-first gate

For new capabilities, dependencies, framework replacement, Agent expansion,
core refactors, and open-source transformation, OFE requires this order:

```text
visible native capability
        -> hidden or disconnected capability
        -> installed dependency or framework feature
        -> configuration or adapter
        -> mature external solution
        -> bounded local improvement
        -> minimal custom build
```

Serious candidates are compared on function fit, releases, maintenance,
issues and pull requests, license obligations, advisories, provenance, platform
fit, integration, migration, rollback, regional feasibility, and total cost of
ownership. Stars and polished README files are never sufficient evidence.

The allowed decisions are:

`KEEP`, `REUSE_NATIVE`, `INTEGRATE`, `IMPROVE`, `REPLACE`, `MINIMAL_BUILD`,
`DEFER`, and `REJECT`.

## Evidence model

| Level | Meaning |
|---|---|
| `E0` | Unsupported statement |
| `E1` | Claim, README, screenshot, filename, or weak indirect signal |
| `E2` | Traceable current static code, configuration, or schema evidence |
| `E3` | Repeatable local test, build, or analysis with a recorded result |
| `E4` | Isolated end-to-end, migration, recovery, performance, or security validation |
| `E5` | Authorized production, customer, or business outcome with lineage |

Required status vocabulary keeps unknowns honest:

`CONFIRMED`, `RISK`, `UNVERIFIED`, `PASSED`, `NOT_IMPLEMENTED`,
`OUT_OF_SCOPE`, `RESOLVED`, and `DISPUTED`.

`UNVERIFIED` is neither a pass nor a defect. `PASSED` requires an applicable
assertion, a current baseline, actual execution or equivalent direct proof, and
a recorded result.

## Permission classes

| Permission | Boundary |
|---|---|
| `READ_ONLY` | Inspect and report; do not mutate source, configuration, or data |
| `PLAN_ONLY` | Create plans and templates outside business source; do not implement |
| `IMPLEMENT_SCOPED` | Modify only the explicitly approved scope |
| `TEST_IN_SANDBOX` | Run bounded tests without real customer or production mutation |
| `RELEASE_PREPARATION` | Prepare candidate artifacts and gates; high-impact release actions still require separate authorization |

Planning, auditing, diagnosis, and research never imply permission to edit or
deploy. Production mutation, destructive migration, credential disclosure,
license changes, real customer data, public communication, and material paid
calls require explicit authorization.

## Professional responsibility views

OFE includes 81 compact role contracts across four packs:

- business, product, UX, finance, and governance;
- architecture, engineering, desktop, build, migration, and open source;
- AI, Agent, data, privacy, application security, and supply chain security;
- QA, release, SRE, operations, support, delivery, and commercial readiness.

Roles are responsibility views, not fabricated reviewers. High-impact decisions
require an independent counter-review when real delegation exists. Otherwise,
OFE requires a separated adversarial pass and disclosure of that limitation.

## Install

### Codex on macOS or Linux

```bash
git clone https://github.com/vincentlovesnake-maker/openfirst-engineering.git \
  ~/.codex/skills/openfirst-engineering
```

### Codex on Windows PowerShell

```powershell
git clone https://github.com/vincentlovesnake-maker/openfirst-engineering.git "$HOME\.codex\skills\openfirst-engineering"
```

Restart or refresh the agent after installation. The final directory must
contain `SKILL.md` at its root.

To update an existing installation:

```bash
git -C ~/.codex/skills/openfirst-engineering pull --ff-only
```

Automatic discovery is enabled in `agents/openai.yaml`. Explicit invocation is
recommended when the mode, permissions, or evidence contract matters:

```text
$openfirst-engineering
```

## Quick-start prompts

### Open-source selection

```text
Use $openfirst-engineering. Inspect the current project before recommending
change, run the open-source-first gate, compare keep/reuse/integrate/build, and
separate confirmed facts from unverified assumptions.
```

### Read-only audit

```text
Use $openfirst-engineering in MODE-05 with READ_ONLY permission. Establish the
current baseline, identify evidence-backed findings, and do not treat historical
reports or mocks as current pass evidence.
```

### Desktop transformation

```text
Use $openfirst-engineering in MODE-02 to evaluate packaging this open-source Web
Agent as a Windows client. Preserve upstream behavior, compare mature wrappers,
and define install, update, rollback, uninstall, permissions, offline behavior,
and signing acceptance.
```

### Root-cause diagnosis

```text
Use $openfirst-engineering in MODE-06. Reproduce the failure at the narrowest
reliable layer, distinguish trigger from root cause, propose the smallest
control, and define an independent retest condition.
```

### Release decision

```text
Use $openfirst-engineering in MODE-08. Freeze the candidate identity and release
gates before scoring. Return GO, CONDITIONAL_GO, NO_GO, or DEFER with actual
verification evidence and rollback.
```

## Output contract

An OFE decision should include, in the shortest useful form:

- selected mode and permission;
- frozen baseline and scope;
- facts, inferences, unknowns, and recommendations;
- existing or native capability findings;
- open-source gate result when triggered;
- options and an explicit decision;
- tasks with owner role, boundary, dependencies, acceptance, rollback, and done condition;
- independent review result or disclosed self-review limitation;
- verification actually run and evidence not yet obtained;
- completion state: `COMPLETE`, `PARTIAL`, `BLOCKED`, `DEFERRED`, or `NO_CHANGE_NEEDED`.

## Included tools

The helper scripts use only the Python standard library and intentionally make
no network requests.

```bash
# Read-only project inventory
python scripts/inventory.py /path/to/project

# Finding-record validation
python scripts/evidence_check.py findings.json --root /path/to/project

# Decision-output validation
python scripts/validate_outputs.py report.json
```

Inventory excludes known secret files, caches, build outputs, vendor trees, and
browser profiles. Validators check structure and evidence rules without
pretending to judge whether a conclusion is true.

## Templates

Reusable assets are included for open-source comparisons, project plans,
durable project state, implementation tasks, audits, release checklists, and
rescue plans. Templates are scaffolding, not evidence.

## Repository layout

```text
SKILL.md                         Main workflow and mode router
agents/openai.yaml               Agent-facing metadata and invocation policy
references/                      Mode, evidence, safety, quality, and role rules
references/roles/                81 professional responsibility contracts
assets/                          Reusable decision and delivery templates
scripts/                         Read-only inventory and validation helpers
tests/                           Unit, integrity, scenario, and behavioral tests
.github/workflows/tests.yml      Cross-platform CI
```

## Development and validation

Python 3.10 or newer is recommended. The test suite has no third-party runtime
dependencies.

```bash
python -m unittest discover -s tests -v
python -m py_compile scripts/*.py
```

CI runs on Windows, Linux, and macOS using Python 3.10 and 3.13. Tests cover
evidence rules, mode and permission boundaries, open-source decisions, all 81
role contracts, read-only inventory behavior, output validation, broken-project
ground truth, and reference integrity.

## What OFE does not claim

OFE is not legal advice, a security certification, or a release authority. It
does not grant access to secrets, customer data, production systems, or paid
APIs. It does not justify replacing a stable system merely because a newer
project exists, and it does not turn an implementer's opinion into independent
approval.

## Contributing

Focused contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md),
[SECURITY.md](SECURITY.md), and the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

Licensed under the [Apache License 2.0](LICENSE). Attribution information is in
[NOTICE](NOTICE).
