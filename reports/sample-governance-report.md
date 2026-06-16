# IdentityOS Sample Governance Report

Generated: 2026-06-16 14:23:59 UTC

## Executive Summary

This report summarizes sample IdentityOS policy decisions, governance requirements, risk levels, and access actions.

| Metric | Value |
| --- | --- |
| Total Policy Decisions | 7 |
| Pending Approval | 2 |
| Review Required | 2 |
| High Risk Decisions | 2 |
| Critical Risk Decisions | 2 |

## Policy Decision Outcomes

| Policy Result | Count |
| --- | --- |
| Approved | 2 |
| Approved with Review | 1 |
| Pending Approval | 2 |
| Review Required | 2 |

## Risk Distribution

| Risk Level | Count |
| --- | --- |
| Critical | 2 |
| High | 2 |
| Medium | 3 |

## Governance Actions Required

| Decision ID | Event ID | Identity | Policy Result | Approval Required | Review Frequency | Risk Level | Expiration Required |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DEC-JOINER-0001 | EVT-JOINER-0001 | jordan.smith@atlaslegal.example | Approved | False | Quarterly | Medium | False |
| DEC-MOVER-0001 | EVT-MOVER-0001 | morgan.lee@atlaslegal.example | Approved with Review | True | Quarterly | High | Unknown |
| DEC-LEAVER-0001 | EVT-LEAVER-0001 | alex.morgan@atlaslegal.example | Approved | False | Not Applicable | Critical | Unknown |
| DEC-CONTRACTOR-0001 | EVT-CONTRACTOR-0001 | riley.carter.contractor@atlaslegal.example | Pending Approval | True | Monthly | Medium | True |
| DEC-CONTRACTOR-EXP-0001 | EVT-CONTRACTOR-EXP-0001 | riley.carter.contractor@atlaslegal.example | Review Required | True | Monthly | Medium | True |
| DEC-PAM-0001 | EVT-PAM-0001 | casey.nguyen@atlaslegal.example | Pending Approval | True | Monthly | Critical | True |
| DEC-NHI-0001 | EVT-NHI-0001 | svc-document-sync | Review Required | False | Quarterly | High | False |

## Access Remediation Summary

| Decision ID | Event ID | Identity | Access to Remove |
| --- | --- | --- | --- |
| DEC-MOVER-0001 | EVT-MOVER-0001 | morgan.lee@atlaslegal.example | Finance SharePoint, Financial Reporting Portal |
| DEC-LEAVER-0001 | EVT-LEAVER-0001 | alex.morgan@atlaslegal.example | Microsoft 365, Teams, IT SharePoint Workspace, Ticketing System, Endpoint Management Console, Eligible Helpdesk Administrator |
| DEC-CONTRACTOR-EXP-0001 | EVT-CONTRACTOR-EXP-0001 | riley.carter.contractor@atlaslegal.example | Microsoft 365 Limited, Project Workspace |

## Detailed Policy Decisions

### DEC-JOINER-0001

| Field | Value |
| --- | --- |
| Related Event | EVT-JOINER-0001 |
| Event Type | Joiner |
| Identity | jordan.smith@atlaslegal.example |
| Policy Result | Approved |
| Decision Summary | Create new Legal Associate identity and assign standard Legal Associate role package. |
| Access to Grant | Microsoft 365, Teams, Legal SharePoint Workspace, Legal Document Management System, Case Collaboration Workspace |
| Access to Remove | None |
| Controls Required | MFA, Conditional Access, Compliant Device |
| Approval Required | False |
| Review Frequency | Quarterly |
| Risk Level | Medium |
| Expiration Required | False |
| Audit Required | True |
| Audit Reason | Access granted based on Legal Associate role package. |

### DEC-MOVER-0001

| Field | Value |
| --- | --- |
| Related Event | EVT-MOVER-0001 |
| Event Type | Mover |
| Identity | morgan.lee@atlaslegal.example |
| Policy Result | Approved with Review |
| Decision Summary | Remove Finance access and assign Legal Operations access due to department and role change. |
| Access to Grant | Legal Operations Workspace, Legal Document Management System |
| Access to Remove | Finance SharePoint, Financial Reporting Portal |
| Controls Required | Manager Review, Access Drift Check |
| Approval Required | True |
| Review Frequency | Quarterly |
| Risk Level | High |
| Expiration Required | Unknown |
| Audit Required | True |
| Audit Reason | Mover event requires access realignment to new department and job function. |

