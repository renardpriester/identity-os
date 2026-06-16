# IdentityOS Dashboard Concepts

## Purpose

The IdentityOS Dashboard Concepts document defines how identity lifecycle activity, governance status, access risk, access drift, automation results, and audit evidence can be presented through dashboards.

The goal of the dashboard layer is to turn identity operations into measurable visibility for security leaders, IAM teams, auditors, application owners, managers, and executives.

IdentityOS should not only make access decisions. It should help the organization understand identity risk.

---

## Dashboard Philosophy

Identity dashboards should answer practical questions.

Examples:

* Are users being onboarded on time?
* Are leavers being deprovisioned quickly?
* Which identities are highest risk?
* Which access decisions require approval?
* Where is access drift happening?
* Which privileged roles need review?
* Which contractors are near expiration?
* Which access reviews are overdue?
* Which applications have the most stale access?
* Which governance actions are incomplete?
* Can we prove that access decisions were reviewed and remediated?

A dashboard should make identity risk visible, explainable, and actionable.

---

## Dashboard Audiences

Different audiences need different dashboard views.

| Audience                 | Primary Need                                                                           |
| ------------------------ | -------------------------------------------------------------------------------------- |
| Executives               | High-level identity risk, governance health, and program maturity.                     |
| IAM Team                 | Operational queues, automation status, access changes, and remediation work.           |
| Security Team            | High-risk identities, privileged access, access drift, and suspicious access patterns. |
| Auditors                 | Evidence, review completion, remediation proof, and policy alignment.                  |
| Application Owners       | Application access reviews, stale access, and access ownership.                        |
| Managers                 | Direct report access reviews, approvals, and exceptions.                               |
| HR / Business Operations | Joiner, Mover, Leaver status and lifecycle completion.                                 |

---

## Executive Identity Risk Dashboard

The Executive Identity Risk Dashboard provides leadership-level visibility.

### Key Metrics

| Metric                        | Purpose                                                      |
| ----------------------------- | ------------------------------------------------------------ |
| Total Identities              | Shows the size of the identity population.                   |
| High-Risk Identities          | Shows identities with elevated risk scores.                  |
| Critical-Risk Identities      | Shows identities requiring urgent review or remediation.     |
| Access Drift Detected         | Shows where actual access no longer matches expected access. |
| Privileged Access Count       | Shows how many identities have elevated access.              |
| Overdue Access Reviews        | Shows governance delays.                                     |
| Leaver Remediation Time       | Shows how quickly access is removed after departure.         |
| Contractor Expiration Risk    | Shows contractors with upcoming or expired access.           |
| Exceptions Without Expiration | Shows policy exceptions that may become permanent risk.      |

### Executive Questions Answered

* Is identity risk increasing or decreasing?
* Are privileged identities governed?
* Are leavers being removed quickly?
* Are access reviews being completed?
* Where is the organization exposed?
* What identity risks require leadership attention?

---

## IAM Operations Dashboard

The IAM Operations Dashboard is designed for the identity operations team.

### Key Metrics

| Metric                           | Purpose                                     |
| -------------------------------- | ------------------------------------------- |
| Joiner Events Processed          | Tracks onboarding volume.                   |
| Mover Events Processed           | Tracks role and department changes.         |
| Leaver Events Processed          | Tracks offboarding activity.                |
| Pending Approvals                | Shows decisions waiting for action.         |
| Failed Automation Actions        | Shows workflows requiring manual attention. |
| Access Grants                    | Tracks access assigned.                     |
| Access Removals                  | Tracks access removed.                      |
| Remediation Tasks Open           | Shows incomplete governance actions.        |
| Average Workflow Completion Time | Measures IAM operational efficiency.        |

### IAM Questions Answered

* What work is waiting?
* What automation failed?
* Which access removals are pending?
* Which approvals are blocking access?
* Which lifecycle events are incomplete?
* Where is manual intervention needed?

---

## Governance Dashboard

The Governance Dashboard tracks access reviews, approvals, exceptions, and remediation.

### Key Metrics

