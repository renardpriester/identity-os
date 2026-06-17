# IdentityOS Non-Human Identity Dashboard

## Purpose

The Non-Human Identity Dashboard provides visibility into service accounts, automation accounts, application identities, workload identities, app registrations, secrets, certificates, ownership, access scope, credential expiration, and governance risk.

This dashboard is designed to help IAM, security, cloud, DevOps, governance, and audit teams manage identities that are not tied to a human user.

The goal is to answer:

> Which non-human identities exist, who owns them, what access do they have, and are they governed?

---

## Primary Audience

| Audience         | Purpose                                                                |
| ---------------- | ---------------------------------------------------------------------- |
| IAM Teams        | Track non-human identity ownership, access, and governance state.      |
| Security Teams   | Identify risky service accounts, secrets, and workload identities.     |
| Cloud Teams      | Govern application identities and automation identities.               |
| DevOps Teams     | Validate automation account purpose and access scope.                  |
| Governance Teams | Review ownership, expiration, and evidence.                            |
| Auditors         | Confirm that non-human identities are owned, reviewed, and controlled. |

---

## Non-Human Identity Questions

The Non-Human Identity Dashboard should answer:

* Which service accounts exist?
* Which automation identities exist?
* Which app registrations or workload identities exist?
* Who owns each non-human identity?
* What system or process uses the identity?
* What access does the identity have?
* Does the identity have excessive access?
* Are secrets or certificates expiring?
* Are credentials stale or unmanaged?
* Which identities lack owners?
* Which identities require review?
* Which identities create high or critical risk?

---

## Non-Human Identity Dashboard Wireframe

```text id="axpxph"
+--------------------------------------------------------------------------------+
| IdentityOS Non-Human Identity Dashboard                 NHI View: Current       |
+--------------------------------------------------------------------------------+
| Overview | Ownership | Credentials | Access Scope | Drift | Evidence           |
+--------------------------------------------------------------------------------+
| Total NHI | Missing Owner | Expiring Creds | Broad Access | Drift | Critical    |
|    1      |       1       | Future Metric  |    Review    |   1   |    1        |
+--------------------------------------------------------------------------------+
| NHI Overview                         | Ownership and Purpose                   |
|--------------------------------------|-----------------------------------------|
| Service Accounts: 1                  | Owner Assigned: Review                  |
| Automation Identities: Future Metric | Business Purpose: Review                |
| App Identities: Future Metric        | Technical Owner: Review                 |
| Workload Identities: Future Metric   | Application Owner: Review               |
+--------------------------------------------------------------------------------+
| Credential Governance                | Access Scope                            |
|--------------------------------------|-----------------------------------------|
| Secrets Expiring: Future Metric      | Privileged Access: Review               |
| Certificates Expiring: Future Metric | Broad Permissions: Review               |
| Credential Age: Future Metric        | Sensitive App Access: Review            |
| Rotation Required: Future Metric     | Least Privilege Check: Required         |
+--------------------------------------------------------------------------------+
| Drift and Risk                       | Evidence and Reports                    |
|--------------------------------------|-----------------------------------------|
| Missing Owner Drift: 1               | Access Drift Report                     |
| Access Scope Drift: Review           | Risk Score Report                       |
| Credential Drift: Future Metric      | Governance Report                       |
| Critical Risk Findings: 1            | Dashboard Summary                       |
+--------------------------------------------------------------------------------+
```

---

## Top KPI Cards

| KPI Card                   | Purpose                                                                  |
| -------------------------- | ------------------------------------------------------------------------ |
| Total Non-Human Identities | Shows total service accounts, app identities, and automation identities. |
| Missing Owner              | Shows identities without accountable ownership.                          |
| Expiring Credentials       | Shows secrets or certificates approaching expiration.                    |
| Broad Access               | Shows identities with excessive permissions.                             |
| Drift Findings             | Shows non-human identities with governance drift.                        |
| Critical Risk              | Shows urgent non-human identity risk.                                    |

---

## Non-Human Identity Types

| Identity Type                   | Description                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------- |
| Service Account                 | Account used by applications, services, or scheduled tasks.                  |
| Automation Account              | Identity used by scripts, jobs, or automation workflows.                     |
| Application Identity            | Identity tied to an application or app registration.                         |
| Workload Identity               | Identity used by a workload, service, or cloud resource.                     |
| Integration Identity            | Identity used for system-to-system communication.                            |
| Break-Glass Automation Identity | Highly sensitive emergency or automation identity requiring strict controls. |

