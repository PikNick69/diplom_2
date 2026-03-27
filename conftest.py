import pytest
from endpoints.user import create_user, delete_user
from data.test_data import generate_unique_user

@pytest.fixture
def unique_user():
    """Генерирует уникальные данные пользователя"""
    return generate_unique_user()

@pytest.fixture
def registered_user(unique_user):
    """
    Создаёт пользователя, возвращает его данные,
    после теста автоматически удаляет пользователя
    """
    response = create_user(unique_user)
    assert response.status_code == 200
    user_data = response.json()
    yield user_data
    if "accessToken" in user_data:
        delete_user(user_data["accessToken"])

@pytest.fixture
def auth_token(registered_user):
    """Возвращает accessToken для авторизованных запросов"""
    token = registered_user["accessToken"]
    return token

@pytest.fixture
def refresh_token(registered_user):
    """Возвращает refreshToken"""
    return registered_user["refreshToken"]

@pytest.fixture
def login_credentials(registered_user):
    """Возвращает email и пароль для логина"""
    return {
        "email": registered_user["user"]["email"],
        "password": "password123"
    }