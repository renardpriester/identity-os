# IdentityOS Dashboard Data Model

## Purpose

This document defines the data model for the IdentityOS dashboard.

The dashboard data model explains how IdentityOS metrics, reports, identity events, policy decisions, risk scores, access drift findings, and governance outputs can be organized into dashboard views, panels, cards, tables, filters, and drilldowns.

The goal is to make the dashboard structured, explainable, and ready for a future prototype.

---

## Core Dashboard Model

The IdentityOS dashboard is organized around this structure:

```text id="e1eb96"
Dashboard
  ↓
Dashboard View
  ↓
Panel
  ↓
Metric Card / Table / Report Link
  ↓
Source Data
  ↓
Action or Drilldown
```

Each dashboard element should connect back to a source file, metric, workflow, or report.

---

## Core Objects

| Object         | Purpose                                                                     |
| -------------- | --------------------------------------------------------------------------- |
| Dashboard      | The full IdentityOS interface.                                              |
| Dashboard View | A major dashboard page such as Executive Overview or Access Drift.          |
| Panel          | A section inside a dashboard view.                                          |
| Metric Card    | A single high-level metric such as Critical Risk or Pending Approvals.      |
| Metric Group   | A collection of related metrics.                                            |
| Table          | A detailed list of identities, events, decisions, risks, or drift findings. |
| Report Link    | A link to generated Markdown evidence.                                      |
| Filter         | A control that narrows dashboard results.                                   |
| Drilldown      | A detailed view opened from a card, table row, or metric.                   |

---

## Dashboard Views

IdentityOS currently supports these dashboard views.

| View                    | Description                                                             |
| ----------------------- | ----------------------------------------------------------------------- |
| Executive Overview      | High-level identity risk and governance posture.                        |
| IAM Operations          | Lifecycle activity, workflow status, and operational workload.          |
| Governance Health       | Reviews, approvals, exceptions, remediation, and audit evidence.        |
| Risk Scoring            | Risk scores, risk levels, risk factors, and recommended actions.        |
| Access Drift            | Stale access, privilege creep, excess access, and remediation.          |
| Privileged Access       | Elevated access, role eligibility, activation, and review status.       |
| Contractors and Vendors | External identity lifecycle, sponsorship, expiration, and reviews.      |
| Non-Human Identities    | Service accounts, owners, purpose, credential status, and access scope. |
| Automation Health       | Script status, generated reports, failures, and manual intervention.    |
| Reports                 | Generated reports and audit-ready evidence.                             |

---

## Data Sources

The dashboard can use multiple IdentityOS data sources.

| Data Source                              | Purpose                                       |
| ---------------------------------------- | --------------------------------------------- |
| `examples/sample-dashboard-metrics.json` | Provides dashboard-ready summary metrics.     |
| `examples/sample-identity-events.json`   | Provides lifecycle and governance event data. |
| `examples/sample-policy-decisions.json`  | Provides policy decisions and access actions. |
| `reports/sample-governance-report.md`    | Provides governance reporting output.         |
| `reports/sample-risk-score-report.md`    | Provides risk scoring output.                 |
| `reports/sample-access-drift-report.md`  | Provides access drift output.                 |
| `reports/sample-dashboard-summary.md`    | Provides generated dashboard summary output.  |

---

## Metric Card Model

A metric card should include:

| Field              | Purpose                                                               |
| ------------------ | --------------------------------------------------------------------- |
| Card Name          | Display name of the metric.                                           |
| Metric Key         | Data key used to retrieve the metric.                                 |
| Value              | Numeric or text value displayed.                                      |
| Category           | Executive, governance, risk, drift, lifecycle, automation, or report. |
| Risk Indicator     | Low, Medium, High, Critical, or Neutral.                              |
| Source             | File or data source where the value comes from.                       |
| Description        | Business explanation of what the metric means.                        |
| Recommended Action | Suggested action when the metric requires attention.                  |

---

## Example Metric Card

