import requests

from test_create_teacher import create_teacher


def get_teacher(base_url, auth_header):
    response = requests.get(f"{base_url}/api/teacher", headers=auth_header)

    return response


# Positive test

# Testing endpoint to get all teachers
def test_get_teachers_status_code(base_url, auth_header, teacher_payload):
    response = get_teacher(base_url=base_url, auth_header=auth_header)

    # Validate status code
    assert response.status_code == 200, f"Expected 200, Got {response.status_code}"


# Validate payload structure
def test_get_teachers_payload_structure(base_url, auth_header, teacher_payload, test_payload_structure):
    response = get_teacher(base_url=base_url, auth_header=auth_header)

    assert response.status_code == 200, f"Expected 200, Got {response.status_code}"
    teachers = response.json()

    for teacher in teachers:
        for key, expected_type in test_payload_structure.items():
            key_type = type(teacher.get(key))

            # Validate if key in missing or not in the response
            assert key in teacher, f"{key} is missing on teacher: {teacher}"
            # Validate key type
            assert key_type == expected_type, f"Expected {expected_type}, Got {key_type}"
            # Validate if any value is null or not
            assert teacher[key] is not None, f"{teacher['_id']} on {key} has null value: {teacher[key]}"


# Validate if duplicate id exists or not
def test_get_teachers_duplicate_id(base_url, auth_header, teacher_payload):
    response = get_teacher(base_url=base_url, auth_header=auth_header)

    assert response.status_code == 200, f"Expected 200, Got {response.status_code}"
    teachers = response.json()

    ids = [teacher["teacherId"] for teacher in teachers]
    assert len(ids) == len(set(ids)), "Duplicate id exists in the list"


# Validate if created teacher is in the list or not
def test_get_teacher_after_creation(base_url, auth_header, teacher_payload):
    # Create a teacher for testing purpose
    create_teacher(base_url=base_url, auth_header=auth_header, payload=teacher_payload["valid_payload"])

    response = get_teacher(base_url=base_url, auth_header=auth_header)

    assert response.status_code == 200, f"Expected 200, Got {response.status_code}"
    teachers = response.json()

    ids = [teacher["teacherId"] for teacher in teachers]
    teacher_id = teacher_payload["valid_payload"]["teacherId"]
    assert teacher_id in ids, f"{teacher_id} is not in the list after creation"


# Negative test

# Testing get teachers without authorization header
def test_get_teacher_without_authorization(base_url, teacher_payload):
    response = requests.get(f"{base_url}/api/teacher", headers={})

    # Validate status code
    assert response.status_code == 401, f"Expected 401, Got {response.status_code}"
    # Validate message
    assert response.json()["message"] == "Missing or invalid Authorization header", "Message is incorrect"
