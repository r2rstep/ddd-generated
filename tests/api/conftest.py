from typing import Generator

from fastapi.testclient import TestClient
import pytest

from ddd.api.web import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
