from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        "Você responde perguntas sobre o manual de operações do porto. "
        "Use SOMENTE as informações presentes no contexto fornecido, considerando sinônimos e paráfrases diretas do texto. "
        "Se a resposta for negativa segundo o contexto, responda explicando o que o manual diz. "
        "Somente se o assunto não for tratado no contexto, responda exatamente: "
        "Não encontrado no manual de operações."
    ),
    (
        "human",
        "Contexto:\n{contexto}\n\nPergunta: {pergunta}"
    ),
])