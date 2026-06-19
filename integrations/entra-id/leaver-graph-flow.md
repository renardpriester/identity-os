# Leaver Microsoft Graph Flow

## Purpose

This document defines how an IdentityOS Leaver event could map to Microsoft Entra ID and Microsoft Graph actions.

A Leaver event occurs when an employee, contractor, vendor, or other identity leaves the organization or no longer requires access.

Leaver workflows are one of the most important IAM processes because inactive users, stale access, contractor access, and privileged access can become serious security risks if not removed quickly and completely.

---

## Leaver Flow Objective

The objective of the Leaver Graph flow is to answer:

> When an identity leaves the organization, how do we disable access, remove assignments, revoke sessions, preserve evidence, and prove that offboarding was completed?

---

## High-Level Leaver Flow

```text id="hbhgfo"
HR / Source System
        ↓
IdentityOS Leaver Event
        ↓
Identity and Access Snapshot
        ↓
Policy Engine Evaluation
        ↓
Risk and Urgency Classification
        ↓
Microsoft Graph Action Mapping
        ↓
Microsoft Entra ID Disablement and Access Removal
        ↓
Session Revocation
        ↓
Evidence, Reporting, and Dashboard Updates
```

---

## Leaver Event Inputs

IdentityOS expects a Leaver event to include enough context to determine urgency, access removal requirements, and evidence needs.

| Attribute             | Purpose                                                             |
| --------------------- | ------------------------------------------------------------------- |
| `event_id`            | Unique event identifier.                                            |
| `event_type`          | Identifies the event as a Leaver.                                   |
| `identity_id`         | Unique identity reference.                                          |
| `user_principal_name` | Entra ID username.                                                  |
| `display_name`        | User-friendly identity name.                                        |
| `identity_type`       | Employee, contractor, vendor, or service account.                   |
| `department`          | Department associated with access.                                  |
| `job_title`           | Role associated with access.                                        |
| `manager`             | Owner or approval contact.                                          |
| `termination_date`    | Date access should end.                                             |
| `termination_type`    | Voluntary, involuntary, contract ended, vendor ended, or emergency. |
| `privileged_access`   | Indicates whether elevated access exists.                           |
| `sponsor`             | Required for contractors and vendors.                               |

---

## IdentityOS Leaver Decision Flow

```text id="ulvzug"
Leaver Event Received
        ↓
Validate Identity and Termination Context
        ↓
Capture Current Access Snapshot
        ↓
Classify Termination Urgency
        ↓
Identify All Access Assignments
        ↓
Identify Privileged Access
        ↓
Prepare Disablement and Removal Actions
        ↓
Revoke Sessions
        ↓
Remove Group and App Assignments
        ↓
Generate Remediation and Audit Evidence
```

---

## Leaver Urgency Classification

Leaver events should be classified by urgency.

| Classification      | Description                                 | Response                                                             |
| ------------------- | ------------------------------------------- | -------------------------------------------------------------------- |
| Standard Leaver     | Normal employee termination or resignation. | Disable account and remove access based on effective date.           |
| Contractor End Date | Contractor access reaches expiration date.  | Disable or remove access unless sponsor renewal is approved.         |
| Vendor Termination  | Vendor access no longer required.           | Disable access and remove application or group assignments.          |
| Privileged Leaver   | Identity has elevated access.               | Prioritize privileged access removal and security review.            |
| Emergency Leaver    | Immediate access removal required.          | Disable account, revoke sessions, remove access, and alert security. |

---

## Microsoft Graph Action Mapping

| IdentityOS Decision       | Microsoft Graph Action                                        |
| ------------------------- | ------------------------------------------------------------- |
| Disable user access       | Update user account state.                                    |
| Revoke active sessions    | Revoke user sign-in sessions.                                 |
| Remove group access       | Remove user from security groups or Microsoft 365 groups.     |
| Remove application access | Delete app role assignments.                                  |
| Remove department access  | Remove department group membership.                           |
| Remove privileged access  | Route to privileged access removal workflow.                  |
| Preserve access snapshot  | Record current access before removal.                         |
| Generate evidence         | Write disablement, removal, and session revocation evidence.  |
| Update dashboards         | Update lifecycle, drift, risk, governance, and audit metrics. |

---

## Example Leaver Scenario

