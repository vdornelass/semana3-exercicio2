from langchain_core.prompts import ChatPromptTemplate

EXTRACT_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Extraia os navios do relatório abaixo e o limite de velocidade segura em tempestade "
            "para a ROTA DIRETA a partir das regras do manual. Copie os valores exatamente como "
            "estão nos textos e não invente nenhum dado. Ignore a seção 'Sobre este documento'.",
        ),
        ("human", "Regras do manual:\n{regras}\n\nRelatório da frota:\n{relatorio}"),
    ]
)
