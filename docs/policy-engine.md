# IdentityOS Policy Engine

## Purpose

The Policy Engine is the decision-making layer of IdentityOS.

It determines what access should be granted, removed, reviewed, approved, denied, or escalated based on business context, identity attributes, governance requirements, and security policy.

The Policy Engine ensures that access decisions are not random, inconsistent, or based only on manual judgment. Instead, access decisions are driven by defined rules, role models, attributes, risk signals, and business intent.

If the Lifecycle Engine answers, “What happened?”
The Policy Engine answers, “What should happen next?”

---

## Core Responsibility

The Policy Engine is responsible for translating identity context into access outcomes.

It evaluates:

* Who the identity is
* What role the identity performs
* Where the identity works
* What department the identity belongs to
* What systems the identity needs
* What access is allowed
* What access requires approval
* What access should expire
* What access must be reviewed
* What access violates policy

The Policy Engine is the brain of IdentityOS.

---

## Policy Engine Operating Model

The Policy Engine follows this model:

```text id="iz35zu"
Identity Attributes
        ↓
Business Context
        ↓
Policy Rules
        ↓
Role / Access Mapping
        ↓
Access Decision
        ↓
Governance Requirement
        ↓
Provisioning Action
```

The Policy Engine does not directly create accounts or assign groups. Instead, it produces decisions that the Provisioning Engine, Governance Engine, and Automation Engine can execute.

---

## Policy Inputs

The Policy Engine uses several types of input data.

### Identity Attributes

Identity attributes describe the person or identity.

Examples:

* First name
* Last name
* Employee ID
* Worker type
* Employment status
* Department
* Job title
* Location
* Manager
* Business unit
* Cost center
* Start date
* End date
* Risk classification

### Access Attributes

Access attributes describe the permission or resource.

Examples:

* Application name
* Group name
* Role name
* Permission level
* Data sensitivity
* Access owner
* Review frequency
* Approval requirement
* Expiration requirement
* Privileged status

### Governance Attributes

Governance attributes define oversight requirements.

Examples:

* Approver
* Reviewer
* Access owner
* Review cadence
* Exception owner
* Expiration date
* Risk level
* Compliance requirement
* Audit evidence requirement

### Risk Attributes

Risk attributes help determine whether additional controls are required.

Examples:

* Privileged access
* High-risk application
* Sensitive data access
* External user
* Contractor status
* Vendor status
* Unusual location
* Risky sign-in
* Administrative role
* Separation of duties conflict

---

## Policy Outputs

The Policy Engine can produce several types of decisions.

| Decision Type | Description                                      |
| ------------- | ------------------------------------------------ |
| Grant         | Access should be assigned.                       |
| Remove        | Access should be removed.                        |
| Retain        | Access should remain unchanged.                  |
| Review        | Access requires manager or owner review.         |
| Approve       | Access requires approval before assignment.      |
| Deny          | Access should not be granted.                    |
| Expire        | Access should be removed after a defined period. |
| Escalate      | Access requires higher-level review.             |
| Flag          | Access should be marked as risk or exception.    |

The Policy Engine should always produce an explainable decision.

---

## Policy Decision Record

Every Policy Engine decision should generate a policy decision record.

A policy decision record should include:

* Identity
* Event type
* Policy evaluated
* Input attributes
* Decision result
* Access affected
* Approval requirement
* Expiration requirement
* Reviewer
* Timestamp
* Reason
* Audit reference

This record allows identity teams, auditors, security teams, and managers to understand why access was granted or removed.

---

## Role-Based Access Model

IdentityOS uses role-based access control as a foundation.

A role package defines the standard access required for a business role.

### Example Role Package

```yaml id="333gqb"
role_package:
  name: Litigation Associate
  department: Legal
  worker_type: Employee
  baseline_access:
    - Microsoft 365
    - Teams
    - SharePoint Legal Workspace
    - Legal Document Management System
  conditional_access:
    require_mfa: true
    require_compliant_device: true
  governance:
    review_frequency: Quarterly
    owner: Legal Operations
```