| Field              | Example                                                    |
| ------------------ | ---------------------------------------------------------- |
| Card Name          | Critical Risk Decisions                                    |
| Metric Key         | `critical_risk_decisions`                                  |
| Value              | `2`                                                        |
| Category           | Risk                                                       |
| Risk Indicator     | Critical                                                   |
| Source             | `examples/sample-dashboard-metrics.json`                   |
| Description        | Shows the number of identity decisions with critical risk. |
| Recommended Action | Review critical decisions and confirm remediation.         |

---

## Executive Overview Cards

| Card                    | Source Metric             | Purpose                                   |
| ----------------------- | ------------------------- | ----------------------------------------- |
| Total Identities        | `total_sample_identities` | Shows identity population size.           |
| Total Policy Decisions  | `total_policy_decisions`  | Shows evaluated identity decisions.       |
| Pending Approvals       | `pending_approvals`       | Shows decisions waiting for approval.     |
| Review Required         | `review_required`         | Shows decisions requiring review.         |
| High Risk Decisions     | `high_risk_decisions`     | Shows elevated identity risk.             |
| Critical Risk Decisions | `critical_risk_decisions` | Shows urgent identity risk.               |
| Access Drift Detected   | `access_drift_detected`   | Shows access mismatch or privilege creep. |

---

## Lifecycle Operations Cards

| Card                         | Source Metric                  | Purpose                                                       |
| ---------------------------- | ------------------------------ | ------------------------------------------------------------- |
| Joiner Events                | `joiner_events`                | Shows onboarding activity.                                    |
| Mover Events                 | `mover_events`                 | Shows role or department changes.                             |
| Leaver Events                | `leaver_events`                | Shows offboarding activity.                                   |
| Contractor Onboarding Events | `contractor_onboarding_events` | Shows contractor creation activity.                           |
| Contractor Expiration Events | `contractor_expiration_events` | Shows contractor renewal or removal activity.                 |
| Privileged Access Requests   | `privileged_access_requests`   | Shows elevated access requests.                               |
| Non-Human Identity Reviews   | `non_human_identity_reviews`   | Shows service account or automation identity review activity. |

---

## Governance Cards

| Card                     | Source Metric              | Purpose                                          |
| ------------------------ | -------------------------- | ------------------------------------------------ |
| Approvals Required       | `approvals_required`       | Shows total access decisions requiring approval. |
| Pending Approvals        | `pending_approvals`        | Shows approvals not yet completed.               |
| Review Required          | `review_required`          | Shows decisions requiring review.                |
| Monthly Reviews          | `monthly_reviews`          | Shows monthly governance cadence.                |
| Quarterly Reviews        | `quarterly_reviews`        | Shows quarterly governance cadence.              |
| Exceptions Tracked       | `exceptions_tracked`       | Shows documented exceptions.                     |
| Audit Required Decisions | `audit_required_decisions` | Shows decisions requiring audit evidence.        |

---

## Risk Scoring Cards

| Card                     | Source Metric              | Purpose                                   |
| ------------------------ | -------------------------- | ----------------------------------------- |
| Low Risk Identities      | `low_risk_identities`      | Shows identities with low risk.           |
| Medium Risk Identities   | `medium_risk_identities`   | Shows identities with moderate risk.      |
| High Risk Identities     | `high_risk_identities`     | Shows identities requiring review.        |
| Critical Risk Identities | `critical_risk_identities` | Shows identities requiring urgent action. |
| Risk Reports Generated   | `risk_reports_generated`   | Shows risk report generation status.      |

---

## Access Drift Cards

| Card                     | Source Metric              | Purpose                                                  |
| ------------------------ | -------------------------- | -------------------------------------------------------- |
| Total Drift Findings     | `total_drift_findings`     | Shows total access drift findings.                       |
| Department Drift         | `department_drift`         | Shows access from previous departments.                  |
| Leaver Drift             | `leaver_drift`             | Shows access remaining after departure.                  |
| Contractor Drift         | `contractor_drift`         | Shows contractor access requiring expiration or renewal. |
| Non-Human Identity Drift | `non_human_identity_drift` | Shows service account or automation identity drift.      |
| Critical Drift Findings  | `critical_drift_findings`  | Shows urgent drift remediation items.                    |
| High Drift Findings      | `high_drift_findings`      | Shows serious drift findings requiring review.           |

