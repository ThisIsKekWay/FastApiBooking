from datetime import date
from typing import Optional, List

from fastapi_cache.decorator import cache

from app.hotels.schemas import SHotel, SHotelInfo
from fastapi import APIRouter, Depends
from app.hotels.dao import HotelDAO
from app.hotels.dependencies import date_validator

router = APIRouter(
    prefix="/hotels",
    tags=["Отели и номера"]
)


@router.get("/{location}", dependencies=[Depends(date_validator)])
@cache(expire=20)
async def get_hotels_by_location_and_date(
        location: str,
        date_from: date,
        date_to: date,
) -> List[SHotelInfo]:
    hotels = await HotelDAO.find_all(location, date_from, date_to)
    return hotels


@router.get("/id/{hotel_id}")
async def get_hotel_by_id(
        hotel_id: int,
) -> Optional[SHotel]:
    return await HotelDAO.find_one_or_none(id=hotel_id)
