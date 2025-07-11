from fastapi import Query
from pydantic import BaseModel, Field, ConfigDict

from app.schemas.common import BaseQuery


class PositionQuery(BaseQuery):
    keyword: str | None = Query(None)


class Position(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = Field()
    title: str | None = Field()


class PositionList(BaseModel):
    items: list[Position] = Field()
    total: int = Field()
