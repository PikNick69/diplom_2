import allure
import requests
from data.urls import REGISTER_ENDPOINT, LOGIN_ENDPOINT, LOGOUT_ENDPOINT, USER_ENDPOINT

@allure.step("Отправить запрос на регистрацию пользователя")
def create_user(data):
    """Регистрация пользователя"""
    return requests.post(REGISTER_ENDPOINT, json=data)

@allure.step("Отправить запрос на авторизацию пользователя")
def login_user(data):
    """Авторизация пользователя"""
    return requests.post(LOGIN_ENDPOINT, json=data)


@allure.step("Отправить запрос на выход из системы")
def logout_user(refresh_token):
    """Выход из системы"""
    data = {"token": refresh_token}
    return requests.post(LOGOUT_ENDPOINT, json=data)


@allure.step("Отправить запрос на получение данных пользователя")
def get_user_info(token):
    """Получение данных пользователя"""
    headers = {"Authorization": token}
    return requests.get(USER_ENDPOINT, headers=headers)

@allure.step("Отправить запрос на обновление данных пользователя")
def update_user_info(token, data):
    """Обновление данных пользователя"""
    headers = {"Authorization": token}
    return requests.patch(USER_ENDPOINT, headers=headers, json=data)


@allure.step("Отправить запрос на удаление пользователя")
def delete_user(token):
    """Удаление пользователя"""
    headers = {"Authorization": token}
    return requests.delete(USER_ENDPOINT, headers=headers)