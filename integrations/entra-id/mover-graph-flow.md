# Mover Microsoft Graph Flow

## Purpose

This document defines how an IdentityOS Mover event could map to Microsoft Entra ID and Microsoft Graph actions.

A Mover event occurs when an existing identity changes role, department, location, manager, worker type, access requirements, or business responsibility.

Mover events are important because they often create access drift and privilege creep if old access is not removed.

---

## Mover Flow Objective

The objective of the Mover Graph flow is to answer:

> When an identity changes role or department, what access should be added, what access should be removed, what access requires review, and what evidence should be generated?

---

## High-Level Mover Flow

```text id="3nh3p0"
HR / Source System
        ↓
IdentityOS Mover Event
        ↓
Previous State vs New State Comparison
        ↓
Policy Engine Evaluation
        ↓
Expected Access vs Actual Access Comparison
        ↓
Access Drift Detection
        ↓
Microsoft Graph Action Mapping
        ↓
Microsoft Entra ID Access Changes
        ↓
Governance Evidence and Reporting
```

---

## Mover Event Inputs

IdentityOS expects a Mover event to include both old and new identity context.

| Attribute             | Purpose                                           |
| --------------------- | ------------------------------------------------- |
| `event_id`            | Unique event identifier.                          |
| `event_type`          | Identifies the event as a Mover.                  |
| `identity_id`         | Unique identity reference.                        |
| `user_principal_name` | Entra ID username.                                |
| `previous_department` | Prior department.                                 |
| `new_department`      | New department.                                   |
| `previous_job_title`  | Prior role or title.                              |
| `new_job_title`       | New role or title.                                |
| `previous_manager`    | Prior manager.                                    |
| `new_manager`         | New manager.                                      |
| `previous_location`   | Prior work location.                              |
| `new_location`        | New work location.                                |
| `effective_date`      | Date role change takes effect.                    |
| `worker_type`         | Employee, contractor, vendor, or service account. |

---

## IdentityOS Mover Decision Flow

```text id="e86pl4"
Mover Event Received
        ↓
Validate Previous and New Attributes
        ↓
Compare Previous Role Package to New Role Package
        ↓
Identify Access to Add
        ↓
Identify Access to Remove
        ↓
Identify Access to Review
        ↓
Detect Access Drift
        ↓
Evaluate Risk and Governance Requirements
        ↓
Prepare Microsoft Graph Actions
        ↓
Execute or Stage Changes
        ↓
Generate Evidence
```

---

## Mover Access Logic

Mover logic should not only grant new access.

It should also remove access that no longer belongs.

| Access Category             | Action                               |
| --------------------------- | ------------------------------------ |
| New role access             | Add required access.                 |
| Previous role access        | Remove access no longer needed.      |
| Shared access               | Retain only if still justified.      |
| Sensitive access            | Require review or approval.          |
| Privileged access           | Route to privileged access workflow. |
| Contractor or vendor access | Validate sponsor and expiration.     |
| Non-standard access         | Route to exception workflow.         |

---

## Microsoft Graph Action Mapping

| IdentityOS Decision               | Microsoft Graph Action                                       |
| --------------------------------- | ------------------------------------------------------------ |
| Update user department            | Update user attributes.                                      |
| Update job title                  | Update user attributes.                                      |
| Update manager                    | Update manager relationship or related user attribute.       |
| Add new department access         | Add user to new department group.                            |
| Remove previous department access | Remove user from old department group.                       |
| Add application access            | Assign app role or add to application access group.          |
| Remove application access         | Remove app role assignment or group membership.              |
| Retain shared access              | Leave assignment unchanged and record justification.         |
| Require approval                  | Stage access until manager, owner, or security approval.     |
| Detect access drift               | Compare expected access to current assignments.              |
| Generate evidence                 | Record decision, access change, drift status, and timestamp. |

---

## Example Mover Scenario

An employee moves from Finance to Legal.

```text id="vqak9d"
Name: Jordan Ellis
Previous Department: Finance
New Department: Legal
Previous Job Title: Financial Analyst
New Job Title: Legal Operations Analyst
Location: Miami
Worker Type: Employee
Effective Date: 2026-06-20
```

IdentityOS evaluates the event and determines:

```text id="ijn1sc"
Remove Finance department access
Remove Financial Reporting Portal access
Retain base employee access
Add Legal Operations Workspace access
Add Legal Document Management System access
Require review for sensitive legal document access
Generate access drift evidence
Generate governance report entry
```

---

## Example Graph Action Sequence

```text id="1scpf0"
1. Read current user attributes.
2. Read current group and application access.
3. Update user department and job title.
4. Add user to new Legal access group.
5. Remove user from old Finance access group.
6. Remove Financial Reporting application access.
7. Stage sensitive Legal access for approval if required.
8. Record retained access decisions.
9. Generate drift and governance evidence.
10. Update dashboard metrics.
```

---

## Expected Access vs Actual Access

Mover workflows should compare expected access against actual access.

| Access Type     | Meaning                                       |
| --------------- | --------------------------------------------- |
| Expected Access | Access the user should have after the move.   |
| Actual Access   | Access currently detected in Entra ID.        |
| Excess Access   | Access that exists but is no longer expected. |
| Missing Access  | Access expected but not yet assigned.         |
| Shared Access   | Access valid in both old and new roles.       |
| Review Access   | Access requiring human validation.            |

---

## Access Drift Detection

Mover events are one of the most common causes of access drift.

| Drift Type        | Description                                                |
| ----------------- | ---------------------------------------------------------- |
| Department Drift  | User retains access from previous department.              |
| Role Drift        | User retains access from previous job role.                |
| Application Drift | User retains app access no longer required.                |
| Privilege Drift   | User keeps elevated permissions after role change.         |
| Governance Drift  | Review or approval was required but not completed.         |
| Exception Drift   | Temporary exception access was not removed or revalidated. |

