import os
from dotenv import load_dotenv

load_dotenv()

_client = None


def _is_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))


def run_config(
    run_name: str | None = None,
    tags: list[str] | None = None,
) -> dict:
    """Retorna config com callback do Langfuse se as chaves estiverem no .env."""
    global _client
    config: dict = {}
    if run_name:
        config["run_name"] = run_name
    if tags:
        config["tags"] = tags

    if not _is_enabled():
        return config

    from langfuse import get_client
    from langfuse.langchain import CallbackHandler

    _client = get_client()
    config["callbacks"] = [CallbackHandler()]
    return config


def flush() -> None:
    """Envia traces pendentes ao Langfuse (no-op se não estiver configurado)."""
    if _client is not None:
        _client.flush()
