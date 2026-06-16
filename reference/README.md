# IdentityOS Reference Models

## Purpose

This folder contains reference models used by IdentityOS.

Reference models define reusable structures for roles, access packages, governance decisions, review patterns, and identity operating standards.

These models help explain how IdentityOS translates business context into access decisions.

---

## Current Reference Files

| Reference Model                               | Purpose                                                                              |
| --------------------------------------------- | ------------------------------------------------------------------------------------ |
| [Role Catalog](role-catalog.md)               | Defines sample enterprise role packages and access patterns.                         |
| [Access Review Model](access-review-model.md) | Defines how access should be reviewed, certified, remediated, and audited over time. |
| [Risk Scoring Model](risk-scoring-model.md) | Defines how IdentityOS calculates identity risk using lifecycle state, access sensitivity, governance status, privilege, ownership, exceptions, and access drift. |

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

```text id="0us1b4"
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

```text id="myc98e"
Should this identity still have this access?
```

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
* Risk reporting

---

## Relationship to Other IdentityOS Components

Reference models support the rest of IdentityOS.

```text id="ekyn30"
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
Audit Evidence
```

The Role Catalog helps determine what access should be granted.

The Access Review Model helps determine whether access should continue.

Together, they support least privilege, lifecycle automation, governance, and auditability.

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
* Risk scoring model
* Access drift model

---

## Guiding Statement

> Reference models turn identity decisions from guesswork into repeatable architecture.
