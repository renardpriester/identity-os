# IdentityOS Sample Risk Score Report

Generated: 2026-06-16 14:40:15 UTC

## Executive Summary

This report summarizes sample IdentityOS risk scores calculated from identity events and policy decisions.

| Metric | Value |
| --- | --- |
| Total Scored Decisions | 7 |
| Low Risk | 2 |
| Medium Risk | 1 |
| High Risk | 3 |
| Critical Risk | 1 |

## Risk Score Summary

| Decision ID | Event ID | Event Type | Identity | Risk Score | Risk Level | Recommended Action |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-JOINER-0001 | EVT-JOINER-0001 | Joiner | jordan.smith@atlaslegal.example | 25 | Medium | Retain access with standard governance controls. |
| DEC-MOVER-0001 | EVT-MOVER-0001 | Mover | morgan.lee@atlaslegal.example | 70 | High | Trigger review, validate owner, confirm business need, and check for access drift. |
| DEC-LEAVER-0001 | EVT-LEAVER-0001 | Leaver | alex.morgan@atlaslegal.example | 100 | Critical | Escalate for urgent review, require remediation, notify security if needed, and generate audit evidence. |
| DEC-CONTRACTOR-0001 | EVT-CONTRACTOR-0001 | Contractor_Onboarding | riley.carter.contractor@atlaslegal.example | 20 | Low | Retain access and follow normal review schedule. |
| DEC-CONTRACTOR-EXP-0001 | EVT-CONTRACTOR-EXP-0001 | Contractor_Expiration | riley.carter.contractor@atlaslegal.example | 45 | High | Trigger review, validate owner, confirm business need, and check for access drift. |
| DEC-PAM-0001 | EVT-PAM-0001 | Privileged_Access_Request | casey.nguyen@atlaslegal.example | 55 | High | Trigger review, validate owner, confirm business need, and check for access drift. |
| DEC-NHI-0001 | EVT-NHI-0001 | Non_Human_Identity_Review | svc-document-sync | 20 | Low | Retain access and follow normal review schedule. |

## Detailed Risk Factors

### DEC-JOINER-0001 - jordan.smith@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-JOINER-0001 |
| Event Type | Joiner |
| Policy Result | Approved |
| Risk Score | 25 |
| Risk Level | Medium |
| Recommended Action | Retain access with standard governance controls. |

#### Risk Factors

| Risk Factor | Points | Reason |
| --- | --- | --- |
| Standard business access | 5 | Access is being granted and should be tracked. |
| Sensitive application access | 20 | Access involves sensitive or business-critical systems. |

### DEC-MOVER-0001 - morgan.lee@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-MOVER-0001 |
| Event Type | Mover |
| Policy Result | Approved with Review |
| Risk Score | 70 |
| Risk Level | High |
| Recommended Action | Trigger review, validate owner, confirm business need, and check for access drift. |

#### Risk Factors

| Risk Factor | Points | Reason |
| --- | --- | --- |
| Standard business access | 5 | Access is being granted and should be tracked. |
| Sensitive application access | 20 | Access involves sensitive or business-critical systems. |
| Access drift detected | 25 | Mover event includes access that should be removed from the previous role. |
| Access outside role package | 20 | Current access does not fully align with the new role. |

### DEC-LEAVER-0001 - alex.morgan@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-LEAVER-0001 |
| Event Type | Leaver |
| Policy Result | Approved |
| Risk Score | 100 |
| Risk Level | Critical |
| Recommended Action | Escalate for urgent review, require remediation, notify security if needed, and generate audit evidence. |

#### Risk Factors

| Risk Factor | Points | Reason |
| --- | --- | --- |
| Sensitive application access | 20 | Access involves sensitive or business-critical systems. |
| Privileged access | 30 | Access includes elevated or security-relevant permissions. |
| Leaver with active access | 40 | Leaver event requires complete access removal. |
| Privileged leaver access | 50 | Leaver event includes privileged or security-relevant access removal. |

### DEC-CONTRACTOR-0001 - riley.carter.contractor@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-CONTRACTOR-0001 |
| Event Type | Contractor_Onboarding |
| Policy Result | Pending Approval |
| Risk Score | 20 |
| Risk Level | Low |
| Recommended Action | Retain access and follow normal review schedule. |

#### Risk Factors

| Risk Factor | Points | Reason |
| --- | --- | --- |
| Standard business access | 5 | Access is being granted and should be tracked. |
| Contractor identity | 15 | Contractor identities require sponsorship, expiration, and review. |

### DEC-CONTRACTOR-EXP-0001 - riley.carter.contractor@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-CONTRACTOR-EXP-0001 |
| Event Type | Contractor_Expiration |
| Policy Result | Review Required |
| Risk Score | 45 |
| Risk Level | High |
| Recommended Action | Trigger review, validate owner, confirm business need, and check for access drift. |

#### Risk Factors

| Risk Factor | Points | Reason |
| --- | --- | --- |
| Contractor identity | 15 | Contractor identities require sponsorship, expiration, and review. |
| Expired or expiring access | 30 | Contractor access requires renewal or removal at expiration. |

### DEC-PAM-0001 - casey.nguyen@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-PAM-0001 |
| Event Type | Privileged_Access_Request |
| Policy Result | Pending Approval |
| Risk Score | 55 |
| Risk Level | High |
| Recommended Action | Trigger review, validate owner, confirm business need, and check for access drift. |

#### Risk Factors

| Risk Factor | Points | Reason |
| --- | --- | --- |
| Standard business access | 5 | Access is being granted and should be tracked. |
| Sensitive application access | 20 | Access involves sensitive or business-critical systems. |
| Privileged access | 30 | Access includes elevated or security-relevant permissions. |

### DEC-NHI-0001 - svc-document-sync

| Field | Value |
| --- | --- |
| Event ID | EVT-NHI-0001 |
| Event Type | Non_Human_Identity_Review |
| Policy Result | Review Required |
| Risk Score | 20 |
| Risk Level | Low |
| Recommended Action | Retain access and follow normal review schedule. |

#### Risk Factors

| Risk Factor | Points | Reason |
| --- | --- | --- |
| Non-human identity | 20 | Service accounts and automation identities require ownership and credential governance. |

## Summary

This report demonstrates how IdentityOS can calculate identity risk from lifecycle events, access decisions, governance conditions, and audit signals.

Risk scoring helps prioritize review, remediation, escalation, and reporting.

> Identity risk should be measurable, explainable, and actionable.
