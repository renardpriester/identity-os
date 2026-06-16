# IdentityOS Risk Scoring Model

## Purpose

The IdentityOS Risk Scoring Model defines how identity risk can be evaluated using business context, access sensitivity, governance status, lifecycle state, privileged access, exception status, and audit signals.

The purpose of this model is to help IdentityOS identify identities, access decisions, and governance conditions that may require additional review, approval, remediation, or security attention.

Identity risk should not be based on one signal alone. It should be calculated from multiple factors that describe how much access exists, how sensitive that access is, whether it is governed, and whether it still aligns with business need.

---

## Core Concept

IdentityOS assigns a risk score to identity-related decisions.

The score ranges from:

```text
0 to 100
```

A higher score means greater identity risk.

Risk scoring helps IdentityOS answer questions such as:

* Is this identity over-permissioned?
* Is this access privileged?
* Is this access stale?
* Is this access outside the standard role model?
* Is the user a contractor or vendor?
* Is the access expired?
* Is the access review overdue?
* Is there an approved exception?
* Is the identity missing an owner?
* Does this access create a separation of duties issue?

---

## Risk Levels

| Risk Score | Risk Level | Meaning                                                                                                              |
| ---------- | ---------- | -------------------------------------------------------------------------------------------------------------------- |
| 0-20       | Low        | Standard access with minimal risk indicators.                                                                        |
| 21-40      | Medium     | Normal business access with some governance or sensitivity considerations.                                           |
| 41-70      | High       | Sensitive access, stale access, exception-based access, or missing governance signals.                               |
| 71-100     | Critical   | Privileged access, major governance gaps, expired access, separation of duties conflict, or unmanaged identity risk. |

Risk scores should be capped at 100.

---

## Risk Factors

IdentityOS can assign risk points based on identity and access conditions.

| Risk Factor                   | Points | Reason                                                                                  |
| ----------------------------- | -----: | --------------------------------------------------------------------------------------- |
| Standard business access      |      5 | Normal baseline access still carries minimal risk.                                      |
| Sensitive application access  |     20 | Access to sensitive data or business-critical systems increases risk.                   |
| Privileged access             |     30 | Elevated access can impact security posture and must be tightly governed.               |
| Permanent privileged access   |     35 | Standing privilege creates greater risk than eligible or time-bound access.             |
| Contractor identity           |     15 | External or temporary identities require stronger governance.                           |
| Vendor identity               |     20 | Vendor access often involves external risk and sponsor dependency.                      |
| Non-human identity            |     20 | Service accounts and automation identities require ownership and credential governance. |
| Missing owner                 |     25 | Access or identity without an owner cannot be properly governed.                        |
| Expired access still active   |     30 | Access that should have expired represents immediate governance failure.                |
| Overdue access review         |     20 | Access has not been recently validated.                                                 |
| Exception-based access        |     20 | Access outside standard policy requires documented justification.                       |
| Exception without expiration  |     30 | Exceptions without expiration can become permanent risk.                                |
| Access outside role package   |     20 | Access does not align with expected business role.                                      |
| Access drift detected         |     25 | Current access has moved away from intended access.                                     |
| Separation of duties conflict |     35 | Conflicting access can create fraud, abuse, or compliance risk.                         |
| Leaver with active access     |     40 | Former workers with active access represent critical risk.                              |
| Privileged leaver access      |     50 | Former workers with privileged access require urgent remediation.                       |
| Stale access                  |     15 | Access has not been used or reviewed within expected timeframe.                         |
| No MFA requirement            |     25 | Lack of strong authentication increases account compromise risk.                        |
| No audit evidence             |     25 | Access cannot be properly explained or proven.                                          |

---

## Risk Score Formula

IdentityOS can calculate risk using a simple additive model.

```text
Risk Score = Sum of Applicable Risk Factors
```

The score should be capped at 100.

```text
If Risk Score > 100, set Risk Score = 100
```

Example:

```text
Contractor Identity: 15
Sensitive Application Access: 20
Exception-Based Access: 20
Exception Without Expiration: 30

Total Risk Score: 85
Risk Level: Critical
```

---

## Risk Level Logic

IdentityOS should convert the numeric score into a risk level.

```text
0-20     = Low
21-40    = Medium
41-70    = High
71-100   = Critical
```

This allows reports, dashboards, and governance workflows to group access decisions by risk severity.

---

## Example Scenario: Standard Employee Access

```text
Identity Type: Employee
Access Type: Standard business access
Governance Status: Reviewed
MFA Required: Yes
Exception: No
Privileged Access: No
```

