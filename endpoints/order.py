import requests
from data.test_data import BASE_URL

def create_order(ingredients, token=None):
    """Создание заказа - POST /api/orders"""
    headers = {"Authorization": token} if token else {}
    data = {"ingredients": ingredients}
    return requests.post(f"{BASE_URL}/orders", json=data, headers=headers)

def get_orders_all():
    """Получение всех заказов - GET /api/orders/all"""
    return requests.get(f"{BASE_URL}/orders/all")

def get_user_orders(token):
    """Получение заказов пользователя - GET /api/orders"""
    headers = {"Authorization": token}
    return requests.get(f"{BASE_URL}/orders", headers=headers)