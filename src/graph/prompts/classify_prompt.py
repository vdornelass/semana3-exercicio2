from langchain_core.prompts import ChatPromptTemplate

CLASSIFY_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Classifique a pergunta de um operador de porto:\n"
            "- regra: dúvida sobre regras, limites, valores, custos, prazos ou procedimentos "
            "do manual de operações marítimas/portuárias (ex.: velocidade, tempestade, nevoeiro, "
            "rotas, combustível, reserva, abastecimento, reparo de motor, descarga, segurança)\n"
            "- frota: pergunta sobre a situação atual dos navios da frota (quem chega primeiro, "
            "ETA, distância atual, qual navio está impedido de zarpar)\n"
            "- fora_escopo: qualquer assunto sem relação com navios, portos ou operações marítimas "
            "(ex.: geografia geral, capitais, receitas, esportes)",
        ),
        ("human", "{pergunta}"),
    ]
)
