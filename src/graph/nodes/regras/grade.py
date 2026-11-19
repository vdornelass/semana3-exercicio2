from pydantic import BaseModel

from src.graph.prompts.grade_prompt import GRADE_PROMPT
from src.graph.state import State
from src.infra.llm_adapter import get_llm


class Relevancia(BaseModel):
    suficiente: bool


def grade(state: State) -> dict:
    partes = []

    for doc in state["contextos"]:
        partes.append(doc.page_content)
    
    contexto = "\n\n".join(partes)

    resposta = (
        GRADE_PROMPT | get_llm().with_structured_output(Relevancia)
    ).invoke(
        {
            "contexto": contexto,
            "pergunta": state["pergunta"],
        }
    )

    return {"suficiente": resposta.suficiente}
