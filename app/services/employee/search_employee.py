from sqlalchemy.orm import Session

from app.constant.employee_constant import EmployeeStatus
from app.schemas.employee import EmployeeList, Employee
from app.repository import employee_repository, organization_repository


def execute(
    session: Session,
    organization_id: int,
    keyword: str | None,
    status: EmployeeStatus | None,
    location_ids: list[int] | None,
    organization_ids: list[int] | None,
    department_ids: list[int] | None,
    position_ids: list[int] | None,
    limit: int,
    offset: int,
) -> EmployeeList:
    organization = organization_repository.find_by_id(session, organization_id)
    allowed_fields: list[str] = list(set(organization.column_config) | {'id'})
    employees, total = employee_repository.search(
        session,
        keyword=keyword,
        fields=allowed_fields,
        status=status,
        location_ids=location_ids,
        organization_ids=organization_ids,
        department_ids=department_ids,
        position_ids=position_ids,
        limit=limit,
        offset=offset,
    )

    items = []
    for e in employees:
        schemas = Employee.model_validate(e)
        schemas.allowed_fields = allowed_fields
        items.append(schemas)

    return EmployeeList(items=items, total=total)
