# IdentityOS IAM Operations Dashboard

## Purpose

The IAM Operations Dashboard provides operational visibility for identity engineers, IAM analysts, platform owners, and identity operations teams.

This dashboard focuses on lifecycle activity, pending work, access changes, remediation tasks, automation health, and operational throughput.

The goal is to answer:

> What identity work needs action right now?

---

## Primary Audience

| Audience                  | Purpose                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| IAM Engineers             | Monitor identity lifecycle events, access changes, automation results, and remediation tasks. |
| IAM Analysts              | Review pending approvals, access changes, access drift findings, and governance queues.       |
| Identity Platform Owners  | Track workflow health, automation reliability, and operational bottlenecks.                   |
| Help Desk / Support Teams | Understand onboarding, offboarding, and access request status.                                |
| Security Operations       | Identify identity actions that require urgent response or escalation.                         |

---

## IAM Operations Questions

The IAM Operations Dashboard should answer:

* Which Joiner, Mover, and Leaver events occurred?
* Which access decisions are pending approval?
* Which access removals are required?
* Which drift findings require remediation?
* Which automation scripts ran successfully?
* Which workflows failed?
* Which users need manual intervention?
* Which reports were generated?
* What work is open today?

---

## IAM Operations Wireframe

```text id="atp4q4"
+--------------------------------------------------------------------------------+
| IdentityOS IAM Operations Dashboard                       Work Queue: Today     |
+--------------------------------------------------------------------------------+
| Lifecycle | Approvals | Remediation | Automation | Reports | Search            |
+--------------------------------------------------------------------------------+
| Joiners | Movers | Leavers | Pending Approvals | Drift Findings | Failures     |
|   1     |   1    |    1    |        2          |       4        |     0        |
+--------------------------------------------------------------------------------+
| Lifecycle Activity                     | Operational Queue                     |
|----------------------------------------|---------------------------------------|
| Joiner Events: 1                       | Pending Approvals: 2                  |
| Mover Events: 1                        | Review Required: 2                    |
| Leaver Events: 1                       | Remediation Tasks: 4                  |
| Contractor Events: 2                   | Manual Intervention: 0                |
| Privileged Requests: 1                 | Automation Failures: 0                |
+--------------------------------------------------------------------------------+
| Access Actions                         | Drift and Risk Work                   |
|----------------------------------------|---------------------------------------|
| Access Grants: Review policy decisions | Department Drift: 1                   |
| Access Removals: Review removals       | Leaver Drift: 1                       |
| Privileged Access: Review request      | Contractor Drift: 1                   |
| Non-Human Identity: Review ownership   | Non-Human Identity Drift: 1           |
+--------------------------------------------------------------------------------+
| Automation Status                      | Generated Reports                     |
|----------------------------------------|---------------------------------------|
| Policy Evaluator: Available            | Governance Report                     |
| Governance Report Generator: Available | Risk Score Report                     |
| Risk Scorer: Available                 | Access Drift Report                   |
| Access Drift Detector: Available       | Dashboard Summary                     |
| Dashboard Summary Generator: Available |                                       |
+--------------------------------------------------------------------------------+
```

---

## Top KPI Cards

| KPI Card            | Purpose                                      |
| ------------------- | -------------------------------------------- |
| Joiners             | Shows new identity onboarding events.        |
| Movers              | Shows role or department change events.      |
| Leavers             | Shows offboarding events.                    |
| Pending Approvals   | Shows work waiting for approval.             |
| Drift Findings      | Shows access mismatch requiring remediation. |
| Automation Failures | Shows workflow issues requiring attention.   |

---

## Lifecycle Activity Panel

The Lifecycle Activity panel shows identity events that require operational awareness.

| Metric                       | Purpose                                                   |
| ---------------------------- | --------------------------------------------------------- |
| Joiner Events                | Shows onboarding activity.                                |
| Mover Events                 | Shows role or department changes.                         |
| Leaver Events                | Shows offboarding activity.                               |
| Contractor Onboarding Events | Shows contractor creation activity.                       |
| Contractor Expiration Events | Shows contractor renewal or removal work.                 |
| Privileged Access Requests   | Shows elevated access activity.                           |
| Non-Human Identity Reviews   | Shows service account or automation identity review work. |

### Operational Interpretation

Lifecycle activity helps IAM teams understand daily workload and where automation should be applied.

---

## Operational Queue Panel

The Operational Queue panel shows work that may require action.

| Queue Item          | Meaning                                                                |
| ------------------- | ---------------------------------------------------------------------- |
| Pending Approvals   | Access decisions waiting for approval.                                 |
| Review Required     | Decisions that require manager, owner, security, or governance review. |
| Remediation Tasks   | Access removals or changes that need completion.                       |
| Manual Intervention | Work that automation could not complete.                               |
| Automation Failures | Scripts or workflows that failed.                                      |

### Operational Interpretation

The IAM team should prioritize:

1. Critical leaver or privileged access work
2. Access drift remediation
3. Pending approvals
4. Review-required items
5. Automation failures

---

## Access Actions Panel

The Access Actions panel summarizes what access needs to be granted, removed, retained, or reviewed.

| Access Action   | Purpose                                                    |
| --------------- | ---------------------------------------------------------- |
| Grant Access    | Assign role-based or approved access.                      |
| Remove Access   | Remove stale, excessive, expired, or previous-role access. |
| Retain Access   | Confirm access remains valid.                              |
| Review Access   | Route access to reviewer or owner.                         |
| Expire Access   | Remove temporary access at expiration.                     |
| Escalate Access | Route risky access to security or leadership.              |

