from src.graph.builder import build_graph
from src.infra.langfuse_client import flush, run_config


def main():
    graph = build_graph()

    while True:
        
        try:
            pergunta = input("Pergunta: ").strip()
            
            if pergunta in ["sair", "exit", "quit"]:
                break

            resultado = graph.invoke(
                {"pergunta": pergunta},
                config=run_config()
            )

            print(resultado["resultado"])
            flush()
        except KeyboardInterrupt:
            flush()
            break


if __name__ == "__main__":
    main()
