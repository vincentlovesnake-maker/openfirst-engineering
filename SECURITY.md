# Security Policy

## Supported versions

Security fixes are applied to the latest revision on the default branch.
Tagged releases may receive a patch release when maintainers judge that a
widely used version is materially affected.

## Reporting a vulnerability

Do not open a public issue for a vulnerability that could expose credentials,
private data, execute unintended commands, or bypass an authorization boundary.

Use GitHub's private vulnerability reporting feature for this repository. If
that feature is unavailable, open a minimal public issue asking maintainers for
a private contact channel without including exploit details or sensitive data.

Include the affected version or commit, impact, reproduction conditions, and a
suggested containment if known. Reports will be acknowledged as capacity
allows; no fixed response or disclosure deadline is promised.

## Scope

Relevant reports include unsafe behavior in the bundled scripts, secret
exposure, path traversal, unintended mutation, validation bypass, and skill
instructions that systematically grant authority beyond the user's request.

The skill is not a security scanner or legal compliance certification system.
Incorrect use of third-party tools, production credentials, or generated
engineering recommendations is outside the repository's direct control.
