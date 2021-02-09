from sqlalchemy.orm import Session

from ddd.domain import some_aggregate, commands


async def create_aggreg(db: Session, command: commands.CreateSomeAggregate) -> some_aggregate.SomeAggregate:
    logic = some_aggregate.SomeAggregateLogic()
    return logic.create()
