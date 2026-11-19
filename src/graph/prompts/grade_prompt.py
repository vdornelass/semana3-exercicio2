from langchain_core.prompts import ChatPromptTemplate

GRADE_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Diga se o contexto contém a informação necessária para responder à pergunta. "
            "Responda suficiente=true somente se a resposta estiver explícita no contexto.",
        ),
        ("human", "Contexto:\n{contexto}\n\nPergunta: {pergunta}"),
    ]
)
