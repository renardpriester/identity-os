# IdentityOS Audit Evidence Dashboard

## Purpose

The Audit Evidence Dashboard provides visibility into the evidence produced by identity lifecycle events, policy decisions, access reviews, approvals, remediation actions, exceptions, risk scoring, access drift detection, and report generation.

This dashboard is designed to help IAM, governance, compliance, security, audit, and leadership teams prove that access decisions were reviewed, approved, remediated, and documented.

The goal is to answer:

> Can we prove who had access, why they had it, who approved it, when it was reviewed, and whether remediation was completed?

---

## Primary Audience

| Audience             | Purpose                                                      |
| -------------------- | ------------------------------------------------------------ |
| Auditors             | Validate that access decisions are supported by evidence.    |
| Compliance Teams     | Confirm that governance controls are operating effectively.  |
| IAM Governance Teams | Track review, approval, remediation, and exception evidence. |
| IAM Operations Teams | Confirm that actions were completed and documented.          |
| Security Teams       | Review evidence for high-risk or critical-risk access.       |
| Leadership           | Understand audit readiness and governance maturity.          |

---

## Audit Evidence Questions

The Audit Evidence Dashboard should answer:

* Which access decisions require audit evidence?
* Which access decisions already have evidence?
* Which approvals are documented?
* Which access reviews are documented?
* Which remediation actions were completed?
* Which exceptions were approved and time-bound?
* Which reports were generated?
* Which evidence is missing?
* Which evidence is stale?
* Which high-risk or critical-risk findings require audit review?
* Can access decisions be explained clearly?

---

## Audit Evidence Dashboard Wireframe

```text id="vj26hm"
+--------------------------------------------------------------------------------+
| IdentityOS Audit Evidence Dashboard                     Evidence View: Current  |
+--------------------------------------------------------------------------------+
| Overview | Decisions | Reviews | Remediation | Exceptions | Reports             |
+--------------------------------------------------------------------------------+
| Audit Required | Evidence Available | Missing Evidence | Reports | Remediation   |
|       7        |        4           |   Future Metric  |    4    |     4         |
+--------------------------------------------------------------------------------+
| Evidence Overview                     | Policy Decision Evidence               |
|---------------------------------------|----------------------------------------|
| Audit Required Decisions: 7           | Decisions Generated: 7                 |
| Governance Evidence: Available        | Approval Required: 4                   |
| Risk Evidence: Available              | Review Required: 2                     |
| Drift Evidence: Available             | Audit Required: 7                      |
+--------------------------------------------------------------------------------+
| Review and Approval Evidence          | Remediation Evidence                   |
|---------------------------------------|----------------------------------------|
| Pending Approvals: 2                  | Drift Findings Requiring Action: 4     |
| Reviews Required: 2                   | Critical Drift Findings: 2             |
| Manager Evidence: Future Metric       | Access Removal Evidence: Review        |
| Sponsor Evidence: Review              | Completion Evidence: Future Metric     |
+--------------------------------------------------------------------------------+
| Evidence Reports                      | Evidence Quality                       |
|---------------------------------------|----------------------------------------|
| Governance Report                     | Owner Present: Review                  |
| Risk Score Report                     | Timestamp Present: Review              |
| Access Drift Report                   | Decision Reason Present: Review        |
| Dashboard Summary                     | Report Link Present: Review            |
+--------------------------------------------------------------------------------+
```

---

## Top KPI Cards

| KPI Card                 | Purpose                                          |
| ------------------------ | ------------------------------------------------ |
| Audit Required Decisions | Shows decisions requiring audit evidence.        |
| Evidence Available       | Shows evidence artifacts already generated.      |
| Missing Evidence         | Shows decisions or actions lacking proof.        |
| Reports Generated        | Shows available report artifacts.                |
| Remediation Evidence     | Shows whether remediation actions have evidence. |
| Evidence Quality         | Shows whether evidence contains required fields. |

---

## Evidence Overview Panel

The Evidence Overview panel summarizes audit readiness.

| Metric                   | Purpose                                                    |
| ------------------------ | ---------------------------------------------------------- |
| Audit Required Decisions | Shows access decisions that must be explainable.           |
| Evidence Available       | Shows reports or artifacts supporting decisions.           |
| Evidence Missing         | Shows gaps that require follow-up.                         |
| Evidence Stale           | Shows evidence that may need regeneration.                 |
| Evidence Complete        | Shows decisions with required supporting information.      |
| Evidence Exceptions      | Shows access outside policy requiring documented approval. |

### Audit Interpretation

Audit evidence should make identity decisions explainable.

Strong evidence answers:

