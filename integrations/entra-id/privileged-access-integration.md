# Privileged Access Integration

## Purpose

This document defines how IdentityOS could integrate with Microsoft Entra Privileged Identity Management concepts.

Privileged access requires stronger governance because elevated permissions can affect users, applications, security controls, tenant configuration, identity policies, and sensitive systems.

IdentityOS should treat privileged access as a separate, high-risk workflow that requires approval, justification, time limitation, review, monitoring, and audit evidence.

---

## Objective

The objective of privileged access integration is to answer:

> Who has elevated access, why do they have it, how long should they have it, who approved it, and can we prove it was reviewed and controlled?

---

## Conceptual Model

```text id="3jxgvy"
IdentityOS Privileged Access Event
        ↓
Policy Engine
        ↓
Risk Scoring
        ↓
Approval and Justification
        ↓
Microsoft Entra PIM Concept
        ↓
Eligible or Active Assignment
        ↓
Activation, Expiration, Review
        ↓
Audit Evidence
```

---

## IdentityOS Privileged Access Concepts

| IdentityOS Concept        | Microsoft Entra / PIM Concept                              |
| ------------------------- | ---------------------------------------------------------- |
| Privileged Access Request | Role assignment or activation request.                     |
| Eligible Access           | Eligible role assignment.                                  |
| Active Access             | Active role assignment.                                    |
| Standing Privilege        | Permanent or long-lived active assignment.                 |
| Justification             | Activation or assignment reason.                           |
| Approval Requirement      | PIM approval workflow or governance approval.              |
| Time-Bound Access         | Assignment or activation expiration.                       |
| Privileged Review         | Access review or privileged access review.                 |
| Privileged Drift          | Elevated access no longer justified.                       |
| Audit Evidence            | PIM assignment, activation, approval, and review evidence. |

---

## Privileged Access Types

IdentityOS should classify privileged access into several types.

| Type                             | Description                                                                              |
| -------------------------------- | ---------------------------------------------------------------------------------------- |
| Directory Role Access            | Microsoft Entra administrative role access.                                              |
| Role-Assignable Group Access     | Access through a group eligible for privileged role assignment.                          |
| Application Administrator Access | Elevated access to manage enterprise applications.                                       |
| Security Reader Access           | Read-only security visibility access.                                                    |
| Privileged App Role Access       | Elevated access inside a business or security application.                               |
| Break-Glass Access               | Emergency access requiring strict monitoring and review.                                 |
| Non-Human Privileged Access      | Service accounts, app registrations, or automation identities with elevated permissions. |

---

## Preferred Privileged Access Pattern

IdentityOS should prefer just-in-time access over standing privilege.

```text id="0k6c8o"
Eligible Assignment
        ↓
User Requests Activation
        ↓
MFA / Justification / Approval
        ↓
Temporary Active Assignment
        ↓
Expiration
        ↓
Audit Evidence
```

Standing privileged access should be minimized and reviewed frequently.

---

## Privileged Access Flow

```text id="n4j5eb"
Privileged Access Need Identified
        ↓
IdentityOS Validates Request
        ↓
Risk Score Calculated
        ↓
Approval Requirement Determined
        ↓
PIM Eligibility or Activation Concept Mapped
        ↓
Access Is Granted Temporarily or Staged
        ↓
Activation and Expiration Are Tracked
        ↓
Evidence Is Generated
```

---

## Joiner Privileged Access Handling

Joiner events should not automatically grant privileged access unless explicitly approved.

| Joiner Scenario      | Privileged Access Action                                  | Governance Requirement                                       |
| -------------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| New IAM engineer     | Make eligible for limited admin role only after approval. | Manager and security approval.                               |
| New security analyst | Assign read-only security role if approved.               | Security owner approval.                                     |
| New helpdesk user    | Assign eligible support role if justified.                | Role owner approval.                                         |
| New executive admin  | Avoid broad admin access unless explicitly required.      | Strong review and approval.                                  |
| New contractor       | Do not grant privileged access by default.                | Sponsor, security, expiration, and elevated review required. |

---

## Mover Privileged Access Handling

Mover events are high-risk because users may retain privileged access from a previous role.

| Mover Scenario                           | Required Action                                        |
| ---------------------------------------- | ------------------------------------------------------ |
| User leaves IAM team                     | Remove eligible or active identity admin roles.        |
| User moves into security role            | Review and approve security-related privileged access. |
| User changes department                  | Validate privileged access still aligns with new role. |
| User retains old admin group             | Flag as privileged access drift.                       |
| User gains new privileged responsibility | Require approval, justification, and time limitation.  |

---

## Leaver Privileged Access Handling

Leaver events involving privileged access require immediate action.

