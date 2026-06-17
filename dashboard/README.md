# IdentityOS Dashboard

## Purpose

This folder contains dashboard design concepts, wireframes, interface ideas, and future dashboard prototype assets for IdentityOS.

The IdentityOS dashboard is designed to provide visibility into identity lifecycle activity, access risk, governance status, access drift, privileged access, contractor and vendor access, non-human identity risk, automation health, and audit evidence.

The dashboard layer helps turn IdentityOS from a backend identity architecture into an understandable identity command center.

---

## Dashboard Mission

The mission of the IdentityOS dashboard is to make identity risk visible, explainable, and actionable.

The dashboard should help users answer:

* What identity risks need attention?
* Which access decisions are pending?
* Where is access drift happening?
* Which privileged identities need review?
* Which contractors or vendors are near expiration?
* Which leavers still have access?
* Which non-human identities are unmanaged?
* Which automation workflows succeeded or failed?
* What evidence exists for audit and governance?

---

## Primary Dashboard Views

| Dashboard View          | Purpose                                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------------- |
| Executive Overview      | Shows high-level identity risk, governance health, and critical findings.                    |
| IAM Operations          | Shows lifecycle activity, pending approvals, remediation tasks, and automation status.       |
| Governance Health       | Shows access reviews, approvals, exceptions, remediation, and audit evidence.                |
| Risk Scoring            | Shows identity risk scores, risk levels, risk factors, and recommended actions.              |
| Access Drift            | Shows stale access, privilege creep, role drift, department drift, and leaver drift.         |
| Privileged Access       | Shows elevated access, privileged reviews, activation activity, and standing privilege risk. |
| Contractors and Vendors | Shows external identities, expirations, sponsorship, and review status.                      |
| Non-Human Identities    | Shows service accounts, automation accounts, owners, credential status, and access scope.    |
| Automation Health       | Shows scripts, generated reports, workflow success, failures, and manual intervention.       |
| Audit Evidence          | Shows report outputs, decision records, review evidence, and remediation evidence.           |

---

## Dashboard Design Principles

The IdentityOS dashboard should follow these design principles:

* Prioritize critical identity risk.
* Make access decisions explainable.
* Separate executive views from operational views.
* Show trends and status clearly.
* Make governance work actionable.
* Connect every metric to a workflow or decision.
* Avoid overwhelming the user.
* Support audit and evidence needs.
* Show where automation is working.
* Show where human action is required.

---

## Key Metrics

The dashboard should display metrics such as:

* Total identities
* Total policy decisions
* Pending approvals
* Review-required decisions
* High-risk identities
* Critical-risk identities
* Access drift findings
* Privileged identities
* Contractor expirations
* Vendor access reviews
* Non-human identities without owners
* Overdue access reviews
* Remediation tasks open
* Automation scripts available
* Reports generated
* Automation failures

---

## Current Dashboard Data Sources

The current dashboard concept is supported by:

| Source                                     | Purpose                                        |
| ------------------------------------------ | ---------------------------------------------- |
| `examples/sample-dashboard-metrics.json`   | Provides dashboard-ready sample metrics.       |
| `reports/sample-dashboard-summary.md`      | Provides a generated dashboard summary report. |
| `reports/sample-governance-report.md`      | Provides governance reporting data.            |
| `reports/sample-risk-score-report.md`      | Provides risk scoring data.                    |
| `reports/sample-access-drift-report.md`    | Provides access drift reporting data.          |
| `automation/generate-dashboard-summary.py` | Generates the dashboard summary report.        |

---

## Planned Dashboard Assets

This folder will eventually include:

| File                          | Purpose                                                           |
| ----------------------------- | ----------------------------------------------------------------- |
| `dashboard-wireframe.md`      | Text-based dashboard layout and interface structure.              |
| `dashboard-data-model.md`     | Defines dashboard cards, panels, metrics, and data relationships. |
| `executive-dashboard.md`      | Defines the executive-level dashboard view.                       |
| `iam-operations-dashboard.md` | Defines the IAM operations dashboard view.                        |
| `governance-dashboard.md`     | Defines the governance dashboard view.                            |
| `risk-dashboard.md`           | Defines the risk scoring and access drift dashboard view.         |
| `streamlit-prototype/`        | Future Python dashboard prototype folder.                         |
| [Dashboard Wireframe](dashboard-wireframe.md) | Defines the first text-based dashboard layout, including KPI cards, dashboard panels, navigation tabs, filters, interactions, and data mapping. |
| [Dashboard Data Model](dashboard-data-model.md) | Defines dashboard views, panels, metric cards, tables, filters, drilldowns, data sources, and metric relationships. |

---

## Future Prototype Direction

The first prototype dashboard could be built with Python and Streamlit.

A future Streamlit prototype could:

* Load sample dashboard metrics.
* Display identity risk cards.
* Show lifecycle event metrics.
* Show governance status.
* Show risk scoring summaries.
* Show access drift findings.
* Show report links.
* Display dashboard tables.
* Provide a simple identity risk command center interface.

---

## Guiding Statement

> IdentityOS dashboard design turns identity data into actionable trust visibility.
