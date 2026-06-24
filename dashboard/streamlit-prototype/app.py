import json
from datetime import datetime
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
ASSETS_DIR = ROOT_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "identityos-logo.png"
IDENTITYOS_STATE_DIR = ROOT_DIR / "identityos-state"

IDENTITYOS_STATE_FILES = {
    "hr_identity_intake_queue": IDENTITYOS_STATE_DIR / "hr-identity-intake-queue.json",
    "approval_queue": IDENTITYOS_STATE_DIR / "approval-queue.json",
    "provisioning_history": IDENTITYOS_STATE_DIR / "provisioning-history.json",
    "access_decision_audit_log": IDENTITYOS_STATE_DIR / "joiner-access-decision-audit-log.json",
    "mover_audit_log": IDENTITYOS_STATE_DIR / "mover-audit-log.json",
    "leaver_audit_log": IDENTITYOS_STATE_DIR / "leaver-audit-log.json",
    "identityos_persistence_events": IDENTITYOS_STATE_DIR / "persistence-events.json",
}
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
def load_json(path: Path) -> Dict[str, Any]:
    """Load a JSON file and return a dictionary."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_optional_json(path: Path) -> Dict[str, Any]:
    """Load a JSON file if it exists. Return an empty dictionary if missing."""
    if not path.exists():
        return {}

    return load_json(path)


def load_state_file(path: Path):
    """Load a persisted IdentityOS state file from disk."""
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError):
        return []


def save_state_file(path: Path, records):
    """Save IdentityOS state records to disk as JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


def load_identityos_state_from_disk():
    """Load all persisted IdentityOS workflow records into Streamlit session state."""
    for state_key, state_path in IDENTITYOS_STATE_FILES.items():
        if state_key not in st.session_state:
            st.session_state[state_key] = load_state_file(state_path)


def save_identityos_state_to_disk():
    """Save all IdentityOS workflow records from Streamlit session state to disk."""
    for state_key, state_path in IDENTITYOS_STATE_FILES.items():
        records = st.session_state.get(state_key, [])
        save_state_file(state_path, records)


def record_persistence_event(event_type, event_details):
    """Record save/load activity for audit visibility."""
    if "identityos_persistence_events" not in st.session_state:
        st.session_state.identityos_persistence_events = []

    st.session_state.identityos_persistence_events.append(
        {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Event Type": event_type,
            "Event Details": event_details,
            "Decision Source": "IdentityOS Data Persistence Layer"
        }
    )
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
if "identityos_state_loaded_from_disk" not in st.session_state:
    load_identityos_state_from_disk()
    st.session_state.identityos_state_loaded_from_disk = True


st.markdown("---")
# ------------------------------------------------------------
# IdentityOS - System Status Banner
# ------------------------------------------------------------

status_col1, status_col2, status_col3, status_col4 = st.columns(4)

with status_col1:
    st.metric("System Status", "Operational")

with status_col2:
    st.metric("Workflow Engine", "Online")

with status_col3:
    persistence_status = "Enabled" if IDENTITYOS_STATE_DIR.exists() else "Ready"
    st.metric("Persistence", persistence_status)

with status_col4:
    st.metric("Governance Mode", "Active")

st.success(
    "IdentityOS v0.2 is running with HR Intake, JML workflows, approval queue, "
    "provisioning actions, governance scoring, audit evidence, and local persistence."
)

st.markdown("---")

header_col1, header_col2 = st.columns([1, 5])

with header_col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=95)
    else:
        st.markdown("### 🛡️")

with header_col2:
    st.markdown(
        """
        # IdentityOS
        ### Identity Lifecycle Command Center
        """
    )

    st.caption(
        "v0.2 | HR Intake • JML Workflows • Approval Queue • Provisioning • Governance • Persistence"
    )

st.markdown("---")

st.title("IdentityOS Dashboard Prototype")
st.caption(
    "Enterprise identity lifecycle, governance, approval, provisioning, and audit simulation."
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
# ------------------------------------------------------------
# Identity Lifecycle Management - Leaver Workflow Engine
# ------------------------------------------------------------

st.markdown("---")
st.subheader("Leaver Workflow Engine")

st.markdown(
    """
    This section simulates how IdentityOS handles employee offboarding. The engine
    evaluates the employee's department, job role, access package, and risk level
    to recommend account disablement, access removal, session revocation, and
    audit evidence capture.
    """
)

leaver_col1, leaver_col2 = st.columns(2)

with leaver_col1:
    leaver_name = st.text_input(
        "Employee Name",
        value="Marcus Lee",
        key="leaver_employee_name"
    )

    leaver_department = st.selectbox(
        "Leaver Department",
        ["HR", "Finance", "Security", "IT", "Executives", "Legal", "Operations"],
        key="leaver_department_select"
    )

with leaver_col2:
    leaver_job_title = st.selectbox(
        "Leaver Job Title",
        [
            "HR Specialist",
            "Finance Analyst",
            "Security Analyst",
            "IT Support Technician",
            "Executive Assistant",
            "Legal Analyst",
            "Operations Coordinator"
        ],
        key="leaver_job_title_select"
    )

    leaver_type = st.selectbox(
        "Departure Type",
        [
            "Voluntary Departure",
            "Involuntary Departure",
            "Contract End",
            "High Risk Termination"
        ],
        key="leaver_type_select"
    )

leaver_access = recommend_access_package(leaver_department, leaver_job_title)

leaver_risk_level = leaver_access["Risk Level"]

if leaver_type in ["Involuntary Departure", "High Risk Termination"]:
    leaver_risk_level = "High"

st.write("### Leaver Access Evaluation")

leaver_metric_col1, leaver_metric_col2, leaver_metric_col3 = st.columns(3)

with leaver_metric_col1:
    st.metric("Current Access Package", leaver_access["Access Package"])

with leaver_metric_col2:
    st.metric("Leaver Risk Level", leaver_risk_level)

with leaver_metric_col3:
    st.metric("Departure Type", leaver_type)

if leaver_risk_level == "High":
    leaver_priority = "Immediate Offboarding Required"
    leaver_action = (
        "Disable account immediately, revoke active sessions, remove all group memberships, "
        "block sign-in, preserve mailbox/data for investigation, and notify Security."
    )
else:
    leaver_priority = "Standard Offboarding"
    leaver_action = (
        "Disable account on scheduled departure date, remove assigned access package, "
        "revoke sessions, remove group memberships, and retain audit evidence."
    )

if leaver_risk_level == "High":
    st.error(f"Leaver Priority: {leaver_priority}")
else:
    st.success(f"Leaver Priority: {leaver_priority}")

st.info(f"Recommended Offboarding Action: {leaver_action}")

leaver_control_summary = [
    {
        "Offboarding Control": "Account Status",
        "Action": "Disable user account",
        "Priority": "Immediate" if leaver_risk_level == "High" else "Scheduled"
    },
    {
        "Offboarding Control": "Access Package",
        "Action": f"Remove {leaver_access['Access Package']}",
        "Priority": "Immediate" if leaver_risk_level == "High" else "Standard"
    },
    {
        "Offboarding Control": "Group Memberships",
        "Action": "Remove all assigned security and application groups",
        "Priority": "Immediate" if leaver_risk_level == "High" else "Standard"
    },
    {
        "Offboarding Control": "Active Sessions",
        "Action": "Revoke refresh tokens and active sessions",
        "Priority": "Immediate"
    },
    {
        "Offboarding Control": "Audit Evidence",
        "Action": "Record offboarding decision and retain evidence",
        "Priority": "Required"
    }
]

leaver_control_df = pd.DataFrame(leaver_control_summary)

st.dataframe(leaver_control_df, use_container_width=True)

if "leaver_audit_log" not in st.session_state:
    st.session_state.leaver_audit_log = []

if st.button("Record Leaver Decision"):
    leaver_audit_entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Employee": leaver_name,
        "Department": leaver_department,
        "Job Title": leaver_job_title,
        "Access Package Removed": leaver_access["Access Package"],
        "Departure Type": leaver_type,
        "Leaver Risk Level": leaver_risk_level,
        "Leaver Priority": leaver_priority,
        "Recommended Action": leaver_action,
        "Decision Source": "IdentityOS Leaver Workflow Engine"
    }

    st.session_state.leaver_audit_log.append(leaver_audit_entry)
    st.success("Leaver decision recorded in the audit log.")

