# TRACE

### Technical Root-cause Analysis & Contextual Engineering

**An evidence-driven AI engineering agent for investigating, diagnosing, and resolving technical incidents across enterprise systems.**

**Project Status:** 🚧 In Development — Phase 0: Foundation

---

## The Problem

Modern enterprise systems consist of interconnected APIs, services, devices, databases, and configurations.

When failures occur, engineers often have to investigate multiple systems independently, correlate logs, verify dependencies, check configuration states, and manually narrow down possible causes.

This creates several challenges:

- **Fragmented diagnostics:** Evidence is distributed across different systems and tools.
- **Time-consuming investigations:** Engineers repeatedly perform manual diagnostic checks.
- **Inconsistent troubleshooting:** Investigation approaches depend heavily on individual experience.
- **Limited traceability:** It can be difficult to reconstruct why a particular diagnosis was reached.
- **Unverified resolutions:** A recommended fix does not necessarily mean the underlying problem has been resolved.

## The Solution

TRACE is designed to automate structured technical investigations using **agentic AI, dynamic tool calling, and evidence-based root-cause analysis**.

Instead of generating answers based only on an incident description, TRACE will interact with a controlled enterprise environment, inspect actual system states, evaluate competing hypotheses, and produce an explainable investigation report.

The planned end-to-end workflow is:

**Incident → Hypotheses → Diagnostic Tools → Evidence → Root Cause → Human Approval → Remediation → Verification**

If the evidence is insufficient, TRACE should report an inconclusive result rather than inventing a diagnosis.

## Planned Capabilities

| Capability | Description |
|---|---|
| AI-driven investigation | Stateful multi-step troubleshooting using LangGraph |
| Dynamic tool calling | Select diagnostic tools based on incident context |
| Hypothesis tracking | Maintain and update potential root causes |
| Evidence collection | Capture observations from APIs, devices, configurations and logs |
| Root-cause reporting | Produce structured diagnoses with supporting evidence |
| Controlled failure injection | Reproduce technical incidents with known ground truth |
| Knowledge retrieval | Retrieve technical documentation and historical incidents |
| Human-approved remediation | Require authorization before modifying system state |
| Resolution verification | Validate whether corrective actions restore expected behavior |
| Evaluation | Measure diagnosis accuracy, efficiency and reliability |

These capabilities represent the target system. Implementation progress will be updated as each milestone is completed.

## High-Level Architecture

The planned system consists of six major areas:

1. **Presentation and API:** Angular dashboard and FastAPI backend.
2. **AI Investigation Engine:** LangGraph workflow for diagnostic planning, tool execution and hypothesis management.
3. **Diagnostic Tools:** Validated interfaces to device, firmware, configuration, connectivity and log services.
4. **Simulated Enterprise Environment:** Reproducible services and injected failure scenarios.
5. **Persistence and Knowledge:** PostgreSQL, investigation state, documentation and historical incidents.
6. **Remediation and Evaluation:** Human approval, resolution verification and controlled benchmark scenarios.

**[View the Master Architecture Diagram](docs/high-level-design.md)**

**[Read the Detailed System Architecture](architecture.md)**

## Example Investigation

**Incident:** Firmware update failed for device `DC-104`.

A planned TRACE investigation could proceed as follows:

| Step | Diagnostic Action | Example Observation |
|---|---|---|
| 1 | Check device status | Device online |
| 2 | Check connectivity | Connection healthy |
| 3 | Retrieve installed firmware | Version 4.1.0 |
| 4 | Check target firmware compatibility | Compatibility validation failed |
| 5 | Inspect update logs | Firmware prerequisite mismatch |
| 6 | Evaluate evidence | Firmware incompatibility supported |
| 7 | Recommend action | Select a compatible firmware package |
| 8 | Request approval | Await engineer authorization |
| 9 | Verify after remediation | Confirm firmware and device health |

*Illustrative workflow only — not an actual TRACE execution result.*

## Technology Stack

| Area | Technology |
|---|---|
| Programming language | Python |
| Backend framework | FastAPI |
| Agent orchestration | LangGraph |
| AI model | Configurable LLM provider |
| Database | PostgreSQL |
| Frontend | Angular, TypeScript |
| Testing | Pytest |
| Containerization | Docker, Docker Compose |
| Source control | Git, GitHub |

**Planned extensions:** RAG, historical incident memory, MCP-compatible tool integrations, observability, multi-model benchmarking and cloud deployment.

## Initial Failure Scenarios

The first MVP will focus on five reproducible incidents.

| Scenario | Failure Type |
|---|---|
| INC-001 | Device offline |
| INC-002 | Firmware incompatibility |
| INC-003 | Invalid device configuration |
| INC-004 | API returns an empty result |
| INC-005 | Authentication failure |

Each scenario will have a known root cause, expected diagnostic observations and an acceptable remediation path.

Ground-truth information will remain separate from the investigating agent to prevent answer leakage during evaluation.

## Project Roadmap

- [ ] **Phase 0 — Foundation:** Architecture, repository setup, initial schemas and infrastructure configuration.
- [ ] **Phase 1 — Simulation:** Device, firmware and configuration services with failure injection.
- [ ] **Phase 2 — Agent MVP:** LLM integration, LangGraph workflow and diagnostic tools.
- [ ] **Phase 3 — Investigation Engine:** Evidence tracking, hypothesis evaluation and structured diagnosis.
- [ ] **Phase 4 — Advanced Workflows:** RAG, historical incidents, human-approved remediation and verification.
- [ ] **Phase 5 — Evaluation and Deployment:** Benchmarking, observability, dashboard and deployment.

## Getting Started

TRACE is currently in its foundation phase. A runnable application is not available yet.

Once the first simulated services are implemented, the intended local setup will be:

```bash
git clone https://github.com/Chinmayigarlapet/TRACE.git
cd TRACE
docker compose up --build
```

*The command above is the planned setup workflow and will be verified once the Docker environment is implemented. The repository URL assumes the repository is named `TRACE`.*

### Prerequisites

Planned local development requirements:

- Git
- Python 3.11 or newer
- Docker and Docker Compose
- An LLM API key for agent-based features
- Node.js and Angular CLI for the future dashboard

## Evaluation Approach

TRACE will be evaluated using reproducible failure scenarios with known ground truth.

The evaluation framework will measure:

- Root-cause diagnosis accuracy
- Evidence quality
- False diagnosis rate
- Tool-call efficiency
- Investigation latency
- Remediation correctness
- Post-remediation verification success

Actual benchmark results will be published after the evaluation harness is implemented.

## Engineering Principles

**Evidence before conclusions.** Diagnoses must be supported by observable system data.

**Safe execution.** The AI cannot directly execute unrestricted system operations.

**Human control.** State-changing remediation requires explicit approval.

**Reproducibility.** Failure scenarios must be repeatable and independently verifiable.

**Model independence.** The architecture should support evaluating and replacing LLM providers.

**Measurable performance.** Engineering claims must be backed by actual tests and evaluation results.

## Documentation

- [System Architecture](architecture.md)
- [High-Level Design Diagram](docs/high-level-design.md)

Additional setup, API and evaluation documentation will be added as the project develops.

## Project Status

**Current milestone:** Phase 0 — Architecture and Foundation.

TRACE is an independent portfolio project under active development. It uses synthetic or publicly available information and is not affiliated with or endorsed by any employer.

---

**TRACE — From technical incidents to evidence-backed engineering decisions.**