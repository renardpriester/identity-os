# IdentityOS Diagrams

## Purpose

This folder contains visual models for IdentityOS.

The diagrams explain how IdentityOS works across identity lifecycle management, policy evaluation, governance, access reviews, and enterprise identity orchestration.

These visuals are designed to help security leaders, IAM engineers, architects, auditors, and hiring managers quickly understand the system design.

---

## Diagram Index

| Diagram                                                          | Purpose                                                                                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| [High-Level Architecture](identityos-high-level-architecture.md) | Shows the overall IdentityOS system context, core engines, and identity event pipeline.                                      |
| [Joiner Workflow](joiner-workflow.md)                            | Shows how IdentityOS handles new workers, role assignment, provisioning, controls, and audit evidence.                       |
| [Mover Workflow](mover-workflow.md)                              | Shows how IdentityOS handles role changes, access realignment, privilege creep reduction, and governance.                    |
| [Leaver Workflow](leaver-workflow.md)                            | Shows how IdentityOS handles offboarding, deprovisioning, session revocation, privileged access removal, and audit evidence. |
| [Policy Engine Decision Flow](policy-engine-decision-flow.md)    | Shows how the Policy Engine evaluates identity events and generates access decisions.                                        |
| [Governance Workflow](governance-workflow.md)                    | Shows how IdentityOS handles approvals, reviews, exceptions, remediation, and evidence.                                      |
| [Access Review Cycle](access-review-cycle.md)                    | Shows how access reviews are scoped, routed, decided, remediated, evidenced, and improved over time.                         |

---

## Recommended Reading Order

For a quick understanding of IdentityOS, review the diagrams in this order:

1. [High-Level Architecture](identityos-high-level-architecture.md)
2. [Joiner Workflow](joiner-workflow.md)
3. [Mover Workflow](mover-workflow.md)
4. [Leaver Workflow](leaver-workflow.md)
5. [Policy Engine Decision Flow](policy-engine-decision-flow.md)
6. [Governance Workflow](governance-workflow.md)
7. [Access Review Cycle](access-review-cycle.md)

This order moves from system-level architecture to lifecycle workflows, policy decisions, and governance operations.

---

## Visual Coverage

The diagram set currently covers:

* Enterprise identity orchestration
* Joiner, Mover, and Leaver lifecycle events
* Policy-based access decisions
* Provisioning and deprovisioning logic
* Governance workflows
* Approval workflows
* Access reviews
* Exception handling
* Remediation tracking
* Audit evidence creation
* Analytics and reporting feedback loops

---

## Why These Diagrams Matter

Identity systems are complex because they connect people, roles, applications, access, risk, compliance, and business operations.

These diagrams make that complexity easier to understand.

They show that IdentityOS is not just an access management concept. It is a structured operating model for managing identity as a security, governance, and business capability.

---

## Guiding Statement

> Identity architecture should be understandable, explainable, and auditable.
