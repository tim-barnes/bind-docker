import pytest
from starlette.testclient import TestClient
from app import app as fastapi_app


@pytest.fixture
def client():
    return TestClient(fastapi_app)