if st.session_state.leaver_audit_log:
    st.write("### Leaver Decision Audit Log")

    leaver_audit_df = pd.DataFrame(st.session_state.leaver_audit_log)
    st.dataframe(leaver_audit_df, use_container_width=True)

    high_risk_leaver_count = leaver_audit_df[
        leaver_audit_df["Leaver Risk Level"] == "High"
    ].shape[0]

    immediate_offboarding_count = leaver_audit_df[
        leaver_audit_df["Leaver Priority"] == "Immediate Offboarding Required"
    ].shape[0]

    leaver_log_col1, leaver_log_col2, leaver_log_col3 = st.columns(3)

    with leaver_log_col1:
        st.metric("Leaver Decisions", len(leaver_audit_df))

    with leaver_log_col2:
        st.metric("High Risk Leavers", high_risk_leaver_count)

    with leaver_log_col3:
        st.metric("Immediate Offboarding", immediate_offboarding_count)

st.info(
    "IAM Governance Note: Leaver workflows are one of the most important controls in identity security. "
    "IdentityOS supports offboarding governance by identifying access removal, account disablement, "
    "session revocation, and audit evidence requirements before access is fully removed."
)
# ------------------------------------------------------------
# Identity Lifecycle Management - Executive Summary
# ------------------------------------------------------------

st.markdown("---")
st.header("Identity Lifecycle Executive Summary")

st.markdown(
    """
    This section provides an executive-level view of Joiner, Mover, and Leaver
    activity across IdentityOS. It summarizes lifecycle decisions, high-risk events,
    manual review volume, and offboarding priority to support IAM governance,
    audit readiness, and leadership reporting.
    """
)

# Safely load lifecycle logs from Streamlit session state
joiner_audit_log = st.session_state.get("access_decision_audit_log", [])
mover_audit_log = st.session_state.get("mover_audit_log", [])
leaver_audit_log = st.session_state.get("leaver_audit_log", [])

joiner_summary_df = pd.DataFrame(joiner_audit_log)
mover_summary_df = pd.DataFrame(mover_audit_log)
leaver_summary_df = pd.DataFrame(leaver_audit_log)


def count_value(df, column_name, target_value):
    if column_name in df.columns:
        return df[df[column_name] == target_value].shape[0]
    return 0


def count_contains(df, column_name, target_text):
    if column_name in df.columns:
        return df[df[column_name].astype(str).str.contains(target_text, case=False, na=False)].shape[0]
    return 0


total_joiner_decisions = len(joiner_summary_df)
total_mover_decisions = len(mover_summary_df)
total_leaver_decisions = len(leaver_summary_df)

total_lifecycle_events = (
    total_joiner_decisions
    + total_mover_decisions
    + total_leaver_decisions
)

joiner_high_risk = count_value(joiner_summary_df, "Risk Level", "High")
mover_high_risk = count_value(mover_summary_df, "New Risk Level", "High")
leaver_high_risk = count_value(leaver_summary_df, "Leaver Risk Level", "High")

total_high_risk_events = (
    joiner_high_risk
    + mover_high_risk
    + leaver_high_risk
)

manual_review_count = count_value(
    joiner_summary_df,
    "Recommended Access Package",
    "Manual Review Required"
)

package_change_count = count_value(
    mover_summary_df,
    "Mover Decision",
    "Access Package Change Required"
)

immediate_offboarding_count = count_value(
    leaver_summary_df,
    "Leaver Priority",
    "Immediate Offboarding Required"
)

summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)

with summary_col1:
    st.metric("Total Lifecycle Events", total_lifecycle_events)

with summary_col2:
    st.metric("High Risk Events", total_high_risk_events)

with summary_col3:
    st.metric("Manual Reviews", manual_review_count)

with summary_col4:
    st.metric("Immediate Offboarding", immediate_offboarding_count)

st.write("### Lifecycle Activity Breakdown")

lifecycle_activity_summary = [
    {
        "Lifecycle Stage": "Joiner",
        "Recorded Decisions": total_joiner_decisions,
        "High Risk Events": joiner_high_risk,
        "Governance Focus": "Access package recommendation and approval"
    },
    {
        "Lifecycle Stage": "Mover",
        "Recorded Decisions": total_mover_decisions,
        "High Risk Events": mover_high_risk,
        "Governance Focus": "Access change review and access creep prevention"
    },
    {
        "Lifecycle Stage": "Leaver",
        "Recorded Decisions": total_leaver_decisions,
        "High Risk Events": leaver_high_risk,
        "Governance Focus": "Access removal, session revocation, and account disablement"
    }
]

lifecycle_activity_df = pd.DataFrame(lifecycle_activity_summary)

