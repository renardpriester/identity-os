# IdentityOS Automation Health Dashboard

## Purpose

The Automation Health Dashboard provides visibility into IdentityOS automation scripts, job status, report generation, automation failures, manual intervention, evidence outputs, and operational health.

This dashboard is designed to help IAM operations teams understand whether identity automation is reliable, observable, and producing the evidence required for governance and audit.

The goal is to answer:

> Are identity automation workflows running successfully, producing evidence, and reducing manual effort?

---

## Primary Audience

| Audience             | Purpose                                                                          |
| -------------------- | -------------------------------------------------------------------------------- |
| IAM Operations Teams | Monitor automation workflows, reports, failures, and remediation queues.         |
| IAM Engineers        | Validate script execution, outputs, and operational reliability.                 |
| Security Teams       | Confirm that identity automation supports risk and remediation workflows.        |
| Governance Teams     | Verify that automation produces reports and audit evidence.                      |
| Leadership           | Understand automation maturity, manual effort reduction, and operational health. |
| Auditors             | Confirm that automated identity processes produce traceable evidence.            |

---

## Automation Health Questions

The Automation Health Dashboard should answer:

* Which automation scripts are available?
* Which scripts ran successfully?
* Which scripts failed?
* Which reports were generated?
* Which reports are stale or missing?
* Which automation tasks require manual intervention?
* Which input files were processed?
* Which outputs were created?
* Which failures need escalation?
* Is automation reducing IAM operational workload?

---

## Automation Health Dashboard Wireframe

```text id="x6vp5g"
+--------------------------------------------------------------------------------+
| IdentityOS Automation Health Dashboard                  Automation View: Current|
+--------------------------------------------------------------------------------+
| Overview | Jobs | Reports | Failures | Manual Work | Evidence                  |
+--------------------------------------------------------------------------------+
| Scripts Available | Reports Generated | Failures | Manual Intervention | Health |
|        4          |        3          |    0     |          0          | Healthy|
+--------------------------------------------------------------------------------+
| Automation Inventory                  | Job Run Status                         |
|---------------------------------------|----------------------------------------|
| Policy Evaluator: Available           | Last Run: Future Metric                |
| Governance Report Generator: Available| Successful Runs: Future Metric         |
| Risk Scorer: Available                | Failed Runs: 0                         |
| Access Drift Detector: Available      | Manual Intervention: 0                 |
+--------------------------------------------------------------------------------+
| Report Generation                     | Failure and Exception Queue            |
|---------------------------------------|----------------------------------------|
| Governance Report: Generated          | Failed Jobs: 0                         |
| Risk Score Report: Generated          | Missing Inputs: 0                      |
| Access Drift Report: Generated        | Missing Outputs: 0                     |
| Dashboard Summary: Generated          | Escalations Required: 0                |
+--------------------------------------------------------------------------------+
| Automation Evidence                   | Operational Health                     |
|---------------------------------------|----------------------------------------|
| Input Files Tracked                   | Automation Failures: 0                 |
| Output Reports Available              | Manual Intervention Required: 0        |
| Script Inventory Documented           | Report Generation Healthy              |
| Evidence Artifacts Available          | Overall Status: Healthy                |
+--------------------------------------------------------------------------------+
```

---

## Top KPI Cards

| KPI Card            | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| Scripts Available   | Shows how many automation scripts exist in the project.      |
| Reports Generated   | Shows how many reports were produced by automation.          |
| Automation Failures | Shows failed automation activity.                            |
| Manual Intervention | Shows work that still requires human action.                 |
| Missing Outputs     | Shows expected reports or artifacts that were not generated. |
| Overall Health      | Shows whether automation is healthy, degraded, or failing.   |

---

## Automation Inventory Panel

The Automation Inventory panel shows available IdentityOS automation components.

| Automation Script               | Purpose                                                  |
| ------------------------------- | -------------------------------------------------------- |
| `policy-evaluator.py`           | Evaluates identity events and produces policy decisions. |
| `generate-governance-report.py` | Generates governance reporting from policy decisions.    |
| `risk-scorer.py`                | Calculates identity risk scores and recommended actions. |
| `access-drift-detector.py`      | Detects access drift and excess access.                  |
| `generate-dashboard-summary.py` | Generates dashboard-ready summary metrics.               |

