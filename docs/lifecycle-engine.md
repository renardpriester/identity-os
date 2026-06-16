# IdentityOS Lifecycle Engine

## Purpose

The Lifecycle Engine is the core operating engine of IdentityOS.

It is responsible for detecting, classifying, and orchestrating identity lifecycle events across the enterprise.

In traditional IAM environments, identity lifecycle work is often handled through manual tickets, emails, spreadsheets, approvals, and disconnected scripts. This creates delays, inconsistent access, privilege creep, audit gaps, and security risk.

The Lifecycle Engine is designed to solve that problem by turning identity lifecycle events into structured, policy-driven workflows.

---

## Core Responsibility

The Lifecycle Engine manages the identity journey from creation to removal.

It handles:

* Joiner events
* Mover events
* Leaver events
* Contractor onboarding
* Contractor expiration
* Vendor access lifecycle
* Leave of absence
* Rehire scenarios
* Privileged access lifecycle
* Non-human identity lifecycle

The goal is to ensure that identity changes are handled consistently, securely, and with complete auditability.

---

## Lifecycle Engine Concept

The Lifecycle Engine follows a simple operating model:

```text id="a4n4nh"
Identity Event
      ↓
Event Classification
      ↓
Policy Evaluation
      ↓
Workflow Execution
      ↓
Provisioning / Deprovisioning
      ↓
Governance Record
      ↓
Audit Evidence
```

The Lifecycle Engine does not work alone. It coordinates with the Policy Engine, Provisioning Engine, Governance Engine, Automation Engine, and Analytics Engine.

---

## Primary Lifecycle Events

IdentityOS focuses on three primary lifecycle events:

1. **Joiner**
2. **Mover**
3. **Leaver**

These three events represent the foundation of enterprise identity management.

---

## Joiner Event

A Joiner event occurs when a new identity enters the organization.

This may include:

* Full-time employee
* Part-time employee
* Contractor
* Vendor
* Intern
* Consultant
* Temporary worker

### Joiner Objective

The objective of the Joiner workflow is to ensure that the new identity receives appropriate access before or on their first day.

The Joiner process should balance:

* Security
* Productivity
* Accuracy
* Auditability
* Manager visibility
* Role-based access assignment

### Joiner Workflow

```text id="an7im8"
HR creates worker record
        ↓
Lifecycle Engine detects Joiner event
        ↓
Identity attributes are validated
        ↓
Policy Engine evaluates role and access requirements
        ↓
Provisioning Engine creates identity
        ↓
Baseline access is assigned
        ↓
Role-based access package is assigned
        ↓
MFA and Conditional Access requirements are applied
        ↓
Required applications are provisioned
        ↓
Manager notification is sent
        ↓
Audit record is created
```

### Joiner Required Attributes

A Joiner workflow should require key identity attributes such as:

* First name
* Last name
* Worker type
* Department
* Job title
* Manager
* Location
* Start date
* Employment status
* Business unit
* Cost center
* Role package
* Required applications
* Privileged access eligibility

### Joiner Outcomes

A successful Joiner workflow should result in:

* Identity created
* Correct username assigned
* Correct department and manager attributes populated
* Baseline groups assigned
* Role-based groups assigned
* Required applications provisioned
* MFA required
* Conditional Access applied
* Manager notified
* Audit evidence recorded

The new user should be able to begin work without unnecessary access delays.

---

## Mover Event

A Mover event occurs when an existing identity changes role, department, manager, location, business unit, or responsibility.

Mover events are one of the most important parts of IAM because they are a major source of privilege creep.

A user may move into a new role and receive new access while keeping access from the previous role. Over time, this creates excessive permissions and unnecessary risk.

### Mover Objective

The objective of the Mover workflow is to align access with the user’s current business role.

The system should not simply add new access.

It should evaluate what access must be added, retained, removed, reviewed, or approved.

### Mover Workflow

```text id="vhuje4"
HR updates worker attributes
        ↓
Lifecycle Engine detects Mover event
        ↓
Current access is collected
        ↓
New role requirements are evaluated
        ↓
Access comparison is performed
        ↓
Required access is added
        ↓
Obsolete access is removed
        ↓
Exceptions are routed for approval
        ↓
Manager and application owners are notified if needed
        ↓
Governance record is updated
        ↓
Audit record is created
```

### Mover Trigger Examples

Mover workflows may be triggered by:

* Department change
* Job title change
* Manager change
* Location change
* Promotion
* Demotion
* Transfer
* Temporary assignment
* Project assignment
* Privileged role eligibility change
* Business unit change

### Mover Access Evaluation

The Mover workflow should compare:

* Current access
* Required access for the new role
* Access no longer needed
* Access requiring review
* Access requiring approval
* Privileged access assignments
* Exceptions and temporary access

### Mover Outcomes

A successful Mover workflow should result in:

* New role access assigned
* Old role access removed
* Privileged access reviewed
* Exceptions documented
* Manager notified
* Application owners notified if needed
* Access drift reduced
* Audit evidence created

The Mover workflow is critical to preventing access accumulation.

---

## Leaver Event

A Leaver event occurs when an identity exits the organization or no longer requires access.

This may include:

* Employee termination
* Contractor end date
* Vendor access expiration
* Retirement
* Resignation
* Involuntary termination
* End of temporary assignment

### Leaver Objective

The objective of the Leaver workflow is to remove access quickly, consistently, and completely.

Offboarding is one of the highest-risk identity processes because delayed access removal can expose the organization to unauthorized access, data loss, compliance violations, and insider risk.

