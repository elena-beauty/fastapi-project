from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.dependency import get_db
from app.schemas.organization import OrganizationList, OrganizationQuery
from app.services.organization import search_organization

organization_router = APIRouter(prefix='/organization', tags=['Organization'])


@organization_router.get('/')
def search_organizations(
    session: Annotated[Session, Depends(get_db)],
    query: Annotated[OrganizationQuery, Query()],
) -> OrganizationList:
    return search_organization.execute(
        session,
        keyword=query.keyword,
        limit=query.limit,
        offset=query.offset,
    )
