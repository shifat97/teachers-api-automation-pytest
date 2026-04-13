from faker import Faker

from api.teachers_api import get_email_filter

faker = Faker()


# Testing status code
def test_email_filter_status_code(base_url, auth_header, created_teacher):
    email = created_teacher["email"]

    response = get_email_filter(base_url=base_url, auth_header=auth_header, email=email)

    # Validate status code
    assert response.status_code == 200, f"Expected 200, Got {response.status_code}"


# Testing search filter with email
def test_get_teachers_email_filter(base_url, auth_header, created_teacher):
    email = created_teacher["email"]

    response = get_email_filter(base_url=base_url, auth_header=auth_header, email=email)

    # Validate status code
    assert response.status_code == 200, f"Expected 200, Got {response.status_code}"

    teachers = response.json()
    # Validate teachers length - Must be 1
    assert len(teachers) == 1, f"Multiple response found: {teachers}"
    # Validate search email with response email
    assert teachers[0]["email"] == email, "Search email does not match"


# Negative test

# Search teacher with invalid email
def test_get_teachers_email_filter_invalid_email(base_url, auth_header):
    email = faker.email()
    response = get_email_filter(base_url=base_url, auth_header=auth_header, email=email)

    assert response.status_code == 404, f"Expected 404, Got {response.status_code}"
    # Validate message
    assert response.json().get("message") == "No user found", f"No user found with email: {email}"


# Testing get teachers without authorization header
def test_get_teacher_email_filter_without_authorization(base_url, auth_header, created_teacher):
    email = created_teacher["email"]

    response = get_email_filter(base_url=base_url, auth_header={}, email=email)

    # Validate status code
    assert response.status_code == 401, f"Expected 401, Got {response.status_code}"
    # Validate message
    assert response.json()["message"] == "Missing or invalid Authorization header", "Message is incorrect"


# Testing get teachers filter with invalid token
def test_get_teacher_with_invalid_token(base_url, auth_header, auth_header_with_invalid_token, created_teacher):
    email = created_teacher["email"]

    response = get_email_filter(base_url=base_url, auth_header=auth_header_with_invalid_token, email=email)

    # Validate status code
    assert response.status_code == 401, f"Expected 401, Got {response.status_code}"
    # Validate message
    assert "Invalid" in response.json().get("message", "")