st.dataframe(lifecycle_activity_df, use_container_width=True)

if total_lifecycle_events > 0:
    lifecycle_chart = px.bar(
        lifecycle_activity_df,
        x="Lifecycle Stage",
        y="Recorded Decisions",
        color="Lifecycle Stage",
        title="Recorded Identity Lifecycle Decisions"
    )

    st.plotly_chart(lifecycle_chart, use_container_width=True)

    high_risk_chart = px.bar(
        lifecycle_activity_df,
        x="Lifecycle Stage",
        y="High Risk Events",
        color="Lifecycle Stage",
        title="High Risk Identity Lifecycle Events"
    )

    st.plotly_chart(high_risk_chart, use_container_width=True)
else:
    st.warning(
        "No lifecycle decisions have been recorded yet. Record Joiner, Mover, or Leaver "
        "decisions to populate the executive summary."
    )

st.write("### Governance Interpretation")

if total_lifecycle_events == 0:
    st.info(
        "IdentityOS is ready to summarize lifecycle activity once access decisions are recorded."
    )
elif total_high_risk_events == 0 and immediate_offboarding_count == 0:
    st.success(
        "Current lifecycle activity shows no high-risk events or immediate offboarding cases. "
        "Standard governance workflows appear sufficient for the recorded activity."
    )
elif total_high_risk_events > 0 and immediate_offboarding_count == 0:
    st.warning(
        "High-risk lifecycle events have been recorded. Security or IAM leadership review "
        "should validate approval workflows and access decisions."
    )
else:
    st.error(
        "Immediate offboarding activity has been recorded. Security, IAM, and HR should ensure "
        "account disablement, access removal, session revocation, and evidence retention are complete."
    )

st.info(
    "Executive IAM Note: This summary gives leadership a consolidated view of identity lifecycle "
    "risk across Joiner, Mover, and Leaver workflows. In a production environment, these metrics "
    "could be connected to HR systems, ticketing platforms, identity governance tools, and SIEM reporting."
)
# ------------------------------------------------------------
# IdentityOS - Approval Queue and Ticketing Simulation
# ------------------------------------------------------------

st.markdown("---")
st.header("IdentityOS Approval Queue")

st.markdown(
    """
    This section simulates how IdentityOS turns identity lifecycle decisions into
    approval tickets. Tickets can be generated from Joiner, Mover, and Leaver
    workflows, assigned to the correct approver, and tracked through approval
    and provisioning status.
    """
)

from datetime import datetime

if "approval_queue" not in st.session_state:
    st.session_state.approval_queue = []


def create_ticket_id():
    return f"IAM-{datetime.now().strftime('%Y%m%d%H%M%S')}-{len(st.session_state.approval_queue) + 1}"


def add_approval_ticket(
    lifecycle_stage,
    employee,
    request_type,
    access_package,
    approval_owner,
    risk_level,
    recommended_action,
):
    ticket = {
        "Ticket ID": create_ticket_id(),
        "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Lifecycle Stage": lifecycle_stage,
        "Employee": employee,
        "Request Type": request_type,
        "Access Package / Control": access_package,
        "Approval Owner": approval_owner,
        "Risk Level": risk_level,
        "Recommended Action": recommended_action,
        "Ticket Status": "Pending Approval",
        "Provisioning Status": "Not Started",
        "Decision Source": "IdentityOS Workflow Engine"
    }

    st.session_state.approval_queue.append(ticket)


st.write("### Generate Approval Tickets")

ticket_col1, ticket_col2, ticket_col3 = st.columns(3)

with ticket_col1:
    if st.button("Create Joiner Approval Ticket"):
        joiner_employee = f"{selected_department} New Hire"

        add_approval_ticket(
            lifecycle_stage="Joiner",
            employee=joiner_employee,
            request_type="New Access Package Request",
            access_package=recommendation["Access Package"],
            approval_owner=recommendation["Approval Workflow"],
            risk_level=recommendation["Risk Level"],
            recommended_action=recommendation["Provisioning Action"],
        )

        st.success("Joiner approval ticket created.")

with ticket_col2:
    if st.button("Create Mover Approval Ticket"):
        mover_employee = f"{current_department} to {new_department} Employee"

        add_approval_ticket(
            lifecycle_stage="Mover",
            employee=mover_employee,
            request_type="Access Change Request",
            access_package=new_package,
            approval_owner=new_access["Approval Workflow"],
            risk_level=mover_risk,
            recommended_action=mover_action,
        )

        st.success("Mover approval ticket created.")

with ticket_col3:
    if st.button("Create Leaver Offboarding Ticket"):
        add_approval_ticket(
            lifecycle_stage="Leaver",
            employee=leaver_name,
            request_type="Offboarding Control Request",
            access_package=leaver_access["Access Package"],
            approval_owner="HR + IAM + Security",
            risk_level=leaver_risk_level,
            recommended_action=leaver_action,
        )

        st.success("Leaver offboarding ticket created.")


if st.session_state.approval_queue:
    approval_queue_df = pd.DataFrame(st.session_state.approval_queue)

    st.write("### Active Approval Queue")
    st.dataframe(approval_queue_df, use_container_width=True)

    open_ticket_count = approval_queue_df[
        approval_queue_df["Ticket Status"].isin(["Pending Approval", "Approved"])
    ].shape[0]

    approved_ticket_count = approval_queue_df[
        approval_queue_df["Ticket Status"] == "Approved"
    ].shape[0]

    high_risk_ticket_count = approval_queue_df[
        approval_queue_df["Risk Level"] == "High"
    ].shape[0]

    provisioning_ready_count = approval_queue_df[
        approval_queue_df["Provisioning Status"] == "Ready for Provisioning"
    ].shape[0]

    queue_metric_col1, queue_metric_col2, queue_metric_col3, queue_metric_col4 = st.columns(4)

    with queue_metric_col1:
        st.metric("Open Tickets", open_ticket_count)

    with queue_metric_col2:
        st.metric("Approved Tickets", approved_ticket_count)

    with queue_metric_col3:
        st.metric("High Risk Tickets", high_risk_ticket_count)

    with queue_metric_col4:
        st.metric("Ready for Provisioning", provisioning_ready_count)

    st.write("### Update Ticket Status")

    selected_ticket_id = st.selectbox(
        "Select Ticket",
        approval_queue_df["Ticket ID"].tolist(),
        key="approval_ticket_select"
    )

    selected_ticket_status = st.selectbox(
        "Ticket Status",
        [
            "Pending Approval",
            "Approved",
            "Denied",
            "Provisioning Ready",
            "Provisioned",
            "Closed"
        ],
        key="approval_ticket_status_select"
    )

    selected_provisioning_status = st.selectbox(
        "Provisioning Status",
        [
            "Not Started",
            "Ready for Provisioning",
            "Provisioning In Progress",
            "Provisioned",
            "Access Removed",
            "Blocked"
        ],
        key="approval_provisioning_status_select"
    )

    if st.button("Update Selected Ticket"):
        for ticket in st.session_state.approval_queue:
            if ticket["Ticket ID"] == selected_ticket_id:
                ticket["Ticket Status"] = selected_ticket_status
                ticket["Provisioning Status"] = selected_provisioning_status

        st.success(f"Ticket {selected_ticket_id} updated.")

    st.write("### Approval Queue Risk Breakdown")

    approval_risk_summary = (
        approval_queue_df.groupby(["Lifecycle Stage", "Risk Level"])
        .size()
        .reset_index(name="Ticket Count")
    )

    st.dataframe(approval_risk_summary, use_container_width=True)

    approval_risk_chart = px.bar(
        approval_risk_summary,
        x="Lifecycle Stage",
        y="Ticket Count",
        color="Risk Level",
        title="Approval Tickets by Lifecycle Stage and Risk Level"
    )

    st.plotly_chart(approval_risk_chart, use_container_width=True)

