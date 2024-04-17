import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("email, pwd, status_code", [
    ("kot@pes.com", "kotopes", 200),
    ("kot@pes.com", "kotapes", 409),
    ("pes@kot.com", "kot0pes", 200),
    ("peskot.com", "kot0pes", 422),

])
async def test_register_user(email, pwd, status_code, ac: AsyncClient):
    response = await ac.post("/auth/register", json={
        "email": email,
        "pwd": pwd
    })
    print(response)

    assert response.status_code == status_code


@pytest.mark.parametrize("email, pwd, status_code", [
    ("test@test.com", "test", 200),
    ("artem@example.com", "artem", 200),
    ("kot@pes.com", "kotopes", 200),
    ("kot@pes.com", "kotapes", 401),
    ("pes@kot.com", "kot0pes", 200),
    ("peskot.com", "kot0pes", 422),
])
async def test_login_user(email, pwd, status_code, ac: AsyncClient):
    response = await ac.post("/auth/login", json={
        "email": email,
        "pwd": pwd
    })
    print(response)

    assert response.status_code == status_code
