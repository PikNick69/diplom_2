import allure
import pytest
from endpoints.user import create_user, login_user
from data.test_data import generate_unique_user, ERROR_USER_EXISTS, ERROR_REQUIRED_FIELDS, ERROR_INVALID_CREDENTIALS

@allure.suite("Тесты пользователя")
class TestUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, unique_user):
        with allure.step("Отправить запрос на регистрацию"):
            response = create_user(unique_user)
        
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert response.json()["user"]["email"] == unique_user["email"]
        assert response.json()["user"]["name"] == unique_user["name"]


    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, registered_user):
        existing_user = {
            "email": registered_user["user"]["email"],
            "password": "password123",
            "name": "TestUser"
        }
        
        with allure.step("Отправить запрос на регистрацию существующего пользователя"):
            response = create_user(existing_user)
        
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == ERROR_USER_EXISTS

    
    @allure.title("Создание пользователя без заполнения обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, missing_field):
        user = generate_unique_user()
        del user[missing_field]
        
        with allure.step(f"Отправить запрос на регистрацию без поля {missing_field}"):
            response = create_user(user)
        
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == ERROR_REQUIRED_FIELDS


    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, login_credentials):
        with allure.step("Отправить запрос на авторизацию"):
            response = login_user(login_credentials)
        
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert response.json()["user"]["email"] == login_credentials["email"]


    @allure.title("Вход с неверным логином и паролем")
    @pytest.mark.parametrize("email,password", [
        ("wrong@email.com", "password123"),
        ("user@test.com", "wrongpassword"),
    ])
    def test_login_invalid_credentials(self, email, password):
        login_data = {"email": email, "password": password}
        
        with allure.step("Отправить запрос на авторизацию с неверными данными"):
            response = login_user(login_data)
        
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == ERROR_INVALID_CREDENTIALS