Role packages reduce confusion by defining what access is expected for a specific type of user.

---

## Attribute-Based Access Model

IdentityOS also supports attribute-based access decisions.

Attributes allow access to be determined dynamically based on business context.

### Example Attribute-Based Rule

```yaml id="4x2omw"
policy:
  name: Finance Analyst Baseline Access
  if:
    department: Finance
    job_title: Financial Analyst
    employment_status: Active
  then:
    grant:
      - Microsoft 365
      - Finance SharePoint
      - ERP Reporting
    require:
      - MFA
      - Compliant Device
    review_frequency: Quarterly
```

This allows access to follow the user’s current role and department.

---

## Joiner Policy Evaluation

When a Joiner event occurs, the Policy Engine determines the access package for the new identity.

### Joiner Policy Questions

The Policy Engine should ask:

* Is this identity active?
* What type of worker is this?
* What department do they belong to?
* What is their job title?
* Who is their manager?
* What applications are required?
* Is the identity privileged?
* Is approval required?
* Does access require expiration?
* What governance rules apply?

### Joiner Example

```yaml id="g57ddb"
event:
  type: Joiner
  worker_type: Employee
  department: Human Resources
  job_title: HR Specialist
  location: Miami
  status: Active

decision:
  grant:
    - Microsoft 365
    - HR SharePoint
    - HRIS Basic User
  require:
    - MFA
    - Conditional Access
  review_frequency: Quarterly
  approval_required: false
```

The output of this policy evaluation is sent to the Provisioning Engine.

---

## Mover Policy Evaluation

When a Mover event occurs, the Policy Engine compares the user’s current access against the access required for the new role.

### Mover Policy Questions

The Policy Engine should ask:

* What changed?
* What access does the user currently have?
* What access is required for the new role?
* What access should be removed?
* What access can be retained?
* Does the new role require privileged access?
* Does the previous role include sensitive access?
* Are there any separation of duties conflicts?
* Are exceptions required?
* Should manager or application owner approval be triggered?

### Mover Example

```yaml id="h37ndu"
event:
  type: Mover
  previous_department: Finance
  new_department: Legal
  previous_job_title: Financial Analyst
  new_job_title: Legal Operations Analyst

decision:
  remove:
    - ERP Reporting
    - Finance SharePoint
  grant:
    - Legal Operations Workspace
    - Legal Document Management System
  review:
    - Any retained finance-related access
  approval_required: true
  approver: New Manager
```

The Mover workflow is one of the most important controls for reducing privilege creep.

---

## Leaver Policy Evaluation

When a Leaver event occurs, the Policy Engine determines what access should be removed and what records must be preserved.

### Leaver Policy Questions

The Policy Engine should ask:

* Is this a voluntary or involuntary departure?
* Is the termination immediate or scheduled?
* Does this user have privileged access?
* Does this user own shared resources?
* Does this user own service accounts or applications?
* Does mailbox or file access need to be delegated?
* Are legal hold or retention requirements required?
* What evidence must be generated?

### Leaver Example

```yaml id="bp31sb"
event:
  type: Leaver
  worker_type: Employee
  termination_type: Scheduled
  privileged_access: true

decision:
  disable_account: true
  revoke_sessions: true
  remove_groups: true
  remove_privileged_roles: true
  deprovision_apps: true
  preserve_records: true
  notify:
    - Manager
    - Security Team
  audit_required: true
```

Leaver policies must prioritize speed, security, and evidence.

---

## Contractor Policy Evaluation

Contractor identities require expiration-based policy controls.

### Contractor Policy Requirements

Contractor access should include:

* Sponsor
* Business justification
* Start date
* End date
* Approved applications
* Limited access
* Review cadence
* Expiration enforcement

### Contractor Example

```yaml id="ddmwwe"
event:
  type: Contractor Onboarding
  worker_type: Contractor
  sponsor: Department Manager
  end_date_required: true

decision:
  grant:
    - Microsoft 365 Limited
    - Project Workspace
  require:
    - MFA
    - Expiration Date
    - Sponsor Approval
  review_frequency: Monthly
  auto_expire: true
```

