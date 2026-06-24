import json
from pathlib import Path
from typing import Any, Dict

import pandas as pd
import streamlit as st
import plotly.express as px

ROOT_DIR = Path(__file__).resolve().parents[2]
METRICS_PATH = ROOT_DIR / "examples" / "sample-dashboard-metrics.json"
REPORTS_DIR = ROOT_DIR / "reports"
CORE_DASHBOARD_OUTPUT_PATH = (
    ROOT_DIR / "identityos-core" / "outputs" / "dashboard" / "dashboard-output.json"
)

st.set_page_config(
    page_title="IdentityOS Dashboard Prototype",
    page_icon="🛡️",
    layout="wide",
)


def load_json(path: Path) -> Dict[str, Any]:
    """Load a JSON file and return a dictionary."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
def load_optional_json(path: Path) -> Dict[str, Any]:
    """Load a JSON file if it exists. Return an empty dictionary if missing."""
    if not path.exists():
        return {}

    return load_json(path)

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

core_dashboard_output = load_optional_json(CORE_DASHBOARD_OUTPUT_PATH)

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
        "IdentityOS Core Output",
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
elif selected_view == "IdentityOS Core Output":
    st.header("IdentityOS Core Output")

    if not core_dashboard_output:
        st.warning(
            "No IdentityOS Core output found yet. Run the core processor first:"
        )
        st.code(
            ".\\.venv\\Scripts\\python.exe identityos-core\\engine\\process-identity-event.py",
            language="powershell",
        )
    else:
        render_metric_row(
            [
                (
                    "Events Processed",
                    core_dashboard_output.get("total_events_processed", 0),
                ),
                (
                    "Tickets Created",
                    core_dashboard_output.get("tickets_created", 0),
                ),
                (
                    "Approvals Required",
                    core_dashboard_output.get("approval_required_count", 0),
                ),
                (
                    "Drift Detected",
                    core_dashboard_output.get("drift_detected_count", 0),
                ),
            ]
        )

        st.divider()

        left, right = st.columns(2)

        with left:
            st.subheader("Risk Counts")
            risk_counts = core_dashboard_output.get("risk_counts", {})
            risk_df = section_to_dataframe(risk_counts)
            risk_chart_df = section_to_chart_dataframe(risk_counts)

            st.dataframe(risk_df, width="stretch")

            if not risk_chart_df.empty:
                st.bar_chart(risk_chart_df.set_index("Metric"), width="stretch")

        with right:
            st.subheader("Event Type Counts")
            event_type_counts = core_dashboard_output.get("event_type_counts", {})
            event_df = section_to_dataframe(event_type_counts)
            event_chart_df = section_to_chart_dataframe(event_type_counts)

            st.dataframe(event_df, width="stretch")

            if not event_chart_df.empty:
                st.bar_chart(event_chart_df.set_index("Metric"), width="stretch")

        st.divider()

        st.subheader("Generated Output Files")

        output_paths = core_dashboard_output.get("outputs", {})

        output_df = pd.DataFrame(
            [
                {
                    "Output Type": clean_label(key),
                    "Path": value,
                }
                for key, value in output_paths.items()
            ]
        )

        st.dataframe(output_df, width="stretch")

        st.markdown(
            """
### Core Output Interpretation

This view shows the result of the simulated IAM operating system engine.

It connects:

