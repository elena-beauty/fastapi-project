from fastapi import Query
from pydantic import BaseModel, Field, ConfigDict

from app.schemas.common import BaseQuery


class OrganizationQuery(BaseQuery):
    keyword: str | None = Query(None)


class Organization(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = Field()
    name: str | None = Field()


class OrganizationList(BaseModel):
    items: list[Organization] = Field()
    total: int = Field()
