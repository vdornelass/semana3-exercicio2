from src.graph.state import State
from src.graph.tools import TOOLS
from src.infra.llm_adapter import get_llm


def analyze(state: State) -> dict:
    llm = get_llm().bind_tools(TOOLS)

    resposta = llm.invoke(state["messages"])
    return {"messages": [resposta]}