import json
from pathlib import Path
from typing import Any, Dict

import pandas as pd
import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[2]
METRICS_PATH = ROOT_DIR / "examples" / "sample-dashboard-metrics.json"
REPORTS_DIR = ROOT_DIR / "reports"


st.set_page_config(
    page_title="IdentityOS Dashboard Prototype",
    page_icon="🛡️",
    layout="wide",
)


def load_json(path: Path) -> Dict[str, Any]:
    """Load a JSON file and return a dictionary."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def section_to_dataframe(section: Dict[str, Any]) -> pd.DataFrame:
    """Convert a metric section into a readable table."""
    rows = []

    for key, value in section.items():
        rows.append(
            {
                "Metric": key.replace("_", " ").title(),
                "Value": value,
            }
        )

    return pd.DataFrame(rows)


def get_metric(section: Dict[str, Any], key: str, default: Any = 0) -> Any:
    """Safely retrieve a metric value."""
    return section.get(key, default)


st.title("IdentityOS Dashboard Prototype")
st.caption(
    "Interactive prototype for identity lifecycle, governance, risk, access drift, "
    "automation health, and audit evidence visibility."
)

if not METRICS_PATH.exists():
    st.error(f"Metrics file not found: {METRICS_PATH}")
    st.stop()

metrics = load_json(METRICS_PATH)

executive_identity_risk = metrics.get("executive_identity_risk", {})
lifecycle_operations = metrics.get("lifecycle_operations", {})
governance = metrics.get("governance", {})
risk_scoring = metrics.get("risk_scoring", {})
access_drift = metrics.get("access_drift", {})
automation_health = metrics.get("automation_health", {})

st.header("Executive Identity Risk Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Sample Identities",
        get_metric(executive_identity_risk, "total_sample_identities"),
    )

with col2:
    st.metric(
        "Policy Decisions",
        get_metric(executive_identity_risk, "total_policy_decisions"),
    )

with col3:
    st.metric(
        "High Risk Decisions",
        get_metric(executive_identity_risk, "high_risk_decisions"),
    )

with col4:
    st.metric(
        "Critical Risk Decisions",
        get_metric(executive_identity_risk, "critical_risk_decisions"),
    )

st.header("IdentityOS Operational Views")

tabs = st.tabs(
    [
        "Lifecycle",
        "Governance",
        "Risk Scoring",
        "Access Drift",
        "Automation Health",
        "Reports",
    ]
)

with tabs[0]:
    st.subheader("Lifecycle Operations")
    st.dataframe(section_to_dataframe(lifecycle_operations), width="stretch")

with tabs[1]:
    st.subheader("Governance")
    st.dataframe(section_to_dataframe(governance), width="stretch")

with tabs[2]:
    st.subheader("Risk Scoring")
    st.dataframe(section_to_dataframe(risk_scoring), width="stretch")

with tabs[3]:
    st.subheader("Access Drift")
    st.dataframe(section_to_dataframe(access_drift), width="stretch")

with tabs[4]:
    st.subheader("Automation Health")
    st.dataframe(section_to_dataframe(automation_health), width="stretch")

with tabs[5]:
    st.subheader("Generated Reports")

    reports = [
        {
            "Report": "Governance Report",
            "Path": "reports/sample-governance-report.md",
        },
        {
            "Report": "Risk Score Report",
            "Path": "reports/sample-risk-score-report.md",
        },
        {
            "Report": "Access Drift Report",
            "Path": "reports/sample-access-drift-report.md",
        },
        {
            "Report": "Dashboard Summary",
            "Path": "reports/sample-dashboard-summary.md",
        },
    ]

    st.dataframe(pd.DataFrame(reports), width="stretch")

st.header("IdentityOS Dashboard Interpretation")

st.markdown(
    """
This prototype demonstrates how IdentityOS can turn identity lifecycle events,
policy decisions, governance requirements, risk scores, access drift findings,
automation outputs, and audit evidence into an interactive dashboard.

The current version is intentionally simple. Future iterations can add charts,
filters, drilldowns, report previews, and Entra ID integration views.
"""
)
