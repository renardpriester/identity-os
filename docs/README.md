# IdentityOS Documentation

## Purpose

This folder contains the core architecture and design documentation for IdentityOS.

The documents explain the vision, mission, principles, system architecture, lifecycle model, policy model, governance model, and roadmap for the project.

---

## Documentation Index

| Document                                    | Purpose                                                                                                                    |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Vision](vision.md)                         | Defines the future state IdentityOS is designed to support.                                                                |
| [Mission](mission.md)                       | Explains the practical mission and objectives of IdentityOS.                                                               |
| [Guiding Principles](guiding-principles.md) | Defines the principles used to guide architecture and design decisions.                                                    |
| [Architecture](architecture.md)             | Describes the high-level IdentityOS architecture and core engines.                                                         |
| [Lifecycle Engine](lifecycle-engine.md)     | Explains how IdentityOS handles Joiner, Mover, Leaver, contractor, vendor, privileged, and non-human identity events.      |
| [Policy Engine](policy-engine.md)           | Explains how IdentityOS evaluates identity attributes, business context, and governance rules to produce access decisions. |
| [Governance](governance.md)                 | Defines how IdentityOS manages access reviews, approvals, exceptions, privileged access, remediation, and audit evidence.  |
| [Roadmap](roadmap.md)                       | Outlines the phased development plan for IdentityOS.                                                                       |
| [Dashboard Concepts](dashboard-concepts.md) | Defines executive, IAM operations, governance, risk, access drift, privileged access, contractor/vendor, non-human identity, and automation dashboard concepts. |

---

## Recommended Reading Order

For a complete understanding of the IdentityOS architecture, read the documents in this order:

1. [Vision](vision.md)
2. [Mission](mission.md)
3. [Guiding Principles](guiding-principles.md)
4. [Architecture](architecture.md)
5. [Lifecycle Engine](lifecycle-engine.md)
6. [Policy Engine](policy-engine.md)
7. [Governance](governance.md)
8. [Dashboard Concepts](dashboard-concepts.md)
9. [Roadmap](roadmap.md)


This order moves from strategic purpose to system design, operational engines, governance, and future development.

---

## Documentation Themes

The IdentityOS documentation focuses on:

* Identity as the security perimeter
* Zero Trust-aligned access decisions
* Identity lifecycle automation
* Joiner, Mover, and Leaver orchestration
* Role-based access modeling
* Policy-based decision-making
* Governance and access reviews
* Privileged access control
* Contractor and vendor access control
* Non-human identity governance
* Audit evidence
* Identity risk visibility
* Enterprise scalability

---

## How These Documents Work Together

The documents are connected.

```text id="fc3rqm"
Vision
  ↓
Mission
  ↓
Guiding Principles
  ↓
Architecture
  ↓
Lifecycle Engine
  ↓
Policy Engine
  ↓
Governance
  ↓
Roadmap
```

Each document builds on the previous one.

Together, they define the IdentityOS operating model.

---

## Relationship to Other Folders

The documentation folder connects to the rest of the project.

| Folder        | Relationship                                                                     |
| ------------- | -------------------------------------------------------------------------------- |
| `diagrams/`   | Provides visual models for the architecture and workflows.                       |
| `reference/`  | Provides reusable reference models such as role catalog and access review model. |
| `examples/`   | Provides sample identity events and policy decisions.                            |
| `automation/` | Provides prototype scripts that demonstrate IdentityOS logic.                    |

---

## Guiding Statement

> Strong identity systems begin with clear architecture.
