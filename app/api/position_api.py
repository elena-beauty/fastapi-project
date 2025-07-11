from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.dependency import get_db
from app.schemas.position import PositionList, PositionQuery
from app.services.position import search_position

position_router = APIRouter(prefix='/position', tags=['Position'])


@position_router.get('/')
def search_positions(
    session: Annotated[Session, Depends(get_db)],
    query: Annotated[PositionQuery, Query()],
) -> PositionList:
    return search_position.execute(
        session,
        keyword=query.keyword,
        limit=query.limit,
        offset=query.offset,
    )
