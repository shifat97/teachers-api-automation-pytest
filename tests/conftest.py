import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "http://54.255.195.111:5171"


@pytest.fixture(scope="session")
def login_payload():
    return {
        "valid_username_valid_password": {
            "username": "admin",
            "password": "password123"
        },
        "invalid_username_invalid_password": {
            "username": "admin123",
            "password": "password123"
        },
        "valid_username_invalid_password": {
            "username": "admin123",
            "password": "password123"
        },
        "invalid_username_valid_password": {
            "username": "admin123",
            "password": "password123"
        }
    }
