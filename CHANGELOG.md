# Changelog

All notable changes to IdentityOS will be documented in this file.

---

## [v0.5.0] - Dashboard Design and Operational Visibility Expansion

### Added

* Added dashboard design folder for IdentityOS operational and executive visibility.
* Added executive dashboard design for leadership-level identity risk, governance, and access posture.
* Added IAM operations dashboard design for lifecycle events, approvals, access drift, remediation, automation status, and generated reports.
* Added governance dashboard design for access reviews, approvals, exceptions, remediation, audit evidence, and governance queues.
* Added risk dashboard design for identity risk scores, risk levels, risk factors, critical-risk queues, privileged access risk, and recommended actions.
* Added access drift dashboard design for stale access, privilege creep, excess access, drift severity, and remediation evidence.
* Added privileged access dashboard design for elevated access, standing privilege, access reviews, privileged drift, and audit evidence.
* Added contractor and vendor dashboard design for external identities, sponsor ownership, expiration tracking, renewal decisions, and contractor drift.
* Added non-human identity dashboard design for service accounts, automation identities, workload identities, ownership, credential governance, and access scope.
* Added automation health dashboard design for script status, report generation, failures, manual intervention, evidence outputs, and operational health.
* Added audit evidence dashboard design for policy decisions, approvals, reviews, remediation proof, exception evidence, report evidence, and audit readiness.

### Updated

* Updated the dashboard README with links to completed dashboard design assets.
* Updated the main README to expose dashboard design artifacts from the project front page.

### Outcome

* Completed the IdentityOS dashboard design layer, connecting identity lifecycle, governance, risk, access drift, privileged access, external identities, non-human identities, automation health, and audit evidence into a unified visibility model.


## v0.4.0 - Identity Analytics and Dashboard Concepts

### Added

* Added IdentityOS Dashboard Concepts documentation.
* Added sample dashboard metrics dataset.
* Added sample dashboard summary generator script.
* Added generated sample dashboard summary report.
* Updated documentation README with dashboard concepts.
* Updated examples README with dashboard metrics.
* Updated automation README with dashboard summary generator.
* Updated reports README with dashboard summary report.
* Updated main README with dashboard concepts link.
* Updated main README with dashboard metrics, automation, and report links.

### Project State

IdentityOS v0.4.0 expands the project into identity analytics and dashboard-ready reporting.

This version shows how identity lifecycle activity, governance outcomes, risk scoring, access drift detection, automation health, and reporting outputs can be presented as dashboard metrics for different audiences.

### Current Capabilities

* Defines dashboard concepts for executives, IAM teams, security teams, auditors, application owners, managers, HR, and business operations.
* Provides sample dashboard metrics for executive identity risk, lifecycle operations, governance, risk scoring, access drift, and automation health.
* Generates a Markdown dashboard summary report from sample metrics.
* Connects dashboard concepts, sample data, automation, and reports through README navigation.

### Why This Matters

Identity systems need visibility.

IdentityOS v0.4.0 shows how identity events, access decisions, governance results, risk scoring, and access drift detection can become dashboard-ready information.

This helps translate IAM work into measurable business, security, governance, and audit outcomes.

### Next Planned Work

* Add Microsoft Entra ID integration concepts.
* Add Microsoft Graph action mapping.
* Add Entra ID Joiner, Mover, and Leaver flow examples.
* Add sample Graph PowerShell scripts.
* Add integration documentation for identity providers and governance platforms.


## v0.3.0 - Risk Scoring and Access Drift Detection

### Added

* Added IdentityOS Risk Scoring Model.
* Added IdentityOS Access Drift Model.
* Added sample risk scorer automation script.
* Added sample access drift detector automation script.
* Added generated sample risk score report.
* Added generated sample access drift report.
* Updated reference models index with risk scoring and access drift models.
* Updated automation README with risk scorer and access drift detector.
* Updated reports README with risk score and access drift reports.
* Updated main README with risk scoring links.
* Updated main README with access drift links.

### Project State

IdentityOS v0.3.0 expands the project from architecture, governance, and reporting into identity risk intelligence.

This version introduces the ability to calculate sample identity risk scores and detect access drift using identity lifecycle events and policy decisions.

