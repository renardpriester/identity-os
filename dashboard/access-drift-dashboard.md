# IdentityOS Access Drift Dashboard

## Purpose

The Access Drift Dashboard provides visibility into access that no longer aligns with an identity’s expected role, department, lifecycle state, ownership, or governance requirements.

This dashboard is designed to help IAM, security, governance, and application owner teams identify privilege creep, stale access, excess access, contractor drift, leaver drift, privileged drift, and non-human identity drift.

The goal is to answer:

> Where does actual access no longer match expected access?

---

## Primary Audience

| Audience           | Purpose                                                 |
| ------------------ | ------------------------------------------------------- |
| IAM Engineers      | Identify and remediate stale or excessive access.       |
| Security Teams     | Detect access that increases identity risk.             |
| Governance Teams   | Track access drift requiring review or remediation.     |
| Application Owners | Validate whether users still need application access.   |
| Managers           | Confirm whether direct reports still require access.    |
| Auditors           | Review evidence that drift was detected and remediated. |

---

## Access Drift Questions

The Access Drift Dashboard should answer:

* Which identities have access drift?
* What access is excessive?
* Which users retained access from previous departments?
* Which leavers still had access?
* Which contractors have expired or expiring access?
* Which non-human identities are missing owners or scope validation?
* Which drift findings are critical?
* Which drift findings have been remediated?
* Which applications have the most drift?
* What evidence exists for drift remediation?

---

## Access Drift Dashboard Wireframe

```text id="kvrn0u"
+--------------------------------------------------------------------------------+
| IdentityOS Access Drift Dashboard                       Drift View: Current     |
+--------------------------------------------------------------------------------+
| Drift Overview | Critical Drift | Excess Access | Remediation | Reports         |
+--------------------------------------------------------------------------------+
| Total Drift | Department | Leaver | Contractor | Non-Human | Critical | High    |
|      4      |     1      |   1    |     1      |     1     |    2     |   2     |
+--------------------------------------------------------------------------------+
| Drift Summary                         | Critical Drift Queue                   |
|---------------------------------------|----------------------------------------|
| Department Drift: 1                   | Leaver Access Still Active             |
| Leaver Drift: 1                       | Contractor Access Expiration           |
| Contractor Drift: 1                   | Non-Human Identity Ownership Review    |
| Non-Human Identity Drift: 1           | Previous Department Access             |
+--------------------------------------------------------------------------------+
| Excess Access                         | Remediation Actions                    |
|---------------------------------------|----------------------------------------|
| Finance SharePoint                    | Remove previous department access      |
| Financial Reporting Portal            | Disable expired contractor access      |
| Microsoft 365 Limited                 | Review non-human identity ownership    |
| Project Workspace                     | Generate remediation evidence          |
+--------------------------------------------------------------------------------+
| Drift Evidence                        | Related Reports                        |
|---------------------------------------|----------------------------------------|
| Drift Reason                          | Access Drift Report                    |
| Expected vs Actual Access             | Risk Score Report                      |
| Excess Access                         | Governance Report                      |
| Recommended Remediation               | Dashboard Summary                      |
+--------------------------------------------------------------------------------+
```

---

## Top KPI Cards

| KPI Card         | Purpose                                                       |
| ---------------- | ------------------------------------------------------------- |
| Total Drift      | Shows total access drift findings.                            |
| Department Drift | Shows access from previous departments.                       |
| Leaver Drift     | Shows access remaining after departure.                       |
| Contractor Drift | Shows contractor access requiring expiration or renewal.      |
| Non-Human Drift  | Shows service account or automation identity governance gaps. |
| Critical Drift   | Shows urgent drift requiring remediation.                     |
| High Drift       | Shows serious drift requiring review.                         |

---

## Drift Summary Panel

The Drift Summary panel shows the types of drift detected.

| Drift Type               | Meaning                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------- |
| Department Drift         | Access belongs to a previous department or role.                                              |
| Role Drift               | Access does not align with current role package.                                              |
| Leaver Drift             | Access remains after a user leaves.                                                           |
| Contractor Drift         | Contractor access remains after expiration or requires renewal.                               |
| Vendor Drift             | Vendor access lacks current business sponsorship.                                             |
| Privilege Drift          | Privileged access is no longer justified.                                                     |
| Non-Human Identity Drift | Service account or automation identity lacks owner, purpose, scope, or credential governance. |
| Governance Drift         | Review or remediation is required but not completed.                                          |

---

## Critical Drift Queue

The Critical Drift Queue prioritizes the most urgent drift findings.

| Priority | Drift Finding            | Reason                                                   |
| -------- | ------------------------ | -------------------------------------------------------- |
| 1        | Leaver Drift             | Former users should not retain access.                   |
| 2        | Privileged Drift         | Elevated access outside policy creates serious exposure. |
| 3        | Contractor Drift         | External access should expire or be renewed.             |
| 4        | Non-Human Identity Drift | Unowned service accounts cannot be governed.             |
| 5        | Department Drift         | Previous department access can create privilege creep.   |
| 6        | Governance Drift         | Review-required access may remain unresolved.            |

---

## Excess Access Panel

The Excess Access panel shows access that should be removed or reviewed.

| Field           | Purpose                                          |
| --------------- | ------------------------------------------------ |
| Identity        | User, contractor, vendor, or non-human identity. |
| Event ID        | Related lifecycle or governance event.           |
| Decision ID     | Related policy decision.                         |
| Drift Type      | Type of drift detected.                          |
| Excess Access   | Access that no longer belongs.                   |
| Expected Access | Access that should remain.                       |
| Actual Access   | Access currently detected in the sample model.   |
| Severity        | High or Critical drift level.                    |

