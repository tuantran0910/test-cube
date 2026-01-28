import uuid

from cube import config  # type: ignore[attr-defined]
from cube import file_repository  # type: ignore[attr-defined]


@config("repository_factory")
def repository_factory(ctx: dict) -> list[dict]:
    return file_repository("models")


@config("schema_version")
def schema_version(ctx: dict) -> str:
    return str(uuid.uuid4())[:8]


@config("check_auth")
def check_auth(ctx: dict, token: str) -> None:
    return {"security_context": {"user_id": 42}}