---

## Automation Health Cards

| Card                         | Source Metric                  | Purpose                                       |
| ---------------------------- | ------------------------------ | --------------------------------------------- |
| Automation Scripts Available | `automation_scripts_available` | Shows available prototype automation scripts. |
| Reports Generated            | `reports_generated`            | Shows generated reporting output.             |
| Automation Failures          | `automation_failures`          | Shows failed automation runs.                 |
| Manual Intervention Required | `manual_intervention_required` | Shows where human action is needed.           |

---

## Dashboard Table Model

Dashboard tables should provide drilldown detail.

A table row may include:

| Field              | Purpose                                                                       |
| ------------------ | ----------------------------------------------------------------------------- |
| Identity           | User, service account, contractor, or vendor identity.                        |
| Event ID           | Related lifecycle or governance event.                                        |
| Decision ID        | Related policy decision.                                                      |
| Event Type         | Joiner, Mover, Leaver, contractor, privileged, or non-human identity.         |
| Risk Level         | Low, Medium, High, or Critical.                                               |
| Drift Type         | Department, role, leaver, contractor, privilege, or non-human identity drift. |
| Status             | Approved, pending approval, review required, remediated, or open.             |
| Recommended Action | Suggested remediation or governance action.                                   |
| Evidence Link      | Related report or audit artifact.                                             |

---

## Filter Model

The dashboard should support filters.

| Filter            | Example Values                                                             |
| ----------------- | -------------------------------------------------------------------------- |
| Risk Level        | Low, Medium, High, Critical                                                |
| Event Type        | Joiner, Mover, Leaver, Contractor, Privileged, Non-Human Identity          |
| Worker Type       | Employee, Contractor, Vendor, Service Account                              |
| Department        | Legal, Finance, Security, IT, HR                                           |
| Governance Status | Approved, Pending Approval, Review Required                                |
| Drift Type        | Department Drift, Leaver Drift, Contractor Drift, Non-Human Identity Drift |
| Report Type       | Governance, Risk, Drift, Dashboard Summary                                 |

---

## Drilldown Model

Dashboard cards and tables should support drilldowns.

| Drilldown         | Purpose                                                              |
| ----------------- | -------------------------------------------------------------------- |
| Identity Detail   | Shows identity attributes, access, risk score, and governance state. |
| Event Detail      | Shows lifecycle event details and policy decision.                   |
| Risk Detail       | Shows risk factors and score explanation.                            |
| Drift Detail      | Shows expected access, actual access, and excess access.             |
| Governance Detail | Shows approvals, reviews, exceptions, and remediation status.        |
| Report Detail     | Opens related Markdown report or evidence.                           |

---

## Data Relationship Model

```text id="y7s97f"
Identity Event
      ↓
Policy Decision
      ↓
Risk Score
      ↓
Access Drift Finding
      ↓
Governance Action
      ↓
Report Output
      ↓
Dashboard Metric
      ↓
Dashboard Card
      ↓
User Action
```

This relationship ensures that dashboard metrics are not isolated numbers. They connect back to identity events, policy decisions, governance actions, and audit evidence.

---

## Success Criteria

The dashboard data model is successful when:

* Every dashboard card has a clear source.
* Every metric has a business meaning.
* Every risk metric can be explained.
* Every drift finding can be traced to excess access.
* Every governance metric connects to review, approval, or remediation.
* Every report can be linked to dashboard evidence.
* Dashboard data supports future prototype development.

---

## Summary

The IdentityOS dashboard data model defines how identity data becomes dashboard visibility.

It connects sample metrics, reports, identity events, policy decisions, risk scoring, access drift detection, and automation health into a structured dashboard design.

> Good dashboard design starts with a clear data model.
