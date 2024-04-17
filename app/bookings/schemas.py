from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    model_config = SettingsConfigDict(from_attributes=True)


class SBookingInfo(BaseModel):
    image_id: int
    name: str
    description: Optional[str]
    services: list[str]

    model_config = SettingsConfigDict(from_attributes=True)


class SBookingExpanded(SBookingInfo, SBooking):

    model_config = SettingsConfigDict(from_attributes=True)


class SNewBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
