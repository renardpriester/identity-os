# IdentityOS Access Review Model

## Purpose

The Access Review Model defines how IdentityOS validates whether users, contractors, vendors, privileged identities, and non-human identities should continue to have access over time.

Access reviews are a core part of identity governance. They help reduce stale access, privilege creep, unnecessary permissions, audit gaps, and unmanaged risk.

In IdentityOS, access reviews are not treated as once-a-year compliance exercises. They are part of continuous identity governance.

---

## Core Question

Every access review should answer one question:

> Should this identity still have this access?

To answer that question properly, reviewers need context.

They should understand:

* Who the identity belongs to
* What role the identity performs
* What access exists
* Why the access was granted
* Who approved it
* Whether the access is sensitive or privileged
* Whether the access is temporary
* When it was last reviewed
* Whether the access still aligns with business need

Access reviews should be meaningful, not mechanical.

---

## Review Types

IdentityOS supports multiple review types.

| Review Type               | Purpose                                                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| Manager Review            | Confirms whether direct reports still need access.                                           |
| Application Owner Review  | Confirms whether users still need access to a specific application.                          |
| Privileged Access Review  | Validates elevated or administrative access.                                                 |
| Contractor Review         | Confirms whether contractor access should continue.                                          |
| Vendor Review             | Confirms whether vendor access remains appropriate.                                          |
| Exception Review          | Reviews access outside the standard role model.                                              |
| Non-Human Identity Review | Validates service accounts, automation accounts, API identities, and application identities. |
| High-Risk Access Review   | Reviews sensitive or critical access.                                                        |

---

## Review Frequency Model

Review frequency should be based on risk.

| Access Type                  | Suggested Frequency          |
| ---------------------------- | ---------------------------- |
| Standard baseline access     | Annually                     |
| Department-specific access   | Quarterly                    |
| Sensitive application access | Quarterly                    |
| HR or Finance access         | Quarterly                    |
| Contractor access            | Monthly                      |
| Vendor access                | Monthly                      |
| Privileged access            | Monthly                      |
| Break-glass access           | Monthly                      |
| Exceptions                   | Monthly or before expiration |
| Non-human identities         | Quarterly                    |

The higher the risk, the more frequently access should be reviewed.

---

## Review Context

Reviewers should receive business-friendly context.

An access review should include:

* User name
* User principal name
* Department
* Job title
* Manager
* Worker type
* Employment status
* Application name
* Access package
* Permission level
* Risk level
* Date granted
* Last reviewed date
* Access owner
* Approval history
* Expiration date, if applicable
* Exception status, if applicable

Reviewers should not be forced to make decisions based only on technical group names.

---

## Review Decision Types

Reviewers should have clear decision options.

| Decision          | Meaning                                                       |
| ----------------- | ------------------------------------------------------------- |
| Approve           | Access is still required.                                     |
| Remove            | Access is no longer needed.                                   |
| Modify            | Access should be reduced or changed.                          |
| Extend            | Temporary access should continue until a new expiration date. |
| Expire            | Temporary access should end.                                  |
| Escalate          | Reviewer is unsure and needs another owner to review.         |
| Mark as Exception | Access is outside policy but has a documented justification.  |

Every decision should be recorded with reviewer, timestamp, and justification when needed.

---

## Manager Review Example

```text id="hs7c81"
User: Jordan Smith
Department: Finance
Job Title: Financial Analyst
Manager: Taylor Brooks
Access Package: Finance Analyst Baseline
Applications:
- Microsoft 365
- Finance SharePoint
- Financial Reporting Portal

Risk Level: High
Last Reviewed: 90 days ago

Decision Required:
Does Jordan still require this access?
```

Manager reviews should be simple, understandable, and actionable.

---

## Application Owner Review Example

