from pydantic import BaseModel

from ddd import domain


class SomeAggregateResp(BaseModel):
    class Links(BaseModel):
        self: str = None

    data: domain.SomeAggregateBase
    links: Links = Links()
