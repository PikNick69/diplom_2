import allure
import pytest
from endpoints.order import create_order
from data.test_data import VALID_INGREDIENTS, INVALID_INGREDIENTS

@allure.suite("Тесты заказов")
class TestOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_authorized(self, auth_token):
        response = create_order(VALID_INGREDIENTS, auth_token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    
    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized(self):
        response = create_order(VALID_INGREDIENTS)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, auth_token):
        response = create_order(VALID_INGREDIENTS, auth_token)
        assert response.status_code == 200
        assert response.json()["order"]["number"] is not None

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, auth_token):
        response = create_order([], auth_token)
        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash(self, auth_token):
        response = create_order(INVALID_INGREDIENTS, auth_token)
        assert response.status_code == 500