### Current Capabilities

* Calculates identity risk scores from sample identity events and policy decisions.
* Assigns risk levels such as Low, Medium, High, and Critical.
* Explains risk factors and recommended governance actions.
* Detects access drift from lifecycle and policy decision data.
* Identifies department drift, contractor drift, leaver drift, privileged drift, governance drift, and non-human identity drift.
* Generates Markdown reports for risk scoring and access drift detection.
* Connects risk models, automation scripts, and reports through README navigation.

### Why This Matters

Risk scoring and access drift detection help IdentityOS move beyond basic access management.

They show how identity data can be used to identify excessive access, stale access, privilege creep, contractor risk, privileged access risk, leaver risk, and non-human identity governance gaps.

### Next Planned Work

* Add dashboard concepts.
* Add sample identity risk metrics.
* Add exception detection logic.
* Add separation of duties examples.
* Add Microsoft Entra ID integration examples.
* Add dashboard-ready CSV or JSON exports.


## v0.2.0 - Visual Architecture and Reporting Expansion

### Added

* Added high-level IdentityOS architecture diagram.
* Added Joiner workflow diagram.
* Added Mover workflow diagram.
* Added Leaver workflow diagram.
* Added Policy Engine decision flow diagram.
* Added Governance workflow diagram.
* Added Access Review cycle diagram.
* Added diagrams index.
* Added documentation index.
* Added reference models index.
* Added examples index.
* Added automation index updates.
* Added reports folder and reports index.
* Added IdentityOS project summary.
* Added sample governance report generator script.
* Added generated sample governance report.
* Updated README with Quick Links.
* Updated README with visual diagram links.
* Updated README with reports links.

### Project State

IdentityOS v0.2.0 expands the project from an architecture foundation into a more complete identity architecture portfolio project.

This version adds visual architecture models, lifecycle workflow diagrams, governance diagrams, folder-level navigation, a project summary, and a generated governance report capability.

### Current Capabilities

* Provides a complete project navigation experience.
* Shows IdentityOS architecture visually.
* Models Joiner, Mover, and Leaver workflows.
* Models Policy Engine decision logic.
* Models governance and access review workflows.
* Documents all major project folders.
* Generates a Markdown governance report from sample data.
* Demonstrates how identity decisions can become governance evidence.

### Next Planned Work

* Add additional automation scripts.
* Add risk scoring logic.
* Add access drift detection examples.
* Add exception detection examples.
* Add dashboard concepts.
* Add Microsoft Entra ID integration examples.
* Add expanded reporting outputs.


## v0.1.0 - IdentityOS Architecture Foundation

### Added

* Created the IdentityOS repository structure.
* Added the primary project README.
* Added IdentityOS vision documentation.
* Added IdentityOS mission documentation.
* Added guiding principles for identity architecture.
* Added high-level architecture documentation.
* Added Lifecycle Engine design documentation.
* Added Policy Engine design documentation.
* Added Governance Engine documentation.
* Added IdentityOS roadmap.
* Added sample Role Catalog reference model.
* Added Access Review Model reference documentation.
* Added sample identity event dataset.
* Added sample policy decision dataset.
* Added first prototype automation script: `policy-evaluator.py`.
* Added README navigation map for easier project exploration.

### Project State

IdentityOS v0.1.0 establishes the architecture foundation for an enterprise Identity Operating System.

This version defines the core philosophy, design principles, operating engines, sample identity data, and initial prototype logic needed to demonstrate how modern identity lifecycle management, policy evaluation, governance, automation, and auditability can work together.

### Current Capabilities

* Documents the IdentityOS architectural vision.
* Defines the core IdentityOS engines.
* Models Joiner, Mover, Leaver, contractor, privileged access, and non-human identity events.
* Provides sample policy decisions for identity events.
* Includes a working Python script that evaluates sample identity events against policy decisions.
* Establishes a reference Role Catalog and Access Review Model.

### Next Planned Work

* Add diagrams for the high-level architecture.
* Add Joiner, Mover, and Leaver workflow diagrams.
* Add additional automation examples.
* Add sample role-to-access mapping files.
* Add dashboard concepts for identity governance and risk.
* Add prototype enhancements for policy evaluation and reporting.