else:
    st.warning("No approval tickets have been created yet.")

st.info(
    "IAM Workflow Note: This approval queue represents the bridge between identity lifecycle "
    "decisions and operational execution. In a production environment, IdentityOS could send "
    "these tickets to ServiceNow, Jira, Freshservice, Microsoft Graph workflows, or another "
    "enterprise ticketing and approval platform."
)
# ------------------------------------------------------------
# IdentityOS - Provisioning Action Center
# ------------------------------------------------------------

st.markdown("---")
st.header("IdentityOS Provisioning Action Center")

st.markdown(
    """
    This section simulates how IdentityOS executes approved IAM workflow actions.
    Once an approval ticket is approved and marked ready for provisioning, the
    Provisioning Action Center identifies the required access action, tracks the
    execution result, and records provisioning evidence.
    """
)

from datetime import datetime

if "provisioning_history" not in st.session_state:
    st.session_state.provisioning_history = []

approval_queue = st.session_state.get("approval_queue", [])

if approval_queue:
    provisioning_queue_df = pd.DataFrame(approval_queue)

    ready_for_provisioning_df = provisioning_queue_df[
        (
            provisioning_queue_df["Ticket Status"].isin(
                ["Approved", "Provisioning Ready"]
            )
        )
        | (
            provisioning_queue_df["Provisioning Status"].isin(
                ["Ready for Provisioning", "Provisioning In Progress"]
            )
        )
    ]

    provisioning_col1, provisioning_col2, provisioning_col3 = st.columns(3)

    with provisioning_col1:
        st.metric("Total Tickets", len(provisioning_queue_df))

    with provisioning_col2:
        st.metric("Ready for Provisioning", len(ready_for_provisioning_df))

    with provisioning_col3:
        high_risk_ready_count = ready_for_provisioning_df[
            ready_for_provisioning_df["Risk Level"] == "High"
        ].shape[0]
        st.metric("High Risk Ready Items", high_risk_ready_count)

    if not ready_for_provisioning_df.empty:
        st.write("### Provisioning-Ready Tickets")

        st.dataframe(ready_for_provisioning_df, use_container_width=True)

        selected_provisioning_ticket_id = st.selectbox(
            "Select Ticket for Provisioning",
            ready_for_provisioning_df["Ticket ID"].tolist(),
            key="provisioning_ticket_select"
        )

        selected_ticket = ready_for_provisioning_df[
            ready_for_provisioning_df["Ticket ID"] == selected_provisioning_ticket_id
        ].iloc[0]

        lifecycle_stage = selected_ticket["Lifecycle Stage"]
        request_type = selected_ticket["Request Type"]
        employee = selected_ticket["Employee"]
        access_package = selected_ticket["Access Package / Control"]
        risk_level = selected_ticket["Risk Level"]
        recommended_action = selected_ticket["Recommended Action"]

        st.write("### Selected Provisioning Request")

        selected_col1, selected_col2, selected_col3 = st.columns(3)

        with selected_col1:
            st.metric("Lifecycle Stage", lifecycle_stage)

        with selected_col2:
            st.metric("Risk Level", risk_level)

        with selected_col3:
            st.metric("Current Status", selected_ticket["Provisioning Status"])

        st.info(f"Recommended Action: {recommended_action}")

        if lifecycle_stage == "Joiner":
            provisioning_steps = [
                "Create user account",
                f"Assign access package: {access_package}",
                "Assign required security groups",
                "Apply baseline Conditional Access policies",
                "Send onboarding completion evidence to audit log"
            ]
            final_status = "Provisioned"

        elif lifecycle_stage == "Mover":
            provisioning_steps = [
                "Remove outdated access package",
                f"Assign new access package: {access_package}",
                "Update department and role-based group memberships",
                "Validate access change approval",
                "Record mover provisioning evidence"
            ]
            final_status = "Provisioned"

        elif lifecycle_stage == "Leaver":
            provisioning_steps = [
                "Disable user account",
                f"Remove access package/control: {access_package}",
                "Remove security and application group memberships",
                "Revoke active sessions and refresh tokens",
                "Record offboarding evidence for audit"
            ]
            final_status = "Access Removed"

        else:
            provisioning_steps = [
                "Manual IAM review required",
                "Validate ticket details",
                "Determine correct provisioning action",
                "Record manual decision evidence"
            ]
            final_status = "Manual Review Required"

        provisioning_steps_df = pd.DataFrame(
            [
                {
                    "Step Number": index + 1,
                    "Provisioning Step": step,
                    "Execution Status": "Pending"
                }
                for index, step in enumerate(provisioning_steps)
            ]
        )

        st.write("### Required Provisioning Steps")
        st.dataframe(provisioning_steps_df, use_container_width=True)

        execution_result = st.selectbox(
            "Provisioning Execution Result",
            [
                "Successful",
                "Partially Completed",
                "Failed",
                "Requires Manual Review"
            ],
            key="provisioning_execution_result"
        )

        execution_notes = st.text_area(
            "Provisioning Notes",
            value="Provisioning action executed in IdentityOS simulation.",
            key="provisioning_execution_notes"
        )

        if st.button("Execute Provisioning Action"):
            provisioning_record = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Ticket ID": selected_provisioning_ticket_id,
                "Lifecycle Stage": lifecycle_stage,
                "Employee": employee,
                "Access Package / Control": access_package,
                "Risk Level": risk_level,
                "Execution Result": execution_result,
                "Final Provisioning Status": final_status if execution_result == "Successful" else execution_result,
                "Provisioning Notes": execution_notes,
                "Decision Source": "IdentityOS Provisioning Action Center"
            }

            st.session_state.provisioning_history.append(provisioning_record)

            for ticket in st.session_state.approval_queue:
                if ticket["Ticket ID"] == selected_provisioning_ticket_id:
                    if execution_result == "Successful":
                        ticket["Provisioning Status"] = final_status
                        ticket["Ticket Status"] = "Closed"
                    elif execution_result == "Partially Completed":
                        ticket["Provisioning Status"] = "Provisioning In Progress"
                        ticket["Ticket Status"] = "Approved"
                    elif execution_result == "Failed":
                        ticket["Provisioning Status"] = "Blocked"
                        ticket["Ticket Status"] = "Pending Approval"
                    else:
                        ticket["Provisioning Status"] = "Manual Review Required"
                        ticket["Ticket Status"] = "Pending Approval"

            st.success(f"Provisioning action recorded for ticket {selected_provisioning_ticket_id}.")

    else:
        st.warning(
            "No tickets are currently ready for provisioning. Approve a ticket and set "
            "Provisioning Status to 'Ready for Provisioning' in the Approval Queue."
        )

