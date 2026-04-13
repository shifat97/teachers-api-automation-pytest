import requests


def create_teacher(base_url, auth_header, payload):
    if auth_header:
        response = requests.post(f"{base_url}/api/teacher", json=payload, headers=auth_header)
    else:
        response = requests.post(f"{base_url}/api/teacher", json=payload)

    return response


# Positive tests
# Testing create teacher with valid payload
def test_post_teacher_with_valid_payload(base_url, auth_header, teacher_payload):
    response = create_teacher(base_url=base_url, auth_header=auth_header, payload=teacher_payload["valid_payload"])
    data = response.json()

    # Validate status code
    assert response.status_code in [200, 201], f"Expected 200 or 201, Got {response.status_code}"
    # Validate if _id exists in the payload or not
    assert "_id" in data, "_id is missing from response"
    # Validate if _id is not empty
    assert data["_id"], "_id is empty in the response"
    # Validate if response is empty or not
    assert data, "Response is empty"

    # Validate response body with payload
    for key in teacher_payload["valid_payload"]:
        actual_value = teacher_payload["valid_payload"][key]

        # Validate actual key exits in the response or not
        assert key in data, f"{key} is missing from response"
        # Validate actual payload with response payload
        assert actual_value == data[key], f"Expected {actual_value}, got {data[key]}"


# Negative tests

# Testing create teacher without authorization header
def test_post_teacher_without_authorization(base_url, teacher_payload):
    response = create_teacher(base_url, auth_header=None, payload=teacher_payload)

    # Validate status code
    assert response.status_code == 401, f"Expected 401, Got {response.status_code}"
    # Validate message
    assert response.json()["message"] == "Missing or invalid Authorization header", "Message is incorrect"


# Testing create teacher without name field
def test_post_teacher_without_name_field(base_url, auth_header, teacher_payload):
    response = create_teacher(base_url=base_url, auth_header=auth_header,
                              payload=teacher_payload["payload_without_name"])

    # Validate status code
    assert response.status_code == 400, f"Expected 400, Got {response.status_code}"
    # Validate error message
    assert response.json()["error"] == "Name is required", "Error message is incorrect"


# Testing create teacher without email field
def test_post_teacher_without_email_field(base_url, auth_header, teacher_payload):
    response = create_teacher(base_url=base_url, auth_header=auth_header,
                              payload=teacher_payload["payload_without_email"])

    # Validate status code
    assert response.status_code == 400, f"Expected 400, Got {response.status_code}"
    # Validate error message
    assert response.json()["error"] == "Email is required", "Error message is incorrect"


# Testing create teacher without department field
def test_post_teacher_without_department_field(base_url, auth_header, teacher_payload):
    response = create_teacher(base_url=base_url, auth_header=auth_header,
                              payload=teacher_payload["payload_without_department"])

    # Validate status code
    assert response.status_code == 400, f"Expected 400, Got {response.status_code}"
    # Validate error message
    assert response.json()["error"] == "Department is required", "Error message is incorrect"


# Testing create teacher without teacherId field
def test_post_teacher_without_teacher_id_field(base_url, auth_header, teacher_payload):
    response = create_teacher(base_url=base_url, auth_header=auth_header,
                              payload=teacher_payload["payload_without_teacher_id"])

    # Validate status code
    assert response.status_code == 400, f"Expected 400, Got {response.status_code}"
    # Validate error message
    assert response.json()["error"] == "Teacher ID is required", "Error message is incorrect"


# Testing create teacher without designation field
def test_post_teacher_without_designation_field(base_url, auth_header, teacher_payload):
    response = create_teacher(base_url=base_url, auth_header=auth_header,
                              payload=teacher_payload["payload_without_designation"])

    # Validate status code
    assert response.status_code == 400, f"Expected 400, Got {response.status_code}"
    # Validate error message
    assert response.json()["error"] == "Designation is required", "Error message is incorrect"


# Testing create teacher with invalid department
def test_post_teacher_with_invalid_department(base_url, auth_header, teacher_payload):
    response = create_teacher(base_url=base_url, auth_header=auth_header,
                              payload=teacher_payload["payload_with_invalid_department"])

    # Validate status code
    assert response.status_code == 400, f"Expected 400, Got {response.status_code}"
    # Validate error message
    assert response.json()[
               "error"] == "Department must be one of CSE, BBA, MBA, LAW, PHARMACY, ENGLISH", "Error message is incorrect"


# Testing create teacher with invalid email
def test_post_teacher_with_invalid_email(base_url, auth_header, teacher_payload):
    response = create_teacher(base_url=base_url, auth_header=auth_header,
                              payload=teacher_payload["payload_with_invalid_email"])
    print(response.json(), response.status_code)
    # Validate status code
    assert response.status_code == 400, f"Expected 400, Got {response.status_code}"
    # Validate error message
    assert response.json()["error"] == "Email must be valid", "Error message is incorrect"