### Automation Interpretation

A mature identity platform should not rely only on manual review.

Automation should help:

* Evaluate identity events
* Apply policy logic
* Generate governance decisions
* Score identity risk
* Detect access drift
* Produce reports
* Create audit evidence
* Reduce manual effort

---

## Job Run Status Panel

The Job Run Status panel shows whether automation jobs are running successfully.

| Metric                       | Purpose                                                   |
| ---------------------------- | --------------------------------------------------------- |
| Last Run Time                | Shows when automation last executed.                      |
| Successful Runs              | Shows completed automation executions.                    |
| Failed Runs                  | Shows automation failures.                                |
| Skipped Runs                 | Shows jobs that did not run.                              |
| Manual Intervention Required | Shows items needing human action.                         |
| Escalations Required         | Shows failures requiring support or leadership awareness. |

### Job Health States

| Status   | Meaning                                                 |
| -------- | ------------------------------------------------------- |
| Healthy  | Jobs are running and producing expected outputs.        |
| Warning  | Jobs completed but require review or have missing data. |
| Degraded | Jobs partially failed or outputs are incomplete.        |
| Failed   | Jobs failed and require remediation.                    |
| Unknown  | Job state cannot be confirmed.                          |

---

## Report Generation Panel

The Report Generation panel shows whether expected reports were created.

| Report              | Purpose                                                             |
| ------------------- | ------------------------------------------------------------------- |
| Governance Report   | Shows governance requirements, approvals, reviews, and audit needs. |
| Risk Score Report   | Shows identity risk levels, risk factors, and recommended actions.  |
| Access Drift Report | Shows stale access, excess access, and remediation needs.           |
| Dashboard Summary   | Shows executive and operational dashboard metrics.                  |

### Report Health Interpretation

Report generation is healthy when:

* Expected reports exist
* Reports are generated from current input data
* Reports align with dashboard metrics
* Outputs are easy to find
* Evidence can support audit and governance review

---

## Failure and Exception Queue

The Failure and Exception Queue shows automation problems that require attention.

| Failure Type           | Meaning                                             |
| ---------------------- | --------------------------------------------------- |
| Script Failure         | Automation script did not complete.                 |
| Missing Input File     | Required sample data or source file was missing.    |
| Invalid Data Format    | Input data could not be processed correctly.        |
| Missing Output Report  | Expected report was not created.                    |
| Stale Report           | Report exists but may be outdated.                  |
| Manual Review Required | Automation completed but requires human validation. |

---

## Manual Intervention Panel

Not every identity decision should be fully automated.

The dashboard should show when human action is still required.

| Manual Action            | Reason                                                       |
| ------------------------ | ------------------------------------------------------------ |
| Manager Approval         | Business owner must approve access.                          |
| Sponsor Renewal          | Contractor or vendor sponsor must renew or deny access.      |
| Security Review          | High-risk or privileged access requires security validation. |
| Exception Approval       | Access outside standard policy requires approval.            |
| Remediation Confirmation | Access removal or modification must be verified.             |
| Audit Review             | Evidence must be reviewed for compliance.                    |

### Manual Intervention Interpretation

Manual intervention is not always bad.

A strong identity platform automates repeatable work while routing sensitive decisions to the right human approver.

---

## Automation Evidence Panel

The Automation Evidence panel shows whether automation produced traceable artifacts.

| Evidence Type        | Purpose                                              |
| -------------------- | ---------------------------------------------------- |
| Input Evidence       | Shows source files or events used by automation.     |
| Decision Evidence    | Shows policy decisions created by automation.        |
| Report Evidence      | Shows generated governance, risk, and drift reports. |
| Dashboard Evidence   | Shows dashboard summary metrics.                     |
| Failure Evidence     | Shows job failures and operational exceptions.       |
| Remediation Evidence | Shows actions taken based on automation findings.    |

---

## Operational Health Panel

The Operational Health panel summarizes automation reliability.

