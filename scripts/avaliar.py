import json

from src.graph.builder import build_graph
from src.infra.langfuse_client import flush, run_config
from src.infra.vector_store import DADOS


def main() -> None:
    graph = build_graph()
    casos = json.loads((DADOS / "avaliacao.json").read_text(encoding="utf-8"))
    acertos = 0
    for caso in casos:
        saida = graph.invoke(
            {"pergunta": caso["pergunta"]},
            config=run_config(run_name=f"avaliacao-{caso['id']}", tags=["avaliacao", "semana-3"]),
        )
        texto = saida["resultado"].lower()
        ok = all(esperado.lower() in texto for esperado in caso["esperado"])
        acertos += ok
        print(caso["id"], "OK" if ok else "FALHOU")
    print(f"Acertos: {acertos}/{len(casos)}")
    flush()


if __name__ == "__main__":
    main()
