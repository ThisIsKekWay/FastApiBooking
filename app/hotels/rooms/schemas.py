from typing import List, Optional

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class SRoom(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: Optional[str]
    services: List[str]
    price: int
    quantity: int
    image_id: int

    model_config = SettingsConfigDict(from_attributes=True)


class SRoomInfo(SRoom):
    total_cost: int
    rooms_left: int

    model_config = SettingsConfigDict(from_attributes=True)
