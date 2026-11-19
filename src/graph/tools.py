from langchain_core.tools import tool


@tool
def reserva_ok(navio: str, combustivel_t: float, reserva_t: float) -> dict:
    """Verifica se o combustível a bordo cobre a reserva mínima (True = pode zarpar, False = bloqueado)."""
    return {"navio": navio, "reserva_ok": combustivel_t >= reserva_t}


@tool
def velocidade_efetiva(
    navio: str, velocidade_kn: float, em_tempestade: bool, limite_tempestade_kn: float
) -> dict:
    """Calcula a velocidade efetiva do navio. Em tempestade, limita a `limite_tempestade_kn`, que deve ser a velocidade segura na ROTA DIRETA em tempestade lida da seção Tempestade do manual."""
    vel = min(velocidade_kn, limite_tempestade_kn) if em_tempestade else velocidade_kn
    return {"navio": navio, "velocidade_efetiva_kn": vel}


@tool
def calcular_eta_horas(navio: str, distancia_nm: float, velocidade_kn: float) -> dict:
    """Calcula o ETA em horas do navio: distancia_nm dividida por velocidade_kn (use a velocidade efetiva)."""
    return {"navio": navio, "eta_horas": round(distancia_nm / velocidade_kn, 2)}


TOOLS = [reserva_ok, velocidade_efetiva, calcular_eta_horas]
