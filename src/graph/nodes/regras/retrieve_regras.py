from src.graph.state import State
from src.infra.vector_store import buscar, fonte


def retrieve_regras(state: State) -> dict:
    docs = buscar(state["pergunta"], "manual_operacoes", k=3)

    fontes = []
    
    for doc in docs:
        fontes.append(fonte(doc))

    return {
        "contextos": docs,
        "fontes": fontes,
    }