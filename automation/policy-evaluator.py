from pathlib import Path
import json
from typing import Any, Dict, List


ROOT_DIR = Path(__file__).resolve().parents[1]

EVENTS_FILE = ROOT_DIR / "examples" / "sample-identity-events.json"
DECISIONS_FILE = ROOT_DIR / "examples" / "sample-policy-decisions.json"


def load_json(file_path: Path) -> Dict[str, Any]:
    """Load JSON data from a file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Required file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def format_list(items: List[str]) -> str:
    """Format a list of values for console output."""
    if not items:
        return "None"

    return ", ".join(items)


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


def build_decision_lookup(decisions: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Map policy decisions to their related event IDs."""
    return {
        decision["related_event_id"]: decision
        for decision in decisions
        if "related_event_id" in decision
    }


def print_header(title: str) -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def print_event_evaluation(event: Dict[str, Any], decision: Dict[str, Any]) -> None:
    """Print a readable IdentityOS policy evaluation summary."""
    identity = event.get("identity", {})
    governance = decision.get("governance", {})
    audit = decision.get("audit", {})

    print_header(f"IdentityOS Policy Evaluation: {event.get('event_id')}")

    print(f"Event Type:        {event.get('event_type')}")
    print(f"Source System:     {event.get('source_system')}")
    print(f"Identity:          {get_identity_name(identity)}")
    print(f"Policy Result:     {decision.get('policy_result')}")
    print(f"Decision Summary:  {decision.get('decision_summary')}")

    print("\nAccess Decision")
    print("-" * 80)
    print(f"Grant Access:      {format_list(decision.get('access_to_grant', []))}")
    print(f"Remove Access:     {format_list(decision.get('access_to_remove', []))}")
    print(f"Controls Required: {format_list(decision.get('controls_required', []))}")

    print("\nGovernance")
    print("-" * 80)
    print(f"Approval Required: {governance.get('approval_required', 'Unknown')}")
    print(f"Review Frequency:  {governance.get('review_frequency', 'Unknown')}")
    print(f"Risk Level:        {governance.get('risk_level', 'Unknown')}")
    print(f"Expiration Req.:   {governance.get('expiration_required', 'Unknown')}")

    if governance.get("approver"):
        print(f"Approver:          {governance.get('approver')}")

    if governance.get("expiration_date"):
        print(f"Expiration Date:   {governance.get('expiration_date')}")

    print("\nAudit")
    print("-" * 80)
    print(f"Audit Required:    {audit.get('audit_required', 'Unknown')}")
    print(f"Audit Reason:      {audit.get('reason', 'No reason provided')}")


def print_summary(decisions: List[Dict[str, Any]]) -> None:
    """Print high-level decision metrics."""
    total = len(decisions)

    pending_approval = sum(
        1 for decision in decisions
        if decision.get("policy_result") == "Pending Approval"
    )

    review_required = sum(
        1 for decision in decisions
        if decision.get("policy_result") == "Review Required"
    )

    critical_risk = sum(
        1 for decision in decisions
        if decision.get("governance", {}).get("risk_level") == "Critical"
    )

    high_risk = sum(
        1 for decision in decisions
        if decision.get("governance", {}).get("risk_level") == "High"
    )

    print_header("IdentityOS Evaluation Summary")
    print(f"Total Decisions:          {total}")
    print(f"Pending Approval:         {pending_approval}")
    print(f"Review Required:          {review_required}")
    print(f"High Risk Decisions:      {high_risk}")
    print(f"Critical Risk Decisions:  {critical_risk}")


def main() -> None:
    """Run the IdentityOS sample policy evaluator."""
    events_data = load_json(EVENTS_FILE)
    decisions_data = load_json(DECISIONS_FILE)

    events = events_data.get("events", [])
    decisions = decisions_data.get("policy_decisions", [])

    decision_lookup = build_decision_lookup(decisions)

    print_header("IdentityOS Sample Policy Evaluator")
    print("Reading identity events and matching them to policy decisions...")

    for event in events:
        event_id = event.get("event_id")
        decision = decision_lookup.get(event_id)

        if not decision:
            print_header(f"No Policy Decision Found for Event: {event_id}")
            continue

        print_event_evaluation(event, decision)

    print_summary(decisions)


if __name__ == "__main__":
    main()