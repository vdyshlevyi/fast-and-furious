from fastapi import APIRouter, Depends
from starlette import status

from app.api.root.schemas import HealthCheckSchema, RootSchema
from app.config import Settings
from app.dependencies.settings import get_settings

router = APIRouter(tags=["infrastructure"])


@router.get(
    path="/",
    response_model=RootSchema,
    status_code=status.HTTP_200_OK,
    tags=["infrastructure"],
)
async def root(
    settings: Settings = Depends(get_settings),
) -> dict:
    return {"message": f"Welcome to the {settings.TITLE} application!"}


@router.get(
    path="/healthcheck",
    response_model=HealthCheckSchema,
    status_code=status.HTTP_200_OK,
    tags=["infrastructure"],
)
async def healthcheck() -> dict:  # type: ignore[assignment]
    return {"result": "success"}
