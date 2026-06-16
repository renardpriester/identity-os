from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import json
from typing import Any, Dict, List


ROOT_DIR = Path(__file__).resolve().parents[1]

EVENTS_FILE = ROOT_DIR / "examples" / "sample-identity-events.json"
DECISIONS_FILE = ROOT_DIR / "examples" / "sample-policy-decisions.json"

REPORTS_DIR = ROOT_DIR / "reports"
REPORT_FILE = REPORTS_DIR / "sample-governance-report.md"


def load_json(file_path: Path) -> Dict[str, Any]:
    """Load JSON data from a file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Required file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_identity_name(identity: Dict[str, Any]) -> str:
    """Return the best available display name for an identity."""
    if "user_principal_name" in identity:
        return identity["user_principal_name"]

    if "identity_name" in identity:
        return identity["identity_name"]

    first_name = identity.get("first_name", "")
    last_name = identity.get("last_name", "")
    full_name = f"{first_name} {last_name}".strip()

    return full_name if full_name else "Unknown Identity"


def format_list(items: List[str]) -> str:
    """Format a list for Markdown output."""
    if not items:
        return "None"

    return ", ".join(items)


def build_event_lookup(events: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Map identity events by event ID."""
    return {
        event["event_id"]: event
        for event in events
        if "event_id" in event
    }


def count_by_field(decisions: List[Dict[str, Any]], field_name: str) -> Counter:
    """Count decisions by a top-level field."""
    return Counter(
        decision.get(field_name, "Unknown")
        for decision in decisions
    )


def count_by_governance_field(decisions: List[Dict[str, Any]], field_name: str) -> Counter:
    """Count decisions by a governance field."""
    return Counter(
        decision.get("governance", {}).get(field_name, "Unknown")
        for decision in decisions
    )


def markdown_table(headers: List[str], rows: List[List[Any]]) -> str:
    """Create a Markdown table."""
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"

    body_rows = [
        "| " + " | ".join(str(value) for value in row) + " |"
        for row in rows
    ]

    return "\n".join([header_row, separator_row] + body_rows)


