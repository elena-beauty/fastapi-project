from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.dependency import get_db
from app.schemas.location import LocationList, LocationQuery
from app.services.location import search_location

location_router = APIRouter(prefix='/location', tags=['Location'])


@location_router.get('/')
def search_locations(
    session: Annotated[Session, Depends(get_db)],
    query: Annotated[LocationQuery, Query()],
) -> LocationList:
    return search_location.execute(
        session,
        keyword=query.keyword,
        limit=query.limit,
        offset=query.offset,
    )