| Leaver Scenario                      | Required Action                                 |
| ------------------------------------ | ----------------------------------------------- |
| Leaver has active privileged role    | Remove active assignment immediately.           |
| Leaver has eligible privileged role  | Remove eligibility.                             |
| Leaver is member of privileged group | Remove from group.                              |
| Leaver has privileged app role       | Remove app role assignment.                     |
| Leaver is break-glass owner          | Escalate to security leadership.                |
| Leaver is non-human identity owner   | Transfer ownership or disable related identity. |

---

## Privileged Access Risk Factors

| Risk Factor                              | Impact                            |
| ---------------------------------------- | --------------------------------- |
| Permanent active assignment              | High risk.                        |
| Privileged access without approval       | High governance risk.             |
| Privileged access without justification  | High audit risk.                  |
| Privileged access without expiration     | Standing privilege risk.          |
| Privileged access after role change      | Privileged drift.                 |
| Privileged access after termination      | Critical risk.                    |
| Privileged service account without owner | Critical non-human identity risk. |
| Break-glass access not reviewed          | Critical operational risk.        |

---

## PIM Assignment Concepts

IdentityOS should distinguish between eligibility and activation.

| Concept               | Meaning                                                  |
| --------------------- | -------------------------------------------------------- |
| Eligible Assignment   | User can activate role when needed.                      |
| Active Assignment     | User currently has elevated access.                      |
| Permanent Assignment  | User has standing privileged access.                     |
| Time-Bound Assignment | Access expires after a defined period.                   |
| Activation            | User turns eligible access into temporary active access. |
| Deactivation          | Active access is removed or expires.                     |
| Renewal               | Assignment is extended.                                  |
| Revocation            | Assignment is removed.                                   |

---

## Privileged Access Decision Matrix

| Decision                   | IdentityOS Action                                     |
| -------------------------- | ----------------------------------------------------- |
| Grant eligible access      | Require approval and document eligibility.            |
| Activate privileged access | Require MFA, justification, approval, and expiration. |
| Extend privileged access   | Require renewed justification.                        |
| Revoke privileged access   | Remove active or eligible assignment.                 |
| Review privileged access   | Route to privileged access owner.                     |
| Detect standing access     | Flag as privileged risk.                              |
| Detect privileged drift    | Create remediation task.                              |

---

## Suggested Microsoft Graph Resources

| Resource or Concept                      | Purpose                                                                             |
| ---------------------------------------- | ----------------------------------------------------------------------------------- |
| Role eligibility schedule request        | Request eligible privileged access.                                                 |
| Role assignment schedule request         | Request active privileged access, activation, deactivation, renewal, or revocation. |
| Role assignment schedule instance        | Read active role assignments.                                                       |
| Role eligibility schedule                | Read eligible role assignments.                                                     |
| Role management directory                | Read or manage Microsoft Entra role assignment information.                         |
| Privileged access group schedule request | Manage time-bound privileged group membership concepts.                             |

---

## Suggested Graph Permissions

| Permission                           | Purpose                                                |
| ------------------------------------ | ------------------------------------------------------ |
| `RoleManagement.Read.Directory`      | Read privileged role definitions and assignments.      |
| `RoleManagement.ReadWrite.Directory` | Manage privileged role assignments when approved.      |
| `PrivilegedAccess.Read.AzureAD`      | Read privileged access information where supported.    |
| `PrivilegedAccess.ReadWrite.AzureAD` | Manage privileged access workflows where supported.    |
| `Group.Read.All`                     | Read role-assignable group metadata.                   |
| `GroupMember.Read.All`               | Read privileged group membership.                      |
| `GroupMember.ReadWrite.All`          | Add or remove privileged group members where approved. |
| `AuditLog.Read.All`                  | Read privileged access evidence and activity.          |

---

## Approval Requirements

Privileged access should require stronger approval than standard access.

| Privileged Access Type        | Approval Requirement                                |
| ----------------------------- | --------------------------------------------------- |
| Security Reader               | Security owner approval.                            |
| User Administrator            | IAM manager or identity owner approval.             |
| Application Administrator     | Application owner and IAM approval.                 |
| Privileged Role Administrator | Security leadership approval.                       |
| Global Administrator          | Executive security approval or break-glass process. |
| Privileged group membership   | Group owner and security approval.                  |
| Break-glass access            | Emergency access governance and post-use review.    |
| Non-human privileged access   | Technical owner, security, and governance approval. |

---

## Evidence Requirements

Every privileged access workflow should generate evidence.

