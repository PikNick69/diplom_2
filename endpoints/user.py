import requests
from data.test_data import BASE_URL

def create_user(data):
    """Регистрация пользователя - POST /api/auth/register"""
    return requests.post(f"{BASE_URL}/auth/register", json=data)

def login_user(data):
    """Авторизация пользователя - POST /api/auth/login"""
    return requests.post(f"{BASE_URL}/auth/login", json=data)

def logout_user(refresh_token):
    """Выход из системы - POST /api/auth/logout"""
    data = {"token": refresh_token}
    return requests.post(f"{BASE_URL}/auth/logout", json=data)

def get_user_info(token):
    """Получение данных пользователя - GET /api/auth/user"""
    headers = {"Authorization": token}
    return requests.get(f"{BASE_URL}/auth/user", headers=headers)

def update_user_info(token, data):
    """Обновление данных пользователя - PATCH /api/auth/user"""
    headers = {"Authorization": token}
    return requests.patch(f"{BASE_URL}/auth/user", headers=headers, json=data)

def delete_user(token):
    """Удаление пользователя - DELETE /api/auth/user"""
    headers = {"Authorization": token}
    return requests.delete(f"{BASE_URL}/auth/user", headers=headers)