Risk factors:

```text
Standard business access: 5
```

Result:

```text
Risk Score: 5
Risk Level: Low
```

---

## Example Scenario: Contractor with Sensitive Access

```text
Identity Type: Contractor
Access Type: Sensitive project workspace
Governance Status: Active
MFA Required: Yes
Expiration Date: Present
Exception: No
Privileged Access: No
```

Risk factors:

```text
Contractor identity: 15
Sensitive application access: 20
```

Result:

```text
Risk Score: 35
Risk Level: Medium
```

---

## Example Scenario: Mover with Access Drift

```text
Identity Type: Employee
Previous Department: Finance
New Department: Legal Operations
Current Access: Finance Reporting Portal
Expected Access: Legal Operations Workspace
Access Drift: Yes
```

Risk factors:

```text
Sensitive application access: 20
Access outside role package: 20
Access drift detected: 25
```

Result:

```text
Risk Score: 65
Risk Level: High
```

---

## Example Scenario: Privileged Leaver

```text
Identity Type: Former Employee
Lifecycle Event: Leaver
Account Status: Active
Privileged Access: Yes
Sessions Active: Yes
```

Risk factors:

```text
Leaver with active access: 40
Privileged leaver access: 50
Privileged access: 30
```

Raw score:

```text
120
```

Capped result:

```text
Risk Score: 100
Risk Level: Critical
```

---

## Example Scenario: Non-Human Identity Without Owner

```text
Identity Type: Service Account
Owner: Missing
Credential Rotation: Unknown
Access Scope: Sensitive API
```

Risk factors:

```text
Non-human identity: 20
Missing owner: 25
Sensitive application access: 20
No audit evidence: 25
```

Result:

```text
Risk Score: 90
Risk Level: Critical
```

---

## Governance Actions by Risk Level

IdentityOS should recommend governance actions based on risk level.

| Risk Level | Recommended Action                                                                             |
| ---------- | ---------------------------------------------------------------------------------------------- |
| Low        | Retain access and follow normal review schedule.                                               |
| Medium     | Retain access with standard governance controls.                                               |
| High       | Trigger review, validate owner, confirm business justification, and check for access drift.    |
| Critical   | Escalate for urgent review, require remediation, notify security, and generate audit evidence. |

---

## Risk Decision Output

A risk scoring decision should produce a record that includes:

* Identity
* Event ID
* Decision ID
* Risk score
* Risk level
* Risk factors
* Access involved
* Governance action
* Remediation recommendation
* Audit reason
* Timestamp

Example output:

```json
{
  "identity": "morgan.lee@atlaslegal.example",
  "event_id": "EVT-MOVER-0001",
  "decision_id": "DEC-MOVER-0001",
  "risk_score": 65,
  "risk_level": "High",
  "risk_factors": [
    "Sensitive application access",
    "Access outside role package",
    "Access drift detected"
  ],
  "recommended_action": "Trigger manager review and remove stale access",
  "audit_reason": "Mover event created access drift risk"
}
```

---

## Relationship to IdentityOS Components

The Risk Scoring Model supports multiple IdentityOS components.

```text
Identity Events
      ↓
Policy Engine
      ↓
Risk Scoring Model
      ↓
Governance Engine
      ↓
Remediation Workflow
      ↓
Audit Evidence
      ↓
Analytics Engine
```

Risk scoring helps the Policy Engine prioritize decisions and helps the Governance Engine determine the correct level of review.

---

## Future Enhancements

Future versions of the Risk Scoring Model may include:

* Weighted scoring by application criticality
* Time-based risk decay
* Identity behavior analytics
* Sign-in risk signals
* Device compliance signals
* Data sensitivity labels
* Access usage frequency
* Privileged activation history
* Risk score trend analysis
* Dashboard-ready risk summaries
* Integration with Microsoft Entra ID risk signals
* Integration with SIEM alerts

---

## Success Criteria

The Risk Scoring Model is successful when:

* Risk scores are explainable.
* Risk factors are transparent.
* High-risk identities are easy to identify.
* Critical-risk access is escalated.
* Stale access can be detected.
* Privilege creep becomes visible.
* Exceptions are governed.
* Non-human identity risk is measurable.
* Reports and dashboards can show identity risk clearly.
* Governance actions are prioritized by risk.

---

## Summary

The IdentityOS Risk Scoring Model adds intelligence to identity governance.

It helps IdentityOS move beyond simple access decisions and toward risk-aware identity operations.

> Identity risk should be measurable, explainable, and actionable.
