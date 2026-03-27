import allure
import pytest
from endpoints.user import create_user, login_user
from data.test_data import generate_unique_user

@allure.suite("Тесты пользователя")
class TestUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, unique_user):
        response = create_user(unique_user)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert response.json()["user"]["email"] == unique_user["email"]
        assert response.json()["user"]["name"] == unique_user["name"]
        token = response.json()["accessToken"]
        from endpoints.user import delete_user
        delete_user(token)


    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, registered_user):
        existing_user = {
            "email": registered_user["user"]["email"],
            "password": "password123",
            "name": "TestUser"
        }
        response = create_user(existing_user)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    
    @allure.title("Создание пользователя без заполнения обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, missing_field):
        user = generate_unique_user()
        del user[missing_field]
        response = create_user(user)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"


    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, login_credentials):
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
        response = login_user(login_data)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"