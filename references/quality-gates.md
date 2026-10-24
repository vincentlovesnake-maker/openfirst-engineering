# Quality and Completion Gates

Freeze gates before implementation, scoring, or release review.

A useful gate is tied to a requirement, objectively observable, bounded in environment, time, and cost, reproducible, assigned to an owner role, and explicit about rollback or containment.

## Classification

- BLOCKER: proven violation of a mandatory product, safety, legal, data, or delivery condition.
- CONTROL_REQUIRED: material risk acceptable only with a named temporary control and deadline.
- NON_BLOCKING: useful improvement that does not prevent the current approved delivery.
- DEFERRED: intentionally postponed with rationale and reconsideration trigger.

Do not make every improvement a release blocker.

## Minimum gates by risk

- Correctness: current-baseline tests for changed and core behavior; mocks do not replace external-contract verification.
- Security and privacy: trust boundaries, authentication and authorization, secret handling, data lifecycle, dependency and advisory review.
- Reliability: failure, retry or idempotency, recovery, observability, and bounded resource behavior proportional to impact.
- Delivery: reproducible candidate identity, installation or upgrade or uninstall, deployment or rollback, and operator documentation.
- License and supply chain: provenance, obligations, source and artifact identity, dependency inventory.
- Commercial: scope, acceptance, support, cost drivers, and customer outcome evidence when commercial readiness is claimed.

## Definition of done

Include exact deliverable, excluded scope, acceptance commands or scenarios, required evidence level, accepted unresolved risks, owner, deadline if any, rollback, and stop condition.

NO_CHANGE_NEEDED is valid when current capability satisfies the frozen requirement and evidence supports keeping it.
