# Access Package Mapping

## Purpose

This document defines how IdentityOS role packages and access decisions could map to Microsoft Entra entitlement management access packages.

Access packages provide a structured way to bundle resources, policies, approvals, expiration, and governance controls around access.

IdentityOS can use access package mapping to connect lifecycle events, policy decisions, governance requirements, risk scoring, access drift detection, and audit evidence to Microsoft Entra ID Governance concepts.

---

## Mapping Objective

The objective of access package mapping is to answer:

> Which IdentityOS access decision should map to which Microsoft Entra access package, and what approval, expiration, review, and evidence controls should apply?

---

## Conceptual Model

```text id="su5l3m"
IdentityOS Lifecycle Event
        ↓
IdentityOS Policy Engine
        ↓
IdentityOS Role Package Decision
        ↓
Access Package Mapping
        ↓
Microsoft Entra Access Package
        ↓
Assignment Policy
        ↓
Approval / Expiration / Review
        ↓
Audit Evidence
```

---

## IdentityOS Role Package vs Entra Access Package

| IdentityOS Concept   | Microsoft Entra Concept                          |
| -------------------- | ------------------------------------------------ |
| Role Package         | Access Package                                   |
| Access Rule          | Assignment Policy                                |
| Approval Requirement | Approval Settings                                |
| Expiration Rule      | Assignment Expiration                            |
| Review Requirement   | Access Review                                    |
| Sponsor Requirement  | Request Approval or Sponsor Review               |
| Governance Evidence  | Access Package Assignment and Request Evidence   |
| Access Drift Check   | Expected Package vs Actual Assignment Comparison |

---

## Access Package Components

An access package mapping should define:

| Component            | Purpose                                                            |
| -------------------- | ------------------------------------------------------------------ |
| Access Package Name  | Human-readable package name.                                       |
| Business Purpose     | Why the package exists.                                            |
| Eligible Users       | Who can request or receive the package.                            |
| Resources Included   | Groups, applications, SharePoint sites, Teams, or other resources. |
| Approval Requirement | Whether manager, sponsor, owner, or security approval is needed.   |
| Assignment Duration  | How long the access should last.                                   |
| Review Frequency     | How often access should be reviewed.                               |
| Risk Level           | IdentityOS risk level associated with the package.                 |
| Evidence Requirement | Whether assignment evidence must be retained.                      |

---

## Recommended Naming Convention

Use a clear naming convention so access packages can be understood by IAM, security, governance, and business teams.

```text id="ot2h9f"
AP-[Department]-[Role]-[AccessType]-[Environment]
```

Examples:

```text id="z92bfd"
AP-Finance-Analyst-Standard-Prod
AP-Legal-Operations-Standard-Prod
AP-Security-Reader-Privileged-Prod
AP-Contractor-ProjectA-Temporary-Prod
AP-Vendor-LegalDocs-Temporary-Prod
```

---

## Sample Access Package Catalog

| IdentityOS Role Package   | Microsoft Entra Access Package          | Purpose                                                           |
| ------------------------- | --------------------------------------- | ----------------------------------------------------------------- |
| Base Employee Access      | `AP-Employee-Baseline-Standard-Prod`    | Provides standard employee access.                                |
| Finance Analyst Access    | `AP-Finance-Analyst-Standard-Prod`      | Provides Finance analyst resources and apps.                      |
| Legal Operations Access   | `AP-Legal-Operations-Standard-Prod`     | Provides Legal operations access.                                 |
| Security Reader Access    | `AP-Security-Reader-Privileged-Prod`    | Provides security visibility access with approval.                |
| Contractor Project Access | `AP-Contractor-ProjectA-Temporary-Prod` | Provides temporary contractor access.                             |
| Vendor Legal Docs Access  | `AP-Vendor-LegalDocs-Temporary-Prod`    | Provides vendor access to approved legal resources.               |
| Non-Human Identity Review | `AP-NHI-ServiceAccount-Review-Prod`     | Tracks access review for service accounts or workload identities. |

---

## Joiner Access Package Mapping

Joiner events may assign baseline or role-based access packages.