```text id="3hcuw5"
Application: Financial Reporting Portal
Application Owner: Finance Operations
Review Scope: Users with reporting access

User: Jordan Smith
Department: Finance
Role: Financial Analyst
Access Level: Report Viewer
Risk Level: High
Last Used: 14 days ago

Decision Required:
Should this user retain access to the Financial Reporting Portal?
```

Application owner reviews help ensure that access remains aligned with data ownership and system responsibility.

---

## Privileged Access Review Example

```text id="ynfs8f"
User: Casey Nguyen
Department: Security
Role: Security Analyst
Privileged Assignment: Eligible Security Reader
Assignment Type: Eligible
Last Activated: 7 days ago
Approval Required: Yes
MFA Required: Yes
Risk Level: Critical

Decision Required:
Should this user remain eligible for this privileged role?
```

Privileged access should be reviewed more frequently than standard access.

---

## Contractor Review Example

```text id="qse4u8"
User: Riley Carter
Worker Type: Contractor
Sponsor: Taylor Brooks
Department: Legal Operations
Access Package: Project Workspace Access
Start Date: 2026-06-24
End Date: 2026-08-31
Review Frequency: Monthly

Decision Required:
Should this contractor's access continue?
```

Contractor access should expire automatically unless renewed by the sponsor.

---

## Non-Human Identity Review Example

```text id="9fgmjf"
Identity Name: svc-document-sync
Identity Type: Service Account
Owner: Legal Technology Team
Purpose: Synchronizes legal documents between systems
Access Scope:
- Document Management API
- Legal Archive Storage

Credential Rotation Required: Yes
Review Frequency: Quarterly
Risk Level: High

Decision Required:
Is this service account still required and properly scoped?
```

Non-human identities should always have an owner, purpose, access scope, and review cadence.

---

## Review Workflow

IdentityOS access reviews follow this workflow:

```text id="cag7e5"
Review campaign created
        ↓
Review scope selected
        ↓
Reviewers assigned
        ↓
Review context generated
        ↓
Reviewer decision submitted
        ↓
Decision recorded
        ↓
Remediation action triggered
        ↓
Audit evidence generated
        ↓
Metrics updated
```

Reviews should result in action, not just documentation.

---

## Remediation Actions

| Review Decision   | IdentityOS Action                       |
| ----------------- | --------------------------------------- |
| Approve           | Access remains active.                  |
| Remove            | Provisioning Engine removes access.     |
| Modify            | Access is reduced or changed.           |
| Extend            | New expiration date is applied.         |
| Expire            | Access is removed at expiration.        |
| Escalate          | Review is routed to another owner.      |
| Mark as Exception | Exception record is created or updated. |

The Governance Engine should track whether remediation was completed.

---

## Audit Evidence

Every access review should produce evidence.

Evidence should include:

* Review campaign name
* Review scope
* Reviewer
* Identity reviewed
* Access reviewed
* Decision
* Justification
* Timestamp
* Remediation status
* Policy reference
* Exception reference, if applicable

Audit evidence should be easy to retrieve, export, and explain.

---

## Access Review Metrics

IdentityOS should track metrics such as:

* Review completion rate
* Overdue reviews
* Access approved
* Access removed
* Access modified
* Exceptions extended
* Privileged access removed
* Contractor access expired
* Vendor access removed
* Non-human identities without owners
* Average review completion time
* Applications with the most stale access

Metrics help turn governance into operational visibility.

---

## Success Criteria

The Access Review Model is successful when:

* Reviewers understand what they are reviewing.
* Access decisions are completed on time.
* Stale access is removed.
* Privileged access is reviewed frequently.
* Contractor and vendor access expires appropriately.
* Exceptions do not become permanent.
* Non-human identities have owners.
* Audit evidence is automatically produced.
* Review outcomes reduce identity risk.

---

## Summary

The IdentityOS Access Review Model turns access review from a compliance burden into a continuous governance process.

Access should not only be granted correctly.

Access should remain correct over time.

> IdentityOS reviews access because trust must be continuously verified.
