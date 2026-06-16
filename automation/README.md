# IdentityOS Automation

## Purpose

This folder contains prototype automation scripts for IdentityOS.

The goal of these scripts is to demonstrate how identity events, policy decisions, governance logic, and audit outputs can be processed programmatically.

IdentityOS automation is designed to show how identity operations can move from manual ticket-based work to repeatable, policy-driven workflows.

---

## Current Scripts

| Script                                     | Purpose                                                                                                     |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| [policy-evaluator.py](policy-evaluator.py) | Reads sample identity events and sample policy decisions, then prints a readable policy evaluation summary. |
| [generate-governance-report.py](generate-governance-report.py) | Reads sample identity events and policy decisions, then generates a Markdown governance report. |
| [risk-scorer.py](risk-scorer.py) | Calculates sample identity risk scores from identity events and policy decisions, then generates a Markdown risk score report. |

---

## Policy Evaluator

The `policy-evaluator.py` script is the first working prototype for IdentityOS.

It demonstrates the following pattern:

```text id="z4m4fg"
Identity Event
      ↓
Policy Decision Lookup
      ↓
Access Decision Summary
      ↓
Governance Requirements
      ↓
Audit Reason
      ↓
Evaluation Metrics
```

---

## Governance Report Generator

The `generate-governance-report.py` script creates a Markdown governance report from the sample IdentityOS data.

It demonstrates the following pattern:

```text id="dpuzsn"
Identity Events
      ↓
Policy Decisions
      ↓
Governance Summary
      ↓
Risk Distribution
      ↓
Access Remediation Summary
      ↓
Detailed Audit Evidence
      ↓
Markdown Report
```

The script reads:

```text id="z22c2d"
examples/sample-identity-events.json
examples/sample-policy-decisions.json
```

And generates:

```text id="q578j8"
reports/sample-governance-report.md
```

Run the script from the project root:

```powershell id="1yfjuq"
python automation/generate-governance-report.py
```

Or, if using the Windows Python launcher:

```powershell id="gnun3y"
py automation/generate-governance-report.py
```

This report helps demonstrate how IdentityOS can turn identity decisions into governance visibility, audit evidence, and risk reporting.


## Input Files

The script uses two sample data files:

| File                                    | Purpose                                                     |
| --------------------------------------- | ----------------------------------------------------------- |
| `examples/sample-identity-events.json`  | Contains sample identity lifecycle and governance events.   |
| `examples/sample-policy-decisions.json` | Contains sample policy decisions linked to identity events. |

---

## Risk Scorer

The `risk-scorer.py` script calculates sample identity risk scores using identity events and policy decisions.

It demonstrates the following pattern:

```text id="9xzxf9"
Identity Events
      ↓
Policy Decisions
      ↓
Risk Factor Evaluation
      ↓
Risk Score
      ↓
Risk Level
      ↓
Recommended Governance Action
      ↓
Markdown Risk Report
```

The script reads:

```text id="xhedne"
examples/sample-identity-events.json
examples/sample-policy-decisions.json
```

And generates:

```text id="8na141"
reports/sample-risk-score-report.md
```

Run the script from the project root:

```powershell id="g0jn5e"
python automation/risk-scorer.py
```

Or, if using the Windows Python launcher:

```powershell id="k9c43u"
py automation/risk-scorer.py
```

The risk scorer helps demonstrate how IdentityOS can turn access decisions into measurable identity risk.


## Supported Event Types

The current prototype includes sample logic for:

* Joiner events
* Mover events
* Leaver events
* Contractor onboarding
* Contractor expiration
* Privileged access requests
* Non-human identity reviews

---

## Run the Script

From the project root, run:

```powershell id="3i8t9o"
python automation/policy-evaluator.py
```

Or, if using the Windows Python launcher:

```powershell id="ae3mdq"
py automation/policy-evaluator.py
```

---

## Example Output

The script prints:

* Event ID
* Event type
* Source system
* Identity
* Policy result
* Decision summary
* Access to grant
* Access to remove
* Controls required
* Approval requirement
* Review frequency
* Risk level
* Expiration requirement
* Audit reason
* Summary metrics

---

## Current Evaluation Metrics

The prototype currently summarizes:

* Total decisions
* Pending approvals
* Review-required decisions
* High-risk decisions
* Critical-risk decisions

These metrics demonstrate how IdentityOS can turn identity events into governance and risk visibility.

---

## Why This Matters

This script shows the beginning of an identity automation engine.

In a real enterprise environment, the same pattern could be extended to:

* Create users
* Assign access packages
* Remove stale access
* Trigger approvals
* Start access reviews
* Disable leaver accounts
* Remove privileged roles
* Create audit evidence
* Send alerts to security teams
* Update dashboards

---

## Future Automation Enhancements

Planned enhancements include:

* Generate Markdown governance reports
* Export evaluation results to JSON
* Add policy scoring
* Add risk scoring
* Add exception detection
* Add access drift detection
* Add simulated provisioning actions
* Add Microsoft Entra ID integration examples
* Add dashboard-ready output files

---

## Guiding Statement

> Identity automation should make access decisions faster, safer, more consistent, and easier to audit.
