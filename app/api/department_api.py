from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.dependency import get_db
from app.schemas.department import DepartmentList, DepartmentQuery
from app.services.department import search_department

department_router = APIRouter(prefix='/department', tags=['Department'])


@department_router.get('/')
def search_departments(
    session: Annotated[Session, Depends(get_db)],
    query: Annotated[DepartmentQuery, Query()],
) -> DepartmentList:
    return search_department.execute(
        session,
        keyword=query.keyword,
        limit=query.limit,
        offset=query.offset,
    )
