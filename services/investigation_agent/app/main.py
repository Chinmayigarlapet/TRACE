from .graph import build_investigation_graph


def main():
    incident = (
        "Device DEV-003 is unreachable. "
        "The monitoring system has stopped receiving data."
    )

    graph = build_investigation_graph()

    initial_state = {
        "incident_description": incident,
        "device_id": "DEV-003",
        "investigation_plan": None,
        "evidence": [],
        "evaluation": None,
    }

    result = graph.invoke(initial_state)

    print("\nTRACE — Evidence-Based Investigation")

    # 1. Display investigation plan
    plan = result["investigation_plan"]

    if plan is not None:
        print("\nInvestigation Plan:")
        print(plan.model_dump_json(indent=2))

    # 2. Display collected evidence
    print("\nCollected Evidence:")

    for item in result["evidence"]:
        print(item.model_dump_json(indent=2))

    # 3. Display evidence evaluation
    evaluation = result["evaluation"]

    if evaluation is not None:
        print("\nEvidence Evaluation:")
        print(evaluation.model_dump_json(indent=2))


if __name__ == "__main__":
    main()