# IdentityOS Risk Dashboard

## Purpose

The Risk Dashboard provides visibility into identity risk scores, risk levels, risk factors, access risk, privileged access exposure, access drift, and recommended governance actions.

This dashboard is designed for IAM teams, security teams, governance teams, risk leaders, and security leadership.

The goal is to answer:

> Which identities, access decisions, or governance conditions create the most risk?

---

## Primary Audience

| Audience             | Purpose                                                   |
| -------------------- | --------------------------------------------------------- |
| Security Teams       | Identify high-risk and critical-risk identity conditions. |
| IAM Teams            | Prioritize risky access decisions and remediation work.   |
| IAM Governance Teams | Use risk levels to prioritize reviews and approvals.      |
| Risk Leaders         | Understand identity risk trends and exposure.             |
| Security Leadership  | Track critical identity risks requiring escalation.       |

---

## Risk Questions

The Risk Dashboard should answer:

* Which identities are high risk?
* Which identities are critical risk?
* What risk factors caused the score?
* Which access decisions require urgent review?
* Which identities have privileged access risk?
* Which users have access drift risk?
* Which contractors, vendors, or service accounts increase risk?
* Which risks require remediation?
* Which risks require leadership escalation?

---

## Risk Dashboard Wireframe

```text id="0brn4o"
+--------------------------------------------------------------------------------+
| IdentityOS Risk Dashboard                              Risk View: Current       |
+--------------------------------------------------------------------------------+
| Risk Overview | Risk Factors | Critical Queue | Drift Risk | Reports            |
+--------------------------------------------------------------------------------+
| Low Risk | Medium Risk | High Risk | Critical Risk | Drift Findings | Reports   |
|    1     |      2      |     3     |       1       |       4        |    3      |
+--------------------------------------------------------------------------------+
| Risk Level Distribution              | Critical Risk Queue                      |
|--------------------------------------|------------------------------------------|
| Low: 1                               | Privileged Leaver Risk                   |
| Medium: 2                            | Leaver Access Still Active               |
| High: 3                              | Contractor Access Expiration             |
| Critical: 1                          | Non-Human Identity Ownership Gap         |
+--------------------------------------------------------------------------------+
| Risk Factors                         | Recommended Actions                      |
|--------------------------------------|------------------------------------------|
| Privileged Access                    | Review Critical Risk Identities          |
| Sensitive Application Access         | Remove Excess Access                     |
| Access Drift                         | Validate Contractor Sponsorship          |
| Contractor / Vendor Status           | Review Privileged Access                 |
| Missing Owner                        | Create Audit Evidence                    |
+--------------------------------------------------------------------------------+
| Access Drift Risk                    | Reports                                  |
|--------------------------------------|------------------------------------------|
| Department Drift: 1                  | Risk Score Report                        |
| Leaver Drift: 1                      | Access Drift Report                      |
| Contractor Drift: 1                  | Governance Report                        |
| Non-Human Identity Drift: 1          | Dashboard Summary                        |
+--------------------------------------------------------------------------------+
```

---

## Top KPI Cards

| KPI Card       | Purpose                                                     |
| -------------- | ----------------------------------------------------------- |
| Low Risk       | Shows identities or decisions with minimal risk.            |
| Medium Risk    | Shows moderate-risk conditions requiring normal governance. |
| High Risk      | Shows access or identities requiring review.                |
| Critical Risk  | Shows urgent risk requiring escalation or remediation.      |
| Drift Findings | Shows access mismatch contributing to risk.                 |
| Reports        | Shows available evidence and reporting outputs.             |

---

## Risk Level Distribution Panel

The Risk Level Distribution panel summarizes identity risk severity.

| Risk Level | Meaning                                                                   |
| ---------- | ------------------------------------------------------------------------- |
| Low        | Standard access with minimal risk indicators.                             |
| Medium     | Normal business access with some governance or sensitivity concerns.      |
| High       | Sensitive access, stale access, drift, or missing governance signals.     |
| Critical   | Privileged, expired, leaver, or unmanaged access requiring urgent action. |

### Risk Interpretation

Risk should be prioritized based on severity.

Critical risk should be reviewed first, followed by high-risk identities and decisions.

---

## Critical Risk Queue

The Critical Risk Queue shows the most urgent identity risks.

Examples include:

| Critical Risk Item               | Reason                                                      |
| -------------------------------- | ----------------------------------------------------------- |
| Privileged Leaver Risk           | Former users with privileged access create urgent exposure. |
| Leaver Access Still Active       | Departed workers should not retain access.                  |
| Contractor Access Expiration     | External access should expire unless renewed.               |
| Non-Human Identity Ownership Gap | Service accounts without owners cannot be governed.         |
| Privileged Access Without Review | Elevated access must be reviewed frequently.                |

### Risk Interpretation

Critical risk findings should trigger:

* Security review
* IAM remediation
* Privileged access review
* Manager or owner validation
* Audit evidence generation
* Leadership awareness when needed

---

## Risk Factor Panel

The Risk Factor panel explains why risk exists.

| Risk Factor                  | Why It Matters                                                       |
| ---------------------------- | -------------------------------------------------------------------- |
| Privileged Access            | Elevated access can impact systems, users, data, or tenant security. |
| Sensitive Application Access | Access to sensitive systems increases business impact.               |
| Access Drift                 | Access no longer aligns with expected role or business need.         |
| Contractor or Vendor Status  | External identities require sponsorship and expiration controls.     |
| Missing Owner                | Access or identity cannot be governed without accountability.        |
| Expired Access               | Temporary access that remains active becomes unmanaged risk.         |
| Missing Audit Evidence       | Decisions cannot be explained or proven.                             |
| Non-Human Identity           | Service accounts can be long-lived, sensitive, and under-governed.   |

