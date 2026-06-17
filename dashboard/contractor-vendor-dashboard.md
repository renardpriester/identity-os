# IdentityOS Contractor and Vendor Dashboard

## Purpose

The Contractor and Vendor Dashboard provides visibility into external identities, temporary access, sponsor ownership, access expiration, renewal decisions, access drift, and offboarding readiness.

This dashboard is designed to help IAM, security, governance, procurement, business sponsors, and application owners manage non-employee access.

The goal is to answer:

> Which external identities have access, who owns them, when should access expire, and is that access still justified?

---

## Primary Audience

| Audience           | Purpose                                                                            |
| ------------------ | ---------------------------------------------------------------------------------- |
| IAM Teams          | Track contractor and vendor access lifecycle events.                               |
| Security Teams     | Identify risky external access and stale access.                                   |
| Governance Teams   | Review approvals, expirations, renewals, and evidence.                             |
| Business Sponsors  | Confirm whether external users still need access.                                  |
| Application Owners | Validate external access to business applications.                                 |
| Auditors           | Confirm that external access was approved, reviewed, expired, or renewed properly. |

---

## Contractor and Vendor Access Questions

The Contractor and Vendor Dashboard should answer:

* Which contractors and vendors currently have access?
* Who sponsors each external identity?
* What access was granted?
* When does access expire?
* Which external identities are near expiration?
* Which external identities are expired but still active?
* Which access requires renewal?
* Which access requires removal?
* Which contractor or vendor access is high risk?
* Which external identities have access drift?
* What audit evidence exists?

---

## Contractor and Vendor Dashboard Wireframe

```text id="grbmkn"
+--------------------------------------------------------------------------------+
| IdentityOS Contractor and Vendor Dashboard              External Access: Current|
+--------------------------------------------------------------------------------+
| Overview | Expiration | Sponsors | Reviews | Drift | Evidence                  |
+--------------------------------------------------------------------------------+
| External Identities | Pending Renewals | Expiring Soon | Drift | Critical Risk  |
|         2           |        1         |       1       |   1   |       1        |
+--------------------------------------------------------------------------------+
| External Access Overview              | Expiration and Renewal Queue           |
|---------------------------------------|----------------------------------------|
| Contractors: 1                        | Contractor Access Expiration: Review   |
| Vendors: 1                            | Pending Sponsor Renewal: 1             |
| Active External Access: Review        | Expired Access: Future Metric          |
| Temporary Access: Review              | Renewal Decision Required: 1           |
+--------------------------------------------------------------------------------+
| Sponsor Ownership                     | Access Drift                           |
|---------------------------------------|----------------------------------------|
| Sponsor Assigned: Yes                 | Contractor Drift Findings: 1           |
| Sponsor Missing: Future Metric        | Excess Access: Review                  |
| Sponsor Review Required: Yes          | Expiration Drift: Review               |
| Sponsor Escalation: Future Metric     | Remediation Required: Yes              |
+--------------------------------------------------------------------------------+
| Governance Controls                   | Evidence and Reports                   |
|---------------------------------------|----------------------------------------|
| Sponsor Approval                      | Governance Report                      |
| Expiration Date                       | Access Drift Report                    |
| Renewal Review                        | Risk Score Report                      |
| Access Removal                        | Dashboard Summary                      |
+--------------------------------------------------------------------------------+
```

---

## Top KPI Cards

| KPI Card            | Purpose                                                  |
| ------------------- | -------------------------------------------------------- |
| External Identities | Shows total contractor and vendor identities.            |
| Pending Renewals    | Shows access requiring sponsor renewal.                  |
| Expiring Soon       | Shows access approaching expiration.                     |
| Expired Access      | Shows access that should be removed or renewed.          |
| Contractor Drift    | Shows external access that no longer aligns with policy. |
| Critical Risk       | Shows urgent external access risk.                       |

---

## External Access Overview Panel