| Joiner Scenario          | Access Package                          | Governance Requirement                                    |
| ------------------------ | --------------------------------------- | --------------------------------------------------------- |
| New employee             | `AP-Employee-Baseline-Standard-Prod`    | Standard lifecycle evidence.                              |
| Finance analyst          | `AP-Finance-Analyst-Standard-Prod`      | Manager or app owner approval for sensitive finance apps. |
| Legal operations analyst | `AP-Legal-Operations-Standard-Prod`     | Legal document access review.                             |
| Security analyst         | `AP-Security-Reader-Privileged-Prod`    | Security approval and privileged review.                  |
| Contractor onboarding    | `AP-Contractor-ProjectA-Temporary-Prod` | Sponsor approval and expiration.                          |
| Vendor onboarding        | `AP-Vendor-LegalDocs-Temporary-Prod`    | Sponsor approval, expiration, and legal owner review.     |

---

## Mover Access Package Mapping

Mover events compare previous package assignments to new package requirements.

| Mover Scenario             | Remove Package                     | Add Package                          | Governance Requirement                               |
| -------------------------- | ---------------------------------- | ------------------------------------ | ---------------------------------------------------- |
| Finance to Legal           | `AP-Finance-Analyst-Standard-Prod` | `AP-Legal-Operations-Standard-Prod`  | Remove old access and review sensitive legal access. |
| Employee to Security       | Previous department package        | `AP-Security-Reader-Privileged-Prod` | Security approval required.                          |
| Contractor changes project | Old contractor package             | New project package                  | Sponsor renewal and expiration validation.           |
| Vendor scope changes       | Previous vendor package            | Updated vendor package               | Sponsor and application owner approval.              |

---

## Leaver Access Package Mapping

Leaver events should remove or expire access package assignments.

| Leaver Scenario               | Access Package Action                | Governance Requirement                             |
| ----------------------------- | ------------------------------------ | -------------------------------------------------- |
| Employee termination          | Remove all active employee packages. | Offboarding evidence required.                     |
| Contractor end date reached   | Remove or expire contractor package. | Sponsor decision required if renewal is requested. |
| Vendor contract ends          | Remove vendor package assignment.    | Vendor access closure evidence required.           |
| Privileged leaver             | Remove privileged package first.     | Security escalation and evidence required.         |
| Non-human identity retirement | Remove or review package assignment. | Owner approval and credential review required.     |

---

## Assignment Policy Mapping

Access package assignment policies define how users receive access.

| IdentityOS Requirement             | Assignment Policy Setting                              |
| ---------------------------------- | ------------------------------------------------------ |
| Automatic baseline employee access | Direct assignment or automatic assignment policy.      |
| Manager approval required          | Approval workflow with manager or configured approver. |
| Sponsor approval required          | Sponsor or business owner approval.                    |
| Security approval required         | Security or privileged access owner approval.          |
| Time-bound contractor access       | Assignment expiration.                                 |
| Recurring review required          | Access review configuration.                           |
| Exception access                   | Separate policy with expiration and justification.     |

---

## Approval Mapping

| Access Type                            | Approval Owner                                     |
| -------------------------------------- | -------------------------------------------------- |
| Standard baseline access               | May not require approval.                          |
| Department access                      | Manager or department owner.                       |
| Sensitive application access           | Application owner.                                 |
| Legal, finance, HR, or security access | Business owner and governance reviewer.            |
| Contractor access                      | Sponsor.                                           |
| Vendor access                          | Sponsor and application owner.                     |
| Privileged access                      | Security approver or privileged access owner.      |
| Exception access                       | Business owner, security, and governance approver. |

---

## Expiration Mapping

| Identity Type              | Expiration Requirement                              |
| -------------------------- | --------------------------------------------------- |
| Employee baseline access   | No fixed expiration, but recurring review required. |
| Department access          | Reviewed during mover or access review cycles.      |
| Contractor access          | Expiration required.                                |
| Vendor access              | Expiration required.                                |
| Project access             | Expiration based on project end date.               |
| Temporary exception access | Expiration required.                                |
| Privileged access          | Time-bound or review-based access preferred.        |

---

## Access Review Mapping

| Package Type                 | Review Frequency                            |
| ---------------------------- | ------------------------------------------- |
| Baseline employee access     | Annual or policy-based.                     |
| Sensitive application access | Quarterly.                                  |
| Privileged access            | Monthly or more frequent.                   |
| Contractor access            | Monthly or at contract milestone.           |
| Vendor access                | Monthly or contract-based.                  |
| Exception access             | Monthly or before expiration.               |
| Non-human identity access    | Quarterly or based on credential lifecycle. |

---

## Risk Scoring Mapping

IdentityOS risk scoring can use access package assignments as risk signals.