* What happened?
* Who was involved?
* Why did it happen?
* Who approved it?
* What access changed?
* Was the action completed?
* When did it happen?
* What report or artifact proves it?

---

## Policy Decision Evidence Panel

Policy decisions should be traceable from event to action.

| Evidence Field    | Purpose                                                               |
| ----------------- | --------------------------------------------------------------------- |
| Decision ID       | Unique identifier for the policy decision.                            |
| Event ID          | Links the decision to the identity lifecycle event.                   |
| Identity          | Shows the user, contractor, vendor, or service account.               |
| Event Type        | Joiner, Mover, Leaver, Contractor, Privileged, or Non-Human Identity. |
| Policy Action     | Grant, remove, retain, review, disable, or escalate.                  |
| Reason            | Explains why the decision was made.                                   |
| Required Approval | Shows whether approval was required.                                  |
| Required Review   | Shows whether review was required.                                    |
| Audit Required    | Shows whether evidence must be retained.                              |

---

## Review Evidence Panel

Access reviews should produce evidence showing the reviewer, decision, and outcome.

| Review Evidence        | Purpose                                        |
| ---------------------- | ---------------------------------------------- |
| Reviewer               | Identifies who reviewed the access.            |
| Review Date            | Shows when the review occurred.                |
| Access Reviewed        | Shows what access was evaluated.               |
| Review Decision        | Retain, remove, modify, or escalate.           |
| Business Justification | Explains why access was retained or changed.   |
| Review Frequency       | Monthly, quarterly, annual, or event-driven.   |
| Review Outcome         | Shows whether action was required.             |
| Evidence Link          | Connects the decision to a report or artifact. |

---

## Approval Evidence Panel

Approvals should prove that the right person approved access before it was granted or retained.

| Approval Evidence      | Purpose                                                                       |
| ---------------------- | ----------------------------------------------------------------------------- |
| Approver               | Identifies manager, sponsor, app owner, or security approver.                 |
| Approval Date          | Shows when approval occurred.                                                 |
| Access Requested       | Shows the access being approved.                                              |
| Business Justification | Explains why access was needed.                                               |
| Approval Outcome       | Approved, denied, pending, expired, or escalated.                             |
| Approval Type          | Manager, sponsor, application owner, security, or privileged access approval. |
| Expiration Date        | Shows whether access is time-bound.                                           |
| Evidence Link          | Connects approval to governance reporting.                                    |

---

## Remediation Evidence Panel

Remediation evidence proves that access was removed, modified, disabled, or reviewed after a finding.

| Remediation Evidence | Purpose                                                                          |
| -------------------- | -------------------------------------------------------------------------------- |
| Remediation Action   | Remove access, disable identity, revoke sessions, reduce scope, or assign owner. |
| Remediation Owner    | Person or team responsible for the action.                                       |
| Remediation Status   | Open, in progress, completed, overdue, or escalated.                             |
| Completion Date      | Shows when remediation was finished.                                             |
| Access Removed       | Shows what access was removed.                                                   |
| Identity Disabled    | Shows whether a leaver or expired contractor was disabled.                       |
| Drift Resolved       | Shows whether access drift was corrected.                                        |
| Evidence Link        | Connects remediation to audit proof.                                             |

---

## Exception Evidence Panel

Exceptions must be documented, approved, owned, and time-bound.

| Exception Evidence     | Purpose                                             |
| ---------------------- | --------------------------------------------------- |
| Exception ID           | Unique identifier for the exception.                |
| Exception Owner        | Person accountable for the exception.               |
| Business Justification | Explains why the exception exists.                  |
| Approval Owner         | Shows who approved the exception.                   |
| Start Date             | Shows when the exception began.                     |
| Expiration Date        | Shows when the exception should end.                |
| Review Date            | Shows when the exception must be revalidated.       |
| Risk Level             | Shows risk introduced by the exception.             |
| Remediation Plan       | Shows how the exception will be removed or renewed. |

---

## Report Evidence Panel

The dashboard should show which reports support audit evidence.

| Report              | Evidence Provided                                                      |
| ------------------- | ---------------------------------------------------------------------- |
| Governance Report   | Shows access approvals, review requirements, and audit requirements.   |
| Risk Score Report   | Shows risk levels, risk factors, and recommended actions.              |
| Access Drift Report | Shows excess access, stale access, and remediation needs.              |
| Dashboard Summary   | Shows dashboard-ready governance, risk, drift, and automation metrics. |

---

## Evidence Quality Panel

Evidence should be evaluated for completeness.

