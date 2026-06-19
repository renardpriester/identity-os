# Audit Evidence Mapping

## Purpose

This document defines how IdentityOS audit evidence could map to Microsoft Entra ID and Microsoft Graph evidence sources.

IdentityOS should be able to explain identity and access decisions using evidence from lifecycle events, policy decisions, Microsoft Entra activity, Microsoft Graph actions, access assignments, privileged access workflows, access reviews, and generated reports.

---

## Objective

The objective of audit evidence mapping is to answer:

> What happened, who did it, why did it happen, what access changed, and can we prove it?

---

## Evidence Mapping Model

```text id="k7w5o1"
IdentityOS Event
        ↓
IdentityOS Policy Decision
        ↓
Microsoft Graph Action
        ↓
Microsoft Entra Activity
        ↓
Audit Log / Assignment / Sign-In Evidence
        ↓
IdentityOS Report
        ↓
Dashboard Evidence
```

---

## Evidence Categories

IdentityOS should organize audit evidence into several categories.

| Category                          | Purpose                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------- |
| Lifecycle Evidence                | Shows joiner, mover, leaver, contractor, vendor, and non-human identity events. |
| Policy Decision Evidence          | Shows why access was granted, removed, retained, reviewed, or escalated.        |
| Graph Action Evidence             | Shows API-level actions taken through Microsoft Graph.                          |
| Microsoft Entra Activity Evidence | Shows directory activity such as user, group, app, or role changes.             |
| Assignment Evidence               | Shows group, app role, access package, or privileged role assignment state.     |
| Sign-In Evidence                  | Shows authentication and access activity.                                       |
| Governance Evidence               | Shows reviews, approvals, exceptions, and remediation actions.                  |
| Report Evidence                   | Shows generated governance, risk, drift, automation, and audit reports.         |

---

## Microsoft Entra Evidence Sources

| Evidence Source            | Purpose                                                   |
| -------------------------- | --------------------------------------------------------- |
| Directory Audit Logs       | Show traceable directory activities and changes.          |
| Sign-In Logs               | Show authentication activity and access attempts.         |
| User Objects               | Show user attributes and account state.                   |
| Group Memberships          | Show access granted through group assignment.             |
| App Role Assignments       | Show application role access.                             |
| Access Package Assignments | Show entitlement management access.                       |
| PIM Role Assignments       | Show privileged access eligibility and activation.        |
| Application Objects        | Show app registration and enterprise application context. |
| Service Principals         | Show non-human identity and app access context.           |

---

## IdentityOS Evidence Sources

| Evidence Source                          | Purpose                                                |
| ---------------------------------------- | ------------------------------------------------------ |
| `examples/sample-identity-events.json`   | Provides sample lifecycle events.                      |
| `examples/sample-policy-decisions.json`  | Provides sample policy decision evidence.              |
| `examples/sample-dashboard-metrics.json` | Provides dashboard-ready evidence metrics.             |
| `reports/sample-governance-report.md`    | Provides governance evidence.                          |
| `reports/sample-risk-score-report.md`    | Provides risk evidence.                                |
| `reports/sample-access-drift-report.md`  | Provides drift and remediation evidence.               |
| `reports/sample-dashboard-summary.md`    | Provides dashboard summary evidence.                   |
| Streamlit Dashboard Prototype            | Provides interactive visibility into evidence metrics. |

---

## Lifecycle Evidence Mapping

| IdentityOS Event          | Microsoft Entra / Graph Evidence                                                 |
| ------------------------- | -------------------------------------------------------------------------------- |
| Joiner                    | User creation, group assignment, app role assignment, access package assignment. |
| Mover                     | User attribute update, group removal, group assignment, app role changes.        |
| Leaver                    | Account disablement, session revocation, group removal, app role removal.        |
| Contractor Onboarding     | Sponsor approval, temporary assignment, expiration date.                         |
| Contractor Expiration     | Access package expiration, group removal, account disablement.                   |
| Vendor Access             | External identity access, sponsor ownership, application assignment.             |
| Non-Human Identity Review | Service principal, app registration, credential, owner, and permission evidence. |
| Privileged Access         | PIM eligibility, activation, approval, and role assignment evidence.             |

---

## Policy Decision Evidence Mapping

Each IdentityOS policy decision should map to evidence.

| Policy Decision Field | Evidence Purpose                                             |
| --------------------- | ------------------------------------------------------------ |
| Decision ID           | Unique decision reference.                                   |
| Event ID              | Links decision to lifecycle event.                           |
| Identity              | Shows who or what the decision applied to.                   |
| Action                | Grant, remove, retain, review, disable, or escalate.         |
| Reason                | Explains why the decision occurred.                          |
| Required Approval     | Shows whether approval was required.                         |
| Required Review       | Shows whether review was required.                           |
| Risk Level            | Shows risk context.                                          |
| Audit Required        | Shows whether evidence must be retained.                     |
| Status                | Shows whether action completed, failed, or remained pending. |

