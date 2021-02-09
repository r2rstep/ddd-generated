from typing import List

import attr
from pydantic import BaseModel

from .event import Event


class SomeAggregateBase(BaseModel):
    id: int = None


class SomeAggregate(SomeAggregateBase):
    class Config:
        orm_mode = True


@attr.s(auto_attribs=True)
class SomeAggregateLogic:
    events: List[Event] = attr.ib(factory=list)

    def create(self) -> SomeAggregate:
        return SomeAggregateBase()