### Leaver Workflow

```text id="rj6b10"
HR records termination or end date
        ↓
Lifecycle Engine detects Leaver event
        ↓
Identity status is validated
        ↓
Account is disabled
        ↓
Active sessions are revoked
        ↓
Group memberships are removed
        ↓
Privileged access is removed
        ↓
Application access is deprovisioned
        ↓
Mailbox and data handling policies are applied
        ↓
Manager or owner is notified
        ↓
Audit record is created
```

### Leaver Required Actions

A Leaver workflow should include:

* Disable account
* Revoke sessions
* Reset or block credentials
* Remove security groups
* Remove distribution groups
* Remove application access
* Remove privileged roles
* Remove admin eligibility
* Transfer ownership where needed
* Preserve records according to policy
* Notify manager
* Generate audit evidence

### Leaver Outcomes

A successful Leaver workflow should result in:

* Access removed
* Sessions revoked
* Privileged access removed
* Applications deprovisioned
* Resources reassigned where required
* Records preserved
* Audit evidence available
* Identity risk reduced

The Leaver workflow should be fast, reliable, and auditable.

---

## Contractor Lifecycle

Contractors require special lifecycle handling because their access is often temporary.

IdentityOS should enforce:

* Start date
* End date
* Sponsoring manager
* Business justification
* Limited access
* Expiration date
* Periodic review
* Automatic deprovisioning

Contractor access should not remain active indefinitely.

### Contractor Workflow

```text id="okiwg8"
Contractor request submitted
        ↓
Sponsor and business need validated
        ↓
Access package assigned
        ↓
Expiration date enforced
        ↓
Periodic review scheduled
        ↓
Access expires or is renewed
        ↓
Audit evidence recorded
```

---

## Vendor Lifecycle

Vendor access must be carefully governed because vendors often access sensitive enterprise systems from outside the organization.

Vendor identities should include:

* Vendor company
* Business sponsor
* Access purpose
* Approved applications
* Start date
* End date
* Access restrictions
* MFA requirements
* Review cadence
* Expiration policy

Vendor access should be limited, monitored, and reviewed.

---

## Leave of Absence

A leave of absence may require temporary access modification.

IdentityOS should support workflows for:

* Medical leave
* Administrative leave
* Legal hold
* Suspension
* Temporary inactive status
* Return from leave

Access may need to be restricted, paused, or restored depending on business and compliance requirements.

---

## Rehire Scenario

A rehire event occurs when a former employee returns to the organization.

The Lifecycle Engine should determine whether to:

* Create a new identity
* Reactivate an existing identity
* Preserve previous records
* Assign new access based on the current role
* Avoid automatically restoring old access
* Validate manager and department
* Apply current policies

Rehire workflows should not blindly restore historical access.

Access must reflect the user’s current role and business need.

---

## Non-Human Identity Lifecycle

IdentityOS should also manage non-human identities.

Examples include:

* Service accounts
* Automation accounts
* API identities
* Application registrations
* Managed identities
* Integration accounts
* Bots

Non-human identities should have:

* Owner
* Purpose
* Permissions
* Expiration or review date
* Credential rotation policy
* Monitoring
* Documentation
* Decommissioning process

A non-human identity without an owner is an unmanaged risk.

---

## Lifecycle State Model

IdentityOS should track identity states such as:

| State          | Description                                            |
| -------------- | ------------------------------------------------------ |
| Pre-Hire       | Identity record exists before start date.              |
| Active         | Identity is active and access is assigned.             |
| Modified       | Identity attributes or role have changed.              |
| Pending Review | Access requires manager or owner review.               |
| Suspended      | Identity access is temporarily restricted.             |
| Expiring       | Contractor or vendor access is approaching expiration. |
| Terminated     | Identity is no longer active.                          |
| Archived       | Identity records are retained for audit or compliance. |

Tracking lifecycle state helps ensure identity actions are consistent and auditable.

---

## Lifecycle Audit Evidence

Every lifecycle event should generate evidence.

Evidence may include:

* Event type
* Event source
* Identity affected
* Timestamp
* Previous attributes
* New attributes
* Policy decision
* Access added
* Access removed
* Approvals
* Exceptions
* Workflow status
* Completion time

This evidence supports compliance, investigations, and operational reporting.

---

## Lifecycle Metrics

The Lifecycle Engine should produce metrics such as:

* Average onboarding completion time
* Number of pending Joiner events
* Number of Mover events processed
* Access removed during Mover events
* Average offboarding completion time
* Number of failed deprovisioning actions
* Contractor accounts nearing expiration
* Dormant identities
* Privileged access removed during lifecycle events
* Lifecycle workflow error rate

These metrics help IAM and security leaders understand whether identity operations are healthy.

---

## Lifecycle Engine Success Criteria

The Lifecycle Engine is successful when:

* New users receive appropriate access on time.
* Role changes remove outdated access.
* Leavers are deprovisioned quickly.
* Contractors expire automatically unless renewed.
* Privileged access is reviewed during lifecycle changes.
* Audit evidence is generated automatically.
* Manual identity work is reduced.
* Access aligns with business intent.
* Identity risk decreases over time.

---

## Summary

The Lifecycle Engine is the heart of IdentityOS.

It turns business events into secure, automated, auditable identity workflows.

By managing Joiners, Movers, Leavers, contractors, vendors, rehires, and non-human identities, the Lifecycle Engine ensures that access changes as the business changes.

> The Lifecycle Engine ensures identity never becomes stale, forgotten, or disconnected from business reality.