The External Access Overview panel summarizes contractor and vendor identity activity.

| Metric                 | Purpose                                        |
| ---------------------- | ---------------------------------------------- |
| Contractors            | Shows contractor identities.                   |
| Vendors                | Shows vendor identities.                       |
| Active External Access | Shows external identities with current access. |
| Temporary Access       | Shows access intended to expire.               |
| Sponsor Assigned       | Shows whether business ownership exists.       |
| Access Review Required | Shows external access requiring validation.    |

---

## Sponsor Ownership Panel

Every contractor or vendor identity should have an accountable business sponsor.

| Sponsor Field            | Purpose                               |
| ------------------------ | ------------------------------------- |
| Sponsor Name             | Identifies the business owner.        |
| Sponsor Department       | Shows owning department.              |
| Sponsor Approval         | Confirms business need.               |
| Sponsor Review Date      | Shows last sponsor validation.        |
| Sponsor Renewal Decision | Shows whether access should continue. |
| Sponsor Escalation       | Shows when sponsor action is overdue. |

### Sponsor Interpretation

External access without a sponsor becomes unmanaged risk.

A strong IAM program requires that every contractor or vendor identity has:

* A sponsor
* A business purpose
* Approved access
* Expiration date
* Renewal decision
* Offboarding process
* Audit evidence

---

## Expiration and Renewal Queue

The Expiration and Renewal Queue shows external access that needs action.

| Queue Item           | Reason                                                 |
| -------------------- | ------------------------------------------------------ |
| Access Expiring Soon | Sponsor must renew or allow expiration.                |
| Access Expired       | Access should be disabled or removed.                  |
| Renewal Pending      | Sponsor decision is required.                          |
| Sponsor Missing      | Identity lacks business ownership.                     |
| Review Overdue       | External access has not been revalidated.              |
| Contractor Drift     | External access no longer aligns with expected access. |

---

## Contractor and Vendor Risk Panel

External identities should be treated as higher risk when access is temporary, sensitive, stale, or unmanaged.

| Risk Signal                  | Meaning                                            |
| ---------------------------- | -------------------------------------------------- |
| External Identity            | Non-employee access requires stronger governance.  |
| Missing Sponsor              | No accountable business owner exists.              |
| Missing Expiration           | Access may become permanent.                       |
| Expired Access Still Active  | Access should be remediated immediately.           |
| Sensitive Application Access | External users may access sensitive systems.       |
| Privileged Access            | External elevated access requires urgent review.   |
| Access Drift                 | External access no longer matches expected access. |
| Missing Audit Evidence       | Access cannot be explained or proven.              |

---

## Contractor and Vendor Access Drift

Contractor and vendor drift occurs when external access no longer matches expected access.

| Drift Type        | Meaning                                                       |
| ----------------- | ------------------------------------------------------------- |
| Expiration Drift  | Access remains active past expiration.                        |
| Sponsor Drift     | Access lacks current sponsor validation.                      |
| Role Drift        | Access no longer matches approved role or contract scope.     |
| Application Drift | External user retains access to systems outside current need. |
| Privileged Drift  | External user has elevated access that requires review.       |
| Governance Drift  | Required review, approval, or remediation is incomplete.      |

---

## Recommended Remediation

The dashboard should recommend actions based on the external access condition.

| Condition                  | Recommended Action                                      |
| -------------------------- | ------------------------------------------------------- |
| Expiring access            | Notify sponsor and request renewal decision.            |
| Expired access             | Disable identity or remove access.                      |
| Missing sponsor            | Escalate to business owner or revoke access.            |
| Missing expiration         | Add expiration date or remove access.                   |
| Access drift               | Remove excess access and generate remediation evidence. |
| Privileged external access | Require security review and time-bound approval.        |
| Renewal denied             | Remove access and close identity lifecycle event.       |
| Renewal approved           | Extend expiration and retain evidence.                  |

---

## Contractor and Vendor Detail View

