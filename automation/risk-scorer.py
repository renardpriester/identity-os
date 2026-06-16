from pathlib import Path
from datetime import datetime, timezone
import json
from typing import Any, Dict, List


ROOT_DIR = Path(__file__).resolve().parents[1]

EVENTS_FILE = ROOT_DIR / "examples" / "sample-identity-events.json"
DECISIONS_FILE = ROOT_DIR / "examples" / "sample-policy-decisions.json"

REPORTS_DIR = ROOT_DIR / "reports"
RISK_REPORT_FILE = REPORTS_DIR / "sample-risk-score-report.md"


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


def add_factor(
    factors: List[Dict[str, Any]],
    name: str,
    points: int,
    reason: str,
) -> None:
    """Add a risk factor to the factor list."""
    factors.append(
        {
            "name": name,
            "points": points,
            "reason": reason,
        }
    )


def get_risk_level(score: int) -> str:
    """Convert numeric risk score to risk level."""
    if score <= 20:
        return "Low"

    if score <= 40:
        return "Medium"

    if score <= 70:
        return "High"

    return "Critical"


def get_recommended_action(risk_level: str) -> str:
    """Return a recommended governance action based on risk level."""
    actions = {
        "Low": "Retain access and follow normal review schedule.",
        "Medium": "Retain access with standard governance controls.",
        "High": "Trigger review, validate owner, confirm business need, and check for access drift.",
        "Critical": "Escalate for urgent review, require remediation, notify security if needed, and generate audit evidence.",
    }

    return actions.get(risk_level, "Review access decision.")


