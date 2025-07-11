from sqlalchemy.orm import Session

from app.schemas.organization import OrganizationList
from app.repository import organization_repository


def execute(
    session: Session,
    keyword: str | None,
    limit: int,
    offset: int,
) -> OrganizationList:
    organizations, total = organization_repository.search(
        session,
        keyword=keyword,
        limit=limit,
        offset=offset,
    )
    return OrganizationList(items=organizations, total=total)