- HR lifecycle events
- Role package mapping
- Approval requirements
- Mock ticket generation
- Access drift detection
- Risk scoring
- Audit evidence
- Dashboard-ready output
"""
        )
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
# ------------------------------------------------------------
# Identity Lifecycle Management - Joiner Access Packages
# ------------------------------------------------------------

st.markdown("---")
st.header("Identity Lifecycle Management")
st.subheader("New Hire Access Package Recommendations")

st.markdown(
    """
    This section simulates how IdentityOS evaluates new hire identity attributes
    such as department, job title, and workforce role to recommend the appropriate
    access package before provisioning begins.
    """
)

new_hire_access_packages = [
    {
        "Employee": "Alicia Brown",
        "Department": "HR",
        "Job Title": "HR Specialist",
        "Recommended Access Package": "HR Core Access",
        "Approval Required": "Manager Approval",
        "Provisioning Status": "Pending Approval",
        "Risk Level": "Low"
    },
    {
        "Employee": "Marcus Lee",
        "Department": "Finance",
        "Job Title": "Finance Analyst",
        "Recommended Access Package": "Finance Core Access",
        "Approval Required": "Finance Manager Approval",
        "Provisioning Status": "Pending Approval",
        "Risk Level": "Medium"
    },
    {
        "Employee": "Nina Patel",
        "Department": "Security",
        "Job Title": "Security Analyst",
        "Recommended Access Package": "Security Operations Access",
        "Approval Required": "Security Leadership Approval",
        "Provisioning Status": "Pending Approval",
        "Risk Level": "Medium"
    },
    {
        "Employee": "David Kim",
        "Department": "IT",
        "Job Title": "IT Support Technician",
        "Recommended Access Package": "IT Support Access",
        "Approval Required": "IT Manager Approval",
        "Provisioning Status": "Pending Approval",
        "Risk Level": "Medium"
    },
    {
        "Employee": "Executive Admin",
        "Department": "Executives",
        "Job Title": "Executive Assistant",
        "Recommended Access Package": "Executive Support Access",
        "Approval Required": "Executive Approval + Security Review",
        "Provisioning Status": "Pending Review",
        "Risk Level": "High"
    }
]

new_hire_df = pd.DataFrame(new_hire_access_packages)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("New Hire Requests", len(new_hire_df))

with col2:
    pending_count = new_hire_df[
        new_hire_df["Provisioning Status"].str.contains("Pending")
    ].shape[0]
    st.metric("Pending Provisioning", pending_count)

with col3:
    high_risk_count = new_hire_df[
        new_hire_df["Risk Level"] == "High"
    ].shape[0]
    st.metric("High Risk Requests", high_risk_count)

st.dataframe(new_hire_df, use_container_width=True)

risk_chart = px.bar(
    new_hire_df,
    x="Employee",
    y=[1] * len(new_hire_df),
    color="Risk Level",
    title="New Hire Access Request Risk Levels",
    labels={"value": "Request Count", "Employee": "Employee"}
)

st.plotly_chart(risk_chart, use_container_width=True)

st.info(
    "IAM Architecture Note: IdentityOS maps workforce attributes to access packages, "
    "helping standardize joiner access, reduce manual provisioning, and provide "
    "governance visibility before access is granted."
)
# ------------------------------------------------------------
# Identity Lifecycle Management - Access Package Policy Engine
# ------------------------------------------------------------

st.markdown("---")
st.subheader("Access Package Policy Engine")

st.markdown(
    """
    This simulator demonstrates how IdentityOS can evaluate workforce identity
    attributes and recommend a standardized access package based on department
    and job role.
    """
)

access_policy_map = {
    ("HR", "HR Specialist"): {
        "Access Package": "HR Core Access",
        "Approval Workflow": "Manager Approval",
        "Risk Level": "Low",
        "Provisioning Action": "Create account, assign HR group, grant HR application access"
    },
    ("Finance", "Finance Analyst"): {
        "Access Package": "Finance Core Access",
        "Approval Workflow": "Finance Manager Approval",
        "Risk Level": "Medium",
        "Provisioning Action": "Create account, assign Finance group, grant finance application access"
    },
    ("Security", "Security Analyst"): {
        "Access Package": "Security Operations Access",
        "Approval Workflow": "Security Leadership Approval",
        "Risk Level": "Medium",
        "Provisioning Action": "Create account, assign Security Operations group, grant monitoring tool access"
    },
    ("IT", "IT Support Technician"): {
        "Access Package": "IT Support Access",
        "Approval Workflow": "IT Manager Approval",
        "Risk Level": "Medium",
        "Provisioning Action": "Create account, assign IT Support group, grant helpdesk tool access"
    },
    ("Executives", "Executive Assistant"): {
        "Access Package": "Executive Support Access",
        "Approval Workflow": "Executive Approval + Security Review",
        "Risk Level": "High",
        "Provisioning Action": "Create account, assign Executive Support group, require MFA and security review"
    }
}

def recommend_access_package(department, job_title):
    return access_policy_map.get(
        (department, job_title),
        {
            "Access Package": "Manual Review Required",
            "Approval Workflow": "IAM Team Review",
            "Risk Level": "Unknown",
            "Provisioning Action": "Do not provision automatically"
        }
    )

sim_col1, sim_col2 = st.columns(2)

with sim_col1:
    selected_department = st.selectbox(
        "Select Department",
        ["HR", "Finance", "Security", "IT", "Executives", "Legal", "Operations"]
    )

with sim_col2:
    selected_job_title = st.selectbox(
        "Select Job Title",
        [
            "HR Specialist",
            "Finance Analyst",
            "Security Analyst",
            "IT Support Technician",
            "Executive Assistant",
            "Legal Analyst",
            "Operations Coordinator"
        ]
    )

recommendation = recommend_access_package(selected_department, selected_job_title)

st.write("### Recommended IdentityOS Decision")

decision_col1, decision_col2, decision_col3 = st.columns(3)

with decision_col1:
    st.metric("Access Package", recommendation["Access Package"])

with decision_col2:
    st.metric("Risk Level", recommendation["Risk Level"])

with decision_col3:
    st.metric("Approval Workflow", recommendation["Approval Workflow"])

st.success(f"Provisioning Action: {recommendation['Provisioning Action']}")

st.info(
    "IAM Architecture Note: This policy engine represents the foundation of automated "
    "Joiner workflows. In a live enterprise environment, these mappings would be driven "
    "by HR attributes such as department, job title, location, and employment type."
)
# ------------------------------------------------------------
# Identity Lifecycle Management - Access Decision Audit Log
# ------------------------------------------------------------

st.markdown("---")
st.subheader("Access Decision Audit Log")

st.markdown(
    """
    This section captures simulated audit evidence for access package decisions.
    In an enterprise IAM environment, this type of log would support compliance,
    access reviews, security investigations, and governance reporting.
    """
)

from datetime import datetime

if "access_decision_audit_log" not in st.session_state:
    st.session_state.access_decision_audit_log = []

if st.button("Record Current Access Decision"):
    audit_entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Department": selected_department,
        "Job Title": selected_job_title,
        "Recommended Access Package": recommendation["Access Package"],
        "Approval Workflow": recommendation["Approval Workflow"],
        "Risk Level": recommendation["Risk Level"],
        "Provisioning Action": recommendation["Provisioning Action"],
        "Decision Source": "IdentityOS Policy Engine"
    }

    st.session_state.access_decision_audit_log.append(audit_entry)
    st.success("Access decision recorded in the audit log.")

if st.session_state.access_decision_audit_log:
    audit_log_df = pd.DataFrame(st.session_state.access_decision_audit_log)
    st.dataframe(audit_log_df, use_container_width=True)

    high_risk_audit_count = audit_log_df[
        audit_log_df["Risk Level"] == "High"
    ].shape[0]

    manual_review_count = audit_log_df[
        audit_log_df["Recommended Access Package"] == "Manual Review Required"
    ].shape[0]

    audit_col1, audit_col2, audit_col3 = st.columns(3)

    with audit_col1:
        st.metric("Recorded Decisions", len(audit_log_df))

    with audit_col2:
        st.metric("High Risk Decisions", high_risk_audit_count)

    with audit_col3:
        st.metric("Manual Reviews", manual_review_count)

else:
    st.warning("No access decisions have been recorded yet.")

st.info(
    "IAM Governance Note: Access decision logs provide evidence for auditors, "
    "help security teams investigate provisioning activity, and support access "
    "review programs by showing why access was recommended or withheld."
)
# ------------------------------------------------------------
# Identity Lifecycle Management - Mover Workflow Engine
# ------------------------------------------------------------

st.markdown("---")
st.subheader("Mover Workflow Engine")

st.markdown(
    """
    This section simulates how IdentityOS evaluates employee movement between
    departments or job roles. The engine compares the employee's current access
    package against the recommended future-state access package and identifies
    whether access should be retained, removed, added, or reviewed.
    """
)

from datetime import datetime

mover_col1, mover_col2 = st.columns(2)

with mover_col1:
    st.write("### Current Identity Attributes")

    current_department = st.selectbox(
        "Current Department",
        ["HR", "Finance", "Security", "IT", "Executives", "Legal", "Operations"],
        key="current_department_select"
    )

    current_job_title = st.selectbox(
        "Current Job Title",
        [
            "HR Specialist",
            "Finance Analyst",
            "Security Analyst",
            "IT Support Technician",
            "Executive Assistant",
            "Legal Analyst",
            "Operations Coordinator"
        ],
        key="current_job_title_select"
    )

with mover_col2:
    st.write("### New Identity Attributes")

    new_department = st.selectbox(
        "New Department",
        ["HR", "Finance", "Security", "IT", "Executives", "Legal", "Operations"],
        key="new_department_select"
    )

    new_job_title = st.selectbox(
        "New Job Title",
        [
            "HR Specialist",
            "Finance Analyst",
            "Security Analyst",
            "IT Support Technician",
            "Executive Assistant",
            "Legal Analyst",
            "Operations Coordinator"
        ],
        key="new_job_title_select"
    )

current_access = recommend_access_package(current_department, current_job_title)
new_access = recommend_access_package(new_department, new_job_title)

current_package = current_access["Access Package"]
new_package = new_access["Access Package"]

st.write("### Mover Access Evaluation")

mover_decision_col1, mover_decision_col2, mover_decision_col3 = st.columns(3)

with mover_decision_col1:
    st.metric("Current Access Package", current_package)

with mover_decision_col2:
    st.metric("New Access Package", new_package)

with mover_decision_col3:
    st.metric("New Risk Level", new_access["Risk Level"])

if current_package == new_package:
    mover_decision = "No Access Package Change Required"
    mover_action = "Retain current access package"
    mover_risk = new_access["Risk Level"]
else:
    mover_decision = "Access Package Change Required"
    mover_action = (
        f"Remove '{current_package}' and assign '{new_package}' "
        f"after approval workflow: {new_access['Approval Workflow']}"
    )
    mover_risk = new_access["Risk Level"]

st.success(f"Mover Decision: {mover_decision}")
st.info(f"Recommended Action: {mover_action}")

mover_change_summary = [
    {
        "Access Control Area": "Current Access Package",
        "Current State": current_package,
        "Future State": "Remove" if current_package != new_package else "Retain",
        "Action Required": "Review removal" if current_package != new_package else "No change"
    },
    {
        "Access Control Area": "New Access Package",
        "Current State": "Not assigned" if current_package != new_package else current_package,
        "Future State": new_package,
        "Action Required": "Assign after approval" if current_package != new_package else "No change"
    },
    {
        "Access Control Area": "Approval Workflow",
        "Current State": current_access["Approval Workflow"],
        "Future State": new_access["Approval Workflow"],
        "Action Required": "Route to new approver" if current_package != new_package else "No change"
    },
    {
        "Access Control Area": "Risk Level",
        "Current State": current_access["Risk Level"],
        "Future State": new_access["Risk Level"],
        "Action Required": "Security review required" if new_access["Risk Level"] == "High" else "Standard review"
    }
]

mover_change_df = pd.DataFrame(mover_change_summary)

st.dataframe(mover_change_df, use_container_width=True)

if "mover_audit_log" not in st.session_state:
    st.session_state.mover_audit_log = []

if st.button("Record Mover Decision"):
    mover_audit_entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Current Department": current_department,
        "Current Job Title": current_job_title,
        "New Department": new_department,
        "New Job Title": new_job_title,
        "Current Access Package": current_package,
        "New Access Package": new_package,
        "Mover Decision": mover_decision,
        "Recommended Action": mover_action,
        "New Risk Level": mover_risk,
        "Decision Source": "IdentityOS Mover Workflow Engine"
    }

    st.session_state.mover_audit_log.append(mover_audit_entry)
    st.success("Mover decision recorded in the audit log.")

if st.session_state.mover_audit_log:
    st.write("### Mover Decision Audit Log")

    mover_audit_df = pd.DataFrame(st.session_state.mover_audit_log)
    st.dataframe(mover_audit_df, use_container_width=True)

    total_mover_decisions = len(mover_audit_df)

    package_change_count = mover_audit_df[
        mover_audit_df["Mover Decision"] == "Access Package Change Required"
    ].shape[0]

    high_risk_mover_count = mover_audit_df[
        mover_audit_df["New Risk Level"] == "High"
    ].shape[0]

    mover_metric_col1, mover_metric_col2, mover_metric_col3 = st.columns(3)

    with mover_metric_col1:
        st.metric("Mover Decisions", total_mover_decisions)

    with mover_metric_col2:
        st.metric("Package Changes", package_change_count)

    with mover_metric_col3:
        st.metric("High Risk Moves", high_risk_mover_count)

st.info(
    "IAM Architecture Note: Mover workflows are critical because access should not simply "
    "accumulate as employees change roles. IdentityOS compares current access to future-state "
    "access so outdated permissions can be removed and new access can be approved through governance."
)