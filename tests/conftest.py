import pytest
from sqlalchemy.orm import Session

from ddd.adapters import db as _db
from ddd.bootstrap import bootstrap


@pytest.fixture
def db() -> Session:
    bootstrap()
    yield _db.session.Session()
