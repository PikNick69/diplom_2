import uuid

BASE_URL = "https://stellarburgers.education-services.ru/api"

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