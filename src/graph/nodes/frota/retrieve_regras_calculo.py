from src.graph.state import State
from src.infra.vector_store import buscar, fonte


CONSULTA = "velocidade em tempestade, reserva de combustível e cálculo do ETA"


def retrieve_regras_calculo(state: State) -> dict:
    docs = buscar(CONSULTA, "manual_operacoes", k=4,)

    partes = []
    fontes = []

    for doc in docs:
        partes.append(doc.page_content)
        fontes.append(fonte(doc))

    contexto_regras = "\n\n".join(partes)

    return {
        "contexto_regras": contexto_regras,
        "fontes": fontes,
    }