---

## Ownership and Purpose Panel

Every non-human identity should have clear ownership and purpose.

| Ownership Field   | Purpose                                             |
| ----------------- | --------------------------------------------------- |
| Business Owner    | Person or team accountable for business need.       |
| Technical Owner   | Person or team responsible for technical operation. |
| Application Owner | Owner of the application or workload.               |
| Purpose           | Why the identity exists.                            |
| Environment       | Production, development, test, or sandbox.          |
| Review Owner      | Person or group responsible for recurring review.   |

### Ownership Interpretation

A non-human identity without an owner is difficult to govern.

A strong identity program requires every non-human identity to have:

* Owner
* Purpose
* Application or workload mapping
* Access scope
* Credential lifecycle
* Review cadence
* Retirement process
* Audit evidence

---

## Credential Governance Panel

Non-human identities often use secrets, certificates, keys, or tokens.

| Credential Signal        | Meaning                                          |
| ------------------------ | ------------------------------------------------ |
| Secret Expiration        | Secret is approaching expiration.                |
| Certificate Expiration   | Certificate is approaching expiration.           |
| Credential Age           | Credential may be stale or overdue for rotation. |
| Rotation Required        | Credential should be rotated.                    |
| Unknown Credential Owner | Credential ownership is unclear.                 |
| Long-Lived Credential    | Credential may create persistent risk.           |
| Unused Credential        | Credential may be stale and should be reviewed.  |

---

## Access Scope Panel

Non-human identities should follow least privilege.

| Access Scope Signal          | Meaning                                                       |
| ---------------------------- | ------------------------------------------------------------- |
| Broad Permissions            | Identity may have more access than needed.                    |
| Privileged Access            | Identity has elevated permissions.                            |
| Sensitive Application Access | Identity can access sensitive systems or data.                |
| Cross-System Access          | Identity connects multiple systems.                           |
| Write Permissions            | Identity can modify data or configuration.                    |
| Administrative Access        | Identity can manage users, apps, policies, or infrastructure. |
| Unused Access                | Identity has access not recently used or justified.           |

---

## Non-Human Identity Drift

Non-human identity drift occurs when ownership, purpose, credentials, or access scope no longer match policy.

| Drift Type          | Meaning                                                    |
| ------------------- | ---------------------------------------------------------- |
| Missing Owner Drift | Identity lacks accountable owner.                          |
| Purpose Drift       | Identity purpose is unclear or outdated.                   |
| Access Scope Drift  | Identity has broader access than expected.                 |
| Credential Drift    | Secret or certificate lifecycle is unmanaged.              |
| Privilege Drift     | Identity has elevated permissions that require review.     |
| Application Drift   | Identity is not tied to a current application or workload. |
| Dormancy Drift      | Identity appears unused but still has access.              |

---

## Risk Signals

Non-human identities can become high risk when they are powerful, long-lived, or unmanaged.

| Risk Signal          | Reason                                            |
| -------------------- | ------------------------------------------------- |
| Missing Owner        | No one is accountable for the identity.           |
| Missing Purpose      | Business justification is unclear.                |
| Privileged Access    | Elevated permissions increase impact.             |
| Broad Permissions    | Access may exceed business need.                  |
| Long-Lived Secret    | Credential may remain valid too long.             |
| Expired Credential   | Application or automation failure risk.           |
| Unrotated Credential | Increased exposure risk.                          |
| Dormant Identity     | Unused identity may become hidden attack surface. |
| No Review History    | Governance evidence is missing.                   |

---

## Recommended Remediation

| Condition             | Recommended Action                                     |
| --------------------- | ------------------------------------------------------ |
| Missing owner         | Assign business and technical owner.                   |
| Missing purpose       | Document application, workload, or automation purpose. |
| Broad access          | Reduce permissions to least privilege.                 |
| Privileged access     | Require security review and approval.                  |
| Expiring credential   | Rotate secret or certificate.                          |
| Long-lived credential | Shorten credential lifetime and rotate.                |
| Dormant identity      | Disable or remove after validation.                    |
| Missing review        | Schedule recurring access review.                      |
| Missing evidence      | Generate governance evidence and document decision.    |