def score_decision(event: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    """Score a policy decision using IdentityOS sample risk rules."""
    factors: List[Dict[str, Any]] = []

    event_type = event.get("event_type", "Unknown")
    event_type_lower = event_type.lower()

    identity = event.get("identity", {})
    identity_name = get_identity_name(identity).lower()

    access_to_grant = decision.get("access_to_grant", [])
    access_to_remove = decision.get("access_to_remove", [])
    controls_required = decision.get("controls_required", [])

    all_access = access_to_grant + access_to_remove

    audit = decision.get("audit", {})
    audit_required = audit.get("audit_required", False)

    # Baseline access risk.
    if access_to_grant:
        add_factor(
            factors,
            "Standard business access",
            5,
            "Access is being granted and should be tracked.",
        )

    # Sensitive access.
    if contains_keyword(all_access, SENSITIVE_ACCESS_KEYWORDS):
        add_factor(
            factors,
            "Sensitive application access",
            20,
            "Access involves sensitive or business-critical systems.",
        )

    # Privileged access.
    privileged_signal = (
        event_type_lower == "privileged_access_request"
        or contains_keyword(all_access, PRIVILEGED_ACCESS_KEYWORDS)
    )

    if privileged_signal:
        add_factor(
            factors,
            "Privileged access",
            30,
            "Access includes elevated or security-relevant permissions.",
        )

    # Contractor risk.
    contractor_signal = "contractor" in event_type_lower or "contractor" in identity_name

    if contractor_signal:
        add_factor(
            factors,
            "Contractor identity",
            15,
            "Contractor identities require sponsorship, expiration, and review.",
        )

    # Vendor risk.
    vendor_signal = "vendor" in event_type_lower or "vendor" in identity_name

    if vendor_signal:
        add_factor(
            factors,
            "Vendor identity",
            20,
            "Vendor identities require business ownership and external access governance.",
        )

    # Non-human identity risk.
    non_human_signal = (
        "non_human" in event_type_lower
        or "service" in identity_name
        or identity_name.startswith("svc-")
    )

    if non_human_signal:
        add_factor(
            factors,
            "Non-human identity",
            20,
            "Service accounts and automation identities require ownership and credential governance.",
        )

        owner_fields = [
            identity.get("owner"),
            identity.get("business_owner"),
            identity.get("technical_owner"),
            identity.get("manager"),
            identity.get("sponsor"),
        ]

        if not any(owner_fields):
            add_factor(
                factors,
                "Missing owner",
                25,
                "Non-human identity does not show a clear owner in the sample event.",
            )

    # Contractor expiration risk.
    if "contractor_expiration" in event_type_lower:
        add_factor(
            factors,
            "Expired or expiring access",
            30,
            "Contractor access requires renewal or removal at expiration.",
        )

    # Mover access drift risk.
    if event_type_lower == "mover" and access_to_remove:
        add_factor(
            factors,
            "Access drift detected",
            25,
            "Mover event includes access that should be removed from the previous role.",
        )

        add_factor(
            factors,
            "Access outside role package",
            20,
            "Current access does not fully align with the new role.",
        )

    # Leaver risk.
    if event_type_lower == "leaver":
        add_factor(
            factors,
            "Leaver with active access",
            40,
            "Leaver event requires complete access removal.",
        )

        if privileged_signal:
            add_factor(
                factors,
                "Privileged leaver access",
                50,
                "Leaver event includes privileged or security-relevant access removal.",
            )

    # MFA control check.
    has_mfa = any(control.lower() == "mfa" for control in controls_required)

    if access_to_grant and privileged_signal and not has_mfa:
        add_factor(
            factors,
            "No MFA requirement",
            25,
            "Privileged or sensitive access is being granted without MFA listed as a required control.",
        )

    # Audit evidence check.
    if audit_required is not True:
        add_factor(
            factors,
            "No audit evidence",
            25,
            "Audit evidence is missing or not required for this decision.",
        )

    raw_score = sum(factor["points"] for factor in factors)
    score = min(raw_score, 100)
    risk_level = get_risk_level(score)

    return {
        "event_id": event.get("event_id", "Unknown"),
        "event_type": event_type,
        "decision_id": decision.get("decision_id", "Unknown"),
        "identity": get_identity_name(identity),
        "policy_result": decision.get("policy_result", "Unknown"),
        "risk_score": score,
        "risk_level": risk_level,
        "risk_factors": factors,
        "recommended_action": get_recommended_action(risk_level),
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


def generate_risk_report(results: List[Dict[str, Any]]) -> str:
    """Generate a Markdown risk scoring report."""
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    total = len(results)
    low = sum(1 for result in results if result["risk_level"] == "Low")
    medium = sum(1 for result in results if result["risk_level"] == "Medium")
    high = sum(1 for result in results if result["risk_level"] == "High")
    critical = sum(1 for result in results if result["risk_level"] == "Critical")

    report_lines = [
        "# IdentityOS Sample Risk Score Report",
        "",
        f"Generated: {generated_at}",
        "",
        "## Executive Summary",
        "",
        "This report summarizes sample IdentityOS risk scores calculated from identity events and policy decisions.",
        "",
        markdown_table(
            ["Metric", "Value"],
            [
                ["Total Scored Decisions", total],
                ["Low Risk", low],
                ["Medium Risk", medium],
                ["High Risk", high],
                ["Critical Risk", critical],
            ],
        ),
        "",
        "## Risk Score Summary",
        "",
        markdown_table(
            [
                "Decision ID",
                "Event ID",
                "Event Type",
                "Identity",
                "Risk Score",
                "Risk Level",
                "Recommended Action",
            ],
            [
                [
                    result["decision_id"],
                    result["event_id"],
                    result["event_type"],
                    result["identity"],
                    result["risk_score"],
                    result["risk_level"],
                    result["recommended_action"],
                ]
                for result in results
            ],
        ),
        "",
        "## Detailed Risk Factors",
        "",
    ]

    for result in results:
        factor_rows = [
            [
                factor["name"],
                factor["points"],
                factor["reason"],
            ]
            for factor in result["risk_factors"]
        ]

        report_lines.extend(
            [
                f"### {result['decision_id']} - {result['identity']}",
                "",
                markdown_table(
                    ["Field", "Value"],
                    [
                        ["Event ID", result["event_id"]],
                        ["Event Type", result["event_type"]],
                        ["Policy Result", result["policy_result"]],
                        ["Risk Score", result["risk_score"]],
                        ["Risk Level", result["risk_level"]],
                        ["Recommended Action", result["recommended_action"]],
                    ],
                ),
                "",
                "#### Risk Factors",
                "",
            ]
        )

        if factor_rows:
            report_lines.append(
                markdown_table(
                    ["Risk Factor", "Points", "Reason"],
                    factor_rows,
                )
            )
        else:
            report_lines.append("No risk factors were identified.")

        report_lines.append("")

    report_lines.extend(
        [
            "## Summary",
            "",
            "This report demonstrates how IdentityOS can calculate identity risk from lifecycle events, access decisions, governance conditions, and audit signals.",
            "",
            "Risk scoring helps prioritize review, remediation, escalation, and reporting.",
            "",
            "> Identity risk should be measurable, explainable, and actionable.",
            "",
        ]
    )

    return "\n".join(report_lines)


def print_results(results: List[Dict[str, Any]]) -> None:
    """Print risk scoring results to the console."""
    print("\n" + "=" * 80)
    print("IdentityOS Sample Risk Scorer")
    print("=" * 80)

    for result in results:
        print()
        print(f"Decision ID:        {result['decision_id']}")
        print(f"Event ID:           {result['event_id']}")
        print(f"Event Type:         {result['event_type']}")
        print(f"Identity:           {result['identity']}")
        print(f"Risk Score:         {result['risk_score']}")
        print(f"Risk Level:         {result['risk_level']}")
        print(f"Recommended Action: {result['recommended_action']}")

        print("Risk Factors:")

        if not result["risk_factors"]:
            print("  - None")
        else:
            for factor in result["risk_factors"]:
                print(f"  - {factor['name']} (+{factor['points']}): {factor['reason']}")

    print("\n" + "=" * 80)
    print("Risk scoring complete")
    print("=" * 80)


def main() -> None:
    """Run IdentityOS sample risk scoring."""
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

        results.append(score_decision(event, decision))

    REPORTS_DIR.mkdir(exist_ok=True)

    risk_report = generate_risk_report(results)

    with RISK_REPORT_FILE.open("w", encoding="utf-8") as file:
        file.write(risk_report)

    print_results(results)
    print(f"\nRisk score report generated: {RISK_REPORT_FILE}")


if __name__ == "__main__":
    main()