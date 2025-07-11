from fastapi import Query
from pydantic import BaseModel, Field, ConfigDict

from app.schemas.common import BaseQuery


class LocationQuery(BaseQuery):
    keyword: str | None = Query(None)


class Location(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = Field()
    name: str | None = Field()


class LocationList(BaseModel):
    items: list[Location] = Field()
    total: int = Field()
