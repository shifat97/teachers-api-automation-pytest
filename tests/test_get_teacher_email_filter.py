import random

import requests
from faker import Faker

from test_get_teachers import get_teacher

faker = Faker()


# Get and store all email address
# Choose a random email from the list
def generate_random_email(base_url, auth_header):
    teachers = get_teacher(base_url, auth_header)

    emails = [teacher["email"] for teacher in teachers.json()]
    random_email = random.choice(emails)

    return random_email


def get_email_filter(base_url, auth_header, email):
    response = requests.get(f"{base_url}/api/teacher?email={email}", headers=auth_header)
    return response


# Testing status code
def test_email_filter_status_code(base_url, auth_header):
    email = generate_random_email(base_url, auth_header)
    response = get_email_filter(base_url=base_url, auth_header=auth_header, email=email)

    # Validate status code
    assert response.status_code == 200, f"Expected 200, Got {response.status_code}"


# Testing search filter with email
def test_get_teachers_email_filter(base_url, auth_header):
    email = generate_random_email(base_url, auth_header)
    response = get_email_filter(base_url=base_url, auth_header=auth_header, email=email)

    # Validate status code
    assert response.status_code == 200, f"Expected 200, Got {response.status_code}"

    teacher = response.json()
    # Validate teachers length - Must be 1
    assert len(teacher) == 1, f"Multiple response found with same email: {teacher['email']}"
    # Validate search email with response email
    assert teacher[0]["email"] == email, "Search email does not match"
    # Validate response is not null
    assert len(teacher) > 0, "Teacher should not be empty with valid email"


# Search teacher with invalid email
def test_get_teachers_email_filter_invalid_email(base_url, auth_header):
    email = faker.email()
    response = get_email_filter(base_url=base_url, auth_header=auth_header, email=email)

    assert response.status_code == 404, f"Expected 404, Got {response.status_code}"
    # Validate message
    assert response.json().get("message") == "No user found", f"No user found with email: {email}"


# Negative test

# Testing get teachers without authorization header
def test_get_teacher_email_filter_without_authorization(base_url, auth_header):
    email = generate_random_email(base_url, auth_header=auth_header)
    response = get_email_filter(base_url=base_url, auth_header={}, email=email)

    # Validate status code
    assert response.status_code == 401, f"Expected 401, Got {response.status_code}"
    # Validate message
    assert response.json()["message"] == "Missing or invalid Authorization header", "Message is incorrect"


# Testing get teachers filter with invalid token
def test_get_teacher_with_invalid_token(base_url, auth_header):
    email = generate_random_email(base_url, auth_header)

    custom_header = {
        "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNzcyODc0MzM0LCJleHAiOjE3NzI5NjA3MzR9.MLdRG9fIubC-AOmi0KF0wZBYssf-CX1DmS-CGITcLBw"
    }

    response = get_email_filter(base_url=base_url, auth_header=custom_header, email=email)

    # Validate status code
    assert response.status_code == 401, f"Expected 401, Got {response.status_code}"
    # Validate message
    assert response.json()["message"] == "Invalid or expired token", "Message is incorrect"
