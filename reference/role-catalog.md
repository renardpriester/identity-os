# IdentityOS Role Catalog

## Purpose

The Role Catalog defines standard business roles and the access packages associated with each role.

In IdentityOS, access should not be assigned randomly, manually, or only through individual tickets. Access should be based on business context, job function, worker type, risk level, and governance requirements.

The Role Catalog helps translate business roles into access decisions.

---

## Role Catalog Philosophy

A mature identity program should be able to answer:

* What access should this role receive by default?
* What access requires approval?
* What access is privileged?
* What access should expire?
* What access should be reviewed?
* Who owns the access package?
* What evidence exists for the decision?

The Role Catalog supports consistent, explainable, and auditable access decisions.

---

## Role Package Model

Each role package should include the following fields:

| Field               | Description                                                     |
| ------------------- | --------------------------------------------------------------- |
| Role Name           | Business role or job function.                                  |
| Department          | Department or business unit.                                    |
| Worker Type         | Employee, contractor, vendor, intern, or service identity.      |
| Baseline Access     | Standard access required for the role.                          |
| Sensitive Access    | Access to sensitive systems or data.                            |
| Privileged Access   | Administrative or elevated access.                              |
| Approval Required   | Whether approval is needed before access is granted.            |
| Access Owner        | Business or technical owner responsible for the access package. |
| Review Frequency    | How often access should be reviewed.                            |
| Expiration Required | Whether access should expire automatically.                     |
| Risk Level          | Low, Medium, High, or Critical.                                 |

---

## Sample Role Package Template

```yaml id="6h6wz1"
role_package:
  role_name: Example Role
  department: Example Department
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - Department SharePoint
  sensitive_access:
    - None
  privileged_access:
    - None
  approval_required: false
  access_owner: Department Manager
  review_frequency: Quarterly
  expiration_required: false
  risk_level: Low
```

---

## Reference Enterprise

This role catalog is modeled for **Atlas Legal Group**, a fictional global professional services organization.

Atlas Legal Group includes:

* Legal teams
* Human Resources
* Finance
* Information Technology
* Security
* Executives
* Contractors
* Vendors
* Privileged administrators

This fictional model allows IdentityOS to demonstrate real enterprise identity patterns without referencing proprietary employer environments.

---

## Standard Role Packages

## 1. Legal Associate

```yaml id="2rjdrn"
role_package:
  role_name: Legal Associate
  department: Legal
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - Legal SharePoint Workspace
    - Legal Document Management System
    - Case Collaboration Workspace
  sensitive_access:
    - Client Matter Documents
  privileged_access:
    - None
  approval_required: false
  access_owner: Legal Operations
  review_frequency: Quarterly
  expiration_required: false
  risk_level: Medium
```

### Notes

Legal Associates require access to legal collaboration and document systems. Access should be limited to matters, teams, and client workspaces aligned to their assignments.

---

## 2. Partner

```yaml id="ovsj9o"
role_package:
  role_name: Partner
  department: Legal
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - Legal SharePoint Workspace
    - Legal Document Management System
    - Case Collaboration Workspace
    - Client Relationship Workspace
  sensitive_access:
    - Client Matter Documents
    - Business Development Reports
  privileged_access:
    - None
  approval_required: false
  access_owner: Legal Operations
  review_frequency: Quarterly
  expiration_required: false
  risk_level: High
```

### Notes

Partners may require broader visibility into client matters and business development information. Their access should still remain scoped to business need.

---

## 3. Paralegal

```yaml id="sotw63"
role_package:
  role_name: Paralegal
  department: Legal
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - Legal SharePoint Workspace
    - Legal Document Management System
    - Case Support Workspace
  sensitive_access:
    - Client Matter Documents
  privileged_access:
    - None
  approval_required: false
  access_owner: Legal Operations
  review_frequency: Quarterly
  expiration_required: false
  risk_level: Medium
```

### Notes

Paralegal access should support case preparation, document review, filing support, and matter collaboration.

---

## 4. HR Specialist

```yaml id="exckgu"
role_package:
  role_name: HR Specialist
  department: Human Resources
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - HR SharePoint Workspace
    - HRIS Basic User
  sensitive_access:
    - Employee Records
    - HR Case Files
  privileged_access:
    - None
  approval_required: true
  access_owner: HR Operations
  review_frequency: Quarterly
  expiration_required: false
  risk_level: High
```

### Notes

HR roles require stronger governance because they may access sensitive employee information.

---

## 5. Finance Analyst

```yaml id="j13qgx"
role_package:
  role_name: Finance Analyst
  department: Finance
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - Finance SharePoint Workspace
    - Financial Reporting Portal
  sensitive_access:
    - Financial Reports
    - Budget Data
  privileged_access:
    - None
  approval_required: true
  access_owner: Finance Operations
  review_frequency: Quarterly
  expiration_required: false
  risk_level: High
```

### Notes

Finance roles require governance due to access to financial reporting, budgeting, and business-sensitive data.

---

## 6. IT Support Engineer