| Metric                        | Purpose                                      |
| ----------------------------- | -------------------------------------------- |
| Access Reviews Completed      | Shows review progress.                       |
| Access Reviews Overdue        | Shows review risk.                           |
| Access Approved               | Shows retained access.                       |
| Access Removed                | Shows governance effectiveness.              |
| Access Modified               | Shows access reduction or correction.        |
| Exceptions Approved           | Shows policy deviations.                     |
| Exceptions Expired            | Shows exception lifecycle control.           |
| Exceptions Without Expiration | Shows unmanaged exception risk.              |
| Remediation Completed         | Shows follow-through after review decisions. |

### Governance Questions Answered

* Are reviews being completed on time?
* Are reviewers removing unnecessary access?
* Are exceptions being controlled?
* Are remediation actions completed?
* Can we prove governance decisions were made?
* Can we prove access was removed when required?

---

## Access Drift Dashboard

The Access Drift Dashboard focuses on privilege creep and stale access.

### Key Metrics

| Metric                   | Purpose                                         |
| ------------------------ | ----------------------------------------------- |
| Identities with Drift    | Shows how many identities have access mismatch. |
| Department Drift         | Shows access from previous departments.         |
| Role Drift               | Shows access outside current role package.      |
| Privilege Drift          | Shows privileged access no longer justified.    |
| Contractor Drift         | Shows contractor access after expiration.       |
| Leaver Drift             | Shows access remaining after departure.         |
| Non-Human Identity Drift | Shows unmanaged service account risk.           |
| Drift Remediation Rate   | Shows how quickly drift is fixed.               |

### Access Drift Questions Answered

* Where is privilege creep happening?
* Which users retained access from previous roles?
* Which applications have the most drift?
* Which departments create the most drift?
* Which drift findings are critical?
* How quickly is drift remediated?

---

## Privileged Access Dashboard

The Privileged Access Dashboard focuses on elevated permissions.

### Key Metrics

| Metric                             | Purpose                                   |
| ---------------------------------- | ----------------------------------------- |
| Total Privileged Identities        | Shows privileged access population.       |
| Permanent Privileged Assignments   | Shows standing privilege risk.            |
| Eligible Privileged Assignments    | Shows just-in-time privilege posture.     |
| Privileged Activations             | Tracks elevated access usage.             |
| Privileged Access Pending Approval | Shows requests awaiting decision.         |
| Privileged Access Review Overdue   | Shows governance risk.                    |
| Privileged Leaver Access Removed   | Shows offboarding control effectiveness.  |
| High-Risk Privileged Identities    | Shows privileged accounts needing review. |

### Privileged Access Questions Answered

* Who has elevated access?
* Which privileged access is permanent?
* Which privileged access is overdue for review?
* Are privileged leavers fully deprovisioned?
* Which privileged identities are highest risk?

---

## Contractor and Vendor Dashboard

The Contractor and Vendor Dashboard focuses on temporary and external access.

### Key Metrics

| Metric                            | Purpose                                 |
| --------------------------------- | --------------------------------------- |
| Active Contractors                | Shows contractor identity population.   |
| Active Vendors                    | Shows vendor identity population.       |
| Contractors Near Expiration       | Shows upcoming renewal or removal work. |
| Expired Contractors Still Active  | Shows critical governance risk.         |
| Vendors Without Sponsors          | Shows ownership gaps.                   |
| Contractor Access Reviews Overdue | Shows review delays.                    |
| Vendor Access Removed             | Shows offboarding effectiveness.        |
| External Access Exceptions        | Shows non-standard external access.     |

### Contractor and Vendor Questions Answered

* Which contractors are expiring soon?
* Which contractors are still active after expiration?
* Which vendors lack business sponsorship?
* Which external identities have sensitive access?
* Are external identities reviewed more frequently?

---

## Non-Human Identity Dashboard

The Non-Human Identity Dashboard focuses on service accounts, automation accounts, application identities, and API identities.

### Key Metrics

