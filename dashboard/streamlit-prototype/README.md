# IdentityOS Streamlit Dashboard Prototype

## Purpose

This folder contains the first interactive dashboard prototype for IdentityOS.

The prototype uses Streamlit to transform IdentityOS sample metrics into an interactive dashboard view for identity lifecycle activity, governance, risk scoring, access drift, automation health, and report visibility.

The goal is to demonstrate how IdentityOS can move from static architecture documentation into an operational identity dashboard.

---

## Current Prototype Capabilities

The current Streamlit prototype includes:

* Executive identity risk overview
* Sample identity count
* Policy decision count
* High-risk decision count
* Critical-risk decision count
* Lifecycle operations tab
* Governance metrics tab
* Risk scoring metrics tab
* Access drift metrics tab
* Automation health tab
* Generated reports tab

---

## Data Source

The prototype reads dashboard metrics from:

```text
examples/sample-dashboard-metrics.json
```

This allows the dashboard to stay connected to the same sample data model used across the IdentityOS reports and dashboard design documentation.

---

## How to Run Locally

From the root of the repository, create a virtual environment:

```powershell
python -m venv .venv
```

Install the required packages:

```powershell
.\.venv\Scripts\python.exe -m pip install -r dashboard\streamlit-prototype\requirements.txt
```

Run the dashboard:

```powershell
.\.venv\Scripts\streamlit.exe run dashboard\streamlit-prototype\app.py
```

The app should open in the browser at:

```text
http://localhost:8501
```

---

## Prototype Files

| File               | Purpose                                            |
| ------------------ | -------------------------------------------------- |
| `app.py`           | Main Streamlit dashboard prototype.                |
| `requirements.txt` | Python dependencies required to run the dashboard. |
| `README.md`        | Documentation for the dashboard prototype.         |

---

## Relationship to IdentityOS

This prototype connects to the broader IdentityOS architecture by visualizing:

* Identity lifecycle events
* Policy decisions
* Governance metrics
* Risk scoring outputs
* Access drift findings
* Automation health
* Generated evidence reports

It is not intended to replace Entra ID, IAM tools, governance platforms, or SIEM solutions.

Instead, it demonstrates how IdentityOS could provide an orchestration and visibility layer across identity operations.

---

## Future Enhancements

Future versions may include:

* Interactive filters
* Charts and visualizations
* Drilldown views
* Report previews
* Risk trend analysis
* Access drift heatmaps
* Privileged access views
* Contractor and vendor access views
* Non-human identity views
* Audit evidence views
* Entra ID integration concepts
* Microsoft Graph API sample actions

---

## Summary

The IdentityOS Streamlit Dashboard Prototype demonstrates how identity architecture, policy decisions, governance workflows, and risk signals can be turned into an interactive operational dashboard.

> The prototype turns IdentityOS from a documented architecture into a visible identity operations experience.
