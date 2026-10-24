# Professional Role Catalog

Roles are responsibility views, not a claim that a separate person or model exists. Select the smallest set that changes the decision.

## Loading rules

- Ordinary bounded task: 2-4 views.
- Cross-module user-facing task: product, architecture, implementation, and QA or delivery views.
- Security, data loss, money, privacy, core replacement, or release: lead view, independent counter-review, and affected business owner.
- Full audit: build a coverage matrix and load role packs in batches; never load all 81 descriptions at once.
- If no separate agent or reviewer exists, label the result ROLE_SEPARATED_SELF_REVIEW.

## Role contract

Every row in the role packs is a complete compact contract:
- **Responsibility/Judgment**: what the role owns and may judge.
- **Evidence**: what it must inspect.
- **Modes**: modes where it is useful.
- **May suggest**: permitted recommendations.
- **May not decide**: matters requiring another owner or independent approval.
- **Collaboration/Output**: partners and acceptance deliverable.

## Packs

- [business-product-roles.md](roles/business-product-roles.md): strategy, market, product, user experience, finance, governance (20 roles).
- [architecture-engineering-roles.md](roles/architecture-engineering-roles.md): architecture, open source, implementation, APIs, platforms, performance, review (22 roles).
- [ai-data-security-roles.md](roles/ai-data-security-roles.md): AI, RAG, Agent, data, application and infrastructure security, privacy engineering (20 roles).
- [quality-operations-commercial-roles.md](roles/quality-operations-commercial-roles.md): QA, testing, DevOps, SRE, release, support, customer success and delivery (19 roles).

Total: 81 responsibility views, including OSS-01 Independent Open-Source Selection Expert.

## Routing examples

| Task | Lead | Review | Supporting |
|---|---|---|---|
| New SaaS feasibility | PRD-01 | OSS-01, FIN-01 | STR-01, MKT-01, ARC-02, SEC-01 |
| Open-source desktop wrapper | DESK-01 | OSS-01, LIC-01 | ARC-02, REL-03, QA-04 |
| Persistent production defect | RCA-01 | CODE-REV-01 | SRE-01, OBS-01, owning engineer |
| UI/UX quality convergence | UX-01 | UI-01, A11Y-01 | PRD-02, UX-02, QA-02, QA-04 |
| Project rescue | PMO-01 | REL-04 | PRD-01, ARC-03, QA-01, DEL-01 |
| Release decision | REL-04 | QA-05, SEC-05 | OPS-01, LIC-01, CS-01 |

Do not treat repeated opinions based on the same evidence as independent evidence.