| Metric                               | Purpose                                             |
| ------------------------------------ | --------------------------------------------------- |
| Total Non-Human Identities           | Shows non-human identity population.                |
| Non-Human Identities Without Owner   | Shows ownership risk.                               |
| Non-Human Identities Without Purpose | Shows governance gaps.                              |
| High-Risk Service Accounts           | Shows sensitive or privileged non-human identities. |
| Credential Rotation Overdue          | Shows secret and credential risk.                   |
| Access Scope Review Overdue          | Shows access validation gaps.                       |
| Dormant Non-Human Identities         | Shows unused identities that may need removal.      |

### Non-Human Identity Questions Answered

* Which service accounts lack owners?
* Which automation identities have sensitive access?
* Which credentials need rotation?
* Which non-human identities are unused?
* Which non-human identities should be removed or reviewed?

---

## Automation Health Dashboard

The Automation Health Dashboard shows how well IdentityOS automation is working.

### Key Metrics

| Metric                      | Purpose                              |
| --------------------------- | ------------------------------------ |
| Automation Runs Completed   | Shows successful workflow execution. |
| Automation Runs Failed      | Shows failures requiring attention.  |
| Manual Overrides            | Shows where automation was bypassed. |
| Average Processing Time     | Shows workflow performance.          |
| Policy Decisions Generated  | Shows automation volume.             |
| Reports Generated           | Shows reporting activity.            |
| Remediation Tasks Created   | Shows governance follow-through.     |
| Remediation Tasks Completed | Shows completion effectiveness.      |

### Automation Questions Answered

* Is automation reducing manual work?
* Which workflows are failing?
* Which workflows require human intervention?
* Are reports being generated successfully?
* Is remediation being completed?

---

## Dashboard Data Sources

IdentityOS dashboards can use data from multiple project components.

| Data Source                 | Example Data                                                               |
| --------------------------- | -------------------------------------------------------------------------- |
| Identity Events             | Joiner, Mover, Leaver, contractor, privileged, non-human identity events   |
| Policy Decisions            | Access to grant, remove, retain, review, approve, deny, expire             |
| Risk Scoring Results        | Risk score, risk level, risk factors, recommended action                   |
| Access Drift Results        | Drift type, drift severity, excess access, remediation recommendation      |
| Governance Results          | Reviews, approvals, exceptions, remediation, audit evidence                |
| Reports                     | Governance report, risk score report, access drift report                  |
| Future Entra ID Integration | Users, groups, access packages, app assignments, privileged roles, reviews |

---

## Dashboard Design Principles

IdentityOS dashboards should follow these principles:

* Show risk clearly.
* Make governance status visible.
* Highlight critical actions first.
* Separate executive views from operational views.
* Make metrics explainable.
* Connect every metric to an action.
* Show trends over time.
* Support audit and evidence needs.
* Avoid overwhelming users with unnecessary detail.
* Help identity teams prioritize work.

---

## Example Dashboard Layout

An IdentityOS dashboard could include:

| Section              | Purpose                                                 |
| -------------------- | ------------------------------------------------------- |
| Executive Summary    | Overall identity risk and governance health.            |
| Lifecycle Activity   | Joiner, Mover, Leaver, contractor, and vendor activity. |
| Risk Overview        | High-risk and critical-risk identities.                 |
| Access Drift         | Access mismatch, stale access, and privilege creep.     |
| Governance Queue     | Reviews, approvals, exceptions, and remediation tasks.  |
| Privileged Access    | Elevated access assignments and review status.          |
| External Identities  | Contractor and vendor access status.                    |
| Non-Human Identities | Service account ownership and credential governance.    |
| Automation Health    | Workflow success, failure, and manual intervention.     |
| Audit Evidence       | Reports and proof of completed decisions.               |

---

## Success Criteria

The dashboard layer is successful when:

* Leaders can understand identity risk quickly.
* IAM teams can see operational work clearly.
* Security teams can identify high-risk identities.
* Auditors can find evidence easily.
* Managers can complete reviews with context.
* Application owners can validate access.
* Access drift becomes visible.
* Privileged access risk is measurable.
* Contractor and vendor access is governed.
* Non-human identity risk is tracked.
* Automation results are measurable.

---

## Summary

The IdentityOS dashboard layer turns identity activity into visibility.

It helps organizations move from reactive IAM operations to measurable identity governance, risk management, and operational intelligence.

> Identity dashboards make trust visible.
