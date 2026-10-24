# MODE-06 Root Cause Diagnosis

## Goal
Find the smallest evidence-supported cause and repair boundary for a persistent failure.

## Reproduction hierarchy
1. Confirm expected behavior and exact failing observation.
2. Freeze code, build, runtime, configuration identity, data preconditions, user or permission context, and time.
3. Reproduce with the smallest safe case and capture raw result.
4. Trace across UI, API, service, queue or process, database, files, network, external provider, and deployment as relevant.
5. Distinguish product defect, configuration, deployment, environment, data, test defect, dependency behavior, and requirement conflict.
6. Form competing hypotheses and attempt to falsify them.
7. Check native or upstream fixes and mature alternatives before custom repair.
8. For an interface failure, activate [ui-ux-quality.md](ui-ux-quality.md), distinguish visual symptom from cascade, component, state, data, responsive, accessibility, or performance cause, and preserve rendered reproduction evidence.
9. Define minimal containment, fix, regression test, and rollback.

## Rules
Do not use a broad rewrite as diagnosis. Do not repeatedly retry flaky or paid operations to manufacture success. A symptom, log line, or correlation is not root cause until competing explanations are addressed.

## Stop condition
Root cause is confirmed with E3 or stronger evidence, or the remaining hypotheses and exact missing evidence are documented as UNVERIFIED.
