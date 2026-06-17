# IdentityOS Privileged Access Dashboard

## Purpose

The Privileged Access Dashboard provides visibility into elevated access, privileged identities, privileged access requests, standing privilege, eligibility, activation activity, review status, access drift, and remediation needs.

This dashboard is designed to help IAM, security, governance, and leadership teams understand privileged access exposure and prioritize privileged access remediation.

The goal is to answer:

> Who has elevated access, why do they have it, and is it still justified?

---

## Primary Audience

| Audience            | Purpose                                                                |
| ------------------- | ---------------------------------------------------------------------- |
| IAM Engineers       | Track privileged assignments, removals, and governance tasks.          |
| Security Teams      | Monitor elevated access risk and privileged access drift.              |
| Governance Teams    | Review privileged access approvals, reviews, and evidence.             |
| Security Leadership | Understand privileged access exposure and critical-risk findings.      |
| Auditors            | Validate that privileged access was approved, reviewed, and evidenced. |

---

## Privileged Access Questions

The Privileged Access Dashboard should answer:

* Which identities have privileged access?
* Which privileged roles are permanent?
* Which privileged roles are eligible or time-bound?
* Which privileged access requests are pending approval?
* Which privileged assignments require review?
* Which privileged identities are high risk or critical risk?
* Which leavers had privileged access?
* Which privileged access should be removed?
* Which privileged access has audit evidence?
* Which privileged access appears as drift?

---

## Privileged Access Dashboard Wireframe

```text id="wh0xuf"
+--------------------------------------------------------------------------------+
| IdentityOS Privileged Access Dashboard                  Privilege View: Current |
+--------------------------------------------------------------------------------+
| Overview | Requests | Standing Access | Reviews | Drift | Evidence             |
+--------------------------------------------------------------------------------+
| Privileged Identities | Pending Requests | Critical Risk | Reviews Required     |
|          1            |        1         |       1       |        1             |
+--------------------------------------------------------------------------------+
| Privileged Access Overview              | Privileged Request Queue              |
|-----------------------------------------|---------------------------------------|
| Privileged Access Requests: 1           | Requested Role: Security Reader       |
| Eligible Assignments: 1                 | Approval Required: Yes                |
| Standing Privilege: Review              | MFA Required: Yes                     |
| Privileged Reviews Required: 1          | Justification Required: Yes           |
+--------------------------------------------------------------------------------+
| Privileged Risk                         | Privileged Access Drift               |
|-----------------------------------------|---------------------------------------|
| Critical Privileged Findings: 1         | Privileged Leaver Risk: Review        |
| High Risk Privileged Identities: Future | Excess Privileged Access: Review      |
| Privileged Leaver Access: Review        | Privilege Drift: Future Metric        |
| Audit Required: Yes                     | Remediation Required: Yes             |
+--------------------------------------------------------------------------------+
| Governance Controls                     | Evidence and Reports                  |
|-----------------------------------------|---------------------------------------|
| MFA                                     | Risk Score Report                     |
| Justification                           | Access Drift Report                   |
| Approval                                | Governance Report                     |
| Time Limit                              | Dashboard Summary                     |
| Audit Logging                           |                                       |
+--------------------------------------------------------------------------------+
```

---

## Top KPI Cards

| KPI Card              | Purpose                                                |
| --------------------- | ------------------------------------------------------ |
| Privileged Identities | Shows identities with elevated access.                 |
| Pending Requests      | Shows privileged access requests waiting for approval. |
| Critical Risk         | Shows privileged access requiring urgent attention.    |
| Reviews Required      | Shows privileged assignments needing review.           |
| Standing Access       | Shows permanent or long-lived privileged access risk.  |
| Privileged Drift      | Shows elevated access no longer justified.             |

---

## Privileged Access Overview Panel

The Privileged Access Overview panel summarizes elevated access activity.

| Metric                      | Purpose                                            |
| --------------------------- | -------------------------------------------------- |
| Privileged Access Requests  | Shows requests for elevated access.                |
| Eligible Assignments        | Shows just-in-time or eligible access assignments. |
| Permanent Assignments       | Shows standing privilege risk.                     |
| Time-Bound Assignments      | Shows temporary elevated access.                   |
| Privileged Reviews Required | Shows assignments requiring governance review.     |
| Privileged Access Removed   | Shows remediation progress.                        |

### Privileged Access Interpretation

Privileged access should be treated as high impact because it can affect users, applications, systems, tenant settings, security controls, and data.

---

## Privileged Request Queue

The Privileged Request Queue shows elevated access requests requiring action.

| Field                  | Purpose                                            |
| ---------------------- | -------------------------------------------------- |
| Identity               | User requesting elevated access.                   |
| Requested Role         | Privileged role requested.                         |
| Business Justification | Reason for the access request.                     |
| Approval Required      | Whether the request needs human approval.          |
| MFA Required           | Whether strong authentication is required.         |
| Duration               | How long access should last.                       |
| Risk Level             | Risk severity of the request.                      |
| Status                 | Pending, approved, denied, expired, or remediated. |

---

## Governance Controls Panel

Privileged access should require strong governance controls.

| Control          | Purpose                                                          |
| ---------------- | ---------------------------------------------------------------- |
| MFA              | Confirms strong authentication.                                  |
| Justification    | Requires business reason for elevated access.                    |
| Approval         | Ensures a manager, owner, or security approver validates access. |
| Time Limit       | Prevents standing privilege where possible.                      |
| Audit Logging    | Creates evidence of privileged access activity.                  |
| Review Frequency | Ensures privileged access is reviewed frequently.                |
| Remediation      | Removes privileged access when no longer justified.              |

---

## Standing Privilege Panel

Standing privilege means privileged access remains active or assigned for long periods.

