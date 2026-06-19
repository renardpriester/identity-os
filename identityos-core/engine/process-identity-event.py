import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "outputs"

ROLE_PACKAGES_PATH = DATA_DIR / "role-packages.json"
HR_EVENTS_PATH = DATA_DIR / "sample-hr-events.json"

TICKETS_DIR = OUTPUT_DIR / "tickets"
EVIDENCE_DIR = OUTPUT_DIR / "evidence"
DASHBOARD_DIR = OUTPUT_DIR / "dashboard"

TICKETS_OUTPUT_PATH = TICKETS_DIR / "tickets.json"
EVIDENCE_OUTPUT_PATH = EVIDENCE_DIR / "audit-evidence.json"
DASHBOARD_OUTPUT_PATH = DASHBOARD_DIR / "dashboard-output.json"


RISK_ORDER = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Critical": 4,
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def normalize(value: Any) -> str:
    if value is None:
        return ""

    return str(value).strip().lower()


def unique_list(values: List[str]) -> List[str]:
    seen = set()
    output = []

    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)

    return output


def highest_risk(risk_levels: List[str]) -> str:
    if not risk_levels:
        return "Low"

    return max(risk_levels, key=lambda level: RISK_ORDER.get(level, 0))


def get_role_packages() -> List[Dict[str, Any]]:
    data = load_json(ROLE_PACKAGES_PATH)
    return data.get("role_packages", [])


def get_identity_events() -> List[Dict[str, Any]]:
    data = load_json(HR_EVENTS_PATH)
    return data.get("identity_events", [])


def package_matches_event(
    package: Dict[str, Any],
    department: str,
    job_title: str,
    worker_type: str,
) -> bool:
    package_department = normalize(package.get("department"))
    package_worker_types = [normalize(item) for item in package.get("worker_types", [])]
    package_job_titles = [normalize(item) for item in package.get("job_titles", [])]

    department_match = package_department in [normalize(department), "all"]
    worker_type_match = normalize(worker_type) in package_worker_types
    job_title_match = (
        normalize(job_title) in package_job_titles
        or "all employees" in package_job_titles
    )

    return department_match and worker_type_match and job_title_match


