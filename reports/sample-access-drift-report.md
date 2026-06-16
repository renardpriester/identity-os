# IdentityOS Sample Access Drift Report

Generated: 2026-06-16 15:01:58 UTC

## Executive Summary

This report summarizes sample access drift detected from IdentityOS lifecycle events and policy decisions.

| Metric | Value |
| --- | --- |
| Total Evaluated Decisions | 7 |
| Drift Detected | 4 |
| High Severity Drift | 2 |
| Critical Severity Drift | 2 |

## Drift Summary

| Decision ID | Event ID | Event Type | Identity | Drift Type | Severity | Recommended Remediation |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-LEAVER-0001 | EVT-LEAVER-0001 | Leaver | alex.morgan@atlaslegal.example | Leaver Drift | Critical | Disable identity, revoke sessions, remove all access, and notify security if privileged access exists. |
| DEC-CONTRACTOR-EXP-0001 | EVT-CONTRACTOR-EXP-0001 | Contractor_Expiration | riley.carter.contractor@atlaslegal.example | Contractor Drift | Critical | Disable contractor access unless sponsor renewal is approved. |
| DEC-MOVER-0001 | EVT-MOVER-0001 | Mover | morgan.lee@atlaslegal.example | Department Drift | High | Remove access from the previous department and create audit evidence. |
| DEC-NHI-0001 | EVT-NHI-0001 | Non_Human_Identity_Review | svc-document-sync | Non-Human Identity Drift | High | Validate owner, business purpose, access scope, and credential governance. |
| DEC-JOINER-0001 | EVT-JOINER-0001 | Joiner | jordan.smith@atlaslegal.example | No Drift | None | No remediation required. |
| DEC-CONTRACTOR-0001 | EVT-CONTRACTOR-0001 | Contractor_Onboarding | riley.carter.contractor@atlaslegal.example | No Drift | None | No remediation required. |
| DEC-PAM-0001 | EVT-PAM-0001 | Privileged_Access_Request | casey.nguyen@atlaslegal.example | No Drift | None | No remediation required. |

## Detailed Drift Findings

### DEC-LEAVER-0001 - alex.morgan@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-LEAVER-0001 |
| Event Type | Leaver |
| Drift Detected | True |
| Drift Type | Leaver Drift |
| Drift Severity | Critical |
| Expected Access | None |
| Actual Access | Microsoft 365, Teams, IT SharePoint Workspace, Ticketing System, Endpoint Management Console, Eligible Helpdesk Administrator |
| Excess Access | Microsoft 365, Teams, IT SharePoint Workspace, Ticketing System, Endpoint Management Console, Eligible Helpdesk Administrator |
| Controls Required | Disable Account, Revoke Sessions, Remove Groups, Remove Privileged Roles, Notify Manager, Notify Security |
| Drift Reason | Leaver event includes access that must be removed during offboarding. |
| Recommended Remediation | Disable identity, revoke sessions, remove all access, and notify security if privileged access exists. |

### DEC-CONTRACTOR-EXP-0001 - riley.carter.contractor@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-CONTRACTOR-EXP-0001 |
| Event Type | Contractor_Expiration |
| Drift Detected | True |
| Drift Type | Contractor Drift |
| Drift Severity | Critical |
| Expected Access | None |
| Actual Access | Microsoft 365 Limited, Project Workspace |
| Excess Access | Microsoft 365 Limited, Project Workspace |
| Controls Required | Sponsor Renewal Review, Auto-Disable If Not Renewed, Expiration Enforcement |
| Drift Reason | Contractor access is expiring or expired and should not remain active without renewal. |
| Recommended Remediation | Disable contractor access unless sponsor renewal is approved. |

### DEC-MOVER-0001 - morgan.lee@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-MOVER-0001 |
| Event Type | Mover |
| Drift Detected | True |
| Drift Type | Department Drift |
| Drift Severity | High |
| Expected Access | Legal Operations Workspace, Legal Document Management System |
| Actual Access | Legal Operations Workspace, Legal Document Management System, Finance SharePoint, Financial Reporting Portal |
| Excess Access | Finance SharePoint, Financial Reporting Portal |
| Controls Required | Manager Review, Access Drift Check |
| Drift Reason | Mover event includes access from the previous role or department that should be removed. |
| Recommended Remediation | Remove access from the previous department and create audit evidence. |

### DEC-NHI-0001 - svc-document-sync

| Field | Value |
| --- | --- |
| Event ID | EVT-NHI-0001 |
| Event Type | Non_Human_Identity_Review |
| Drift Detected | True |
| Drift Type | Non-Human Identity Drift |
| Drift Severity | High |
| Expected Access | None |
| Actual Access | None |
| Excess Access | None |
| Controls Required | Owner Verification, Business Purpose Verification, Access Scope Review, Credential Rotation Review |
| Drift Reason | Non-human identity requires owner, purpose, scope, and credential governance review. |
| Recommended Remediation | Validate owner, business purpose, access scope, and credential governance. |

### DEC-JOINER-0001 - jordan.smith@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-JOINER-0001 |
| Event Type | Joiner |
| Drift Detected | False |
| Drift Type | No Drift |
| Drift Severity | None |
| Expected Access | Microsoft 365, Teams, Legal SharePoint Workspace, Legal Document Management System, Case Collaboration Workspace |
| Actual Access | Microsoft 365, Teams, Legal SharePoint Workspace, Legal Document Management System, Case Collaboration Workspace |
| Excess Access | None |
| Controls Required | MFA, Conditional Access, Compliant Device |
| Drift Reason | Actual access appears aligned with the sample policy decision. |
| Recommended Remediation | No remediation required. |

### DEC-CONTRACTOR-0001 - riley.carter.contractor@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-CONTRACTOR-0001 |
| Event Type | Contractor_Onboarding |
| Drift Detected | False |
| Drift Type | No Drift |
| Drift Severity | None |
| Expected Access | Microsoft 365 Limited, Project Workspace |
| Actual Access | Microsoft 365 Limited, Project Workspace |
| Excess Access | None |
| Controls Required | Sponsor Approval, MFA, Expiration Date, Monthly Access Review |
| Drift Reason | Actual access appears aligned with the sample policy decision. |
| Recommended Remediation | No remediation required. |

### DEC-PAM-0001 - casey.nguyen@atlaslegal.example

| Field | Value |
| --- | --- |
| Event ID | EVT-PAM-0001 |
| Event Type | Privileged_Access_Request |
| Drift Detected | False |
| Drift Type | No Drift |
| Drift Severity | None |
| Expected Access | Eligible Security Reader |
| Actual Access | Eligible Security Reader |
| Excess Access | None |
| Controls Required | MFA, Justification, Approval, Time Limit, Audit Logging |
| Drift Reason | Actual access appears aligned with the sample policy decision. |
| Recommended Remediation | No remediation required. |

## Summary

This report demonstrates how IdentityOS can identify access that no longer aligns with expected access.

Access drift detection helps reduce privilege creep, stale access, excessive permissions, and unmanaged access risk.

> Access drift is how yesterday’s permissions become tomorrow’s risk.