```yaml id="x17u4t"
role_package:
  role_name: IT Support Engineer
  department: Information Technology
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - IT SharePoint Workspace
    - Ticketing System
    - Endpoint Management Console
  sensitive_access:
    - Device Inventory
    - Support Tickets
  privileged_access:
    - Eligible Helpdesk Administrator
  approval_required: true
  access_owner: IT Operations
  review_frequency: Monthly
  expiration_required: false
  risk_level: High
```

### Notes

IT support access should be governed carefully because support roles may interact with user accounts, devices, tickets, and endpoint management tools.

Privileged access should be eligible or time-bound where possible.

---

## 7. Security Analyst

```yaml id="2y5ipq"
role_package:
  role_name: Security Analyst
  department: Security
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - Security SharePoint Workspace
    - SIEM Portal
    - Identity Monitoring Dashboard
  sensitive_access:
    - Security Alerts
    - Audit Logs
    - Sign-in Logs
  privileged_access:
    - Eligible Security Reader
  approval_required: true
  access_owner: Security Operations
  review_frequency: Monthly
  expiration_required: false
  risk_level: High
```

### Notes

Security Analysts need access to security telemetry and identity monitoring tools. Privileged or sensitive access should be reviewed frequently.

---

## 8. Executive

```yaml id="o80gld"
role_package:
  role_name: Executive
  department: Executive Leadership
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - Executive SharePoint Workspace
    - Leadership Reporting Portal
  sensitive_access:
    - Executive Communications
    - Strategic Planning Documents
    - Board Materials
  privileged_access:
    - None
  approval_required: true
  access_owner: Executive Operations
  review_frequency: Quarterly
  expiration_required: false
  risk_level: Critical
```

### Notes

Executives are high-value identities and should be protected with strong Conditional Access, MFA, risk monitoring, and device compliance controls.

---

## 9. Contractor

```yaml id="xumtl9"
role_package:
  role_name: Contractor
  department: Assigned Department
  worker_type: Contractor
  baseline_access:
    - Microsoft 365 Limited
    - Teams Guest or Limited Workspace
    - Project Workspace
  sensitive_access:
    - Based on approved scope
  privileged_access:
    - None
  approval_required: true
  access_owner: Sponsoring Manager
  review_frequency: Monthly
  expiration_required: true
  risk_level: Medium
```

### Notes

Contractor access should always include a sponsor, end date, limited scope, and expiration policy.

---

## 10. Vendor

```yaml id="lf7dpg"
role_package:
  role_name: Vendor
  department: External
  worker_type: Vendor
  baseline_access:
    - Approved Vendor Portal
    - Limited Collaboration Workspace
  sensitive_access:
    - Based on contract scope
  privileged_access:
    - None
  approval_required: true
  access_owner: Business Sponsor
  review_frequency: Monthly
  expiration_required: true
  risk_level: High
```

### Notes

Vendor access should be limited, monitored, approved, and reviewed regularly. Vendor identities should never remain active without a business sponsor.

---

## 11. Privileged Administrator

```yaml id="neczfu"
role_package:
  role_name: Privileged Administrator
  department: Information Technology or Security
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - IT or Security Workspace
  sensitive_access:
    - Administrative Consoles
    - Identity Logs
    - Security Logs
  privileged_access:
    - Eligible User Administrator
    - Eligible Security Administrator
    - Eligible Application Administrator
  approval_required: true
  access_owner: Identity and Security Leadership
  review_frequency: Monthly
  expiration_required: false
  risk_level: Critical
```

### Notes

Privileged administrator access should be eligible, time-bound, approved, justified, logged, and reviewed frequently.

---

## Role Catalog Governance Rules

The Role Catalog should follow these governance rules:

1. Every role package must have an owner.
2. Every role package must have a review frequency.
3. Sensitive access must require approval or defined ownership.
4. Privileged access must be reviewed more frequently than standard access.
5. Contractor and vendor access must include an expiration date.
6. Role packages should be reviewed when business responsibilities change.
7. Exceptions should be documented outside the standard role package.
8. Access should be removed when it no longer aligns with the role.
9. Role packages should be written in business-friendly language.
10. Technical group names should map clearly to business access outcomes.

---

## Access Risk Levels

| Risk Level | Description                              | Example                        |
| ---------- | ---------------------------------------- | ------------------------------ |
| Low        | Standard productivity access             | Microsoft 365 baseline         |
| Medium     | Department-specific access               | Legal or project workspace     |
| High       | Sensitive business data                  | HR, Finance, Security logs     |
| Critical   | Administrative or executive-level access | Privileged administrator roles |

---

## Role Catalog Success Criteria

The Role Catalog is successful when:

* Access is easier to understand.
* Access is easier to assign.
* Access is easier to review.
* New hires receive accurate baseline access.
* Role changes remove outdated access.
* Sensitive access is governed.
* Privileged access is controlled.
* Contractors and vendors have expiration dates.
* Managers understand what they are approving.
* Auditors can trace access to business role and policy.

---

## Summary

The Role Catalog is the bridge between business roles and technical access.

It allows IdentityOS to make consistent, explainable, and auditable access decisions based on business context.

> A strong Role Catalog turns access from guesswork into architecture.