| Quality Check       | Purpose                                                               |
| ------------------- | --------------------------------------------------------------------- |
| Identity Present    | Evidence identifies the user, contractor, vendor, or service account. |
| Decision Present    | Evidence includes a clear decision or action.                         |
| Reason Present      | Evidence explains why the decision occurred.                          |
| Owner Present       | Evidence identifies who owns the decision or remediation.             |
| Timestamp Present   | Evidence shows when the event or decision occurred.                   |
| Approval Present    | Evidence includes approval when required.                             |
| Review Present      | Evidence includes review when required.                               |
| Report Link Present | Evidence links to supporting artifacts.                               |

---

## Evidence Lifecycle

Audit evidence should follow a lifecycle.

```text id="m0n8hw"
Identity Event
      ↓
Policy Decision
      ↓
Approval or Review
      ↓
Access Action
      ↓
Risk or Drift Evaluation
      ↓
Remediation
      ↓
Report Generation
      ↓
Audit Evidence
```

---

## Audit Work Queue

The Audit Evidence Dashboard should include a work queue.

| Priority | Work Type                             | Reason                                        |
| -------- | ------------------------------------- | --------------------------------------------- |
| 1        | Missing evidence for critical risk    | Critical access risk must be explainable.     |
| 2        | Missing remediation evidence          | Access removal or disablement must be proven. |
| 3        | Pending approval evidence             | Access approval must be documented.           |
| 4        | Pending review evidence               | Access review must be completed and recorded. |
| 5        | Exception evidence missing expiration | Exceptions must be time-bound.                |
| 6        | Stale report evidence                 | Reports may need regeneration.                |
| 7        | Evidence quality gap                  | Evidence must include required fields.        |

---

## Filters

The Audit Evidence Dashboard should support these filters:

| Filter             | Purpose                                                                                |
| ------------------ | -------------------------------------------------------------------------------------- |
| Evidence Type      | Filter by decision, approval, review, remediation, exception, risk, or drift evidence. |
| Evidence Status    | Filter by available, missing, stale, incomplete, or complete.                          |
| Risk Level         | Filter by Low, Medium, High, or Critical.                                              |
| Event Type         | Filter by Joiner, Mover, Leaver, Contractor, Privileged, or Non-Human Identity.        |
| Identity Type      | Filter by employee, contractor, vendor, or service account.                            |
| Report Type        | Filter by governance, risk, drift, or dashboard summary.                               |
| Remediation Status | Filter by open, completed, overdue, or escalated.                                      |
| Approval Status    | Filter by pending, approved, denied, expired, or escalated.                            |

---

## Drilldowns

Users should be able to drill into:

| Drilldown                   | Purpose                                                               |
| --------------------------- | --------------------------------------------------------------------- |
| Decision Evidence Detail    | Shows event, policy decision, action, reason, and audit requirement.  |
| Approval Evidence Detail    | Shows approver, justification, decision, and timestamp.               |
| Review Evidence Detail      | Shows reviewer, access reviewed, decision, and outcome.               |
| Remediation Evidence Detail | Shows required action, owner, status, and completion proof.           |
| Exception Evidence Detail   | Shows exception owner, approval, justification, expiration, and risk. |
| Report Evidence Detail      | Shows report artifact and evidence scope.                             |
| Identity Evidence Detail    | Shows all evidence tied to a single identity.                         |

---

## Data Sources

The Audit Evidence Dashboard uses these sample sources:

| Source                                   | Purpose                                            |
| ---------------------------------------- | -------------------------------------------------- |
| `examples/sample-identity-events.json`   | Provides lifecycle event context.                  |
| `examples/sample-policy-decisions.json`  | Provides decision evidence and audit requirements. |
| `reports/sample-governance-report.md`    | Provides governance evidence.                      |
| `reports/sample-risk-score-report.md`    | Provides risk evidence.                            |
| `reports/sample-access-drift-report.md`  | Provides drift and remediation evidence.           |
| `reports/sample-dashboard-summary.md`    | Provides dashboard evidence.                       |
| `examples/sample-dashboard-metrics.json` | Provides dashboard-ready evidence metrics.         |

---

## Success Criteria

The Audit Evidence Dashboard is successful when users can quickly see:

* Which decisions require audit evidence
* Which reports were generated
* Which approvals are documented
* Which reviews are documented
* Which remediation actions are documented
* Which exceptions are documented
* Which evidence is missing
* Which evidence is incomplete
* Which high-risk findings require proof
* Whether IdentityOS is audit-ready

---

## Summary

The IdentityOS Audit Evidence Dashboard turns identity activity into provable governance evidence.

It helps organizations explain access decisions, demonstrate control effectiveness, and support audit readiness.

> Audit evidence dashboards turn identity decisions into proof.
