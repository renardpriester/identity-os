# Microsoft Graph Permissions Model

## Purpose

This document defines the Microsoft Graph permission model that IdentityOS would use when integrating with Microsoft Entra ID.

The goal is not to request broad permissions by default.

The goal is to design a least-privilege permission model that separates read-only visibility, lifecycle automation, access assignment, privileged access, governance, reporting, and remediation actions.

---

## Design Principle

IdentityOS should use the least privilege required for each integration function.

A reporting workflow should not need the same permissions as an automation workflow that creates users or modifies group membership.

A privileged access workflow should be separated from a basic lifecycle reporting workflow.

---

## Permission Categories

IdentityOS permissions can be grouped into these categories:

| Category                              | Purpose                                                                 |
| ------------------------------------- | ----------------------------------------------------------------------- |
| Read-Only Directory Visibility        | Read users, groups, apps, and assignments for reporting and dashboards. |
| Lifecycle Automation                  | Create, update, disable, or modify user objects.                        |
| Group and Access Assignment           | Add or remove users from groups or access structures.                   |
| Application Access Assignment         | Read or manage app role assignments.                                    |
| Governance and Entitlement Management | Connect access package or entitlement workflows.                        |
| Privileged Access                     | Read or manage privileged role assignments and activation concepts.     |
| Audit and Reporting                   | Collect evidence for governance, risk, drift, and audit reports.        |

---

## Permission Separation Model

IdentityOS should separate permissions by function.

```text id="43b928"
Read-Only Reporting App
        ↓
Dashboards, Reports, Risk Scoring, Drift Detection

Lifecycle Automation App
        ↓
Joiner, Mover, Leaver, Contractor, Vendor Actions

Privileged Access App
        ↓
Privileged Role Review, Elevated Access, PIM Concepts

Governance App
        ↓
Access Packages, Reviews, Approvals, Exceptions, Evidence
```

This prevents one application identity from having unnecessary access across all identity operations.

---

## Suggested App Registration Strategy

| App Registration                   | Purpose                                                                                    | Permission Posture                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| `identityos-reporting-app`         | Reads directory, group, assignment, and governance data for dashboards and reports.        | Read-only where possible.                          |
| `identityos-lifecycle-app`         | Performs lifecycle automation for joiner, mover, leaver, contractor, and vendor workflows. | Write permissions limited to lifecycle operations. |
| `identityos-governance-app`        | Supports access package, review, approval, and evidence workflows.                         | Governance-specific permissions.                   |
| `identityos-privileged-access-app` | Supports privileged access visibility and PIM integration concepts.                        | Highly restricted and separately approved.         |
| `identityos-lab-app`               | Used only in a lab tenant for testing sample Graph actions.                                | Non-production only.                               |

---

## Read-Only Reporting Permissions

Read-only permissions support dashboards, reports, risk scoring, access drift detection, and audit visibility.

| Permission                   | Purpose                                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------------------- |
| `User.Read.All`              | Read user profile and identity attributes for reporting and lifecycle context.                           |
| `Group.Read.All`             | Read group details for access visibility.                                                                |
| `GroupMember.Read.All`       | Read group memberships for access drift detection.                                                       |
| `Application.Read.All`       | Read application registrations and enterprise app metadata.                                              |
| `AppRoleAssignment.Read.All` | Read application role assignments for application access visibility.                                     |
| `Directory.Read.All`         | Broad directory read access; should be used carefully and only if narrower permissions are insufficient. |
| `AuditLog.Read.All`          | Read audit logs for evidence and activity reporting.                                                     |

---

## Lifecycle Automation Permissions

Lifecycle automation permissions support joiner, mover, leaver, contractor, and vendor workflows.

| Permission                  | Purpose                                                                      |
| --------------------------- | ---------------------------------------------------------------------------- |
| `User.ReadWrite.All`        | Create, update, or modify user accounts for lifecycle workflows.             |
| `Directory.ReadWrite.All`   | Broad directory write permission; should be avoided unless clearly required. |
| `GroupMember.ReadWrite.All` | Add or remove users from group memberships.                                  |
| `Group.ReadWrite.All`       | Create or manage groups where IdentityOS is responsible for group lifecycle. |

---

## Group and Access Assignment Permissions

Group-based access is a common IAM control pattern.

IdentityOS may use group assignment logic to model access decisions.

| Permission                  | Purpose                                          |
| --------------------------- | ------------------------------------------------ |
| `Group.Read.All`            | Read group metadata.                             |
| `GroupMember.Read.All`      | Read group members.                              |
| `GroupMember.ReadWrite.All` | Add or remove group members.                     |
| `Group.ReadWrite.All`       | Create or modify group properties when required. |

---

## Application Access Permissions

Application access may be represented through app role assignments.

| Permission                        | Purpose                                                   |
| --------------------------------- | --------------------------------------------------------- |
| `Application.Read.All`            | Read app registration and enterprise application details. |
| `AppRoleAssignment.Read.All`      | Read app role assignment state.                           |
| `AppRoleAssignment.ReadWrite.All` | Assign or remove app role assignments when approved.      |

