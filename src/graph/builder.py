from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from src.graph.nodes.classify import classify
from src.graph.nodes.frota.analyze import analyze
from src.graph.nodes.frota.extract_frota import extract_frota
from src.graph.nodes.frota.format_frota import format_frota
from src.graph.nodes.frota.prepare import prepare
from src.graph.nodes.frota.retrieve_frota import retrieve_frota
from src.graph.nodes.frota.retrieve_regras_calculo import (
    retrieve_regras_calculo,
)
from src.graph.nodes.refuse import refuse
from src.graph.nodes.regras.format_output import format_output
from src.graph.nodes.regras.generate import generate
from src.graph.nodes.regras.grade import grade
from src.graph.nodes.regras.nao_encontrado import nao_encontrado
from src.graph.nodes.regras.retrieve_regras import retrieve_regras
from src.graph.routing import route_after_grade
from src.graph.state import State
from src.graph.tools import TOOLS


def build_regras_graph():
    graph = StateGraph(State)

    graph.add_node("retrieve_regras", retrieve_regras)
    graph.add_node("grade", grade)
    graph.add_node("generate", generate)
    graph.add_node("format_output", format_output)
    graph.add_node("nao_encontrado", nao_encontrado)

    graph.add_edge(START, "retrieve_regras")
    graph.add_edge("retrieve_regras", "grade")

    graph.add_conditional_edges(
        "grade",
        route_after_grade,
        {
            "suficiente": "generate",
            "insuficiente": "nao_encontrado",
        },
    )

    graph.add_edge("generate", "format_output")
    graph.add_edge("format_output", END)
    graph.add_edge("nao_encontrado", END)

    return graph.compile()


def build_frota_graph():
    graph = StateGraph(State)

    graph.add_node("retrieve_frota", retrieve_frota)
    graph.add_node("retrieve_regras_calculo", retrieve_regras_calculo)
    graph.add_node("extract_frota", extract_frota)
    graph.add_node("prepare", prepare)
    graph.add_node("analyze", analyze)
    graph.add_node("tools", ToolNode(TOOLS))
    graph.add_node("format_frota", format_frota)

    graph.add_edge(START, "retrieve_frota")
    graph.add_edge("retrieve_frota", "retrieve_regras_calculo")
    graph.add_edge("retrieve_regras_calculo", "extract_frota")
    graph.add_edge("extract_frota", "prepare")
    graph.add_edge("prepare", "analyze")
    graph.add_conditional_edges(
        "analyze",
        tools_condition,
        {"tools": "tools", END: "format_frota"},
    )
    graph.add_edge("tools", "analyze")
    graph.add_edge("format_frota", END)

    return graph.compile()


def build_graph():
    graph = StateGraph(State)

    graph.add_node("classify", classify)
    graph.add_node("regras", build_regras_graph())
    graph.add_node("frota", build_frota_graph())
    graph.add_node("refuse", refuse)

    graph.add_edge(START, "classify")
    graph.add_edge("regras", END)
    graph.add_edge("frota", END)
    graph.add_edge("refuse", END)

    return graph.compile()


def build_frota_graph():
    graph = StateGraph(State)

    graph.add_node("retrieve_frota", retrieve_frota)
    graph.add_node("retrieve_regras_calculo", retrieve_regras_calculo)
    graph.add_node("extract_frota", extract_frota)
    graph.add_node("prepare", prepare)
    graph.add_node("analyze", analyze)
    graph.add_node("tools", ToolNode(TOOLS))
    graph.add_node("format_frota", format_frota)

    graph.add_edge(START, "retrieve_frota")
    graph.add_edge("retrieve_frota", "retrieve_regras_calculo")
    graph.add_edge("retrieve_regras_calculo", "extract_frota")
    graph.add_edge("extract_frota", "prepare")
    graph.add_edge("prepare", "analyze")
    graph.add_conditional_edges(
        "analyze",
        tools_condition,
        {"tools": "tools", END: "format_frota"},
    )
    graph.add_edge("tools", "analyze")
    graph.add_edge("format_frota", END)

    return graph.compile()


def build_graph():
    graph = StateGraph(State)

    graph.add_node("classify", classify)
    graph.add_node("regras", build_regras_graph())
    graph.add_node("frota", build_frota_graph())
    graph.add_node("refuse", refuse)

    graph.add_edge(START, "classify")
    graph.add_edge("regras", END)
    graph.add_edge("frota", END)
    graph.add_edge("refuse", END)

    return graph.compile()
