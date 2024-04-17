from sqladmin import ModelView

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.users.models import Users


class UserAdmin(ModelView, model=Users):
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    column_details_list = [Users.id, Users.email, Users.booking]
    can_delete = False
    column_list = [
                      c.name for c in Users.__table__.c
                      if c.name not in ['hashed_pwd']
                  ] + [Users.booking]


class BookingsAdmin(ModelView, model=Bookings):
    name = "Бронирование"
    name_plural = "Бронирования"
    icon = "fa-solid fa-ticket"
    column_list = [
                      c.name for c in Bookings.__table__.c
                      if c.name not in ['id', 'user_id', 'room_id']
                  ] + [Bookings.user, Bookings.room]


class RoomsAdmin(ModelView, model=Rooms):
    name = "Номер"
    name_plural = "Номера"
    icon = "fa-solid fa-bed"
    column_list = [
                      c.name for c in Rooms.__table__.c
                      if c.name not in ['id', 'hotel_id', 'image_id']
                  ] + [Rooms.booking, Rooms.hotel]


class HotelsAdmin(ModelView, model=Hotels):
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-hotel"
    column_list = [
                      c.name for c in Hotels.__table__.c
                      if c.name not in ['id', 'image_id']
                  ] + [Hotels.room]
