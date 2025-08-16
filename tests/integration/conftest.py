
import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from app.dependencies.settings import get_settings
from app.main import fastapi_app
from tests.conftest import TestSettings

DROP_TABLE_SQL = """DROP TABLE IF EXISTS {name} CASCADE;"""
SET_IS_TEMPLATE_SQL = """ALTER DATABASE {name} WITH is_template = true;"""
DROP_DATABASE_SQL = """DROP DATABASE IF EXISTS {name};"""
COPY_DATABASE_SQL = """CREATE DATABASE {name} TEMPLATE {template};"""
INSTALL_POSTGIS_SQL = """CREATE EXTENSION IF NOT EXISTS postgis;"""
INSTALL_POSTGIS_TOPOLOGY_SQL = """CREATE EXTENSION IF NOT EXISTS postgis_topology;"""


####################################################################################################
# Session fixtures
####################################################################################################


@pytest.fixture(scope="session", autouse=False)
async def test_app(test_settings: TestSettings) -> FastAPI:
    """Create test FastAPI application."""

    async def override_get_settings() -> TestSettings:
        """Override settings for testing."""
        return test_settings

    fastapi_app.dependency_overrides[get_settings] = override_get_settings

    return fastapi_app


####################################################################################################
# Function fixtures
####################################################################################################
@pytest.fixture(scope="function", autouse=False)
async def unauthenticated_client(test_app: FastAPI) -> AsyncClient:
    """Build database and create unauthenticated test client."""
    return AsyncClient(transport=ASGITransport(app=test_app), base_url="http://test")