An employee in Finance leaves the organization.

```text id="dnbbnw"
Name: Morgan Lee
Department: Finance
Job Title: Financial Analyst
Identity Type: Employee
Termination Type: Standard Leaver
Termination Date: 2026-06-20
Privileged Access: No
```

IdentityOS evaluates the event and determines:

```text id="boh84e"
Capture access snapshot
Disable user account
Revoke active sessions
Remove base employee access
Remove Finance department access
Remove Financial Reporting application access
Generate offboarding evidence
Update governance and audit reports
```

---

## Example Graph Action Sequence

```text id="rrucm9"
1. Read user identity attributes.
2. Read group memberships.
3. Read app role assignments.
4. Record pre-removal access snapshot.
5. Disable user account.
6. Revoke sign-in sessions.
7. Remove group memberships.
8. Remove app role assignments.
9. Record completed and failed actions.
10. Generate audit evidence.
11. Update dashboard metrics.
```

---

## Access Snapshot Requirement

Before removing access, IdentityOS should capture a snapshot of current access.

| Snapshot Item                | Purpose                                             |
| ---------------------------- | --------------------------------------------------- |
| User attributes              | Shows who the identity was and where they belonged. |
| Group memberships            | Shows group-based access before removal.            |
| App role assignments         | Shows application access before removal.            |
| Privileged roles             | Shows elevated access before removal.               |
| Contractor or vendor sponsor | Shows business owner for external identities.       |
| Risk score                   | Shows risk level before remediation.                |
| Access drift findings        | Shows stale or excessive access before removal.     |

---

## Leaver Access Removal Model

| Access Type               | Action                                                              |
| ------------------------- | ------------------------------------------------------------------- |
| Base employee access      | Remove group membership.                                            |
| Department access         | Remove department group membership.                                 |
| Application access        | Remove app role assignment or application access group.             |
| Privileged access         | Remove or deactivate through privileged access workflow.            |
| Contractor access         | Disable or expire access unless renewed.                            |
| Vendor access             | Remove access and validate sponsor closure.                         |
| Non-human identity access | Review owner, purpose, credential, and access scope before removal. |

---

## Privileged Leaver Handling

Privileged leavers should be treated as high priority.

| Condition                          | Required Response                            |
| ---------------------------------- | -------------------------------------------- |
| User has privileged role           | Route to privileged access removal workflow. |
| User has admin group membership    | Remove privileged group access.              |
| User has app admin role            | Remove app role assignment.                  |
| User has security-sensitive access | Notify security or IAM leadership.           |
| User has active sessions           | Revoke sign-in sessions.                     |
| Privileged access removal fails    | Escalate immediately.                        |

---

## Contractor and Vendor Leaver Handling

External identities require sponsor-aware offboarding.

| Condition                               | Required Response                       |
| --------------------------------------- | --------------------------------------- |
| Contractor end date reached             | Disable or remove access.               |
| Sponsor renewal approved                | Extend access with new expiration date. |
| Sponsor renewal denied                  | Disable account and remove access.      |
| Sponsor missing                         | Escalate or remove access.              |
| Vendor contract ended                   | Remove access and generate evidence.    |
| External identity has privileged access | Require security review.                |

---

## Risk Factors

The Leaver flow should evaluate risk before and after access removal.

| Risk Factor                        | Impact                                       |
| ---------------------------------- | -------------------------------------------- |
| Privileged access exists           | Critical offboarding risk.                   |
| Active sessions exist              | Requires session revocation.                 |
| App role assignments exist         | Requires application access removal.         |
| Contractor or vendor access exists | Requires sponsor validation or expiration.   |
| Group memberships remain           | Creates leaver access drift.                 |
| Disablement fails                  | Requires urgent remediation.                 |
| Access removal partially fails     | Requires follow-up evidence and remediation. |

---

## Required Evidence

Each Leaver event should generate evidence.

| Evidence Item            | Purpose                                        |
| ------------------------ | ---------------------------------------------- |
| Event ID                 | Links action to source lifecycle event.        |
| Identity                 | Shows who was offboarded.                      |
| Termination Type         | Shows why the leaver workflow was triggered.   |
| Access Snapshot          | Shows access before removal.                   |
| Account Disablement      | Shows account state was changed.               |
| Session Revocation       | Shows sessions were revoked.                   |
| Access Removed           | Shows groups, apps, or roles removed.          |
| Privileged Access Review | Shows elevated access was reviewed or removed. |
| Failure Log              | Shows any incomplete action.                   |
| Timestamp                | Shows when actions occurred.                   |
| Audit Status             | Shows whether evidence was generated.          |