else:
    st.warning(
        "No approval tickets exist yet. Create approval tickets before using the Provisioning Action Center."
    )

if st.session_state.provisioning_history:
    st.write("### Provisioning Execution History")

    provisioning_history_df = pd.DataFrame(st.session_state.provisioning_history)
    st.dataframe(provisioning_history_df, use_container_width=True)

    successful_provisioning_count = provisioning_history_df[
        provisioning_history_df["Execution Result"] == "Successful"
    ].shape[0]

    failed_provisioning_count = provisioning_history_df[
        provisioning_history_df["Execution Result"] == "Failed"
    ].shape[0]

    manual_review_provisioning_count = provisioning_history_df[
        provisioning_history_df["Execution Result"] == "Requires Manual Review"
    ].shape[0]

    provision_metric_col1, provision_metric_col2, provision_metric_col3 = st.columns(3)

    with provision_metric_col1:
        st.metric("Successful Actions", successful_provisioning_count)

    with provision_metric_col2:
        st.metric("Failed Actions", failed_provisioning_count)

    with provision_metric_col3:
        st.metric("Manual Reviews", manual_review_provisioning_count)

    provisioning_result_summary = (
        provisioning_history_df.groupby(["Lifecycle Stage", "Execution Result"])
        .size()
        .reset_index(name="Action Count")
    )

    st.write("### Provisioning Result Breakdown")

    st.dataframe(provisioning_result_summary, use_container_width=True)

    provisioning_result_chart = px.bar(
        provisioning_result_summary,
        x="Lifecycle Stage",
        y="Action Count",
        color="Execution Result",
        title="Provisioning Actions by Lifecycle Stage and Result"
    )

    st.plotly_chart(provisioning_result_chart, use_container_width=True)

st.info(
    "IAM Operations Note: The Provisioning Action Center represents the execution layer "
    "of IdentityOS. In a production environment, these actions could call Microsoft Graph, "
    "Entra ID, HRIS workflows, ticketing APIs, or identity governance platforms to create users, "
    "assign groups, remove access, disable accounts, and revoke sessions."
)
# ------------------------------------------------------------
# IdentityOS - HR Identity Intake Portal
# ------------------------------------------------------------

st.markdown("---")
st.header("HR Identity Intake Portal")

st.markdown(
    """
    This section simulates the HR front door for IdentityOS. HR can submit new hire
    identity details, and IdentityOS will evaluate workforce attributes to recommend
    the correct access package, approval workflow, risk level, and provisioning action.
    """
)

if "hr_identity_intake_queue" not in st.session_state:
    st.session_state.hr_identity_intake_queue = []


def create_intake_id():
    return f"HR-{datetime.now().strftime('%Y%m%d%H%M%S')}-{len(st.session_state.hr_identity_intake_queue) + 1}"


st.write("### Submit New Hire Identity Intake")

with st.form("hr_identity_intake_form"):
    intake_col1, intake_col2 = st.columns(2)

    with intake_col1:
        new_hire_name = st.text_input(
            "New Hire Name",
            value="Jordan Williams",
            key="hr_intake_new_hire_name"
        )

        new_hire_department = st.selectbox(
            "Department",
            ["HR", "Finance", "Security", "IT", "Executives", "Legal", "Operations"],
            key="hr_intake_department"
        )

        new_hire_job_title = st.selectbox(
            "Job Title",
            [
                "HR Specialist",
                "Finance Analyst",
                "Security Analyst",
                "IT Support Technician",
                "Executive Assistant",
                "Legal Analyst",
                "Operations Coordinator"
            ],
            key="hr_intake_job_title"
        )

    with intake_col2:
        new_hire_location = st.selectbox(
            "Location",
            ["Orlando", "Miami", "Remote", "New York", "Atlanta", "Dallas"],
            key="hr_intake_location"
        )

        employment_type = st.selectbox(
            "Employment Type",
            ["Full-Time", "Part-Time", "Contractor", "Intern"],
            key="hr_intake_employment_type"
        )

        start_date = st.date_input(
            "Start Date",
            key="hr_intake_start_date"
        )

    submit_intake = st.form_submit_button("Submit HR Intake")

if submit_intake:
    intake_recommendation = recommend_access_package(
        new_hire_department,
        new_hire_job_title
    )

    intake_record = {
        "Intake ID": create_intake_id(),
        "Submitted": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "New Hire Name": new_hire_name,
        "Department": new_hire_department,
        "Job Title": new_hire_job_title,
        "Location": new_hire_location,
        "Employment Type": employment_type,
        "Start Date": str(start_date),
        "Recommended Access Package": intake_recommendation["Access Package"],
        "Approval Workflow": intake_recommendation["Approval Workflow"],
        "Risk Level": intake_recommendation["Risk Level"],
        "Provisioning Action": intake_recommendation["Provisioning Action"],
        "Intake Status": "Submitted",
        "Ticket Created": "No"
    }

    st.session_state.hr_identity_intake_queue.append(intake_record)

    st.success(
        f"HR intake submitted for {new_hire_name}. "
        f"Recommended package: {intake_recommendation['Access Package']}."
    )


