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


def clean_label(value: str) -> str:
    """Convert snake_case keys into readable dashboard labels."""
    return value.replace("_", " ").title()


EXPECTED_SECTIONS = {
    "executive_identity_risk",
    "lifecycle_operations",
    "governance",
    "risk_scoring",
    "access_drift",
    "automation_health",
}


def normalize_metrics(raw_metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Handle both flat and nested dashboard metrics JSON structures."""
    if not isinstance(raw_metrics, dict):
        return {}

    if any(section in raw_metrics for section in EXPECTED_SECTIONS):
        return raw_metrics

    for value in raw_metrics.values():
        if isinstance(value, dict) and any(section in value for section in EXPECTED_SECTIONS):
            return value

    return raw_metrics


def section_to_dataframe(section: Dict[str, Any]) -> pd.DataFrame:
    """Convert a metric section into a readable table."""
    rows = []

    if isinstance(section, dict):
        for key, value in section.items():
            if isinstance(value, (dict, list)):
                value = json.dumps(value)

            rows.append(
                {
                    "Metric": clean_label(key),
                    "Value": value,
                }
            )

    if not rows:
        return pd.DataFrame(
            [
                {
                    "Metric": "No metrics found",
                    "Value": "Check metrics JSON structure",
                }
            ],
            columns=["Metric", "Value"],
        )

    return pd.DataFrame(rows, columns=["Metric", "Value"])


def section_to_chart_dataframe(section: Dict[str, Any]) -> pd.DataFrame:
    """Convert a metric section into a numeric chart-friendly table."""
    df = section_to_dataframe(section)

    if "Value" not in df.columns:
        return pd.DataFrame(columns=["Metric", "Value"])

    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
    return df.dropna()


def get_metric(section: Dict[str, Any], key: str, default: Any = 0) -> Any:
    """Safely retrieve a metric value."""
    return section.get(key, default)


def render_metric_row(items: list[tuple[str, Any]]) -> None:
    """Render metrics across a row of columns."""
    columns = st.columns(len(items))

    for column, (label, value) in zip(columns, items):
        with column:
            st.metric(label, value)


def render_section_table_and_chart(title: str, section: Dict[str, Any]) -> None:
    """Render a dashboard section with a table and bar chart."""
    st.subheader(title)

    table_df = section_to_dataframe(section)
    chart_df = section_to_chart_dataframe(section)

    st.dataframe(table_df, width="stretch")

    if not chart_df.empty:
        st.bar_chart(chart_df.set_index("Metric"), width="stretch")


if not METRICS_PATH.exists():
    st.error(f"Metrics file not found: {METRICS_PATH}")
    st.stop()

raw_metrics = load_json(METRICS_PATH)
metrics = normalize_metrics(raw_metrics)

executive_identity_risk = metrics.get("executive_identity_risk", {})
lifecycle_operations = metrics.get("lifecycle_operations", {})
governance = metrics.get("governance", {})
risk_scoring = metrics.get("risk_scoring", {})
access_drift = metrics.get("access_drift", {})
automation_health = metrics.get("automation_health", {})

st.sidebar.title("IdentityOS")
st.sidebar.caption("IAM Visibility Prototype")

selected_view = st.sidebar.radio(
    "Dashboard View",
    [
        "Executive Overview",
        "Lifecycle Operations",
        "Governance",
        "Risk and Drift",
        "Automation Health",
        "Reports",
    ],
)

st.sidebar.divider()

st.sidebar.markdown(
    """
**Prototype Scope**

- Identity lifecycle
- Governance
- Risk scoring
- Access drift
- Automation health
- Audit evidence
"""
)

st.title("IdentityOS Dashboard Prototype")
st.caption(
    "Interactive IAM dashboard prototype for lifecycle operations, governance, "
    "risk scoring, access drift, automation health, and audit evidence."
)

if selected_view == "Executive Overview":
    st.header("Executive Identity Risk Overview")

    render_metric_row(
        [
            (
                "Sample Identities",
                get_metric(executive_identity_risk, "total_sample_identities"),
            ),
            (
                "Policy Decisions",
                get_metric(executive_identity_risk, "total_policy_decisions"),
            ),
            (
                "Pending Approvals",
                get_metric(executive_identity_risk, "pending_approvals"),
            ),
            (
                "Review Required",
                get_metric(executive_identity_risk, "review_required"),
            ),
        ]
    )

    render_metric_row(
        [
            (
                "High Risk Decisions",
                get_metric(executive_identity_risk, "high_risk_decisions"),
            ),
            (
                "Critical Risk Decisions",
                get_metric(executive_identity_risk, "critical_risk_decisions"),
            ),
            (
                "Access Drift Detected",
                get_metric(executive_identity_risk, "access_drift_detected"),
            ),
            (
                "Automation Failures",
                get_metric(automation_health, "automation_failures"),
            ),
        ]
    )

    st.divider()

    left, right = st.columns(2)

    with left:
        render_section_table_and_chart(
            "Executive Identity Risk Metrics",
            executive_identity_risk,
        )

    with right:
        render_section_table_and_chart(
            "Automation Health Snapshot",
            automation_health,
        )

    st.markdown(
        """
### Executive Interpretation

This view gives leadership a fast readout of identity posture:

- How many sample identities and policy decisions exist
- How many approvals and reviews are pending
- How many high-risk or critical-risk decisions exist
- Whether access drift is present
- Whether automation appears healthy
"""
    )

elif selected_view == "Lifecycle Operations":
    st.header("Lifecycle Operations")

    render_metric_row(
        [
            ("Joiner Events", get_metric(lifecycle_operations, "joiner_events")),
            ("Mover Events", get_metric(lifecycle_operations, "mover_events")),
            ("Leaver Events", get_metric(lifecycle_operations, "leaver_events")),
            (
                "Contractor Events",
                get_metric(lifecycle_operations, "contractor_onboarding_events"),
            ),
        ]
    )

    st.divider()

    render_section_table_and_chart(
        "Lifecycle Operations Metrics",
        lifecycle_operations,
    )

    st.markdown(
        """
### Lifecycle Interpretation

This view shows how IdentityOS models identity changes across:

- Joiners
- Movers
- Leavers
- Contractors
- Expiration events
- Privileged access requests
- Non-human identity reviews
"""
    )

elif selected_view == "Governance":
    st.header("Governance")

    render_metric_row(
        [
            ("Approvals Required", get_metric(governance, "approvals_required")),
            ("Pending Approvals", get_metric(governance, "pending_approvals")),
            ("Review Required", get_metric(governance, "review_required")),
            (
                "Audit Required Decisions",
                get_metric(governance, "audit_required_decisions"),
            ),
        ]
    )

    st.divider()

    render_section_table_and_chart(
        "Governance Metrics",
        governance,
    )

    st.markdown(
        """
### Governance Interpretation

This view shows whether identity decisions require:

- Approval
- Review
- Exception tracking
- Audit evidence
- Recurring governance
"""
    )

elif selected_view == "Risk and Drift":
    st.header("Risk and Access Drift")

    render_metric_row(
        [
            ("Low Risk", get_metric(risk_scoring, "low_risk_identities")),
            ("Medium Risk", get_metric(risk_scoring, "medium_risk_identities")),
            ("High Risk", get_metric(risk_scoring, "high_risk_identities")),
            ("Critical Risk", get_metric(risk_scoring, "critical_risk_identities")),
        ]
    )

    render_metric_row(
        [
            ("Total Drift Findings", get_metric(access_drift, "total_drift_findings")),
            ("Department Drift", get_metric(access_drift, "department_drift")),
            ("Leaver Drift", get_metric(access_drift, "leaver_drift")),
            ("Critical Drift", get_metric(access_drift, "critical_drift_findings")),
        ]
    )

    st.divider()

    left, right = st.columns(2)

    with left:
        render_section_table_and_chart(
            "Risk Scoring Metrics",
            risk_scoring,
        )

    with right:
        render_section_table_and_chart(
            "Access Drift Metrics",
            access_drift,
        )

    st.markdown(
        """
### Risk and Drift Interpretation

This view connects risk scoring to access drift.

It helps answer:

- Which identities are high or critical risk?
- Where does access no longer align with expected access?
- Which drift findings require remediation?
- Which access conditions should be reviewed first?
"""
    )

elif selected_view == "Automation Health":
    st.header("Automation Health")

    render_metric_row(
        [
            (
                "Automation Scripts",
                get_metric(automation_health, "automation_scripts_available"),
            ),
            (
                "Reports Generated",
                get_metric(automation_health, "reports_generated"),
            ),
            (
                "Automation Failures",
                get_metric(automation_health, "automation_failures"),
            ),
            (
                "Manual Intervention",
                get_metric(automation_health, "manual_intervention_required"),
            ),
        ]
    )

    st.divider()

    render_section_table_and_chart(
        "Automation Health Metrics",
        automation_health,
    )

    st.markdown(
        """
### Automation Interpretation

This view shows whether IdentityOS automation is operating cleanly.

It helps answer:

- Are scripts available?
- Are reports being generated?
- Are there automation failures?
- Is manual intervention required?
- Can automation outputs support evidence and dashboards?
"""
    )

elif selected_view == "Reports":
    st.header("Generated Reports and Evidence")

    reports = [
        {
            "Report": "Governance Report",
            "Path": "reports/sample-governance-report.md",
            "Purpose": "Governance decisions, approvals, reviews, and audit requirements.",
        },
        {
            "Report": "Risk Score Report",
            "Path": "reports/sample-risk-score-report.md",
            "Purpose": "Risk scores, risk levels, risk factors, and recommended actions.",
        },
        {
            "Report": "Access Drift Report",
            "Path": "reports/sample-access-drift-report.md",
            "Purpose": "Stale access, excess access, drift findings, and remediation.",
        },
        {
            "Report": "Dashboard Summary",
            "Path": "reports/sample-dashboard-summary.md",
            "Purpose": "Dashboard-ready summary of IAM metrics.",
        },
    ]

    st.dataframe(pd.DataFrame(reports), width="stretch")

    st.divider()

    st.markdown(
        """
### Report Interpretation

Reports provide the evidence layer behind IdentityOS dashboards.

They help connect:

- Lifecycle events
- Policy decisions
- Risk scoring
- Access drift
- Governance actions
- Audit evidence
"""
    )

st.divider()

st.markdown(
    """
### IdentityOS Prototype Summary

IdentityOS demonstrates how IAM architecture can connect lifecycle events,
policy decisions, governance workflows, risk signals, access drift findings,
automation outputs, Microsoft Entra ID integration concepts, and audit evidence
into an interactive dashboard experience.
"""
)