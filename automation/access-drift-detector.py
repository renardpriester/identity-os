from pathlib import Path
from datetime import datetime, timezone
import json
from typing import Any, Dict, List


ROOT_DIR = Path(__file__).resolve().parents[1]

EVENTS_FILE = ROOT_DIR / "examples" / "sample-identity-events.json"
DECISIONS_FILE = ROOT_DIR / "examples" / "sample-policy-decisions.json"

REPORTS_DIR = ROOT_DIR / "reports"
DRIFT_REPORT_FILE = REPORTS_DIR / "sample-access-drift-report.md"


PRIVILEGED_ACCESS_KEYWORDS = [
    "admin",
    "administrator",
    "privileged",
    "eligible",
    "security reader",
    "global administrator",
    "user administrator",
    "security administrator",
]

SENSITIVE_ACCESS_KEYWORDS = [
    "finance",
    "financial",
    "legal document",
    "security",
    "endpoint",
    "reporting",
    "hr",
    "payroll",
    "confidential",
    "sensitive",
]


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


def build_event_lookup(events: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Map identity events by event ID."""
    return {
        event["event_id"]: event
        for event in events
        if "event_id" in event
    }


def contains_keyword(values: List[str], keywords: List[str]) -> bool:
    """Return True if any value contains one of the supplied keywords."""
    combined_values = " ".join(values).lower()

    return any(keyword in combined_values for keyword in keywords)


def format_list(items: List[str]) -> str:
    """Format a list for console and report output."""
    if not items:
        return "None"

    return ", ".join(items)


def get_severity_rank(severity: str) -> int:
    """Return a numeric severity rank for sorting."""
    ranks = {
        "None": 0,
        "Low": 1,
        "Medium": 2,
        "High": 3,
        "Critical": 4,
    }

    return ranks.get(severity, 0)


def get_recommended_remediation(drift_type: str) -> str:
    """Return recommended remediation based on drift type."""
    recommendations = {
        "No Drift": "No remediation required.",
        "Department Drift": "Remove access from the previous department and create audit evidence.",
        "Role Drift": "Remove access outside the current role package and validate expected access.",
        "Leaver Drift": "Disable identity, revoke sessions, remove all access, and notify security if privileged access exists.",
        "Contractor Drift": "Disable contractor access unless sponsor renewal is approved.",
        "Vendor Drift": "Remove vendor access or validate current business sponsorship.",
        "Privilege Drift": "Remove or review privileged access immediately.",
        "Non-Human Identity Drift": "Validate owner, business purpose, access scope, and credential governance.",
        "Governance Drift": "Route access for review and track remediation outcome.",
    }

    return recommendations.get(drift_type, "Review access and determine remediation.")


def detect_access_drift(event: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    """Detect access drift from sample event and policy decision data."""
    event_type = event.get("event_type", "Unknown")
    event_type_lower = event_type.lower()

    identity = event.get("identity", {})
    identity_name = get_identity_name(identity)

    access_to_grant = decision.get("access_to_grant", [])
    access_to_remove = decision.get("access_to_remove", [])
    controls_required = decision.get("controls_required", [])

    actual_access = access_to_grant + access_to_remove
    expected_access = access_to_grant
    excess_access = access_to_remove

    drift_detected = False
    drift_type = "No Drift"
    drift_severity = "None"
    drift_reason = "Actual access appears aligned with the sample policy decision."

    privileged_drift = contains_keyword(excess_access, PRIVILEGED_ACCESS_KEYWORDS)
    sensitive_drift = contains_keyword(excess_access, SENSITIVE_ACCESS_KEYWORDS)

    # Mover drift: access from prior role or department should be removed.
    if event_type_lower == "mover" and excess_access:
        drift_detected = True
        drift_type = "Department Drift"
        drift_severity = "High"
        drift_reason = "Mover event includes access from the previous role or department that should be removed."

    # Leaver drift: any remaining access for a leaver is critical.
    elif event_type_lower == "leaver" and excess_access:
        drift_detected = True
        drift_type = "Leaver Drift"
        drift_severity = "Critical"
        drift_reason = "Leaver event includes access that must be removed during offboarding."

    # Contractor expiration drift.
    elif "contractor_expiration" in event_type_lower and excess_access:
        drift_detected = True
        drift_type = "Contractor Drift"
        drift_severity = "Critical"
        drift_reason = "Contractor access is expiring or expired and should not remain active without renewal."

    # Vendor drift.
    elif "vendor" in event_type_lower and excess_access:
        drift_detected = True
        drift_type = "Vendor Drift"
        drift_severity = "High"
        drift_reason = "Vendor access requires active business sponsorship and review."

    # Privileged drift.
    elif privileged_drift:
        drift_detected = True
        drift_type = "Privilege Drift"
        drift_severity = "Critical"
        drift_reason = "Privileged access was identified as excess or removable access."

    # Non-human identity drift.
    elif "non_human" in event_type_lower:
        owner_fields = [
            identity.get("owner"),
            identity.get("business_owner"),
            identity.get("technical_owner"),
            identity.get("manager"),
            identity.get("sponsor"),
        ]

        if not any(owner_fields) or decision.get("policy_result") == "Review Required":
            drift_detected = True
            drift_type = "Non-Human Identity Drift"
            drift_severity = "High"
            drift_reason = "Non-human identity requires owner, purpose, scope, and credential governance review."

    # Governance drift: review required but no direct access removal listed.
    elif decision.get("policy_result") == "Review Required":
        drift_detected = True
        drift_type = "Governance Drift"
        drift_severity = "Medium"
        drift_reason = "Policy decision requires review before access can be considered fully aligned."

    # Escalate severity if sensitive or privileged access appears in excess access.
    if drift_detected and sensitive_drift and drift_severity in ["Low", "Medium"]:
        drift_severity = "High"

    if drift_detected and privileged_drift:
        drift_severity = "Critical"

    return {
        "event_id": event.get("event_id", "Unknown"),
        "event_type": event_type,
        "decision_id": decision.get("decision_id", "Unknown"),
        "identity": identity_name,
        "drift_detected": drift_detected,
        "drift_type": drift_type,
        "drift_severity": drift_severity,
        "expected_access": expected_access,
        "actual_access": actual_access,
        "excess_access": excess_access,
        "controls_required": controls_required,
        "drift_reason": drift_reason,
        "recommended_remediation": get_recommended_remediation(drift_type),
    }


def markdown_table(headers: List[str], rows: List[List[Any]]) -> str:
    """Create a Markdown table."""
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"

    body_rows = [
        "| " + " | ".join(str(value) for value in row) + " |"
        for row in rows
    ]

    return "\n".join([header_row, separator_row] + body_rows)


def generate_drift_report(results: List[Dict[str, Any]]) -> str:
    """Generate a Markdown access drift report."""
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    total = len(results)
    drift_detected = sum(1 for result in results if result["drift_detected"])
    high = sum(1 for result in results if result["drift_severity"] == "High")
    critical = sum(1 for result in results if result["drift_severity"] == "Critical")

    sorted_results = sorted(
        results,
        key=lambda result: get_severity_rank(result["drift_severity"]),
        reverse=True,
    )

    report_lines = [
        "# IdentityOS Sample Access Drift Report",
        "",
        f"Generated: {generated_at}",
        "",
        "## Executive Summary",
        "",
        "This report summarizes sample access drift detected from IdentityOS lifecycle events and policy decisions.",
        "",
        markdown_table(
            ["Metric", "Value"],
            [
                ["Total Evaluated Decisions", total],
                ["Drift Detected", drift_detected],
                ["High Severity Drift", high],
                ["Critical Severity Drift", critical],
            ],
        ),
        "",
        "## Drift Summary",
        "",
        markdown_table(
            [
                "Decision ID",
                "Event ID",
                "Event Type",
                "Identity",
                "Drift Type",
                "Severity",
                "Recommended Remediation",
            ],
            [
                [
                    result["decision_id"],
                    result["event_id"],
                    result["event_type"],
                    result["identity"],
                    result["drift_type"],
                    result["drift_severity"],
                    result["recommended_remediation"],
                ]
                for result in sorted_results
            ],
        ),
        "",
        "## Detailed Drift Findings",
        "",
    ]

    for result in sorted_results:
        report_lines.extend(
            [
                f"### {result['decision_id']} - {result['identity']}",
                "",
                markdown_table(
                    ["Field", "Value"],
                    [
                        ["Event ID", result["event_id"]],
                        ["Event Type", result["event_type"]],
                        ["Drift Detected", result["drift_detected"]],
                        ["Drift Type", result["drift_type"]],
                        ["Drift Severity", result["drift_severity"]],
                        ["Expected Access", format_list(result["expected_access"])],
                        ["Actual Access", format_list(result["actual_access"])],
                        ["Excess Access", format_list(result["excess_access"])],
                        ["Controls Required", format_list(result["controls_required"])],
                        ["Drift Reason", result["drift_reason"]],
                        ["Recommended Remediation", result["recommended_remediation"]],
                    ],
                ),
                "",
            ]
        )

    report_lines.extend(
        [
            "## Summary",
            "",
            "This report demonstrates how IdentityOS can identify access that no longer aligns with expected access.",
            "",
            "Access drift detection helps reduce privilege creep, stale access, excessive permissions, and unmanaged access risk.",
            "",
            "> Access drift is how yesterday’s permissions become tomorrow’s risk.",
            "",
        ]
    )

    return "\n".join(report_lines)


def print_results(results: List[Dict[str, Any]]) -> None:
    """Print access drift results to the console."""
    print("\n" + "=" * 80)
    print("IdentityOS Sample Access Drift Detector")
    print("=" * 80)

    for result in results:
        print()
        print(f"Decision ID:              {result['decision_id']}")
        print(f"Event ID:                 {result['event_id']}")
        print(f"Event Type:               {result['event_type']}")
        print(f"Identity:                 {result['identity']}")
        print(f"Drift Detected:           {result['drift_detected']}")
        print(f"Drift Type:               {result['drift_type']}")
        print(f"Drift Severity:           {result['drift_severity']}")
        print(f"Excess Access:            {format_list(result['excess_access'])}")
        print(f"Recommended Remediation:  {result['recommended_remediation']}")

    print("\n" + "=" * 80)
    print("Access drift detection complete")
    print("=" * 80)


def main() -> None:
    """Run IdentityOS sample access drift detection."""
    events_data = load_json(EVENTS_FILE)
    decisions_data = load_json(DECISIONS_FILE)

    events = events_data.get("events", [])
    decisions = decisions_data.get("policy_decisions", [])

    event_lookup = build_event_lookup(events)

    results = []

    for decision in decisions:
        related_event_id = decision.get("related_event_id")
        event = event_lookup.get(related_event_id)

        if not event:
            continue

        results.append(detect_access_drift(event, decision))

    REPORTS_DIR.mkdir(exist_ok=True)

    drift_report = generate_drift_report(results)

    with DRIFT_REPORT_FILE.open("w", encoding="utf-8") as file:
        file.write(drift_report)

    print_results(results)
    print(f"\nAccess drift report generated: {DRIFT_REPORT_FILE}")


if __name__ == "__main__":
    main()