from sqlalchemy.orm import Session

from app.schemas.position import PositionList
from app.repository import position_repository


def execute(
    session: Session,
    keyword: str | None,
    limit: int,
    offset: int,
) -> PositionList:
    positions, total = position_repository.search(
        session,
        keyword=keyword,
        limit=limit,
        offset=offset,
    )
    return PositionList(items=positions, total=total)