Contractor access should never exist without an owner or expiration path.

---

## Privileged Access Policy

Privileged access requires stricter policy controls.

### Privileged Access Requirements

Privileged access should be:

* Eligible instead of permanently assigned
* Time-bound
* Approved when required
* Justified
* Protected by MFA
* Logged
* Reviewed
* Removed automatically when no longer needed

### Privileged Access Example

```yaml id="3cpwyw"
policy:
  name: Privileged Role Activation
  if:
    requested_role: User Administrator
    access_type: Privileged
  then:
    require:
      - MFA
      - Justification
      - Approval
      - Time Limit
    max_duration: 2 hours
    log_activation: true
    review_frequency: Monthly
```

Privileged access should be treated as a controlled event, not a permanent assignment.

---

## Exception Policy

Exceptions are sometimes necessary, but they must be governed.

### Exception Requirements

Every exception should include:

* Business justification
* Owner
* Approver
* Risk classification
* Expiration date
* Review date
* Audit record

### Exception Example

```yaml id="ssrhag"
exception:
  requested_access: Finance Reporting
  requester_department: Legal
  reason: Temporary cross-functional reporting project
  approver: Finance Application Owner
  expiration: 30 days
  review_required: true
  risk_level: Medium
```

An exception without an expiration date becomes unmanaged risk.

---

## Separation of Duties

The Policy Engine should identify access combinations that create risk.

Examples:

* A user should not both request and approve payments.
* A user should not administer a system and approve their own access.
* A developer should not have unrestricted production access without approval.
* A finance user should not hold conflicting transaction and approval roles.

### Separation of Duties Example

```yaml id="997g5v"
policy:
  name: Payment Approval Separation
  conflict:
    - Payment Requestor
    - Payment Approver
  decision:
    deny_combination: true
    require_exception_approval: true
```

Separation of duties controls help prevent fraud, misuse, and control failures.

---

## Policy Evaluation Priority

When multiple policies apply, IdentityOS should evaluate them in a predictable order.

Suggested evaluation priority:

1. Identity status
2. Worker type
3. Department
4. Job title
5. Location
6. Role package
7. Application sensitivity
8. Privileged access
9. Compliance requirements
10. Exceptions
11. Risk signals
12. Expiration rules

Policy evaluation should be predictable and explainable.

---

## Policy-as-Code Direction

IdentityOS should eventually support policy-as-code.

Policy-as-code allows identity rules to be:

* Version controlled
* Reviewed
* Tested
* Documented
* Reused
* Audited
* Deployed consistently

A future IdentityOS implementation may store policies in formats such as:

* YAML
* JSON
* Markdown
* Database-backed policy objects
* API-driven policy stores

Policy-as-code helps identity teams manage access rules with the same discipline used in modern infrastructure and security engineering.

---

## Policy Engine Metrics

The Policy Engine should produce metrics such as:

* Number of policy evaluations
* Number of access grants
* Number of removals
* Number of denied requests
* Number of exceptions
* Number of privileged access approvals
* Number of access drift findings
* Number of separation of duties conflicts
* Average policy evaluation time
* Most common access exceptions
* Policies with high override frequency

These metrics help security and IAM leaders understand whether access policy is operating effectively.

---

## Policy Engine Success Criteria

The Policy Engine is successful when:

* Access decisions are consistent.
* Access decisions are explainable.
* Least privilege is enforced.
* Role changes remove outdated access.
* Exceptions are governed.
* Privileged access is controlled.
* Policy violations are detected.
* Audit evidence is generated.
* Business roles map clearly to access.
* Access aligns with current identity attributes.

---

## Summary

The Policy Engine is the brain of IdentityOS.

It transforms identity attributes, business rules, governance requirements, and risk context into access decisions.

A strong Policy Engine helps organizations move from manual access judgment to consistent, explainable, auditable identity policy.

> The Policy Engine ensures that access is not only granted, but justified.
