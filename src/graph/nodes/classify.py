from typing import Literal, TypedDict

from langgraph.types import Command

from src.graph.prompts.classify_prompt import CLASSIFY_PROMPT
from src.graph.state import State
from src.infra.llm_adapter import get_llm

DESTINOS = {
    "regra": "regras",
    "frota": "frota",
    "fora_escopo": "refuse",
}


class Intencao(TypedDict):
    intent: Literal["regra", "frota", "fora_escopo"]


chain = CLASSIFY_PROMPT | get_llm().with_structured_output(Intencao)


def classify(
    state: State,
) -> Command[Literal["regras", "frota", "refuse"]]:

    result = chain.invoke({"pergunta": state["pergunta"]})

    return Command(update=result, goto=DESTINOS[result["intent"]])