---

## Graph Action Evidence Mapping

Microsoft Graph actions should be logged or documented as part of evidence.

| Graph Action Type     | Evidence to Capture                                          |
| --------------------- | ------------------------------------------------------------ |
| Create User           | User ID, UPN, attributes, timestamp, initiating workflow.    |
| Update User           | Changed attributes, old value, new value, timestamp.         |
| Disable User          | Account state, termination event, timestamp.                 |
| Add Group Member      | Group ID, group name, user ID, reason, timestamp.            |
| Remove Group Member   | Group ID, group name, user ID, reason, timestamp.            |
| Assign App Role       | Application, app role, principal, approver, timestamp.       |
| Remove App Role       | Application, app role, principal, reason, timestamp.         |
| Assign Access Package | Package, assignment policy, approval status, expiration.     |
| Revoke Sessions       | User ID, action time, workflow reason.                       |
| PIM Activation        | Role, principal, justification, approver, activation window. |

---

## Directory Audit Evidence

Directory audit evidence should help answer:

* Who changed the directory object?
* What object changed?
* What property changed?
* When did it happen?
* Was the action successful?
* Which service logged the action?
* Which workflow or correlation ID connects the action?

| Directory Audit Field | Evidence Purpose                               |
| --------------------- | ---------------------------------------------- |
| Activity Date Time    | Shows when the action occurred.                |
| Activity Display Name | Shows what action occurred.                    |
| Category              | Shows the type of activity.                    |
| Operation Type        | Shows add, update, delete, or other operation. |
| Result                | Shows success or failure.                      |
| Initiated By          | Shows who or what initiated the action.        |
| Target Resources      | Shows which objects were affected.             |
| Correlation ID        | Helps connect related events.                  |

---

## Sign-In Evidence

Sign-in evidence helps explain access activity and risk.

| Sign-In Evidence          | Purpose                                     |
| ------------------------- | ------------------------------------------- |
| User                      | Shows who signed in.                        |
| Application               | Shows which application was accessed.       |
| Sign-In Time              | Shows when authentication occurred.         |
| Status                    | Shows success or failure.                   |
| IP Address                | Shows network source.                       |
| Location                  | Shows sign-in geography.                    |
| Device                    | Shows device context.                       |
| Conditional Access Status | Shows policy evaluation result.             |
| Risk Detail               | Shows risk-related context where available. |

---

## Access Assignment Evidence

IdentityOS should map each access assignment to proof.

| Assignment Type            | Evidence                                                |
| -------------------------- | ------------------------------------------------------- |
| Group Membership           | Group name, group ID, user ID, assignment reason.       |
| App Role Assignment        | App name, role name, principal, assignment ID.          |
| Access Package Assignment  | Package name, policy, start date, expiration, approver. |
| Privileged Role Assignment | Role, eligibility, activation, approval, duration.      |
| Contractor Access          | Sponsor, expiration, renewal decision.                  |
| Vendor Access              | Sponsor, app owner, expiration, business justification. |
| Non-Human Identity Access  | Owner, purpose, credential state, access scope.         |

---

## Governance Evidence

Governance evidence should prove control effectiveness.

| Governance Control | Evidence                                       |
| ------------------ | ---------------------------------------------- |
| Approval           | Approver, decision, justification, timestamp.  |
| Access Review      | Reviewer, access reviewed, decision, outcome.  |
| Exception          | Exception owner, approval, reason, expiration. |
| Remediation        | Action owner, action completed, timestamp.     |
| Risk Review        | Risk score, risk factor, recommended action.   |
| Drift Review       | Expected access, actual access, excess access. |
| Privileged Review  | Role reviewed, decision, duration, approval.   |

---

## Evidence Quality Checklist

Evidence should be complete enough for audit review.

| Quality Check                | Required             |
| ---------------------------- | -------------------- |
| Identity is present          | Yes                  |
| Event ID is present          | Yes                  |
| Decision ID is present       | Yes                  |
| Action is documented         | Yes                  |
| Reason is documented         | Yes                  |
| Timestamp is present         | Yes                  |
| Owner or approver is present | Yes, when applicable |
| Risk level is present        | Yes, when applicable |
| Evidence source is present   | Yes                  |
| Completion status is present | Yes                  |

---

## Evidence Chain Example

