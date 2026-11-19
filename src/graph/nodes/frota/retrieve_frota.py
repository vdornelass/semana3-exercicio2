
from src.graph.state import State
from src.infra.vector_store import buscar, fonte


def retrieve_frota(state: State) -> dict:
    # k alto de propósito: a pergunta compara todos os navios,
    # então todas as seções entram.
    docs = buscar(
        state["pergunta"],
        "relatorio_frota",
        k=10,
    )

    fontes = []

    for doc in docs:
        fontes.append(fonte(doc))

    return {
        "contextos": docs,
        "fontes": fontes,
    }
