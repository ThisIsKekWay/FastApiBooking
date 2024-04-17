from datetime import datetime

import pytest

from app.bookings.dao import BookingDAO


@pytest.mark.parametrize("user_id, room_id, date_from, date_to, is_exists", [
    (2, 2, "2023-07-10", "2023-07-24", True),
    (1, 50, "2023-07-10", "2023-07-24", False)
])
async def test_add_and_get_booking(
        user_id,
        room_id,
        date_from,
        date_to,
        is_exists,
):
    date_from = datetime.strptime(date_from, "%Y-%m-%d")
    date_to = datetime.strptime(date_to, "%Y-%m-%d")
    new_booking = await BookingDAO.add(user_id, room_id, date_from, date_to)

    if is_exists:
        assert new_booking
        assert user_id == new_booking.user_id
    else:
        assert not new_booking
