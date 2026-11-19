
from src.graph.prompts.rag_prompt import RAG_PROMPT
from src.graph.state import State
from src.infra.llm_adapter import get_llm


def generate(state: State) -> dict:
    partes = []

    for doc in state["contextos"]:
        partes.append(doc.page_content)

    contexto = "\n\n".join(partes)

    resposta = (
        RAG_PROMPT | get_llm()
    ).invoke(
        {
            "contexto": contexto,
            "pergunta": state["pergunta"],
        }
    )

    return {"resposta": str(resposta.content)}