if st.session_state.hr_identity_intake_queue:
    st.write("### HR Intake Queue")

    hr_intake_df = pd.DataFrame(st.session_state.hr_identity_intake_queue)
    st.dataframe(hr_intake_df, use_container_width=True)

    intake_metric_col1, intake_metric_col2, intake_metric_col3, intake_metric_col4 = st.columns(4)

    with intake_metric_col1:
        st.metric("Total Intakes", len(hr_intake_df))

    with intake_metric_col2:
        high_risk_intakes = hr_intake_df[
            hr_intake_df["Risk Level"] == "High"
        ].shape[0]
        st.metric("High Risk Intakes", high_risk_intakes)

    with intake_metric_col3:
        manual_review_intakes = hr_intake_df[
            hr_intake_df["Recommended Access Package"] == "Manual Review Required"
        ].shape[0]
        st.metric("Manual Reviews", manual_review_intakes)

    with intake_metric_col4:
        tickets_created_count = hr_intake_df[
            hr_intake_df["Ticket Created"] == "Yes"
        ].shape[0]
        st.metric("Tickets Created", tickets_created_count)

    st.write("### Generate Approval Ticket from HR Intake")

    selected_intake_id = st.selectbox(
        "Select HR Intake",
        hr_intake_df["Intake ID"].tolist(),
        key="hr_intake_ticket_select"
    )

    selected_intake = hr_intake_df[
        hr_intake_df["Intake ID"] == selected_intake_id
    ].iloc[0]

    selected_intake_col1, selected_intake_col2, selected_intake_col3 = st.columns(3)

    with selected_intake_col1:
        st.metric("New Hire", selected_intake["New Hire Name"])

    with selected_intake_col2:
        st.metric("Recommended Package", selected_intake["Recommended Access Package"])

    with selected_intake_col3:
        st.metric("Risk Level", selected_intake["Risk Level"])

    st.info(f"Approval Workflow: {selected_intake['Approval Workflow']}")
    st.info(f"Provisioning Action: {selected_intake['Provisioning Action']}")

    if st.button("Create Approval Ticket from HR Intake"):
        add_approval_ticket(
            lifecycle_stage="Joiner",
            employee=selected_intake["New Hire Name"],
            request_type="HR New Hire Access Request",
            access_package=selected_intake["Recommended Access Package"],
            approval_owner=selected_intake["Approval Workflow"],
            risk_level=selected_intake["Risk Level"],
            recommended_action=selected_intake["Provisioning Action"],
        )

        for intake in st.session_state.hr_identity_intake_queue:
            if intake["Intake ID"] == selected_intake_id:
                intake["Ticket Created"] = "Yes"
                intake["Intake Status"] = "Approval Ticket Created"

        st.success(
            f"Approval ticket created for {selected_intake['New Hire Name']}."
        )

    st.write("### HR Intake Risk Breakdown")

    hr_intake_risk_summary = (
        hr_intake_df.groupby(["Department", "Risk Level"])
        .size()
        .reset_index(name="Intake Count")
    )

    st.dataframe(hr_intake_risk_summary, use_container_width=True)

    hr_intake_risk_chart = px.bar(
        hr_intake_risk_summary,
        x="Department",
        y="Intake Count",
        color="Risk Level",
        title="HR Identity Intakes by Department and Risk Level"
    )

    st.plotly_chart(hr_intake_risk_chart, use_container_width=True)

else:
    st.warning("No HR identity intakes have been submitted yet.")

st.info(
    "IAM Operating Model Note: The HR Identity Intake Portal represents the front door "
    "of the Joiner lifecycle. In a production IdentityOS environment, this intake could "
    "come directly from an HRIS platform such as Workday, SAP SuccessFactors, BambooHR, "
    "or another source of truth. IdentityOS would then evaluate user attributes, recommend "
    "access, create approval tickets, and trigger provisioning workflows."
)
# ------------------------------------------------------------
# IdentityOS - Governance Control Center
# ------------------------------------------------------------

st.markdown("---")
st.header("IdentityOS Governance Control Center")

st.markdown(
    """
    This section provides a consolidated governance view across IdentityOS.
    It summarizes approval risk, lifecycle events, provisioning outcomes,
    audit evidence, manual review volume, and immediate offboarding activity
    to help IAM, Security, HR, and leadership understand identity governance posture.
    """
)

# Safely pull IdentityOS workflow data from session state
governance_approval_queue = st.session_state.get("approval_queue", [])
governance_provisioning_history = st.session_state.get("provisioning_history", [])
governance_hr_intake_queue = st.session_state.get("hr_identity_intake_queue", [])
governance_joiner_log = st.session_state.get("access_decision_audit_log", [])
governance_mover_log = st.session_state.get("mover_audit_log", [])
governance_leaver_log = st.session_state.get("leaver_audit_log", [])

approval_governance_df = pd.DataFrame(governance_approval_queue)
provisioning_governance_df = pd.DataFrame(governance_provisioning_history)
hr_governance_df = pd.DataFrame(governance_hr_intake_queue)
joiner_governance_df = pd.DataFrame(governance_joiner_log)
mover_governance_df = pd.DataFrame(governance_mover_log)
leaver_governance_df = pd.DataFrame(governance_leaver_log)


def governance_count_equal(df, column_name, target_value):
    if column_name in df.columns:
        return df[df[column_name] == target_value].shape[0]
    return 0


def governance_count_in(df, column_name, target_values):
    if column_name in df.columns:
        return df[df[column_name].isin(target_values)].shape[0]
    return 0


def governance_total_rows(df):
    return len(df) if not df.empty else 0


# Approval queue metrics
open_approval_count = governance_count_in(
    approval_governance_df,
    "Ticket Status",
    ["Pending Approval", "Approved", "Provisioning Ready"]
)

pending_approval_count = governance_count_equal(
    approval_governance_df,
    "Ticket Status",
    "Pending Approval"
)

approved_ticket_count = governance_count_equal(
    approval_governance_df,
    "Ticket Status",
    "Approved"
)

closed_ticket_count = governance_count_equal(
    approval_governance_df,
    "Ticket Status",
    "Closed"
)

high_risk_ticket_count = governance_count_equal(
    approval_governance_df,
    "Risk Level",
    "High"
)

manual_review_ticket_count = governance_count_in(
    approval_governance_df,
    "Provisioning Status",
    ["Manual Review Required", "Blocked"]
)

# Provisioning metrics
successful_provisioning_count = governance_count_equal(
    provisioning_governance_df,
    "Execution Result",
    "Successful"
)