| Access Package Condition                  | Risk Impact            |
| ----------------------------------------- | ---------------------- |
| Sensitive access package assigned         | Increases risk.        |
| Privileged access package assigned        | High or critical risk. |
| Contractor access package near expiration | Increases risk.        |
| Vendor package without sponsor            | High risk.             |
| Package assigned outside expected role    | Access drift.          |
| Package assignment expired but active     | Critical risk.         |
| Exception package without expiration      | High risk.             |

---

## Access Drift Mapping

Access drift detection should compare expected access packages to actual assignments.

| Drift Condition                           | Meaning           |
| ----------------------------------------- | ----------------- |
| User has package from previous department | Department drift. |
| User has package outside current role     | Role drift.       |
| Contractor has expired package            | Contractor drift. |
| Vendor package lacks sponsor              | Sponsor drift.    |
| Privileged package not recently reviewed  | Privilege drift.  |
| Exception package lacks expiration        | Exception drift.  |

---

## Evidence Mapping

Each access package assignment should generate evidence.

| Evidence Item         | Purpose                                           |
| --------------------- | ------------------------------------------------- |
| Access Package Name   | Shows what access was assigned.                   |
| Assignment Policy     | Shows how access was granted.                     |
| Requestor             | Shows who requested access.                       |
| Approver              | Shows who approved access.                        |
| Assignment Start Date | Shows when access began.                          |
| Assignment End Date   | Shows expiration.                                 |
| Review Status         | Shows whether access was reviewed.                |
| Risk Level            | Shows IdentityOS risk scoring output.             |
| Drift Status          | Shows whether assignment matches expected access. |
| Audit Status          | Shows whether evidence was retained.              |

---

## Example Mapping Record

```text id="aczwwf"
IdentityOS Role Package: Finance Analyst Access
Microsoft Entra Access Package: AP-Finance-Analyst-Standard-Prod
Resources:
  - Finance SharePoint
  - Financial Reporting Portal
  - Finance Teams Workspace
Approval Required: Yes
Approver: Finance Application Owner
Expiration: None for employee, required for contractor
Review Frequency: Quarterly
Risk Level: Medium
Audit Required: Yes
```

---

## Suggested Graph Permissions

| Permission                            | Purpose                                                               |
| ------------------------------------- | --------------------------------------------------------------------- |
| `EntitlementManagement.Read.All`      | Read access packages, policies, assignments, and entitlement objects. |
| `EntitlementManagement.ReadWrite.All` | Create or manage access package assignments and requests.             |
| `AccessReview.Read.All`               | Read access review status and results.                                |
| `AccessReview.ReadWrite.All`          | Create or manage reviews where required.                              |
| `Directory.Read.All`                  | Read identity and directory context for mapping decisions.            |

---

## Safety Controls

Access package automation should include safety controls.

| Control                    | Purpose                                                         |
| -------------------------- | --------------------------------------------------------------- |
| Package Mapping Validation | Confirms IdentityOS package maps to the correct access package. |
| Approval Enforcement       | Prevents access assignment without required approval.           |
| Expiration Enforcement     | Prevents temporary access from becoming permanent.              |
| Review Enforcement         | Ensures packages are reviewed on schedule.                      |
| Sponsor Validation         | Ensures external access has an owner.                           |
| Drift Detection            | Detects package assignments outside expected role.              |
| Audit Evidence             | Proves access was assigned, reviewed, approved, or removed.     |

---

## Dashboard Impact

Access package mapping supports multiple dashboards.

| Dashboard                       | Impact                                                       |
| ------------------------------- | ------------------------------------------------------------ |
| Executive Dashboard             | Shows high-level access, risk, and governance posture.       |
| IAM Operations Dashboard        | Shows assignments, renewals, removals, and remediation work. |
| Governance Dashboard            | Shows approvals, reviews, and exceptions.                    |
| Risk Dashboard                  | Uses packages as risk signals.                               |
| Access Drift Dashboard          | Compares expected and actual package assignments.            |
| Contractor and Vendor Dashboard | Tracks sponsor-owned temporary access.                       |
| Audit Evidence Dashboard        | Shows assignment, approval, review, and expiration evidence. |

---

## Summary

Access package mapping connects IdentityOS role logic to Microsoft Entra entitlement management.

The key architectural idea is:

> Access packages turn role-based access decisions into governed, reviewable, time-bound, and auditable access assignments.