| Evidence Item      | Purpose                                             |
| ------------------ | --------------------------------------------------- |
| Request ID         | Links request to privileged access workflow.        |
| Principal          | User, group, or service principal receiving access. |
| Role               | Privileged role requested or assigned.              |
| Assignment Type    | Eligible, active, permanent, or time-bound.         |
| Justification      | Business reason for elevation.                      |
| Approver           | Person or group approving access.                   |
| Activation Time    | When privileged access became active.               |
| Expiration Time    | When privileged access ends.                        |
| Risk Level         | IdentityOS risk score.                              |
| Review Status      | Whether access was reviewed.                        |
| Remediation Status | Whether access was removed when no longer needed.   |

---

## Privileged Access Drift

IdentityOS should detect privileged access drift.

| Drift Condition                                        | Meaning                              |
| ------------------------------------------------------ | ------------------------------------ |
| User has privileged access outside role                | Role drift.                          |
| User retains privileged access after department change | Department drift.                    |
| User retains privileged access after termination       | Critical leaver drift.               |
| Eligible role is never reviewed                        | Review drift.                        |
| Active role has no expiration                          | Standing privilege drift.            |
| Privileged group lacks owner                           | Ownership drift.                     |
| Service principal has excessive permissions            | Non-human identity privileged drift. |

---

## Privileged Access Work Queue

IdentityOS should prioritize privileged access issues.

| Priority | Work Item                              | Reason                                              |
| -------- | -------------------------------------- | --------------------------------------------------- |
| 1        | Privileged leaver access               | Former users must not retain elevated access.       |
| 2        | Permanent global or broad admin access | Standing privilege creates tenant-wide risk.        |
| 3        | Privileged access without approval     | Governance control failure.                         |
| 4        | Privileged access without expiration   | Access may become permanent.                        |
| 5        | Privileged non-human identity          | Automation identities can become high-impact risks. |
| 6        | Privileged group owner missing         | Access cannot be governed.                          |
| 7        | Privileged review overdue              | Elevated access must be revalidated.                |

---

## Dashboard Impact

Privileged access integration supports multiple dashboards.

| Dashboard                    | Impact                                                            |
| ---------------------------- | ----------------------------------------------------------------- |
| Executive Dashboard          | Shows critical privileged access risk.                            |
| IAM Operations Dashboard     | Shows privileged access requests and remediation tasks.           |
| Governance Dashboard         | Shows approvals, reviews, and exception handling.                 |
| Risk Dashboard               | Uses privileged access as a high-impact risk signal.              |
| Access Drift Dashboard       | Detects privileged access outside expected role.                  |
| Privileged Access Dashboard  | Shows active, eligible, standing, and reviewed privileged access. |
| Non-Human Identity Dashboard | Shows privileged service accounts and workload identities.        |
| Audit Evidence Dashboard     | Shows privileged access evidence.                                 |

---

## Safety Controls

Privileged access automation should include strict controls.

| Control                              | Purpose                                                     |
| ------------------------------------ | ----------------------------------------------------------- |
| Separate Privileged App Registration | Prevents normal automation from managing privileged access. |
| MFA Requirement                      | Strengthens activation security.                            |
| Justification Requirement            | Explains why access is needed.                              |
| Approval Requirement                 | Adds human control.                                         |
| Time Limitation                      | Prevents standing privilege.                                |
| Review Frequency                     | Ensures access remains justified.                           |
| Break-Glass Monitoring               | Tracks emergency access.                                    |
| Audit Logging                        | Preserves evidence for every privileged action.             |
| Post-Use Review                      | Confirms access was used appropriately.                     |

---

## Failure Handling

| Failure                          | Response                                     |
| -------------------------------- | -------------------------------------------- |
| Privileged role not found        | Stop workflow and escalate.                  |
| Principal not found              | Stop workflow and validate identity.         |
| Approval missing                 | Do not grant privileged access.              |
| MFA requirement not satisfied    | Do not activate privileged access.           |
| Assignment creation fails        | Log and escalate to privileged access owner. |
| Revocation fails                 | Escalate immediately.                        |
| Leaver privileged access remains | Escalate to security leadership.             |
| Evidence missing                 | Create audit remediation task.               |

---

## Example Privileged Access Record

```text id="hwhy4s"
Request ID: PIM-REQ-001
Principal: Daniel Kim
Role: User Administrator
Assignment Type: Eligible
Activation Required: Yes
Approval Required: Yes
Approver: IAM Manager
Justification: Temporary user administration support
Duration: 2 hours
MFA Required: Yes
Risk Level: High
Audit Required: Yes
Status: Approved with time-bound activation
```

---

## Summary

The Privileged Access Integration model shows how IdentityOS could connect privileged access decisions to Microsoft Entra PIM concepts.

The key architectural idea is:

> Privileged access should be eligible, justified, approved, time-bound, reviewed, monitored, and evidenced.