### Operational Interpretation

Access actions should connect directly to policy decisions and governance evidence.

---

## Drift and Risk Work Panel

The Drift and Risk Work panel shows access issues requiring IAM attention.

| Finding                  | Purpose                                                                |
| ------------------------ | ---------------------------------------------------------------------- |
| Department Drift         | User retains access from previous department.                          |
| Leaver Drift             | Former user still has access requiring removal.                        |
| Contractor Drift         | Contractor access is expiring or expired.                              |
| Non-Human Identity Drift | Service account or automation identity requires owner or scope review. |
| High-Risk Identity       | Identity requires review or remediation.                               |
| Critical-Risk Identity   | Identity requires urgent action.                                       |

### Operational Interpretation

Access drift findings should become remediation tasks.

---

## Automation Status Panel

The Automation Status panel shows the prototype automation tools available in IdentityOS.

| Script                          | Purpose                                                     |
| ------------------------------- | ----------------------------------------------------------- |
| `policy-evaluator.py`           | Evaluates identity events against policy decisions.         |
| `generate-governance-report.py` | Generates governance reporting output.                      |
| `risk-scorer.py`                | Calculates identity risk scores and generates risk reports. |
| `access-drift-detector.py`      | Detects access drift and generates drift reports.           |
| `generate-dashboard-summary.py` | Generates dashboard summary reporting.                      |

### Operational Interpretation

The automation panel should help identity teams understand which workflows are available, which workflows ran, and whether any failures occurred.

---

## Reports Panel

The Reports panel links operational users to generated evidence.

| Report              | Purpose                                                             |
| ------------------- | ------------------------------------------------------------------- |
| Governance Report   | Shows policy decisions, governance requirements, and audit reasons. |
| Risk Score Report   | Shows identity risk scores, factors, and recommended actions.       |
| Access Drift Report | Shows drift findings, severity, and remediation recommendations.    |
| Dashboard Summary   | Shows dashboard-ready metrics across IdentityOS.                    |

---

## Work Queue Prioritization

IAM operations should prioritize work using this order:

| Priority | Work Type                  | Reason                                                          |
| -------- | -------------------------- | --------------------------------------------------------------- |
| 1        | Leaver access still active | Former users with access create urgent risk.                    |
| 2        | Privileged access risk     | Elevated access can create tenant-wide or system-wide exposure. |
| 3        | Critical access drift      | Drift can indicate privilege creep or incomplete remediation.   |
| 4        | Contractor expiration      | External access should not remain active without sponsorship.   |
| 5        | Pending approvals          | Access decisions may block productivity or governance.          |
| 6        | Review-required decisions  | Reviews help maintain least privilege.                          |
| 7        | Automation failures        | Failed workflows may require manual correction.                 |

---

## Filters

The IAM Operations Dashboard should support these filters:

| Filter            | Purpose                                                                           |
| ----------------- | --------------------------------------------------------------------------------- |
| Event Type        | Filter by Joiner, Mover, Leaver, Contractor, Privileged, or Non-Human Identity.   |
| Risk Level        | Filter by Low, Medium, High, or Critical.                                         |
| Drift Type        | Filter by department, leaver, contractor, privilege, or non-human identity drift. |
| Governance Status | Filter by approved, pending approval, review required, or remediation required.   |
| Worker Type       | Filter by employee, contractor, vendor, or service account.                       |
| Report Type       | Filter by governance, risk, drift, or dashboard summary report.                   |

---

## Drilldowns

Operational users should be able to drill down into:

| Drilldown          | Purpose                                                              |
| ------------------ | -------------------------------------------------------------------- |
| Identity Detail    | Show identity attributes, access, risk, drift, and governance state. |
| Event Detail       | Show lifecycle event details and related policy decision.            |
| Remediation Detail | Show what access needs removal or adjustment.                        |
| Approval Detail    | Show approver, status, and decision reason.                          |
| Drift Detail       | Show expected access, actual access, and excess access.              |
| Report Detail      | Open related Markdown report evidence.                               |

---

## Data Sources

The IAM Operations Dashboard uses:

| Source                                   | Purpose                                                |
| ---------------------------------------- | ------------------------------------------------------ |
| `examples/sample-identity-events.json`   | Provides lifecycle events.                             |
| `examples/sample-policy-decisions.json`  | Provides access decisions and governance requirements. |
| `examples/sample-dashboard-metrics.json` | Provides dashboard-ready metrics.                      |
| `reports/sample-governance-report.md`    | Provides governance evidence.                          |
| `reports/sample-risk-score-report.md`    | Provides risk scoring evidence.                        |
| `reports/sample-access-drift-report.md`  | Provides drift detection evidence.                     |
| `reports/sample-dashboard-summary.md`    | Provides dashboard summary output.                     |

---

## Success Criteria

The IAM Operations Dashboard is successful when IAM teams can quickly see:

* What work is open
* What access needs action
* Which lifecycle events occurred
* Which approvals are pending
* Which drift findings need remediation
* Which automation scripts are available
* Which reports were generated
* Which items require manual intervention

---

## Summary

The IdentityOS IAM Operations Dashboard turns identity activity into an operational command center.

It helps IAM teams prioritize work, reduce manual effort, track automation, remediate drift, and maintain governance visibility.

> IAM operations dashboards turn identity work into organized action.
