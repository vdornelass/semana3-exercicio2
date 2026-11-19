
from pydantic import BaseModel, Field

from src.graph.prompts.extract_prompt import EXTRACT_PROMPT
from src.graph.state import State
from src.infra.llm_adapter import get_llm


class NavioRelatorio(BaseModel):
    id: str
    destino: str
    rota: str
    distancia_nm: float
    velocidade_kn: float
    combustivel_t: float
    reserva_t: float
    em_tempestade: bool


class Frota(BaseModel):
    navios: list[NavioRelatorio]

    limite_tempestade_rota_direta_kn: float = Field(
        description=(
            "Velocidade segura em tempestade na rota direta "
            "(em nós), conforme o manual."
        )
    )


def extract_frota(state: State) -> dict:
    partes = []

    for doc in state["contextos"]:
        partes.append(doc.page_content)

    relatorio = "\n\n".join(partes)

    chain = (
        EXTRACT_PROMPT | get_llm().with_structured_output(Frota)
    )

    frota = chain.invoke(
        {
            "relatorio": relatorio,
            "regras": state["contexto_regras"],
        }
    )

    navios = sorted(
        frota.navios,
        key=lambda navio: navio.id,
    )

    dados_navios = []

    for navio in navios:
        dados_navios.append(navio.model_dump())

    return {
        "frota": dados_navios,
        "limite_tempestade_kn": (
            frota.limite_tempestade_rota_direta_kn
        ),
    }
