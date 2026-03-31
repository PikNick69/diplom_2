import uuid

def generate_unique_user():
    email = f"user_{uuid.uuid4()}@test.com"
    return {
        "email": email,
        "password": "password123",
        "name": "TestUser"
    }

VALID_INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",
    "61c0c5a71d1f82001bdaaa6f"
]

INVALID_INGREDIENTS = ["invalid_hash_123"]

# Ожидаемые сообщения об ошибках
ERROR_USER_EXISTS = "User already exists"
ERROR_REQUIRED_FIELDS = "Email, password and name are required fields"
ERROR_INVALID_CREDENTIALS = "email or password are incorrect"
ERROR_NO_INGREDIENTS = "Ingredient ids must be provided"