# Joiner Microsoft Graph Flow

## Purpose

This document defines how an IdentityOS Joiner event could map to Microsoft Entra ID and Microsoft Graph actions.

A Joiner event occurs when a new employee, contractor, vendor, or service identity enters the organization and requires identity creation, attribute assignment, access assignment, governance review, and audit evidence.

---

## Joiner Flow Objective

The objective of the Joiner Graph flow is to answer:

> When a new identity joins the organization, what identity object should be created, what access should be assigned, what approvals are required, and what evidence should be generated?

---

## High-Level Joiner Flow

```text id="aifoh8"
HR / Source System
        ↓
IdentityOS Joiner Event
        ↓
Attribute Mapping
        ↓
Policy Engine Evaluation
        ↓
Risk and Governance Evaluation
        ↓
Microsoft Graph Action Mapping
        ↓
Microsoft Entra ID User / Group / App Assignment
        ↓
Audit Evidence and Reporting
```

---

## Joiner Event Inputs

IdentityOS expects a Joiner event to include identity attributes that can drive policy decisions.

| Attribute             | Purpose                                           |
| --------------------- | ------------------------------------------------- |
| `event_id`            | Unique event identifier.                          |
| `event_type`          | Identifies the event as a Joiner.                 |
| `identity_type`       | Employee, contractor, vendor, or service account. |
| `display_name`        | User-friendly name.                               |
| `user_principal_name` | Entra ID username.                                |
| `department`          | Department used for policy and access logic.      |
| `job_title`           | Role-based access decision input.                 |
| `manager`             | Approval and reporting relationship.              |
| `location`            | Location-based access and policy input.           |
| `start_date`          | Lifecycle start date.                             |
| `sponsor`             | Required for contractors or vendors.              |
| `expiration_date`     | Required for temporary external access.           |

---

## IdentityOS Joiner Decision Flow

```text id="yxvk66"
Joiner Event Received
        ↓
Validate Required Attributes
        ↓
Classify Identity Type
        ↓
Map Department and Job Title to Role Package
        ↓
Evaluate Risk Factors
        ↓
Determine Approval Requirements
        ↓
Determine Access Assignments
        ↓
Prepare Microsoft Graph Actions
        ↓
Execute or Stage Actions
        ↓
Generate Evidence
```

---

## Microsoft Graph Action Mapping

| IdentityOS Decision                | Microsoft Graph Action                                       |
| ---------------------------------- | ------------------------------------------------------------ |
| Create new employee identity       | Create user object.                                          |
| Set identity attributes            | Update user profile attributes.                              |
| Assign base access                 | Add user to standard security groups.                        |
| Assign department access           | Add user to department-based groups.                         |
| Assign application access          | Assign app role or group-based application access.           |
| Assign temporary contractor access | Add user to time-bound contractor groups or access packages. |
| Require approval                   | Stage assignment until approval is completed.                |
| Require governance review          | Mark event for access review tracking.                       |
| Require audit evidence             | Write decision and action details to report output.          |

---

## Example Joiner Scenario

A new Finance employee joins the company.

```text id="hhn93j"
Name: Morgan Lee
Department: Finance
Job Title: Financial Analyst
Location: Miami
Identity Type: Employee
Start Date: 2026-06-20
```

IdentityOS evaluates the event and determines:

```text id="w465fl"
Create Entra ID user
Assign base employee group
Assign Finance department group
Assign Financial Reporting application access
Require MFA policy alignment
Require audit evidence
Generate governance record
```

---

## Example Graph Action Sequence

```text id="uk7b8f"
1. Create user.
2. Update user attributes.
3. Add user to base employee group.
4. Add user to Finance department group.
5. Assign application role or access group.
6. Record policy decision.
7. Generate governance evidence.
8. Update dashboard metrics.
```

---

## Joiner Access Assignment Model

| Access Type          | Assignment Method                                                                     |
| -------------------- | ------------------------------------------------------------------------------------- |
| Base Employee Access | Group membership.                                                                     |
| Department Access    | Department-based security group.                                                      |
| Application Access   | App role assignment or access group.                                                  |
| Contractor Access    | Sponsor-approved time-bound access.                                                   |
| Vendor Access        | Sponsor-approved external access.                                                     |
| Privileged Access    | Not granted automatically; requires separate approval and privileged access workflow. |

---

## Approval Gates

Not all Joiner access should be assigned automatically.

