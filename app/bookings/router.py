from fastapi import APIRouter, BackgroundTasks, Depends

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookingExpanded, SNewBooking
from app.exceptions import RoomCannotBeBookedException
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingExpanded]:
    return await BookingDAO.find_all_with_images(user_id=user.id)


@router.post("")
async def add_booking(
        # background_tasks: BackgroundTasks,
        booking: SNewBooking,
        user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(user.id, booking.room_id, booking.date_from, booking.date_to)
    if not booking:
        raise RoomCannotBeBookedException
    booking = SNewBooking.model_validate(booking).model_dump()
    # celery
    send_booking_confirmation_email.delay(booking, user.email)
    # BG_tasks
    # background_tasks.add_task(send_booking_confirmation_email, booking, user.email)
    return booking


@router.delete("/{booking_id}")
async def delete_booking(booking_id: int, current_user: Users = Depends(get_current_user)):
    await BookingDAO.delete(id=booking_id, user_id=current_user.id)
