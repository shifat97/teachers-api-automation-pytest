import requests


# Function for post teacher endpoint
def create_teacher(base_url, auth_header, payload):
    response = requests.post(f"{base_url}/api/teacher", json=payload, headers=auth_header)
    return response


# Function for get teacher endpoint
def get_teacher(base_url, auth_header):
    response = requests.get(f"{base_url}/api/teacher", headers=auth_header)
    return response


# Function for email filter endpoint
def get_email_filter(base_url, auth_header, email):
    response = requests.get(f"{base_url}/api/teacher?email={email}", headers=auth_header)
    return response