| Health Metric                | Purpose                                   |
| ---------------------------- | ----------------------------------------- |
| Automation Failures          | Shows failed automation jobs.             |
| Reports Generated            | Shows successful reporting outputs.       |
| Manual Intervention Required | Shows unresolved human work.              |
| Missing Inputs               | Shows source data issues.                 |
| Missing Outputs              | Shows report generation gaps.             |
| Stale Outputs                | Shows outputs that may need regeneration. |
| Overall Status               | Summarizes automation health.             |

---

## Automation Work Queue

The Automation Health Dashboard should include a work queue.

| Priority | Work Type                    | Reason                                                           |
| -------- | ---------------------------- | ---------------------------------------------------------------- |
| 1        | Failed automation job        | A failed script may block governance, risk, or drift visibility. |
| 2        | Missing output report        | Reports are required for evidence and dashboard metrics.         |
| 3        | Manual intervention required | Human decision is needed to complete the workflow.               |
| 4        | Missing input data           | Automation cannot run without complete source data.              |
| 5        | Stale report                 | Outdated evidence may misrepresent current state.                |
| 6        | Dashboard summary mismatch   | Metrics should align with source reports.                        |
| 7        | Documentation gap            | Automation should be documented for operators and auditors.      |

---

## Filters

The Automation Health Dashboard should support these filters:

| Filter              | Purpose                                                                   |
| ------------------- | ------------------------------------------------------------------------- |
| Script Name         | Filter by automation script.                                              |
| Job Status          | Filter by healthy, warning, degraded, failed, or unknown.                 |
| Report Type         | Filter by governance, risk, drift, or dashboard summary report.           |
| Output Status       | Filter by generated, missing, stale, or failed.                           |
| Manual Intervention | Filter by approval, review, remediation, exception, or audit action.      |
| Failure Type        | Filter by script failure, missing input, invalid data, or missing output. |
| Severity            | Filter by low, medium, high, or critical operational impact.              |

---

## Drilldowns

Users should be able to drill into:

| Drilldown          | Purpose                                                    |
| ------------------ | ---------------------------------------------------------- |
| Script Detail      | Shows script purpose, input, output, and health state.     |
| Job Detail         | Shows run status, timestamp, errors, and output artifacts. |
| Report Detail      | Shows generated report location and evidence value.        |
| Failure Detail     | Shows error condition and recommended remediation.         |
| Manual Work Detail | Shows owner, action required, and status.                  |
| Evidence Detail    | Shows input, decision, output, and audit artifacts.        |

---

## Data Sources

The Automation Health Dashboard uses these sample sources:

| Source                                     | Purpose                                             |
| ------------------------------------------ | --------------------------------------------------- |
| `automation/README.md`                     | Documents available automation scripts.             |
| `automation/policy-evaluator.py`           | Provides policy decision automation.                |
| `automation/generate-governance-report.py` | Provides governance report automation.              |
| `automation/risk-scorer.py`                | Provides risk scoring automation.                   |
| `automation/access-drift-detector.py`      | Provides access drift detection automation.         |
| `automation/generate-dashboard-summary.py` | Provides dashboard summary automation.              |
| `reports/sample-governance-report.md`      | Shows generated governance evidence.                |
| `reports/sample-risk-score-report.md`      | Shows generated risk evidence.                      |
| `reports/sample-access-drift-report.md`    | Shows generated drift evidence.                     |
| `reports/sample-dashboard-summary.md`      | Shows generated dashboard evidence.                 |
| `examples/sample-dashboard-metrics.json`   | Provides dashboard-ready automation health metrics. |

---

## Success Criteria

The Automation Health Dashboard is successful when users can quickly see:

* Which automation scripts exist
* Which automation workflows are healthy
* Which reports were generated
* Which jobs failed
* Which outputs are missing
* Which tasks require manual intervention
* Which reports support audit evidence
* Whether automation is reducing manual IAM effort
* Whether IdentityOS is operationally reliable

---

## Summary

The IdentityOS Automation Health Dashboard turns identity automation into observable operations.

It helps teams monitor automation health, report generation, failure conditions, evidence creation, and manual work queues.

> Automation health dashboards turn scripts into trusted identity operations.
