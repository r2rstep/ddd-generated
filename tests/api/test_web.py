from fastapi.testclient import TestClient
import pytest
from sqlalchemy.orm import Session

from ddd import domain


@pytest.mark.end2end
def test_create_aggreg(db: Session, client: TestClient):
    aggreg = client.post(f'/api/v1/ddds', json=domain.commands.CreateSomeAggregate().dict())
    assert False
