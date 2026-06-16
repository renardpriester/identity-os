# IdentityOS Reference Models

## Purpose

This folder contains reference models used by IdentityOS.

Reference models define reusable structures for roles, access packages, governance decisions, review patterns, risk scoring, access drift detection, and identity operating standards.

These models help explain how IdentityOS translates business context into access decisions.

---

## Current Reference Files

| Reference Model                               | Purpose                                                                                                                                                           |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Role Catalog](role-catalog.md)               | Defines sample enterprise role packages and access patterns.                                                                                                      |
| [Access Review Model](access-review-model.md) | Defines how access should be reviewed, certified, remediated, and audited over time.                                                                              |
| [Risk Scoring Model](risk-scoring-model.md)   | Defines how IdentityOS calculates identity risk using lifecycle state, access sensitivity, governance status, privilege, ownership, exceptions, and access drift. |
| [Access Drift Model](access-drift-model.md)   | Defines how IdentityOS detects access that no longer aligns with expected role, department, lifecycle state, ownership, or governance requirements.               |

---

## Role Catalog

The Role Catalog defines sample role-based access packages.

A role package may include:

* Role name
* Department
* Worker type
* Baseline access
* Application access
* Sensitive access
* Privileged access
* Risk level
* Review frequency
* Approval requirements
* Expiration requirements

The Role Catalog helps IdentityOS answer:

```text
What access should this identity receive based on business role?
```

---

## Access Review Model

The Access Review Model defines how IdentityOS validates whether access should continue over time.

It includes review types such as:

* Manager reviews
* Application owner reviews
* Privileged access reviews
* Contractor reviews
* Vendor reviews
* Exception reviews
* Non-human identity reviews
* High-risk access reviews

The Access Review Model helps IdentityOS answer:

```text
Should this identity still have this access?
```

---

## Risk Scoring Model

The Risk Scoring Model defines how IdentityOS evaluates identity-related risk.

It helps IdentityOS answer:

```text
How risky is this identity, access decision, or governance condition?
```

The model uses factors such as:

* Privileged access
* Sensitive application access
* Contractor or vendor status
* Non-human identity status
* Missing ownership
* Expired access
* Overdue access reviews
* Exception-based access
* Access outside the role package
* Access drift
* Separation of duties conflicts
* Leaver access risk
* Missing audit evidence

The Risk Scoring Model helps the Policy Engine and Governance Engine prioritize decisions, reviews, remediation, and audit attention.

---

## Access Drift Model

The Access Drift Model defines how IdentityOS detects access that no longer matches an identity’s expected access state.

It helps IdentityOS answer:

```text
Does this identity have access that no longer belongs?
```

The model evaluates conditions such as:

* Access from a previous department
* Access outside the current role package
* Privileged access no longer justified
* Contractor access after expiration
* Vendor access without sponsorship
* Exception access without expiration
* Non-human identity access without ownership
* Leaver access that remains active
* Access review decisions not remediated

The Access Drift Model helps IdentityOS detect privilege creep, stale access, excessive permissions, and unmanaged access risk.

---

## Why Reference Models Matter

Reference models make identity governance repeatable.

Without reference models, organizations often rely on manual decisions, inconsistent approvals, tribal knowledge, and one-off access patterns.

IdentityOS uses reference models to create consistency across:

* Access assignment
* Policy decisions
* Governance workflows
* Review campaigns
* Audit evidence
* Automation logic
* Risk scoring
* Access drift detection
* Risk reporting

---

## Relationship to Other IdentityOS Components

Reference models support the rest of IdentityOS.

```text
Reference Models
      ↓
Policy Engine
      ↓
Lifecycle Workflows
      ↓
Provisioning Actions
      ↓
Governance Reviews
      ↓
Risk Scoring
      ↓
Access Drift Detection
      ↓
Audit Evidence
```

The Role Catalog helps determine what access should be granted.

The Access Review Model helps determine whether access should continue.

The Risk Scoring Model helps determine how risky an identity decision is.

The Access Drift Model helps determine whether actual access still matches expected access.

Together, these models support least privilege, lifecycle automation, governance, auditability, and risk-aware identity operations.

---

## Future Reference Models

Planned reference models include:

* Application catalog
* Access package catalog
* Sensitive access catalog
* Privileged role catalog
* Exception model
* Separation of duties model
* Non-human identity model
* Contractor and vendor access model
* Access remediation model
* Identity analytics model

---

## Guiding Statement

> Reference models turn identity decisions from guesswork into repeatable architecture.