failed_provisioning_count = governance_count_equal(
    provisioning_governance_df,
    "Execution Result",
    "Failed"
)

partial_provisioning_count = governance_count_equal(
    provisioning_governance_df,
    "Execution Result",
    "Partially Completed"
)

manual_review_provisioning_count = governance_count_equal(
    provisioning_governance_df,
    "Execution Result",
    "Requires Manual Review"
)

# Lifecycle risk metrics
joiner_high_risk_count = governance_count_equal(
    joiner_governance_df,
    "Risk Level",
    "High"
)

mover_high_risk_count = governance_count_equal(
    mover_governance_df,
    "New Risk Level",
    "High"
)

leaver_high_risk_count = governance_count_equal(
    leaver_governance_df,
    "Leaver Risk Level",
    "High"
)

total_high_risk_lifecycle_events = (
    joiner_high_risk_count
    + mover_high_risk_count
    + leaver_high_risk_count
    + high_risk_ticket_count
)

immediate_offboarding_count = governance_count_equal(
    leaver_governance_df,
    "Leaver Priority",
    "Immediate Offboarding Required"
)

# HR intake metrics
total_hr_intakes = governance_total_rows(hr_governance_df)

high_risk_hr_intakes = governance_count_equal(
    hr_governance_df,
    "Risk Level",
    "High"
)

manual_review_hr_intakes = governance_count_equal(
    hr_governance_df,
    "Recommended Access Package",
    "Manual Review Required"
)

# Audit evidence metrics
audit_evidence_records = (
    governance_total_rows(joiner_governance_df)
    + governance_total_rows(mover_governance_df)
    + governance_total_rows(leaver_governance_df)
    + governance_total_rows(provisioning_governance_df)
)

total_identity_events = (
    governance_total_rows(joiner_governance_df)
    + governance_total_rows(mover_governance_df)
    + governance_total_rows(leaver_governance_df)
    + governance_total_rows(hr_governance_df)
    + governance_total_rows(approval_governance_df)
    + governance_total_rows(provisioning_governance_df)
)

# Governance health score
governance_health_score = 100

governance_health_score -= min(open_approval_count * 3, 15)
governance_health_score -= min(high_risk_ticket_count * 6, 18)
governance_health_score -= min(failed_provisioning_count * 10, 20)
governance_health_score -= min(manual_review_ticket_count * 5, 15)
governance_health_score -= min(immediate_offboarding_count * 8, 16)
governance_health_score -= min(manual_review_hr_intakes * 4, 12)

governance_health_score = max(governance_health_score, 0)

if governance_health_score >= 85:
    governance_posture = "Healthy"
    governance_posture_message = (
        "Identity governance posture is healthy. Current activity shows manageable risk, "
        "strong evidence capture, and no major operational concerns."
    )
elif governance_health_score >= 70:
    governance_posture = "Watch"
    governance_posture_message = (
        "Identity governance posture requires monitoring. Open approvals, high-risk items, "
        "or manual review activity should be reviewed by IAM operations."
    )
else:
    governance_posture = "Action Required"
    governance_posture_message = (
        "Identity governance posture requires action. High-risk events, failed provisioning, "
        "manual reviews, or immediate offboarding activity need IAM, Security, and HR follow-up."
    )

st.write("### Governance Health Overview")

gov_metric_col1, gov_metric_col2, gov_metric_col3, gov_metric_col4 = st.columns(4)

with gov_metric_col1:
    st.metric("Governance Health Score", governance_health_score)

with gov_metric_col2:
    st.metric("Open Approvals", open_approval_count)

with gov_metric_col3:
    st.metric("High Risk Items", total_high_risk_lifecycle_events)

with gov_metric_col4:
    st.metric("Audit Evidence Records", audit_evidence_records)

st.progress(governance_health_score / 100)

if governance_posture == "Healthy":
    st.success(f"Governance Posture: {governance_posture}")
elif governance_posture == "Watch":
    st.warning(f"Governance Posture: {governance_posture}")
else:
    st.error(f"Governance Posture: {governance_posture}")

st.info(governance_posture_message)

st.write("### Governance Control Summary")

governance_control_summary = [
    {
        "Governance Area": "Approval Management",
        "Current Count": open_approval_count,
        "Risk Signal": "Open approvals waiting for decision",
        "Recommended Owner": "IAM Operations / Managers",
        "Priority": "High" if open_approval_count >= 5 else "Standard"
    },
    {
        "Governance Area": "High Risk Identity Events",
        "Current Count": total_high_risk_lifecycle_events,
        "Risk Signal": "High-risk Joiner, Mover, Leaver, or ticket activity",
        "Recommended Owner": "Security / IAM Leadership",
        "Priority": "High" if total_high_risk_lifecycle_events > 0 else "Standard"
    },
    {
        "Governance Area": "Provisioning Failures",
        "Current Count": failed_provisioning_count,
        "Risk Signal": "Failed IAM execution activity",
        "Recommended Owner": "IAM Engineering",
        "Priority": "High" if failed_provisioning_count > 0 else "Standard"
    },
    {
        "Governance Area": "Manual Reviews",
        "Current Count": manual_review_ticket_count + manual_review_hr_intakes + manual_review_provisioning_count,
        "Risk Signal": "Access decisions requiring human validation",
        "Recommended Owner": "IAM Governance",
        "Priority": "High" if manual_review_ticket_count + manual_review_hr_intakes + manual_review_provisioning_count > 0 else "Standard"
    },
    {
        "Governance Area": "Immediate Offboarding",
        "Current Count": immediate_offboarding_count,
        "Risk Signal": "High-risk leaver activity requiring immediate disablement",
        "Recommended Owner": "HR / Security / IAM",
        "Priority": "Critical" if immediate_offboarding_count > 0 else "Standard"
    },
    {
        "Governance Area": "Audit Evidence",
        "Current Count": audit_evidence_records,
        "Risk Signal": "Recorded evidence for lifecycle and provisioning decisions",
        "Recommended Owner": "Compliance / IAM Governance",
        "Priority": "Standard"
    }
]

governance_control_df = pd.DataFrame(governance_control_summary)
st.dataframe(governance_control_df, use_container_width=True)

st.write("### Governance Risk Dashboard")

