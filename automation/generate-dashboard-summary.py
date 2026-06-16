from pathlib import Path
from datetime import datetime, timezone
import json
from typing import Any, Dict, List


ROOT_DIR = Path(__file__).resolve().parents[1]

DASHBOARD_METRICS_FILE = ROOT_DIR / "examples" / "sample-dashboard-metrics.json"

REPORTS_DIR = ROOT_DIR / "reports"
DASHBOARD_REPORT_FILE = REPORTS_DIR / "sample-dashboard-summary.md"


def load_json(file_path: Path) -> Dict[str, Any]:
    """Load JSON data from a file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Required file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def format_label(value: str) -> str:
    """Format snake_case keys for Markdown display."""
    return value.replace("_", " ").title()


def markdown_table(headers: List[str], rows: List[List[Any]]) -> str:
    """Create a Markdown table."""
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"

    body_rows = [
        "| " + " | ".join(str(value) for value in row) + " |"
        for row in rows
    ]

    return "\n".join([header_row, separator_row] + body_rows)


def build_metric_table(metric_group: Dict[str, Any]) -> str:
    """Build a Markdown table from a metric group."""
    rows = [
        [format_label(metric_name), metric_value]
        for metric_name, metric_value in metric_group.items()
    ]

    return markdown_table(["Metric", "Value"], rows)


def generate_dashboard_summary(data: Dict[str, Any]) -> str:
    """Generate a Markdown dashboard summary report."""
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    metrics = data.get("metrics", {})
    dashboard_views = data.get("dashboard_views", [])

    report_lines = [
        "# IdentityOS Sample Dashboard Summary",
        "",
        f"Generated: {generated_at}",
        "",
        "## Overview",
        "",
        data.get(
            "description",
            "This report summarizes sample IdentityOS dashboard metrics.",
        ),
        "",
        markdown_table(
            ["Field", "Value"],
            [
                ["Dashboard Name", data.get("dashboard_name", "Unknown")],
                ["Version", data.get("version", "Unknown")],
                ["Data Classification", data.get("data_classification", "Unknown")],
            ],
        ),
        "",
        "## Executive Identity Risk",
        "",
        build_metric_table(metrics.get("executive_identity_risk", {})),
        "",
        "## Lifecycle Operations",
        "",
        build_metric_table(metrics.get("lifecycle_operations", {})),
        "",
        "## Governance",
        "",
        build_metric_table(metrics.get("governance", {})),
        "",
        "## Risk Scoring",
        "",
        build_metric_table(metrics.get("risk_scoring", {})),
        "",
        "## Access Drift",
        "",
        build_metric_table(metrics.get("access_drift", {})),
        "",
        "## Automation Health",
        "",
        build_metric_table(metrics.get("automation_health", {})),
        "",
        "## Dashboard Views",
        "",
    ]

    view_rows = [
        [
            view.get("view_name", "Unknown"),
            view.get("primary_audience", "Unknown"),
            view.get("focus", "Unknown"),
        ]
        for view in dashboard_views
    ]

    report_lines.extend(
        [
            markdown_table(
                ["View Name", "Primary Audience", "Focus"],
                view_rows,
            ),
            "",
            "## Dashboard Interpretation",
            "",
            "The sample dashboard metrics show how IdentityOS can present identity activity as operational, governance, risk, and executive visibility.",
            "",
            "These dashboard concepts help connect identity engineering work to business outcomes such as risk reduction, faster lifecycle processing, stronger governance, and better audit readiness.",
            "",
            "## Summary",
            "",
            "This sample dashboard summary demonstrates how IdentityOS can convert identity events, policy decisions, governance outcomes, risk scoring, access drift detection, and automation activity into dashboard-ready reporting.",
            "",
            "> Identity dashboards make trust visible.",
            "",
        ]
    )

    return "\n".join(report_lines)


def print_summary(data: Dict[str, Any]) -> None:
    """Print a short console summary."""
    metrics = data.get("metrics", {})
    executive = metrics.get("executive_identity_risk", {})
    automation = metrics.get("automation_health", {})

    print("\n" + "=" * 80)
    print("IdentityOS Sample Dashboard Summary Generator")
    print("=" * 80)
    print(f"Dashboard Name:       {data.get('dashboard_name', 'Unknown')}")
    print(f"Version:              {data.get('version', 'Unknown')}")
    print(f"Total Decisions:      {executive.get('total_policy_decisions', 'Unknown')}")
    print(f"High Risk Decisions:  {executive.get('high_risk_decisions', 'Unknown')}")
    print(f"Critical Decisions:   {executive.get('critical_risk_decisions', 'Unknown')}")
    print(f"Access Drift Found:   {executive.get('access_drift_detected', 'Unknown')}")
    print(f"Reports Generated:    {automation.get('reports_generated', 'Unknown')}")
    print("=" * 80)


def main() -> None:
    """Generate the IdentityOS sample dashboard summary."""
    data = load_json(DASHBOARD_METRICS_FILE)

    REPORTS_DIR.mkdir(exist_ok=True)

    report = generate_dashboard_summary(data)

    with DASHBOARD_REPORT_FILE.open("w", encoding="utf-8") as file:
        file.write(report)

    print_summary(data)
    print(f"\nDashboard summary generated: {DASHBOARD_REPORT_FILE}")


if __name__ == "__main__":
    main()