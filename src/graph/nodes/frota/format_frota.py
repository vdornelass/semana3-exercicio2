from src.graph.state import State


def format_frota(state: State) -> dict:
    fontes = []

    for fonte_item in state.get("fontes", []):
        if fonte_item not in fontes:
            fontes.append(fonte_item)

    resposta = state["messages"][-1].content

    resultado = (
        f"{resposta}\n"
        f"Fontes: {', '.join(fontes)}"
    )

    return {"resultado": resultado}
