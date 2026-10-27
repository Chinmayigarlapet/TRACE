from langgraph.graph import StateGraph, START, END

from .nodes import (
    generate_hypotheses,
    run_connectivity_check,
    evaluate_evidence_node,
)

from .state import InvestigationState


def build_investigation_graph():

    graph = StateGraph(InvestigationState)

    graph.add_node(
        "generate_hypotheses",
        generate_hypotheses,
    )

    graph.add_node(
        "run_connectivity_check",
        run_connectivity_check,
    )

    graph.add_node(
        "evaluate_evidence",
        evaluate_evidence_node,
    )

    graph.add_edge(
        START,
        "generate_hypotheses",
    )

    graph.add_edge(
        "generate_hypotheses",
        "run_connectivity_check",
    )

    graph.add_edge(
        "run_connectivity_check",
        "evaluate_evidence",
    )

    graph.add_edge(
        "evaluate_evidence",
        END,
    )

    return graph.compile()