---

## Approval Gates

Mover access changes should include approval gates where needed.

| Condition                              | Approval Requirement                              |
| -------------------------------------- | ------------------------------------------------- |
| Standard role access                   | May be automatically assigned.                    |
| Previous role access removal           | May be automatically removed after validation.    |
| Sensitive application access           | Requires manager or application owner approval.   |
| Legal, finance, HR, or security access | Requires governance review.                       |
| Privileged access                      | Requires privileged access workflow.              |
| Retained access from prior role        | Requires justification or review.                 |
| Exception access                       | Requires exception owner approval and expiration. |

---

## Risk Factors

The Mover flow should evaluate risk before and after access changes.

| Risk Factor                                        | Impact                                     |
| -------------------------------------------------- | ------------------------------------------ |
| User retains old department access                 | Creates access drift.                      |
| User gains sensitive application access            | Increases risk level.                      |
| User retains privileged access                     | May create critical risk.                  |
| User changes manager but access owner is unchanged | May require governance review.             |
| User changes location                              | May affect location-based access policy.   |
| User has exception access                          | Requires review and expiration validation. |
| User has contractor or vendor status               | Requires sponsor validation.               |

---

## Required Evidence

Each Mover event should generate evidence.

| Evidence Item   | Purpose                                            |
| --------------- | -------------------------------------------------- |
| Event ID        | Links access change to source lifecycle event.     |
| Previous State  | Shows prior department, role, manager, and access. |
| New State       | Shows new department, role, manager, and access.   |
| Access Added    | Shows new access granted.                          |
| Access Removed  | Shows stale access removed.                        |
| Access Retained | Shows access kept with justification.              |
| Access Reviewed | Shows sensitive or exception access reviewed.      |
| Drift Findings  | Shows detected excess access.                      |
| Risk Evaluation | Shows risk level and risk factors.                 |
| Timestamp       | Shows when action occurred.                        |

---

## Suggested Graph Permissions

| Permission                        | Purpose                                                                    |
| --------------------------------- | -------------------------------------------------------------------------- |
| `User.Read.All`                   | Read current user identity attributes.                                     |
| `User.ReadWrite.All`              | Update user department, title, location, or other lifecycle attributes.    |
| `Group.Read.All`                  | Read group metadata for access mapping.                                    |
| `GroupMember.Read.All`            | Read current group memberships.                                            |
| `GroupMember.ReadWrite.All`       | Add or remove group memberships.                                           |
| `AppRoleAssignment.Read.All`      | Read application role assignments.                                         |
| `AppRoleAssignment.ReadWrite.All` | Add or remove app role assignments when approved.                          |
| `Directory.Read.All`              | Read broader directory context when narrower permissions are insufficient. |

---

## Safety Controls

Mover automation should include strong safety controls.

| Control                 | Purpose                                                   |
| ----------------------- | --------------------------------------------------------- |
| Previous State Snapshot | Captures access before changes are made.                  |
| Expected Access Model   | Defines what access should exist after the move.          |
| Dry Run Mode            | Shows planned additions and removals before execution.    |
| Approval Checks         | Blocks sensitive access changes until approval.           |
| Removal Safeguard       | Prevents accidental removal of shared or required access. |
| Drift Detection         | Identifies excess access.                                 |
| Rollback Plan           | Allows restoration if access is removed incorrectly.      |
| Audit Logging           | Records all decisions and actions.                        |

---

## Failure Handling

Mover automation should handle failures safely.

| Failure                             | Response                                             |
| ----------------------------------- | ---------------------------------------------------- |
| Missing previous state              | Stop workflow and request validation.                |
| Missing new department or job title | Stop role mapping.                                   |
| Old group not found                 | Log issue and continue review.                       |
| New group not found                 | Stop new access assignment and escalate.             |
| App assignment removal failed       | Log remediation task.                                |
| Approval missing                    | Stage sensitive access and wait for approval.        |
| Graph permission denied             | Log permission error and escalate.                   |
| Partial update failure              | Record completed and failed actions for remediation. |

---

## Mover Evidence Output

A Mover flow should produce evidence similar to:

```text id="hychza"
Event ID: EVT-MOVER-001
Identity: Jordan Ellis
Previous Department: Finance
New Department: Legal
Action: Department move processed
Access Added:
  - Legal Operations Workspace
  - Legal Document Management System
Access Removed:
  - Finance SharePoint
  - Financial Reporting Portal
Access Retained:
  - Base Employee Access
Approval Required: Yes, for sensitive Legal access
Drift Detected: Yes, previous Finance access was still active
Risk Level: High
Audit Required: Yes
Status: Completed with governance and drift evidence
```

---

## Dashboard Impact

Successful Mover automation should update dashboard metrics.

| Dashboard Area       | Impact                                           |
| -------------------- | ------------------------------------------------ |
| Lifecycle Operations | Mover event count increases.                     |
| Access Drift         | Department or role drift findings are updated.   |
| Governance           | Review and approval requirements are updated.    |
| Risk Scoring         | Risk level is recalculated.                      |
| Automation Health    | Successful or failed automation run is recorded. |
| Audit Evidence       | Mover evidence artifact is generated.            |
| Executive Dashboard  | Access drift and risk metrics are updated.       |

---

## Summary

The Mover Microsoft Graph Flow shows how IdentityOS could translate a role or department change into Microsoft Entra ID access updates.

The key architectural idea is:

> A mover process is not complete until old access is removed, new access is assigned, retained access is justified, and drift evidence is generated.