---

## Governance and Entitlement Permissions

Governance permissions support access packages, approvals, access reviews, and entitlement workflows.

| Permission                            | Purpose                                                                        |
| ------------------------------------- | ------------------------------------------------------------------------------ |
| `EntitlementManagement.Read.All`      | Read access packages, assignment policies, and entitlement management objects. |
| `EntitlementManagement.ReadWrite.All` | Manage access package assignments and entitlement workflows.                   |
| `AccessReview.Read.All`               | Read access review definitions and results.                                    |
| `AccessReview.ReadWrite.All`          | Create or manage access reviews where required.                                |

---

## Privileged Access Permissions

Privileged access permissions should be separated from normal lifecycle automation.

| Permission                           | Purpose                                                                          |
| ------------------------------------ | -------------------------------------------------------------------------------- |
| `RoleManagement.Read.Directory`      | Read directory role definitions, assignments, and privileged access information. |
| `RoleManagement.ReadWrite.Directory` | Manage directory role assignments and privileged access workflows when approved. |
| `PrivilegedAccess.Read.AzureAD`      | Read privileged access information where supported.                              |
| `PrivilegedAccess.ReadWrite.AzureAD` | Manage privileged access workflows where supported.                              |

---

## Audit and Evidence Permissions

Audit evidence permissions allow IdentityOS to collect activity and decision evidence.

| Permission           | Purpose                                                        |
| -------------------- | -------------------------------------------------------------- |
| `AuditLog.Read.All`  | Read audit logs for access, identity, and governance evidence. |
| `Directory.Read.All` | Read directory state for audit reporting.                      |
| `Reports.Read.All`   | Read reporting data where needed for identity visibility.      |

---

## Permission Risk Levels

| Risk Level | Permission Type                            | Example                                                         |
| ---------- | ------------------------------------------ | --------------------------------------------------------------- |
| Low        | Read-only scoped permissions               | `User.Read.All`, `Group.Read.All`                               |
| Medium     | Read-only broad directory permissions      | `Directory.Read.All`                                            |
| High       | Write permissions for users or groups      | `User.ReadWrite.All`, `GroupMember.ReadWrite.All`               |
| Critical   | Broad write or privileged role permissions | `Directory.ReadWrite.All`, `RoleManagement.ReadWrite.Directory` |

---

## Least-Privilege Design Matrix

| IdentityOS Function            | Preferred Permission Pattern                                                 |
| ------------------------------ | ---------------------------------------------------------------------------- |
| Dashboard reporting            | Read-only permissions only.                                                  |
| Risk scoring                   | Read-only permissions only.                                                  |
| Access drift detection         | Read users, groups, app assignments, and memberships.                        |
| Joiner automation              | User write and group membership write permissions.                           |
| Mover automation               | Group membership write and user attribute update permissions.                |
| Leaver automation              | User update, disablement, group removal, and session revocation permissions. |
| Contractor expiration          | User update and group removal permissions.                                   |
| App role assignment            | App role assignment read/write permissions after approval.                   |
| Privileged access review       | Role management read permissions first.                                      |
| Privileged access modification | Role management write permissions only with strict approval.                 |
| Audit evidence reporting       | Audit log and directory read permissions.                                    |

---

## Recommended Permission Architecture

IdentityOS should avoid assigning all permissions to one application.

Recommended model:

```text id="q9e1ly"
identityos-reporting-app
    - Read-only directory, group, app, audit, and report permissions

identityos-lifecycle-app
    - User and group membership write permissions

identityos-governance-app
    - Access package and access review permissions

identityos-privileged-access-app
    - Privileged access read/write permissions with strict approval

identityos-lab-app
    - Used only for testing in a non-production tenant
```

---

## Admin Consent Requirements

Many Microsoft Graph permissions require administrator consent.

IdentityOS should document:

* Permission requested
* Reason permission is needed
* Whether the permission is delegated or application-based
* Whether admin consent is required
* Which workflow uses the permission
* Risk level of the permission
* Approval owner
* Review frequency
* Evidence location

---

## Permission Review Process

IdentityOS permissions should be reviewed regularly.

Recommended review questions:

* Does this application still need the permission?
* Is a narrower permission available?
* Is the permission read-only or write-capable?
* Does the permission allow broad directory access?
* Is admin consent still justified?
* Is the app registration still owned?
* Are credentials or certificates current?
* Are audit logs being reviewed?
* Is the permission documented in the IAM governance model?

---

## Lab Safety Guidelines

For a lab tenant:

* Use a non-production Microsoft Entra tenant.
* Use test users and test groups.
* Avoid production data.
* Avoid broad write permissions unless required for the lab.
* Separate reporting permissions from automation permissions.
* Review app registration permissions after each test.
* Remove unused app permissions.
* Rotate or remove secrets after testing.
* Document every permission used.

---

## Summary

The Microsoft Graph Permissions Model defines how IdentityOS should approach Entra ID integration safely.

The core idea is simple:

> Read broadly only when needed, write narrowly whenever possible, and separate privileged actions from normal lifecycle automation.
