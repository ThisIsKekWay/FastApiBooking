
import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("room_id, date_from, date_to, status", [
    *[(10, "2024-07-10", "2024-07-11", 200)] * 7,
    (10, "2024-07-10", "2024-07-11", 409),
    (10, "2024-07-10", "2024-07-11", 409),
])
async def test_add_and_get_booking(
        authenticated_ac: AsyncClient,
        room_id,
        date_from,
        date_to,
        status
):
    response = await authenticated_ac.post("/bookings", json={
        "room_id": room_id,
        "date_from": date_from,
        "date_to": date_to,
    })
    assert response.status_code == status


async def test_get_all_bookings(authenticated_ac: AsyncClient):
    bookings = await authenticated_ac.get("/bookings")

    assert len(bookings.json()) == 9
