from fastapi import Query
from pydantic import BaseModel, Field, ConfigDict

from app.schemas.common import BaseQuery


class DepartmentQuery(BaseQuery):
    keyword: str | None = Query()


class Department(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = Field()
    name: str | None = Field()


class DepartmentList(BaseModel):
    items: list[Department] = Field()
    total: int = Field()