def find_matching_packages(
    event: Dict[str, Any],
    department: str,
    job_title: str,
    worker_type: str,
    role_packages: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    matches = []

    for package in role_packages:
        if package_matches_event(package, department, job_title, worker_type):
            matches.append(package)

    return matches


def build_access_plan(packages: List[Dict[str, Any]]) -> List[str]:
    access_items = []

    for package in packages:
        access_items.extend(package.get("access", []))

    return unique_list(access_items)


def approval_required(packages: List[Dict[str, Any]]) -> bool:
    return any(package.get("approval_required", False) for package in packages)


def approval_owners(packages: List[Dict[str, Any]]) -> List[str]:
    owners = [
        package.get("approval_owner")
        for package in packages
        if package.get("approval_required", False)
    ]

    return unique_list([owner for owner in owners if owner])


def risk_from_packages(packages: List[Dict[str, Any]]) -> str:
    return highest_risk([package.get("risk_level", "Low") for package in packages])


def create_ticket(
    event: Dict[str, Any],
    title: str,
    approval_owner: str,
    risk_level: str,
    access_items: List[str],
) -> Dict[str, Any]:
    return {
        "ticket_id": f"TICKET-{event['event_id']}",
        "event_id": event["event_id"],
        "title": title,
        "requestor": event.get("display_name"),
        "approval_owner": approval_owner,
        "risk_level": risk_level,
        "status": "Pending Approval",
        "access_items": access_items,
        "created_at": utc_now(),
    }


def create_evidence_record(
    event: Dict[str, Any],
    decision_type: str,
    risk_level: str,
    access_to_add: List[str],
    access_to_remove: List[str],
    approval_required_value: bool,
    ticket_created: bool,
    drift_detected: bool,
) -> Dict[str, Any]:
    return {
        "evidence_id": f"EVID-{event['event_id']}",
        "event_id": event["event_id"],
        "event_type": event.get("event_type"),
        "identity": event.get("display_name"),
        "user_principal_name": event.get("user_principal_name"),
        "decision_type": decision_type,
        "risk_level": risk_level,
        "access_to_add": access_to_add,
        "access_to_remove": access_to_remove,
        "approval_required": approval_required_value,
        "ticket_created": ticket_created,
        "drift_detected": drift_detected,
        "audit_required": True,
        "status": "Generated",
        "generated_at": utc_now(),
    }


def process_joiner_like_event(
    event: Dict[str, Any],
    role_packages: List[Dict[str, Any]],
) -> Dict[str, Any]:
    department = event.get("department")
    job_title = event.get("job_title")
    worker_type = event.get("worker_type")

    packages = find_matching_packages(
        event=event,
        department=department,
        job_title=job_title,
        worker_type=worker_type,
        role_packages=role_packages,
    )

    access_to_add = build_access_plan(packages)
    risk_level = risk_from_packages(packages)
    requires_approval = approval_required(packages)
    owners = approval_owners(packages)

    tickets = []

    if requires_approval:
        tickets.append(
            create_ticket(
                event=event,
                title=f"Approval required for {event.get('display_name')}",
                approval_owner=", ".join(owners) if owners else "Access Owner",
                risk_level=risk_level,
                access_items=access_to_add,
            )
        )

    evidence = create_evidence_record(
        event=event,
        decision_type="Access Assignment Plan",
        risk_level=risk_level,
        access_to_add=access_to_add,
        access_to_remove=[],
        approval_required_value=requires_approval,
        ticket_created=bool(tickets),
        drift_detected=False,
    )

    return {
        "event": event,
        "matched_role_packages": [package.get("name") for package in packages],
        "access_to_add": access_to_add,
        "access_to_remove": [],
        "risk_level": risk_level,
        "approval_required": requires_approval,
        "tickets": tickets,
        "evidence": evidence,
    }


def process_mover_event(
    event: Dict[str, Any],
    role_packages: List[Dict[str, Any]],
) -> Dict[str, Any]:
    previous_packages = find_matching_packages(
        event=event,
        department=event.get("previous_department"),
        job_title=event.get("previous_job_title"),
        worker_type=event.get("worker_type"),
        role_packages=role_packages,
    )

    new_packages = find_matching_packages(
        event=event,
        department=event.get("new_department"),
        job_title=event.get("new_job_title"),
        worker_type=event.get("worker_type"),
        role_packages=role_packages,
    )

    current_access = event.get("current_access", [])
    expected_access = build_access_plan(new_packages)

    access_to_add = [item for item in expected_access if item not in current_access]
    access_to_remove = [item for item in current_access if item not in expected_access]

    drift_detected = bool(access_to_remove)
    risk_level = "High" if drift_detected else risk_from_packages(new_packages)

    requires_approval = approval_required(new_packages)
    owners = approval_owners(new_packages)

    tickets = []

    if requires_approval or drift_detected:
        tickets.append(
            create_ticket(
                event=event,
                title=f"Mover review required for {event.get('display_name')}",
                approval_owner=", ".join(owners) if owners else "Access Owner",
                risk_level=risk_level,
                access_items=access_to_add + access_to_remove,
            )
        )

    evidence = create_evidence_record(
        event=event,
        decision_type="Mover Access Change Plan",
        risk_level=risk_level,
        access_to_add=access_to_add,
        access_to_remove=access_to_remove,
        approval_required_value=requires_approval,
        ticket_created=bool(tickets),
        drift_detected=drift_detected,
    )

    return {
        "event": event,
        "previous_role_packages": [package.get("name") for package in previous_packages],
        "new_role_packages": [package.get("name") for package in new_packages],
        "access_to_add": access_to_add,
        "access_to_remove": access_to_remove,
        "risk_level": risk_level,
        "approval_required": requires_approval,
        "tickets": tickets,
        "evidence": evidence,
    }


def process_leaver_like_event(event: Dict[str, Any]) -> Dict[str, Any]:
    current_access = event.get("current_access", [])
    privileged_access = event.get("privileged_access", False)

    risk_level = "Critical" if privileged_access else "Medium"

    tickets = [
        create_ticket(
            event=event,
            title=f"Offboarding required for {event.get('display_name')}",
            approval_owner="IAM Operations",
            risk_level=risk_level,
            access_items=current_access,
        )
    ]

    evidence = create_evidence_record(
        event=event,
        decision_type="Access Removal Plan",
        risk_level=risk_level,
        access_to_add=[],
        access_to_remove=current_access,
        approval_required_value=True,
        ticket_created=True,
        drift_detected=bool(current_access),
    )

    return {
        "event": event,
        "access_to_add": [],
        "access_to_remove": current_access,
        "risk_level": risk_level,
        "approval_required": True,
        "tickets": tickets,
        "evidence": evidence,
    }


def process_privileged_access_request(event: Dict[str, Any]) -> Dict[str, Any]:
    requested_access = event.get("requested_access", [])
    risk_level = "High"

    tickets = [
        create_ticket(
            event=event,
            title=f"Privileged access approval required for {event.get('display_name')}",
            approval_owner="Security Manager",
            risk_level=risk_level,
            access_items=requested_access,
        )
    ]

    evidence = create_evidence_record(
        event=event,
        decision_type="Privileged Access Request",
        risk_level=risk_level,
        access_to_add=requested_access,
        access_to_remove=[],
        approval_required_value=True,
        ticket_created=True,
        drift_detected=False,
    )

    return {
        "event": event,
        "access_to_add": requested_access,
        "access_to_remove": [],
        "risk_level": risk_level,
        "approval_required": True,
        "tickets": tickets,
        "evidence": evidence,
    }


def process_event(
    event: Dict[str, Any],
    role_packages: List[Dict[str, Any]],
) -> Dict[str, Any]:
    event_type = normalize(event.get("event_type"))

    if event_type in ["joiner", "contractor_onboarding", "non_human_identity_review"]:
        return process_joiner_like_event(event, role_packages)

    if event_type == "mover":
        return process_mover_event(event, role_packages)

    if event_type in ["leaver", "contractor_expiration"]:
        return process_leaver_like_event(event)

    if event_type == "privileged_access_request":
        return process_privileged_access_request(event)

    evidence = create_evidence_record(
        event=event,
        decision_type="Unknown Event",
        risk_level="Medium",
        access_to_add=[],
        access_to_remove=[],
        approval_required_value=True,
        ticket_created=False,
        drift_detected=False,
    )

    return {
        "event": event,
        "access_to_add": [],
        "access_to_remove": [],
        "risk_level": "Medium",
        "approval_required": True,
        "tickets": [],
        "evidence": evidence,
    }


def build_dashboard_output(results: List[Dict[str, Any]], tickets: List[Dict[str, Any]]) -> Dict[str, Any]:
    risk_counts = {
        "Low": 0,
        "Medium": 0,
        "High": 0,
        "Critical": 0,
    }

    event_type_counts = {}
    drift_count = 0
    approval_required_count = 0

    for result in results:
        risk_level = result.get("risk_level", "Low")
        risk_counts[risk_level] = risk_counts.get(risk_level, 0) + 1

        event_type = result.get("event", {}).get("event_type", "unknown")
        event_type_counts[event_type] = event_type_counts.get(event_type, 0) + 1

        if result.get("evidence", {}).get("drift_detected"):
            drift_count += 1

        if result.get("approval_required"):
            approval_required_count += 1

    return {
        "generated_at": utc_now(),
        "total_events_processed": len(results),
        "tickets_created": len(tickets),
        "approval_required_count": approval_required_count,
        "drift_detected_count": drift_count,
        "risk_counts": risk_counts,
        "event_type_counts": event_type_counts,
        "outputs": {
            "tickets": str(TICKETS_OUTPUT_PATH),
            "audit_evidence": str(EVIDENCE_OUTPUT_PATH),
        },
    }


def main() -> None:
    role_packages = get_role_packages()
    identity_events = get_identity_events()

    results = []
    tickets = []
    evidence_records = []

    for event in identity_events:
        result = process_event(event, role_packages)
        results.append(result)
        tickets.extend(result.get("tickets", []))
        evidence_records.append(result.get("evidence", {}))

    tickets_output = {
        "generated_at": utc_now(),
        "tickets": tickets,
    }

    evidence_output = {
        "generated_at": utc_now(),
        "evidence_records": evidence_records,
    }

    dashboard_output = build_dashboard_output(results, tickets)

    write_json(TICKETS_OUTPUT_PATH, tickets_output)
    write_json(EVIDENCE_OUTPUT_PATH, evidence_output)
    write_json(DASHBOARD_OUTPUT_PATH, dashboard_output)

    print("IdentityOS Core processing completed.")
    print(f"Events processed: {len(results)}")
    print(f"Tickets created: {len(tickets)}")
    print(f"Evidence records generated: {len(evidence_records)}")
    print(f"Dashboard output: {DASHBOARD_OUTPUT_PATH}")


if __name__ == "__main__":
    main()