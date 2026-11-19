from src.graph.state import State


def route_after_grade(state: State) -> str:
    return "suficiente" if state["suficiente"] else "insuficiente"
