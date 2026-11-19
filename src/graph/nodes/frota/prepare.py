
import json

from src.graph.prompts.analyze_prompt import ANALYZE_PROMPT
from src.graph.state import State


def prepare(state: State) -> dict:
    frota_json = json.dumps(
        state["frota"],
        ensure_ascii=False,
    )

    mensagens = ANALYZE_PROMPT.format_messages(
        regras=state["contexto_regras"],
        limite_tempestade_kn=state["limite_tempestade_kn"],
        frota=frota_json,
        pergunta=state["pergunta"],
    )

    return {"messages": mensagens}