| Access Condition                         | Approval Requirement                                       |
| ---------------------------------------- | ---------------------------------------------------------- |
| Standard employee baseline access        | May be automatically assigned.                             |
| Department access                        | May be automatically assigned based on policy.             |
| Sensitive application access             | Requires manager or application owner approval.            |
| Financial, legal, HR, or security access | Requires governance review.                                |
| Contractor or vendor access              | Requires sponsor approval and expiration date.             |
| Privileged access                        | Requires privileged access workflow and security approval. |

---

## Risk Factors

The Joiner flow should evaluate risk before access is assigned.

| Risk Factor                               | Impact                              |
| ----------------------------------------- | ----------------------------------- |
| Privileged access requested               | Increases risk level.               |
| Sensitive application access requested    | May require approval.               |
| Contractor or vendor identity             | Requires sponsor and expiration.    |
| Missing manager                           | Blocks or delays access assignment. |
| Missing department                        | Blocks role package mapping.        |
| Missing expiration for temporary identity | Blocks contractor or vendor access. |
| Non-standard access request               | Requires exception workflow.        |

---

## Required Evidence

Each Joiner event should generate evidence.

| Evidence Item      | Purpose                                                        |
| ------------------ | -------------------------------------------------------------- |
| Event ID           | Links access to source lifecycle event.                        |
| Identity Created   | Confirms user object creation.                                 |
| Attributes Applied | Shows department, title, location, manager, and identity type. |
| Access Assigned    | Shows groups, apps, or packages assigned.                      |
| Approval Status    | Shows whether approval was required and completed.             |
| Risk Evaluation    | Shows risk level and risk factors.                             |
| Policy Decision    | Shows why access was granted or staged.                        |
| Timestamp          | Shows when action occurred.                                    |

---

## Suggested Graph Permissions

| Permission                        | Purpose                                                             |
| --------------------------------- | ------------------------------------------------------------------- |
| `User.ReadWrite.All`              | Create or update user objects.                                      |
| `GroupMember.ReadWrite.All`       | Add users to groups.                                                |
| `Group.Read.All`                  | Read group metadata for mapping decisions.                          |
| `AppRoleAssignment.ReadWrite.All` | Assign application roles when approved.                             |
| `Directory.Read.All`              | Read directory context where narrower permissions are insufficient. |

---

## Safety Controls

Joiner automation should include safety controls.

| Control              | Purpose                                                        |
| -------------------- | -------------------------------------------------------------- |
| Attribute Validation | Prevents incomplete user creation.                             |
| Approval Checks      | Prevents sensitive access from being granted automatically.    |
| Least Privilege      | Limits access to required role packages only.                  |
| Logging              | Records each decision and action.                              |
| Dry Run Mode         | Allows review before executing changes.                        |
| Error Handling       | Captures failed Graph actions.                                 |
| Rollback Plan        | Allows removal of access if assignment fails or was incorrect. |

---

## Failure Handling

Joiner automation should handle failures safely.

| Failure                    | Response                                                |
| -------------------------- | ------------------------------------------------------- |
| Missing required attribute | Stop workflow and request correction.                   |
| User already exists        | Review duplicate identity condition.                    |
| Group not found            | Stop assignment and log missing access target.          |
| App role not found         | Stop assignment and log application mapping issue.      |
| Approval missing           | Stage access and wait for approval.                     |
| Graph permission denied    | Log permission error and escalate to IAM administrator. |
| Partial assignment failure | Record completed and failed actions for remediation.    |

---

## Joiner Evidence Output

A Joiner flow should produce evidence similar to:

```text id="etqtft"
Event ID: EVT-JOINER-001
Identity: Morgan Lee
Identity Type: Employee
Department: Finance
Job Title: Financial Analyst
Action: User created and baseline access assigned
Access Assigned:
  - Base Employee Group
  - Finance Department Group
  - Financial Reporting Access
Approval Required: Yes, for sensitive application access
Risk Level: Medium
Audit Required: Yes
Status: Completed with governance evidence
```

---

## Dashboard Impact

Successful Joiner automation should update dashboard metrics.

| Dashboard Area       | Impact                                       |
| -------------------- | -------------------------------------------- |
| Lifecycle Operations | Joiner event count increases.                |
| Governance           | Approval or review requirements are updated. |
| Risk Scoring         | Identity risk level is calculated.           |
| Automation Health    | Successful automation run is recorded.       |
| Audit Evidence       | Joiner evidence artifact is generated.       |
| Executive Dashboard  | Identity and access metrics are updated.     |

---

## Summary

The Joiner Microsoft Graph Flow shows how IdentityOS could translate a new worker event into Microsoft Entra ID identity creation and access assignment actions.

The key architectural idea is:

> Create the identity, assign only the required access, require approval for sensitive access, and generate evidence for every decision.
