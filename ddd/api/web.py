from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from ddd import bootstrap
from ddd.domain.commands import CreateSomeAggregate
from ddd import service
from .deps import get_db
from .resp_models import SomeAggregateResp

app = FastAPI()


@app.on_event("startup")
def on_startup():
    bootstrap.register_handlers()


@app.post('/api/v1/ddds',
          response_model=SomeAggregateResp,
          status_code=status.HTTP_201_CREATED)
async def create_aggreg(cmd: CreateSomeAggregate, db: Session = Depends(get_db)):
    aggreg = await service.create_aggreg(db, cmd)
    return SomeAggregateResp(data=aggreg)
