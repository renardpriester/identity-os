# IdentityOS Governance Dashboard

## Purpose

The Governance Dashboard provides visibility into access reviews, approvals, exceptions, remediation actions, audit evidence, and governance health.

This dashboard is designed for IAM governance teams, auditors, compliance teams, access owners, application owners, managers, and security leadership.

The goal is to answer:

> Is access being reviewed, approved, remediated, and evidenced properly?

---

## Primary Audience

| Audience            | Purpose                                                                 |
| ------------------- | ----------------------------------------------------------------------- |
| IAM Governance Team | Track reviews, approvals, exceptions, remediation, and evidence.        |
| Auditors            | Validate that access decisions were reviewed and supported by evidence. |
| Compliance Teams    | Monitor review completion, exception handling, and policy alignment.    |
| Managers            | Review direct report access and approve or remove access.               |
| Application Owners  | Validate application-level access.                                      |
| Security Leadership | Understand governance risk and remediation progress.                    |

---

## Governance Questions

The Governance Dashboard should answer:

* Which access decisions require approval?
* Which access reviews are pending?
* Which reviews are overdue?
* Which exceptions exist?
* Which exceptions lack expiration?
* Which remediation tasks are incomplete?
* Which access removals were completed?
* Which privileged access reviews are required?
* Which contractor or vendor reviews are due?
* What audit evidence exists?

---

## Governance Dashboard Wireframe

```text id="hgy9aq"
+--------------------------------------------------------------------------------+
| IdentityOS Governance Dashboard                         Review Period: Current |
+--------------------------------------------------------------------------------+
| Reviews | Approvals | Exceptions | Remediation | Evidence | Reports            |
+--------------------------------------------------------------------------------+
| Pending Approvals | Review Required | Audit Required | Remediation | Exceptions |
|        2          |        2        |       7        |      4      |     0      |
+--------------------------------------------------------------------------------+
| Access Review Status                  | Approval Queue                         |
|---------------------------------------|----------------------------------------|
| Monthly Reviews: 3                    | Pending Approvals: 2                   |
| Quarterly Reviews: 3                  | Privileged Approval Required: 1        |
| Review Required: 2                    | Contractor Approval Required: 1        |
| Overdue Reviews: Future Metric        | Manager Approval Required: Future      |
+--------------------------------------------------------------------------------+
| Exceptions                            | Remediation                            |
|---------------------------------------|----------------------------------------|
| Exceptions Tracked: 0                 | Access Removals Required: 4            |
| Exceptions Without Expiration: 0      | Drift Remediation Required: 4          |
| Temporary Access: Future Metric       | Leaver Remediation Required: 1         |
| Exception Reviews Due: Future Metric  | Contractor Remediation Required: 1     |
+--------------------------------------------------------------------------------+
| Audit Evidence                        | Governance Reports                     |
|---------------------------------------|----------------------------------------|
| Audit Required Decisions: 7           | Governance Report                      |
| Evidence Generated: 3 Reports         | Risk Score Report                      |
| Review Evidence: Future Metric        | Access Drift Report                    |
| Remediation Evidence: Future Metric   | Dashboard Summary                      |
+--------------------------------------------------------------------------------+
```

---

## Top KPI Cards

| KPI Card             | Purpose                                         |
| -------------------- | ----------------------------------------------- |
| Pending Approvals    | Shows access decisions waiting for approval.    |
| Review Required      | Shows decisions requiring governance review.    |
| Audit Required       | Shows decisions requiring audit evidence.       |
| Remediation Required | Shows access actions that need completion.      |
| Exceptions           | Shows access outside the standard policy model. |

---

## Access Review Status Panel

The Access Review Status panel shows review activity and review cadence.

| Metric            | Purpose                                    |
| ----------------- | ------------------------------------------ |
| Monthly Reviews   | Shows higher-risk access reviewed monthly. |
| Quarterly Reviews | Shows recurring access reviews.            |
| Review Required   | Shows decisions needing review.            |
| Overdue Reviews   | Shows reviews not completed on time.       |
| Access Approved   | Shows access retained after review.        |
| Access Removed    | Shows access removed through review.       |

### Governance Interpretation

Access reviews are healthy when:

* Reviews are completed on time.
* Reviewers have enough context.
* Unnecessary access is removed.
* Review decisions generate evidence.
* Remediation is tracked to completion.

---

## Approval Queue Panel

The Approval Queue panel shows access waiting for human decision.

| Approval Type              | Purpose                                  |
| -------------------------- | ---------------------------------------- |
| Manager Approval           | Confirms business need for access.       |
| Application Owner Approval | Confirms application-level access.       |
| Sponsor Approval           | Confirms contractor or vendor access.    |
| Security Approval          | Confirms sensitive or privileged access. |
| Privileged Access Approval | Confirms elevated access justification.  |

### Governance Interpretation

Approvals should be:

* Routed to the correct owner
* Completed within expected time
* Supported by business justification
* Logged for audit
* Connected to the final access decision

---

## Exception Management Panel

The Exception Management panel tracks access outside the standard role or policy model.

