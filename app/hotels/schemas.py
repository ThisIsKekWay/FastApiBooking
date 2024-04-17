from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int

    model_config = SettingsConfigDict(from_attributes=True)


class SHotelInfo(SHotel):
    rooms_left: int

    model_config = SettingsConfigDict(from_attributes=True)
