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
    response = create_teacher(base_url, auth_header, teacher_payload["valid_payload"])
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