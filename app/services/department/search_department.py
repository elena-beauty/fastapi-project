from sqlalchemy.orm import Session

from app.schemas.department import DepartmentList
from app.repository import department_repository


def execute(
    session: Session,
    keyword: str | None,
    limit: int,
    offset: int,
) -> DepartmentList:
    departments, total = department_repository.search(
        session,
        keyword=keyword,
        limit=limit,
        offset=offset,
    )
    return DepartmentList(items=departments, total=total)
