import allure
import requests
from data.urls import ORDERS_ENDPOINT, INGREDIENTS_ENDPOINT

@allure.step("Отправить запрос на получение списка ингредиентов")
def get_ingredients():
    """Получение списка ингредиентов"""
    return requests.get(INGREDIENTS_ENDPOINT)


@allure.step("Отправить запрос на создание заказа")
def create_order(ingredients, token=None):
    """Создание заказа"""
    headers = {"Authorization": token} if token else {}
    data = {"ingredients": ingredients}
    return requests.post(ORDERS_ENDPOINT, json=data, headers=headers)


@allure.step("Отправить запрос на получение всех заказов")
def get_orders_all():
    """Получение всех заказов"""
    return requests.get(f"{ORDERS_ENDPOINT}/all")

@allure.step("Отправить запрос на получение заказов пользователя")
def get_user_orders(token):
    """Получение заказов пользователя"""
    headers = {"Authorization": token}
    return requests.get(ORDERS_ENDPOINT, headers=headers)