---

## Non-Human Identity Detail View

Users should be able to drill into each non-human identity.

| Field              | Purpose                                                                          |
| ------------------ | -------------------------------------------------------------------------------- |
| Identity Name      | Name of the service account, app identity, or workload identity.                 |
| Identity Type      | Service account, automation account, application identity, or workload identity. |
| Owner              | Business or technical owner.                                                     |
| Purpose            | Why the identity exists.                                                         |
| Environment        | Production, development, test, or sandbox.                                       |
| Access Scope       | Systems, roles, or permissions assigned.                                         |
| Credential Status  | Secret or certificate health.                                                    |
| Risk Score         | Calculated risk level.                                                           |
| Drift Status       | Whether drift exists.                                                            |
| Review Status      | Current governance review state.                                                 |
| Recommended Action | Suggested remediation.                                                           |
| Evidence Link      | Related governance, risk, or drift evidence.                                     |

---

## Governance Controls

Non-human identities should include these controls:

| Control             | Purpose                                              |
| ------------------- | ---------------------------------------------------- |
| Owner Required      | Ensures accountability.                              |
| Purpose Required    | Confirms why the identity exists.                    |
| Least Privilege     | Limits access to required permissions.               |
| Credential Rotation | Reduces long-lived credential risk.                  |
| Expiration Tracking | Tracks secrets, certificates, and access expiration. |
| Recurring Review    | Confirms identity is still needed.                   |
| Usage Monitoring    | Identifies dormant or suspicious identities.         |
| Retirement Process  | Removes identities no longer needed.                 |
| Audit Evidence      | Proves ownership, review, and remediation.           |

---

## Filters

The Non-Human Identity Dashboard should support these filters:

| Filter            | Purpose                                                                                                          |
| ----------------- | ---------------------------------------------------------------------------------------------------------------- |
| Identity Type     | Filter by service account, automation account, application identity, workload identity, or integration identity. |
| Owner Status      | Filter by owner assigned or missing owner.                                                                       |
| Credential Status | Filter by valid, expiring, expired, stale, or rotation required.                                                 |
| Risk Level        | Filter by Low, Medium, High, or Critical.                                                                        |
| Access Scope      | Filter by standard, sensitive, broad, or privileged access.                                                      |
| Environment       | Filter by production, development, test, or sandbox.                                                             |
| Drift Type        | Filter by ownership, purpose, credential, access scope, privilege, application, or dormancy drift.               |
| Review Status     | Filter by reviewed, review required, overdue, or remediated.                                                     |

---

## Reports

The Non-Human Identity Dashboard should link to:

| Report              | Purpose                                           |
| ------------------- | ------------------------------------------------- |
| Access Drift Report | Shows non-human identity drift findings.          |
| Risk Score Report   | Shows non-human identity risk factors.            |
| Governance Report   | Shows review and audit requirements.              |
| Dashboard Summary   | Shows dashboard-ready non-human identity metrics. |

---

## Data Sources

The Non-Human Identity Dashboard uses these sample sources:

| Source                                   | Purpose                                       |
| ---------------------------------------- | --------------------------------------------- |
| `examples/sample-identity-events.json`   | Provides non-human identity lifecycle events. |
| `examples/sample-policy-decisions.json`  | Provides governance and policy decisions.     |
| `reports/sample-access-drift-report.md`  | Provides non-human identity drift findings.   |
| `reports/sample-risk-score-report.md`    | Provides risk scoring evidence.               |
| `reports/sample-governance-report.md`    | Provides governance and audit evidence.       |
| `examples/sample-dashboard-metrics.json` | Provides dashboard-ready metrics.             |

---

## Success Criteria

The Non-Human Identity Dashboard is successful when users can quickly see:

* Which non-human identities exist
* Who owns each identity
* What each identity is used for
* Which identities have broad or privileged access
* Which credentials require rotation
* Which identities lack owners
* Which identities require review
* Which identities create high or critical risk
* Which evidence supports governance decisions

---

## Summary

The IdentityOS Non-Human Identity Dashboard turns service accounts, automation identities, and workload identities into visible, governed assets.

It helps organizations reduce hidden identity risk by enforcing ownership, purpose, least privilege, credential governance, and recurring review.

> Non-human identity dashboards turn invisible identities into accountable identities.
