from fastapi import Query
from pydantic import BaseModel, Field, ConfigDict

from app.constant.employee_constant import EmployeeStatus
from app.schemas.common import BaseQuery, SimpleDepartment, SimpleOrganization, SimpleLocation, \
    SimplePosition, MaskedBaseModel


class EmployeeQuery(BaseQuery):
    organization_id: int = Query()
    keyword: str | None = Query(None, min_length=1, max_length=100)
    status: EmployeeStatus = Query(None)
    location_ids: list[int] = Query(None)
    organization_ids: list[int] = Query(None)
    department_ids: list[int] = Query(None)
    position_ids: list[int] = Query(None)


class Employee(MaskedBaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field()
    first_name: str | None = Field()
    last_name: str | None = Field()
    email: str | None = Field()
    phone: str | None = Field()
    organization: SimpleOrganization | None = Field()
    department: SimpleDepartment | None = Field()
    location: SimpleLocation | None = Field()
    position: SimplePosition | None = Field()
    status: EmployeeStatus | None = Field()


class EmployeeList(BaseModel):
    items: list[Employee] = Field()
    total: int = Field()
