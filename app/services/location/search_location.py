from sqlalchemy.orm import Session

from app.schemas.location import LocationList
from app.repository import location_repository


def execute(
    session: Session,
    keyword: str | None,
    limit: int,
    offset: int,
) -> LocationList:
    locations, total = location_repository.search(
        session,
        keyword=keyword,
        limit=limit,
        offset=offset,
    )
    return LocationList(items=locations, total=total)