Users should be able to drill into each external identity.

| Field              | Purpose                                                   |
| ------------------ | --------------------------------------------------------- |
| Identity           | Contractor or vendor name.                                |
| Identity Type      | Contractor, vendor, partner, or external service account. |
| Sponsor            | Business owner responsible for the identity.              |
| Department         | Owning department.                                        |
| Access Granted     | Current approved access.                                  |
| Expiration Date    | Date access should expire.                                |
| Renewal Status     | Pending, approved, denied, expired, or escalated.         |
| Risk Score         | Calculated identity risk.                                 |
| Drift Status       | Whether access drift exists.                              |
| Recommended Action | Suggested next step.                                      |
| Evidence Link      | Related governance, drift, or risk evidence.              |

---

## Governance Controls

Contractor and vendor access should include these controls:

| Control                  | Purpose                                              |
| ------------------------ | ---------------------------------------------------- |
| Sponsor Required         | Ensures business ownership.                          |
| Expiration Required      | Prevents permanent external access.                  |
| Renewal Review           | Confirms continued business need.                    |
| Access Review            | Validates access remains appropriate.                |
| Sensitive Access Review  | Adds governance for sensitive systems.               |
| Privileged Access Review | Adds security approval for elevated external access. |
| Offboarding Trigger      | Removes access when contract ends.                   |
| Audit Evidence           | Proves access decisions and remediation.             |

---

## Filters

The Contractor and Vendor Dashboard should support these filters:

| Filter            | Purpose                                                                           |
| ----------------- | --------------------------------------------------------------------------------- |
| Identity Type     | Filter by contractor, vendor, partner, or external service account.               |
| Sponsor           | Filter by business sponsor.                                                       |
| Department        | Filter by owning department.                                                      |
| Expiration Status | Filter by active, expiring soon, expired, or renewal pending.                     |
| Renewal Status    | Filter by approved, denied, pending, or escalated.                                |
| Risk Level        | Filter by Low, Medium, High, or Critical.                                         |
| Drift Type        | Filter by expiration, sponsor, role, application, privilege, or governance drift. |
| Application       | Filter by system or application access.                                           |

---

## Reports

The Contractor and Vendor Dashboard should link to:

| Report              | Purpose                                           |
| ------------------- | ------------------------------------------------- |
| Governance Report   | Shows approvals, reviews, and audit requirements. |
| Access Drift Report | Shows contractor and vendor access drift.         |
| Risk Score Report   | Shows external identity risk scoring.             |
| Dashboard Summary   | Shows dashboard-ready external access metrics.    |

---

## Data Sources

The Contractor and Vendor Dashboard uses these sample sources:

| Source                                   | Purpose                                           |
| ---------------------------------------- | ------------------------------------------------- |
| `examples/sample-identity-events.json`   | Provides contractor and vendor lifecycle events.  |
| `examples/sample-policy-decisions.json`  | Provides access decisions and governance actions. |
| `reports/sample-governance-report.md`    | Provides governance and audit evidence.           |
| `reports/sample-access-drift-report.md`  | Provides contractor drift findings.               |
| `reports/sample-risk-score-report.md`    | Provides external identity risk scoring.          |
| `examples/sample-dashboard-metrics.json` | Provides dashboard-ready metrics.                 |

---

## Success Criteria

The Contractor and Vendor Dashboard is successful when users can quickly see:

* Which external identities have access
* Who sponsors each identity
* Which access is expiring soon
* Which access is expired
* Which access requires renewal
* Which access requires removal
* Which external identities are high risk
* Which external identities have access drift
* Which evidence supports the access decision

---

## Summary

The IdentityOS Contractor and Vendor Dashboard turns external identity access into visible, governed, and time-bound access.

It helps organizations reduce stale contractor access, enforce sponsor accountability, and prevent external access from becoming permanent risk.

> Contractor and vendor dashboards turn temporary access into accountable access.