| Metric                        | Purpose                                             |
| ----------------------------- | --------------------------------------------------- |
| Exceptions Tracked            | Shows documented policy exceptions.                 |
| Exceptions Without Expiration | Shows unmanaged exception risk.                     |
| Exception Reviews Due         | Shows exceptions requiring revalidation.            |
| Temporary Access              | Shows approved time-bound exceptions.               |
| Exceptions Expired            | Shows exceptions that should be removed or renewed. |

### Governance Interpretation

Exceptions should be:

* Documented
* Approved
* Owned
* Time-bound
* Reviewed frequently
* Removed or renewed before expiration

An exception without expiration can become permanent risk.

---

## Remediation Panel

The Remediation panel shows governance decisions that require action.

| Remediation Type         | Purpose                                                       |
| ------------------------ | ------------------------------------------------------------- |
| Remove Access            | Removes access no longer needed.                              |
| Modify Access            | Reduces or adjusts permissions.                               |
| Expire Access            | Removes temporary access after expiration.                    |
| Disable Identity         | Disables user, contractor, vendor, or service account access. |
| Reassign Ownership       | Transfers ownership of groups, apps, or service accounts.     |
| Review Privileged Access | Confirms elevated access remains justified.                   |

### Governance Interpretation

Governance is incomplete if review decisions do not trigger remediation.

A strong governance process tracks remediation until completion.

---

## Audit Evidence Panel

The Audit Evidence panel shows whether IdentityOS can prove what happened.

| Evidence Type            | Purpose                                                         |
| ------------------------ | --------------------------------------------------------------- |
| Policy Decision Evidence | Shows why access was granted, removed, retained, or reviewed.   |
| Review Evidence          | Shows reviewer decision and timestamp.                          |
| Approval Evidence        | Shows approver, justification, and decision.                    |
| Remediation Evidence     | Shows access removal or adjustment completion.                  |
| Exception Evidence       | Shows justification, owner, approval, and expiration.           |
| Report Evidence          | Shows generated governance, risk, drift, and dashboard reports. |

### Governance Interpretation

Audit evidence should answer:

* Who reviewed the access?
* What decision was made?
* Why was the decision made?
* Was access remediated?
* When did it happen?
* What policy or event triggered it?

---

## Governance Work Queue

The Governance Dashboard should include a work queue.

| Priority | Work Type                         | Reason                                       |
| -------- | --------------------------------- | -------------------------------------------- |
| 1        | Critical access drift remediation | Excess access may create urgent risk.        |
| 2        | Privileged access review          | Elevated access must be governed.            |
| 3        | Leaver remediation evidence       | Offboarding must be provable.                |
| 4        | Contractor expiration review      | External access must expire or be renewed.   |
| 5        | Pending approvals                 | Access decisions require owner action.       |
| 6        | Access reviews required           | Access must remain justified.                |
| 7        | Exception review                  | Exceptions must remain valid and time-bound. |

---

## Filters

The Governance Dashboard should support these filters:

| Filter          | Purpose                                               |
| --------------- | ----------------------------------------------------- |
| Review Status   | Pending, completed, overdue, escalated.               |
| Approval Status | Approved, denied, pending, escalated.                 |
| Risk Level      | Low, Medium, High, Critical.                          |
| Worker Type     | Employee, contractor, vendor, service account.        |
| Access Type     | Standard, sensitive, privileged, exception.           |
| Governance Type | Approval, review, exception, expiration, remediation. |
| Application     | Filter by application or resource.                    |
| Department      | Filter by business unit or department.                |

---

## Drilldowns

Governance users should be able to drill down into:

| Drilldown          | Purpose                                                        |
| ------------------ | -------------------------------------------------------------- |
| Review Detail      | Shows reviewer, decision, access reviewed, and timestamp.      |
| Approval Detail    | Shows approver, business justification, and approval outcome.  |
| Exception Detail   | Shows owner, expiration, risk, and justification.              |
| Remediation Detail | Shows access action, status, and completion evidence.          |
| Audit Detail       | Shows policy decision, evidence, and report link.              |
| Identity Detail    | Shows user context, access, risk, drift, and governance state. |

---

## Data Sources

The Governance Dashboard uses these sample sources:

| Source                                   | Purpose                                                |
| ---------------------------------------- | ------------------------------------------------------ |
| `examples/sample-policy-decisions.json`  | Provides governance requirements and policy decisions. |
| `reports/sample-governance-report.md`    | Provides governance summary and evidence.              |
| `reports/sample-risk-score-report.md`    | Provides risk context for governance prioritization.   |
| `reports/sample-access-drift-report.md`  | Provides drift findings requiring remediation.         |
| `reports/sample-dashboard-summary.md`    | Provides dashboard-ready governance metrics.           |
| `examples/sample-dashboard-metrics.json` | Provides governance dashboard metrics.                 |

---

## Success Criteria

The Governance Dashboard is successful when governance users can quickly see:

* Which reviews are required
* Which approvals are pending
* Which exceptions exist
* Which remediation tasks are open
* Which access removals are required
* Which decisions require evidence
* Which reports prove governance activity
* Which items should be prioritized first

---

## Summary

The IdentityOS Governance Dashboard turns identity governance into operational visibility.

It helps organizations prove that access was reviewed, approved, remediated, and evidenced.

> Governance dashboards turn access accountability into visible action.