```text id="fjvjo9"
Lifecycle Event:
  EVT-LEAVER-001

Policy Decision:
  Disable user and remove access

Graph Actions:
  Update account state
  Revoke sessions
  Remove group memberships
  Remove app role assignments

Microsoft Entra Evidence:
  Directory audit logs
  Group membership changes
  App role assignment removal
  Sign-in session revocation activity

IdentityOS Reports:
  Governance report
  Risk score report
  Access drift report
  Audit evidence dashboard

Audit Question Answered:
  Was the leaver access removed and can we prove it?
```

---

## Audit Evidence Record

A complete audit evidence record should look like this:

```text id="duynq3"
Evidence ID: EVID-001
Event ID: EVT-LEAVER-001
Decision ID: DEC-LEAVER-001
Identity: Morgan Lee
Identity Type: Employee
Action: Disable account and remove access
Reason: Employee termination
Access Removed:
  - Base Employee Group
  - Finance Department Group
  - Financial Reporting App Role
Graph Actions:
  - User account disabled
  - Sessions revoked
  - Group memberships removed
  - App role assignments removed
Evidence Sources:
  - Directory audit logs
  - Group membership changes
  - App role assignment changes
  - IdentityOS governance report
Risk Level: Medium
Audit Required: Yes
Status: Completed
```

---

## Permissions Needed for Evidence Collection

| Permission                       | Purpose                                       |
| -------------------------------- | --------------------------------------------- |
| `AuditLog.Read.All`              | Read audit logs.                              |
| `Directory.Read.All`             | Read directory context for evidence.          |
| `User.Read.All`                  | Read user identity attributes.                |
| `Group.Read.All`                 | Read group metadata.                          |
| `GroupMember.Read.All`           | Read group membership evidence.               |
| `Application.Read.All`           | Read application metadata.                    |
| `AppRoleAssignment.Read.All`     | Read application access assignments.          |
| `EntitlementManagement.Read.All` | Read access package assignments and policies. |
| `RoleManagement.Read.Directory`  | Read privileged role assignments.             |

---

## Dashboard Impact

Audit evidence mapping supports multiple IdentityOS dashboards.

| Dashboard                       | Evidence Impact                                         |
| ------------------------------- | ------------------------------------------------------- |
| Executive Dashboard             | Shows audit readiness and governance posture.           |
| IAM Operations Dashboard        | Shows remediation and action completion.                |
| Governance Dashboard            | Shows approvals, reviews, exceptions, and evidence.     |
| Risk Dashboard                  | Shows risk evidence and recommended actions.            |
| Access Drift Dashboard          | Shows drift evidence and remediation status.            |
| Privileged Access Dashboard     | Shows privileged access activation and review evidence. |
| Contractor and Vendor Dashboard | Shows sponsor, expiration, and renewal evidence.        |
| Non-Human Identity Dashboard    | Shows owner, purpose, credential, and access evidence.  |
| Automation Health Dashboard     | Shows report generation and evidence output health.     |
| Audit Evidence Dashboard        | Centralizes all audit evidence mappings.                |

---

## Retention and Storage Considerations

IdentityOS should define where evidence is stored and how long it is retained.

| Evidence Type        | Storage Consideration                                       |
| -------------------- | ----------------------------------------------------------- |
| Lifecycle Events     | Store as structured event records.                          |
| Policy Decisions     | Store as decision records.                                  |
| Graph Actions        | Store action log and API result details.                    |
| Reports              | Store generated Markdown, JSON, or dashboard outputs.       |
| Audit Logs           | Retrieve from Microsoft Entra or connected logging systems. |
| Sign-In Evidence     | Store references or exported evidence where required.       |
| Remediation Evidence | Store completion records and timestamps.                    |

---

## Safety Controls

Audit evidence workflows should include safety controls.

| Control               | Purpose                                                |
| --------------------- | ------------------------------------------------------ |
| Evidence Integrity    | Prevent unauthorized modification of evidence.         |
| Timestamp Consistency | Ensure all evidence has clear time references.         |
| Correlation IDs       | Connect related events and actions.                    |
| Least Privilege       | Limit evidence collection permissions.                 |
| Data Minimization     | Collect only evidence needed for governance and audit. |
| Secure Storage        | Protect sensitive identity and access evidence.        |
| Review Cadence        | Validate evidence quality regularly.                   |
| Retention Policy      | Define how long evidence is kept.                      |

---

## Summary

Audit evidence mapping connects IdentityOS decisions to Microsoft Entra and Microsoft Graph evidence sources.

The key architectural idea is:

> Identity governance is only complete when decisions, access changes, reviews, removals, and exceptions can be proven with evidence.
