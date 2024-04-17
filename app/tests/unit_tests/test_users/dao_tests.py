import pytest

from app.users.dao import UsersDAO


@pytest.mark.parametrize("email, is_exists", [
    ("test@test.com", True),
    ("artem@example.com", True),
    (".....", False)
])
async def test_find_user_by_id(email, is_exists):
    user = await UsersDAO.find_one_or_none(email=email)

    if is_exists:
        assert user
        print(user)
        assert user["email"] == email
    else:
        assert not user