def generate_report(events: List[Dict[str, Any]], decisions: List[Dict[str, Any]]) -> str:
    """Generate a Markdown governance report."""
    event_lookup = build_event_lookup(events)

    policy_result_counts = count_by_field(decisions, "policy_result")
    risk_counts = count_by_governance_field(decisions, "risk_level")

    pending_approval = policy_result_counts.get("Pending Approval", 0)
    review_required = policy_result_counts.get("Review Required", 0)
    high_risk = risk_counts.get("High", 0)
    critical_risk = risk_counts.get("Critical", 0)

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    report_lines = [
        "# IdentityOS Sample Governance Report",
        "",
        f"Generated: {generated_at}",
        "",
        "## Executive Summary",
        "",
        "This report summarizes sample IdentityOS policy decisions, governance requirements, risk levels, and access actions.",
        "",
        markdown_table(
            ["Metric", "Value"],
            [
                ["Total Policy Decisions", len(decisions)],
                ["Pending Approval", pending_approval],
                ["Review Required", review_required],
                ["High Risk Decisions", high_risk],
                ["Critical Risk Decisions", critical_risk],
            ],
        ),
        "",
        "## Policy Decision Outcomes",
        "",
        markdown_table(
            ["Policy Result", "Count"],
            [[result, count] for result, count in sorted(policy_result_counts.items())],
        ),
        "",
        "## Risk Distribution",
        "",
        markdown_table(
            ["Risk Level", "Count"],
            [[risk_level, count] for risk_level, count in sorted(risk_counts.items())],
        ),
        "",
        "## Governance Actions Required",
        "",
    ]

    governance_rows = []

    for decision in decisions:
        governance = decision.get("governance", {})
        related_event_id = decision.get("related_event_id", "Unknown")
        event = event_lookup.get(related_event_id, {})
        identity = get_identity_name(event.get("identity", {}))

        governance_rows.append(
            [
                decision.get("decision_id", "Unknown"),
                related_event_id,
                identity,
                decision.get("policy_result", "Unknown"),
                governance.get("approval_required", "Unknown"),
                governance.get("review_frequency", "Unknown"),
                governance.get("risk_level", "Unknown"),
                governance.get("expiration_required", "Unknown"),
            ]
        )

    report_lines.extend(
        [
            markdown_table(
                [
                    "Decision ID",
                    "Event ID",
                    "Identity",
                    "Policy Result",
                    "Approval Required",
                    "Review Frequency",
                    "Risk Level",
                    "Expiration Required",
                ],
                governance_rows,
            ),
            "",
            "## Access Remediation Summary",
            "",
        ]
    )

    remediation_rows = []

    for decision in decisions:
        access_to_remove = decision.get("access_to_remove", [])

        if access_to_remove:
            related_event_id = decision.get("related_event_id", "Unknown")
            event = event_lookup.get(related_event_id, {})
            identity = get_identity_name(event.get("identity", {}))

            remediation_rows.append(
                [
                    decision.get("decision_id", "Unknown"),
                    related_event_id,
                    identity,
                    format_list(access_to_remove),
                ]
            )

    if remediation_rows:
        report_lines.append(
            markdown_table(
                ["Decision ID", "Event ID", "Identity", "Access to Remove"],
                remediation_rows,
            )
        )
    else:
        report_lines.append("No access removals were identified in the sample decisions.")

    report_lines.extend(
        [
            "",
            "## Detailed Policy Decisions",
            "",
        ]
    )

    for decision in decisions:
        related_event_id = decision.get("related_event_id", "Unknown")
        event = event_lookup.get(related_event_id, {})
        identity = get_identity_name(event.get("identity", {}))
        governance = decision.get("governance", {})
        audit = decision.get("audit", {})

        report_lines.extend(
            [
                f"### {decision.get('decision_id', 'Unknown Decision')}",
                "",
                markdown_table(
                    ["Field", "Value"],
                    [
                        ["Related Event", related_event_id],
                        ["Event Type", event.get("event_type", "Unknown")],
                        ["Identity", identity],
                        ["Policy Result", decision.get("policy_result", "Unknown")],
                        ["Decision Summary", decision.get("decision_summary", "No summary provided")],
                        ["Access to Grant", format_list(decision.get("access_to_grant", []))],
                        ["Access to Remove", format_list(decision.get("access_to_remove", []))],
                        ["Controls Required", format_list(decision.get("controls_required", []))],
                        ["Approval Required", governance.get("approval_required", "Unknown")],
                        ["Review Frequency", governance.get("review_frequency", "Unknown")],
                        ["Risk Level", governance.get("risk_level", "Unknown")],
                        ["Expiration Required", governance.get("expiration_required", "Unknown")],
                        ["Audit Required", audit.get("audit_required", "Unknown")],
                        ["Audit Reason", audit.get("reason", "No reason provided")],
                    ],
                ),
                "",
            ]
        )

    report_lines.extend(
        [
            "## Summary",
            "",
            "This sample report demonstrates how IdentityOS can turn identity policy decisions into governance visibility.",
            "",
            "The same pattern could be extended to support audit reporting, executive dashboards, access review evidence, privileged access reporting, and identity risk analytics.",
            "",
            "> IdentityOS turns access decisions into governance evidence.",
            "",
        ]
    )

    return "\n".join(report_lines)


def main() -> None:
    """Generate the sample governance report."""
    events_data = load_json(EVENTS_FILE)
    decisions_data = load_json(DECISIONS_FILE)

    events = events_data.get("events", [])
    decisions = decisions_data.get("policy_decisions", [])

    REPORTS_DIR.mkdir(exist_ok=True)

    report = generate_report(events, decisions)

    with REPORT_FILE.open("w", encoding="utf-8") as file:
        file.write(report)

    print(f"Governance report generated: {REPORT_FILE}")


if __name__ == "__main__":
    main()