governance_risk_chart_data = pd.DataFrame(
    [
        {"Metric": "Open Approvals", "Count": open_approval_count},
        {"Metric": "High Risk Items", "Count": total_high_risk_lifecycle_events},
        {"Metric": "Provisioning Failures", "Count": failed_provisioning_count},
        {"Metric": "Manual Reviews", "Count": manual_review_ticket_count + manual_review_hr_intakes + manual_review_provisioning_count},
        {"Metric": "Immediate Offboarding", "Count": immediate_offboarding_count},
        {"Metric": "Audit Evidence Records", "Count": audit_evidence_records}
    ]
)

st.dataframe(governance_risk_chart_data, use_container_width=True)

governance_risk_chart = px.bar(
    governance_risk_chart_data,
    x="Metric",
    y="Count",
    title="IdentityOS Governance Risk and Evidence Summary"
)

st.plotly_chart(governance_risk_chart, use_container_width=True)

st.write("### Operational Response Plan")

response_plan = []

if open_approval_count > 0:
    response_plan.append(
        {
            "Action Item": "Review open approval tickets",
            "Why It Matters": "Pending approvals can delay provisioning or offboarding workflows.",
            "Owner": "IAM Operations / Approvers",
            "Status": "Action Recommended"
        }
    )

if total_high_risk_lifecycle_events > 0:
    response_plan.append(
        {
            "Action Item": "Validate high-risk identity events",
            "Why It Matters": "High-risk lifecycle activity may require additional security review.",
            "Owner": "Security / IAM Leadership",
            "Status": "Action Recommended"
        }
    )

if failed_provisioning_count > 0:
    response_plan.append(
        {
            "Action Item": "Investigate failed provisioning actions",
            "Why It Matters": "Failed provisioning can leave access incomplete, excessive, or inconsistent.",
            "Owner": "IAM Engineering",
            "Status": "Action Required"
        }
    )

if immediate_offboarding_count > 0:
    response_plan.append(
        {
            "Action Item": "Confirm immediate offboarding completion",
            "Why It Matters": "High-risk leavers require fast account disablement, access removal, and session revocation.",
            "Owner": "HR / Security / IAM",
            "Status": "Critical"
        }
    )

if manual_review_ticket_count + manual_review_hr_intakes + manual_review_provisioning_count > 0:
    response_plan.append(
        {
            "Action Item": "Resolve manual review queue",
            "Why It Matters": "Manual review items need validation before access is granted, changed, or removed.",
            "Owner": "IAM Governance",
            "Status": "Action Recommended"
        }
    )

if not response_plan:
    response_plan.append(
        {
            "Action Item": "Continue monitoring identity lifecycle activity",
            "Why It Matters": "No urgent governance issues are currently visible in the recorded IdentityOS activity.",
            "Owner": "IAM Governance",
            "Status": "Monitoring"
        }
    )

response_plan_df = pd.DataFrame(response_plan)
st.dataframe(response_plan_df, use_container_width=True)

st.info(
    "Executive Governance Note: The Governance Control Center gives IdentityOS a consolidated "
    "view of identity risk, operational workload, approval health, provisioning outcomes, and "
    "audit evidence. In a production environment, this could support IAM leadership reporting, "
    "audit readiness, access review programs, and security operations handoffs."
)
# ------------------------------------------------------------
# IdentityOS - Data Persistence Layer
# ------------------------------------------------------------

st.markdown("---")
st.header("IdentityOS Data Persistence Layer")

st.markdown(
    """
    This section manages local JSON persistence for IdentityOS workflow data.
    It allows HR intakes, approval tickets, provisioning history, lifecycle audit
    logs, and persistence events to survive application restarts.
    """
)

st.write("### Persistence Storage Location")

st.code(str(IDENTITYOS_STATE_DIR), language="text")

persistence_summary = []

for state_key, state_path in IDENTITYOS_STATE_FILES.items():
    records = st.session_state.get(state_key, [])

    persistence_summary.append(
        {
            "State Object": state_key,
            "Record Count": len(records),
            "Storage File": str(state_path.name),
            "File Exists": "Yes" if state_path.exists() else "No"
        }
    )

persistence_summary_df = pd.DataFrame(persistence_summary)

st.write("### Persisted IdentityOS State Objects")
st.dataframe(persistence_summary_df, use_container_width=True)

persist_metric_col1, persist_metric_col2, persist_metric_col3 = st.columns(3)

with persist_metric_col1:
    total_persisted_records = persistence_summary_df["Record Count"].sum()
    st.metric("Total Workflow Records", int(total_persisted_records))

with persist_metric_col2:
    existing_file_count = persistence_summary_df[
        persistence_summary_df["File Exists"] == "Yes"
    ].shape[0]
    st.metric("State Files Created", existing_file_count)

with persist_metric_col3:
    tracked_state_count = len(IDENTITYOS_STATE_FILES)
    st.metric("Tracked State Objects", tracked_state_count)

st.write("### Persistence Actions")

persist_action_col1, persist_action_col2 = st.columns(2)

with persist_action_col1:
    if st.button("Save IdentityOS State to Disk"):
        record_persistence_event(
            "Save",
            "IdentityOS workflow state saved to local JSON files."
        )

        save_identityos_state_to_disk()

        st.success("IdentityOS state saved to disk.")

with persist_action_col2:
    if st.button("Reload IdentityOS State from Disk"):
        for state_key, state_path in IDENTITYOS_STATE_FILES.items():
            st.session_state[state_key] = load_state_file(state_path)

        record_persistence_event(
            "Load",
            "IdentityOS workflow state reloaded from local JSON files."
        )

        save_identityos_state_to_disk()

        st.success("IdentityOS state reloaded from disk.")

st.write("### Persistence Event Log")

if st.session_state.get("identityos_persistence_events", []):
    persistence_events_df = pd.DataFrame(
        st.session_state.identityos_persistence_events
    )

    st.dataframe(persistence_events_df, use_container_width=True)

    persistence_event_summary = (
        persistence_events_df.groupby("Event Type")
        .size()
        .reset_index(name="Event Count")
    )

    st.write("### Persistence Events by Type")
    st.dataframe(persistence_event_summary, use_container_width=True)

    persistence_event_chart = px.bar(
        persistence_event_summary,
        x="Event Type",
        y="Event Count",
        title="IdentityOS Persistence Events"
    )

    st.plotly_chart(persistence_event_chart, use_container_width=True)

else:
    st.warning("No persistence events have been recorded yet.")

st.info(
    "IAM Platform Note: The Data Persistence Layer moves IdentityOS closer to operating "
    "system behavior by retaining workflow records across application restarts. In a production "
    "environment, this layer could be replaced with a database such as PostgreSQL, Azure SQL, "
    "Cosmos DB, or another enterprise data store."
)
