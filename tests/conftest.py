import pytest
import requests
import random
from faker import Faker

faker = Faker()

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
            "password": "ppppassword123"
        },
        "valid_username_invalid_password": {
            "username": "admin",
            "password": "passwordddd123"
        },
        "invalid_username_valid_password": {
            "username": "admin123",
            "password": "password123"
        }
    }


@pytest.fixture(scope="session")
def auth_header(login_payload):
    response = requests.post(f"http://54.255.195.111:5171/login", json=login_payload["valid_username_valid_password"])
    auth_token = response.json().get('authToken')
    headers = {"Authorization": f"Bearer {auth_token}"}

    return headers


@pytest.fixture
def teacher_payload():
    valid_department_list = ["CSE", "BBA", "MBA", "LAW", "PHARMACY", "ENGLISH"]
    random_department = random.choice(valid_department_list)
    designation_list = ["Assistant Professor", "Lecturer", "Senior Lecturer", "Associate Professor", "Professor"]
    random_designation = random.choice(designation_list)

    return {
        "valid_payload": {
            "name": faker.first_name() + " " + faker.last_name(),
            "email": faker.email(),
            "department": random_department,
            "teacherId": faker.unique.random_number(digits=6),
            "designation": random_designation
        },
        "payload_without_name": {
            "email": faker.email(),
            "department": random_department,
            "teacherId": faker.unique.random_number(digits=6),
            "designation": random_designation
        },
        "payload_without_email": {
            "name": faker.first_name() + " " + faker.last_name(),
            "department": random_department,
            "teacherId": faker.unique.random_number(digits=6),
            "designation": random_designation
        },
        "payload_without_department": {
            "name": faker.first_name() + " " + faker.last_name(),
            "email": faker.email(),
            "teacherId": faker.unique.random_number(digits=6),
            "designation": random_designation
        },
        "payload_without_teacher_id": {
            "name": faker.first_name() + " " + faker.last_name(),
            "email": faker.email(),
            "department": random_department,
            "designation": random_designation
        },
        "payload_without_designation ": {
            "name": faker.first_name() + " " + faker.last_name(),
            "email": faker.email(),
            "department": random_department,
            "teacherId": faker.unique.random_number(digits=6)
        },
        "payload_with_invalid_department": {
            "name": faker.first_name() + " " + faker.last_name(),
            "email": faker.email(),
            "department": "SWE",
            "teacherId": faker.unique.random_number(digits=6),
            "designation": random_designation
        },
        "payload_with_invalid_email": {
            "name": faker.first_name() + " " + faker.last_name(),
            "email": "johndoe#google.com",
            "department": "SWE",
            "teacherId": faker.unique.random_number(digits=6),
            "designation": random_designation
        },
    }