---

## Expected vs Actual Access

The dashboard should clearly compare expected access and actual access.

Example:

| Category        | Access                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| Expected Access | Legal Operations Workspace, Legal Document Management System                                                 |
| Actual Access   | Legal Operations Workspace, Legal Document Management System, Finance SharePoint, Financial Reporting Portal |
| Excess Access   | Finance SharePoint, Financial Reporting Portal                                                               |

This comparison makes privilege creep visible.

---

## Remediation Actions Panel

The Remediation Actions panel shows what should happen next.

| Drift Condition          | Recommended Remediation                                           |
| ------------------------ | ----------------------------------------------------------------- |
| Department Drift         | Remove access from the previous department.                       |
| Role Drift               | Remove access outside the current role package.                   |
| Leaver Drift             | Disable identity, revoke sessions, and remove access.             |
| Contractor Drift         | Disable access unless sponsor renewal is approved.                |
| Vendor Drift             | Remove access or validate business sponsorship.                   |
| Privilege Drift          | Remove or review privileged access immediately.                   |
| Non-Human Identity Drift | Validate owner, purpose, access scope, and credential governance. |
| Governance Drift         | Route to review and track remediation.                            |

---

## Application Drift View

The Access Drift Dashboard should eventually show drift by application.

| Application                      | Drift Meaning                                      |
| -------------------------------- | -------------------------------------------------- |
| Finance SharePoint               | Possible previous department access.               |
| Financial Reporting Portal       | Sensitive finance access requiring removal.        |
| Project Workspace                | Contractor access requiring expiration review.     |
| Legal Document Management System | Sensitive legal access requiring owner validation. |
| Privileged Access Platform       | Elevated access requiring urgent review.           |

---

## Department Drift View

The dashboard should show where drift occurs across departments.

| Department | Drift Concern                                                     |
| ---------- | ----------------------------------------------------------------- |
| Finance    | Users may retain financial reporting access after moving roles.   |
| Legal      | Users may receive sensitive document access requiring governance. |
| Security   | Users may have privileged or security-sensitive access.           |
| IT         | Users may retain administrative or operational access.            |
| HR         | Users may have access to sensitive employee data.                 |

---

## Non-Human Identity Drift View

Non-human identities should have a dedicated drift view.

| Drift Signal               | Meaning                                          |
| -------------------------- | ------------------------------------------------ |
| Missing Owner              | No accountable owner exists.                     |
| Missing Business Purpose   | Identity purpose is unclear.                     |
| Broad Access Scope         | Service account has more access than required.   |
| Credential Review Required | Secret or credential lifecycle needs validation. |
| Dormant Identity           | Identity may no longer be used.                  |

---

## Drift Evidence Panel

Every drift finding should have evidence.

Evidence should include:

* Event ID
* Decision ID
* Identity
* Drift type
* Drift severity
* Expected access
* Actual access
* Excess access
* Drift reason
* Recommended remediation
* Report link
* Timestamp

---

## Filters

The Access Drift Dashboard should support these filters:

| Filter             | Purpose                                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| Drift Type         | Filter by department, role, leaver, contractor, vendor, privilege, non-human identity, or governance drift. |
| Severity           | Filter by Low, Medium, High, or Critical.                                                                   |
| Identity Type      | Filter by employee, contractor, vendor, or service account.                                                 |
| Department         | Filter by business unit or department.                                                                      |
| Application        | Filter by application or system.                                                                            |
| Remediation Status | Filter by open, completed, overdue, or escalated.                                                           |
| Risk Level         | Filter by Low, Medium, High, or Critical risk.                                                              |

---

## Drilldowns

Users should be able to drill into:

| Drilldown          | Purpose                                                       |
| ------------------ | ------------------------------------------------------------- |
| Drift Detail       | Shows expected access, actual access, and excess access.      |
| Identity Detail    | Shows identity attributes, risk score, and governance status. |
| Remediation Detail | Shows what action is required and whether it is complete.     |
| Application Detail | Shows drift related to a specific application.                |
| Evidence Detail    | Shows report output and audit evidence.                       |

---

## Data Sources

The Access Drift Dashboard uses these sample sources:

| Source                                   | Purpose                                        |
| ---------------------------------------- | ---------------------------------------------- |
| `reports/sample-access-drift-report.md`  | Provides detailed drift findings.              |
| `examples/sample-dashboard-metrics.json` | Provides dashboard-ready drift metrics.        |
| `reports/sample-risk-score-report.md`    | Provides risk context for drift findings.      |
| `reports/sample-governance-report.md`    | Provides governance and audit context.         |
| `examples/sample-policy-decisions.json`  | Provides access actions and removal decisions. |
| `examples/sample-identity-events.json`   | Provides lifecycle context.                    |

---

## Success Criteria

The Access Drift Dashboard is successful when users can quickly see:

* Which identities have access drift
* What excess access exists
* Which drift findings are critical
* Which drift findings require remediation
* Which applications have drift
* Which departments have drift
* Which contractors or vendors require review
* Which non-human identities require owner validation
* What evidence supports the finding

---

## Summary

The IdentityOS Access Drift Dashboard turns stale access and privilege creep into visible, actionable findings.

It helps teams understand where access no longer belongs and what must be remediated.

> Access drift dashboards turn hidden privilege creep into visible risk.