---

## Recommended Actions Panel

The Risk Dashboard should show recommended actions based on risk level.

| Risk Level | Recommended Action                                                           |
| ---------- | ---------------------------------------------------------------------------- |
| Low        | Retain access and follow normal review schedule.                             |
| Medium     | Retain access with standard governance controls.                             |
| High       | Trigger review, validate owner, confirm business need, and check for drift.  |
| Critical   | Escalate, remediate, notify security if needed, and generate audit evidence. |

---

## Access Drift Risk Panel

Access drift should be shown as a risk signal.

| Drift Type               | Risk Meaning                                                                 |
| ------------------------ | ---------------------------------------------------------------------------- |
| Department Drift         | User retained access from a previous department.                             |
| Leaver Drift             | Former worker retained access after departure.                               |
| Contractor Drift         | Contractor access remains active near or after expiration.                   |
| Non-Human Identity Drift | Service account lacks ownership, scope validation, or credential governance. |
| Privilege Drift          | Elevated access is no longer justified.                                      |

### Risk Interpretation

Drift findings should increase risk because they show actual access no longer matches expected access.

---

## Privileged Access Risk Panel

Privileged access should be elevated in the risk view.

| Metric                     | Purpose                                      |
| -------------------------- | -------------------------------------------- |
| Privileged Identities      | Shows identities with elevated access.       |
| Privileged Requests        | Shows privileged access activity.            |
| Privileged Review Required | Shows elevated access requiring validation.  |
| Privileged Drift           | Shows elevated access no longer justified.   |
| Privileged Leaver Risk     | Shows departed users with privileged access. |

### Risk Interpretation

Privileged access should always be:

* Approved
* Justified
* Time-bound where possible
* Reviewed frequently
* Logged
* Removed when no longer required

---

## Risk Detail Drilldown

Users should be able to drill into a risk finding.

A risk detail view should include:

| Field              | Purpose                                             |
| ------------------ | --------------------------------------------------- |
| Identity           | User, contractor, vendor, or service account.       |
| Event ID           | Related lifecycle or governance event.              |
| Decision ID        | Related policy decision.                            |
| Risk Score         | Numeric score.                                      |
| Risk Level         | Low, Medium, High, or Critical.                     |
| Risk Factors       | Reasons risk was assigned.                          |
| Access Involved    | Access granted, removed, retained, or reviewed.     |
| Drift Type         | Drift condition if applicable.                      |
| Governance Status  | Approval, review, exception, or remediation status. |
| Recommended Action | Suggested next step.                                |
| Evidence Link      | Related report or audit artifact.                   |

---

## Risk Work Queue

The Risk Dashboard should include a prioritized work queue.

| Priority | Work Type                   | Reason                                              |
| -------- | --------------------------- | --------------------------------------------------- |
| 1        | Critical privileged risk    | Elevated access can create major exposure.          |
| 2        | Leaver access risk          | Former users should not retain access.              |
| 3        | Contractor expiration risk  | External access should expire or be renewed.        |
| 4        | Access drift risk           | Drift indicates privilege creep or stale access.    |
| 5        | Non-human identity risk     | Service accounts require owner, purpose, and scope. |
| 6        | Pending high-risk approvals | Sensitive access requires owner decision.           |
| 7        | Missing audit evidence      | Decisions must be explainable and provable.         |

---

## Filters

The Risk Dashboard should support these filters:

| Filter            | Purpose                                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| Risk Level        | Filter by Low, Medium, High, or Critical.                                                                  |
| Risk Factor       | Filter by privileged access, contractor status, access drift, missing owner, expired access, or audit gap. |
| Event Type        | Filter by Joiner, Mover, Leaver, Contractor, Privileged, or Non-Human Identity.                            |
| Worker Type       | Filter by employee, contractor, vendor, or service account.                                                |
| Drift Type        | Filter by department, leaver, contractor, privilege, or non-human identity drift.                          |
| Governance Status | Filter by pending approval, review required, approved, or remediation required.                            |

---

## Reports

The Risk Dashboard should link to:

| Report              | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| Risk Score Report   | Shows risk scores, levels, factors, and recommended actions. |
| Access Drift Report | Shows drift findings contributing to risk.                   |
| Governance Report   | Shows governance requirements and audit reasons.             |
| Dashboard Summary   | Shows executive-level dashboard metrics.                     |

---

## Data Sources

The Risk Dashboard uses these sample sources:

| Source                                   | Purpose                                        |
| ---------------------------------------- | ---------------------------------------------- |
| `examples/sample-dashboard-metrics.json` | Provides dashboard-ready risk metrics.         |
| `reports/sample-risk-score-report.md`    | Provides detailed risk score evidence.         |
| `reports/sample-access-drift-report.md`  | Provides access drift findings.                |
| `reports/sample-governance-report.md`    | Provides governance context.                   |
| `examples/sample-policy-decisions.json`  | Provides policy decisions and access actions.  |
| `examples/sample-identity-events.json`   | Provides lifecycle and identity event context. |

---

## Success Criteria

The Risk Dashboard is successful when users can quickly see:

* Which identities are highest risk
* What caused the risk
* Which risks require remediation
* Which risks require escalation
* Which risks are connected to access drift
* Which risks are connected to privileged access
* Which risks have audit evidence
* Which reports support the finding

---

## Summary

The IdentityOS Risk Dashboard turns identity risk into visible, prioritized action.

It helps teams focus on the identities, access decisions, and governance conditions that matter most.

> Risk dashboards turn identity signals into security priorities.