---

## Suggested Graph Permissions

| Permission                           | Purpose                                           |
| ------------------------------------ | ------------------------------------------------- |
| `User.Read.All`                      | Read identity attributes.                         |
| `User.ReadWrite.All`                 | Disable or update user account state.             |
| `GroupMember.Read.All`               | Read current group memberships.                   |
| `GroupMember.ReadWrite.All`          | Remove user from groups.                          |
| `AppRoleAssignment.Read.All`         | Read application role assignments.                |
| `AppRoleAssignment.ReadWrite.All`    | Remove app role assignments.                      |
| `Directory.Read.All`                 | Read broader directory context where required.    |
| `AuditLog.Read.All`                  | Read audit logs for offboarding evidence.         |
| `RoleManagement.Read.Directory`      | Read privileged role assignments.                 |
| `RoleManagement.ReadWrite.Directory` | Remove privileged role assignments when approved. |

---

## Safety Controls

Leaver automation should include strict safety controls.

| Control                 | Purpose                                                             |
| ----------------------- | ------------------------------------------------------------------- |
| Confirm Source Event    | Ensures termination event is authoritative.                         |
| Capture Access Snapshot | Preserves access evidence before removal.                           |
| Urgency Classification  | Determines standard, privileged, or emergency workflow.             |
| Dry Run Mode            | Shows planned removals before execution in non-emergency workflows. |
| Privileged Access Check | Ensures elevated access is prioritized.                             |
| Partial Failure Logging | Captures failed removal actions.                                    |
| Escalation Path         | Routes urgent failures to IAM or security leadership.               |
| Audit Evidence          | Proves offboarding was completed.                                   |

---

## Failure Handling

Leaver automation should handle failures safely.

| Failure                         | Response                                                     |
| ------------------------------- | ------------------------------------------------------------ |
| Identity not found              | Stop workflow and escalate to IAM team.                      |
| Termination date missing        | Stop workflow unless emergency removal is approved.          |
| Access snapshot fails           | Stop non-emergency workflow and escalate.                    |
| Account disablement fails       | Escalate immediately.                                        |
| Session revocation fails        | Log and escalate.                                            |
| Group removal fails             | Create remediation task.                                     |
| App role removal fails          | Create remediation task.                                     |
| Privileged access removal fails | Escalate immediately to security or privileged access owner. |
| Partial removal completed       | Record completed and failed actions separately.              |

---

## Leaver Evidence Output

A Leaver flow should produce evidence similar to:

```text id="a1wex5"
Event ID: EVT-LEAVER-001
Identity: Morgan Lee
Identity Type: Employee
Department: Finance
Termination Type: Standard Leaver
Actions Completed:
  - Access snapshot captured
  - User account disabled
  - Sign-in sessions revoked
  - Base employee access removed
  - Finance department access removed
  - Financial Reporting application access removed
Privileged Access: None detected
Failures: None
Risk Level: Medium
Audit Required: Yes
Status: Completed with offboarding evidence
```

---

## Dashboard Impact

Successful Leaver automation should update dashboard metrics.

| Dashboard Area       | Impact                                                            |
| -------------------- | ----------------------------------------------------------------- |
| Lifecycle Operations | Leaver event count increases.                                     |
| Access Drift         | Leaver drift findings decrease if access is removed successfully. |
| Risk Scoring         | Risk decreases after access removal.                              |
| Governance           | Remediation evidence is updated.                                  |
| Automation Health    | Successful or failed automation run is recorded.                  |
| Audit Evidence       | Leaver evidence artifact is generated.                            |
| Executive Dashboard  | Offboarding and remediation visibility improves.                  |

---

## Summary

The Leaver Microsoft Graph Flow shows how IdentityOS could translate a termination or access end event into Microsoft Entra ID disablement, access removal, session revocation, remediation, and audit evidence.

The key architectural idea is:

> A leaver process is not complete until the identity is disabled, active sessions are revoked, access is removed, privileged access is reviewed, and evidence proves completion.