### DEC-LEAVER-0001

| Field | Value |
| --- | --- |
| Related Event | EVT-LEAVER-0001 |
| Event Type | Leaver |
| Identity | alex.morgan@atlaslegal.example |
| Policy Result | Approved |
| Decision Summary | Disable identity, revoke sessions, remove standard and privileged access, and generate offboarding evidence. |
| Access to Grant | None |
| Access to Remove | Microsoft 365, Teams, IT SharePoint Workspace, Ticketing System, Endpoint Management Console, Eligible Helpdesk Administrator |
| Controls Required | Disable Account, Revoke Sessions, Remove Groups, Remove Privileged Roles, Notify Manager, Notify Security |
| Approval Required | False |
| Review Frequency | Not Applicable |
| Risk Level | Critical |
| Expiration Required | Unknown |
| Audit Required | True |
| Audit Reason | Leaver event requires complete deprovisioning and privileged access removal. |

### DEC-CONTRACTOR-0001

| Field | Value |
| --- | --- |
| Related Event | EVT-CONTRACTOR-0001 |
| Event Type | Contractor_Onboarding |
| Identity | riley.carter.contractor@atlaslegal.example |
| Policy Result | Pending Approval |
| Decision Summary | Create contractor identity with limited access, sponsor approval, MFA, monthly review, and expiration enforcement. |
| Access to Grant | Microsoft 365 Limited, Project Workspace |
| Access to Remove | None |
| Controls Required | Sponsor Approval, MFA, Expiration Date, Monthly Access Review |
| Approval Required | True |
| Review Frequency | Monthly |
| Risk Level | Medium |
| Expiration Required | True |
| Audit Required | True |
| Audit Reason | Contractor identities require sponsorship, expiration, and monthly review. |

### DEC-CONTRACTOR-EXP-0001

| Field | Value |
| --- | --- |
| Related Event | EVT-CONTRACTOR-EXP-0001 |
| Event Type | Contractor_Expiration |
| Identity | riley.carter.contractor@atlaslegal.example |
| Policy Result | Review Required |
| Decision Summary | Trigger renewal review and automatically disable contractor access if sponsor does not approve renewal. |
| Access to Grant | None |
| Access to Remove | Microsoft 365 Limited, Project Workspace |
| Controls Required | Sponsor Renewal Review, Auto-Disable If Not Renewed, Expiration Enforcement |
| Approval Required | True |
| Review Frequency | Monthly |
| Risk Level | Medium |
| Expiration Required | True |
| Audit Required | True |
| Audit Reason | Contractor access must expire unless renewed by sponsor. |

### DEC-PAM-0001

| Field | Value |
| --- | --- |
| Related Event | EVT-PAM-0001 |
| Event Type | Privileged_Access_Request |
| Identity | casey.nguyen@atlaslegal.example |
| Policy Result | Pending Approval |
| Decision Summary | Allow eligible Security Reader activation for two hours with MFA, justification, approval, and audit logging. |
| Access to Grant | Eligible Security Reader |
| Access to Remove | None |
| Controls Required | MFA, Justification, Approval, Time Limit, Audit Logging |
| Approval Required | True |
| Review Frequency | Monthly |
| Risk Level | Critical |
| Expiration Required | True |
| Audit Required | True |
| Audit Reason | Privileged access requires approval, justification, time limit, and logging. |

### DEC-NHI-0001

| Field | Value |
| --- | --- |
| Related Event | EVT-NHI-0001 |
| Event Type | Non_Human_Identity_Review |
| Identity | svc-document-sync |
| Policy Result | Review Required |
| Decision Summary | Review service account ownership, business purpose, access scope, and credential rotation status. |
| Access to Grant | None |
| Access to Remove | None |
| Controls Required | Owner Verification, Business Purpose Verification, Access Scope Review, Credential Rotation Review |
| Approval Required | False |
| Review Frequency | Quarterly |
| Risk Level | High |
| Expiration Required | False |
| Audit Required | True |
| Audit Reason | Non-human identities require ownership, scope validation, and credential governance. |

## Summary

This sample report demonstrates how IdentityOS can turn identity policy decisions into governance visibility.

The same pattern could be extended to support audit reporting, executive dashboards, access review evidence, privileged access reporting, and identity risk analytics.

> IdentityOS turns access decisions into governance evidence.
