# Contributing

Thank you for helping improve OpenFirst Engineering.

## Before opening a change

- Search existing issues and pull requests.
- Keep changes focused on a demonstrated decision or workflow problem.
- Do not turn a project-specific preference into a universal rule.
- Preserve user intent, authorization boundaries, and evidence semantics.
- Add or update tests when behavior, validation, routing, or invariants change.

For substantial behavior changes, open an issue first and describe:

- the realistic request or failure being addressed;
- the current and desired behavior;
- evidence that the change improves decisions rather than wording alone;
- compatibility, migration, and rollback considerations.

## Development setup

Python 3.10 or newer is recommended. The test suite has no third-party runtime
dependencies.

```bash
python -m unittest discover -s tests -v
```

Also check that:

- every Markdown reference linked from `SKILL.md` exists;
- helper scripts remain read-only unless their contract explicitly says
  otherwise;
- helper scripts do not add hidden network access;
- fixtures contain no real credentials, customer data, or private paths;
- generated caches and local evidence are not committed.

## Pull requests

Explain the problem, the smallest justified change, tests performed, and any
remaining limitations. A pull request author should not claim independent
approval of their own major change.

By submitting a contribution, you agree that it is licensed under the Apache
License 2.0 and that you have the right to contribute it.
