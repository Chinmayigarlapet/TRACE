
from .llm import generate_investigation_plan


def main():
    incident = (
        "Device DEV-003 is unreachable. "
        "The monitoring system has stopped receiving data."
    )

    print("\nTRACE — AI Investigation Agent")
    print(f"\nIncident: {incident}")
    print("\nGenerating investigation hypotheses...\n")

    plan = generate_investigation_plan(incident)

    print(plan.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
