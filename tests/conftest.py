from pathlib import Path

import pytest
from pydantic_settings import SettingsConfigDict

from app.config import Settings


class TestSettings(Settings):
    """Settings for tests."""

    TITLE: str = "Test Title"
    SECRET_KEY: str = "1234567890"

    model_config = SettingsConfigDict(env_file=Path(__file__).parent / ".testenv")


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session", autouse=False)
def test_settings() -> TestSettings:
    """Settings for tests."""
    return TestSettings()