| Standing Privilege Signal             | Risk                                                    |
| ------------------------------------- | ------------------------------------------------------- |
| Permanent admin assignment            | High risk because access is always active.              |
| Privileged role without review        | Risk increases when privileged access is not validated. |
| Privileged role without justification | Access cannot be explained.                             |
| Privileged role without expiration    | Access may become permanent.                            |
| Privileged role after role change     | Creates privilege creep.                                |
| Privileged access after departure     | Critical offboarding failure.                           |

### Standing Privilege Interpretation

Standing privilege should be minimized.

The preferred model is:

```text id="jczyku"
Eligible access
      ↓
Justification
      ↓
Approval
      ↓
Time-bound activation
      ↓
Audit logging
      ↓
Automatic expiration
```

---

## Privileged Access Drift Panel

Privileged access drift occurs when elevated access no longer aligns with business need.

| Drift Type       | Meaning                                                            |
| ---------------- | ------------------------------------------------------------------ |
| Role Drift       | Privileged access no longer matches current job role.              |
| Department Drift | Privileged access belongs to previous department responsibilities. |
| Leaver Drift     | Former user still has privileged access.                           |
| Review Drift     | Privileged access review is overdue.                               |
| Exception Drift  | Privileged exception access lacks expiration.                      |
| Ownership Drift  | Privileged access lacks accountable owner.                         |

---

## Privileged Risk Panel

The Privileged Risk panel shows elevated access that contributes to risk scoring.

| Risk Signal              | Meaning                                            |
| ------------------------ | -------------------------------------------------- |
| Privileged Access        | Elevated access increases risk score.              |
| Permanent Privilege      | Standing access increases risk further.            |
| Privileged Leaver Access | Former user with elevated access is critical risk. |
| Missing Justification    | Access cannot be explained.                        |
| Missing Approval         | Access was not governed before assignment.         |
| Missing Review           | Access has not been recently validated.            |
| Missing Audit Evidence   | Access cannot be proven or explained.              |

---

## Privileged Remediation Panel

Privileged access findings should produce remediation actions.

| Condition                               | Recommended Remediation                                  |
| --------------------------------------- | -------------------------------------------------------- |
| Permanent privilege                     | Convert to eligible or time-bound access where possible. |
| Privileged access no longer needed      | Remove privileged assignment.                            |
| Privileged access pending review        | Route to security or privileged access owner.            |
| Privileged leaver access                | Remove immediately and notify security.                  |
| Privileged exception without expiration | Add expiration or remove access.                         |
| Missing justification                   | Require justification or remove access.                  |
| Missing audit evidence                  | Generate evidence and review assignment.                 |

---

## Privileged Access Detail View

Users should be able to drill into privileged access details.

| Field           | Purpose                                         |
| --------------- | ----------------------------------------------- |
| Identity        | User or service account with privileged access. |
| Role            | Privileged role or permission.                  |
| Assignment Type | Permanent, eligible, time-bound, or exception.  |
| Approval Status | Approved, pending, denied, or expired.          |
| Justification   | Business reason for privileged access.          |
| Duration        | Time limit or expiration.                       |
| Risk Score      | Calculated identity risk.                       |
| Risk Factors    | Reasons risk exists.                            |
| Review Status   | Current privileged access review status.        |
| Evidence Link   | Related report or audit artifact.               |

---

## Filters

The Privileged Access Dashboard should support these filters:

| Filter          | Purpose                                                          |
| --------------- | ---------------------------------------------------------------- |
| Assignment Type | Filter by permanent, eligible, time-bound, or exception access.  |
| Risk Level      | Filter by Low, Medium, High, or Critical.                        |
| Approval Status | Filter by approved, pending, denied, or expired.                 |
| Review Status   | Filter by current, due, overdue, or escalated.                   |
| Role Type       | Filter by security, identity, application, user, or global role. |
| Worker Type     | Filter by employee, contractor, vendor, or service account.      |
| Drift Type      | Filter by role, leaver, review, exception, or ownership drift.   |

---

## Reports

The Privileged Access Dashboard should link to:

| Report              | Purpose                                                |
| ------------------- | ------------------------------------------------------ |
| Risk Score Report   | Shows privileged access risk factors.                  |
| Access Drift Report | Shows privileged drift or leaver-related access drift. |
| Governance Report   | Shows approval, review, and audit requirements.        |
| Dashboard Summary   | Shows privileged access metrics in dashboard format.   |

---

## Data Sources

The Privileged Access Dashboard uses these sample sources:

| Source                                   | Purpose                                        |
| ---------------------------------------- | ---------------------------------------------- |
| `examples/sample-policy-decisions.json`  | Provides privileged access decision details.   |
| `examples/sample-identity-events.json`   | Provides privileged access request event data. |
| `reports/sample-risk-score-report.md`    | Provides privileged risk scoring evidence.     |
| `reports/sample-access-drift-report.md`  | Provides privileged drift evidence.            |
| `reports/sample-governance-report.md`    | Provides governance and audit evidence.        |
| `examples/sample-dashboard-metrics.json` | Provides dashboard-ready metrics.              |

---

## Success Criteria

The Privileged Access Dashboard is successful when users can quickly see:

* Who has privileged access
* Which privileged access is pending approval
* Which privileged access is high or critical risk
* Which privileged access requires review
* Which privileged access appears as drift
* Which privileged access requires remediation
* Which evidence supports the access decision
* Which privileged access should be removed or time-limited

---

## Summary

The IdentityOS Privileged Access Dashboard turns elevated access into visible, governed, and actionable information.

It helps identity and security teams reduce standing privilege, govern elevated access, and respond to privileged access risk.

> Privileged access dashboards make elevated trust visible and accountable.
