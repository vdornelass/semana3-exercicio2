
from src.graph.state import State


def format_output(state: State) -> dict:
    fontes_unicas = []

    for fonte in state.get("fontes", []):
        if fonte not in fontes_unicas:
            fontes_unicas.append(fonte)
            
    fontes = ", ".join(fontes_unicas)

    resultado = (
        f"Pergunta: {state['pergunta']}\n"
        f"Resposta: {state['resposta']}\n"
        f"Fontes: {fontes}"
    )

    return {"resultado": resultado}
