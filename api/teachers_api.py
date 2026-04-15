import requests

from utils.logger import logger_init


# POST
# Function for post teacher endpoint
def create_teacher(base_url, auth_header, payload):
    response = requests.post(f"{base_url}/api/teacher", json=payload, headers=auth_header)
    logger_init(response)
    return response


# GET
# Function for get teacher endpoint
def get_teacher(base_url, auth_header):
    response = requests.get(f"{base_url}/api/teacher", headers=auth_header)
    logger_init(response)
    return response


# GET
# Function for email filter endpoint
def get_teacher_filter(base_url, auth_header, filter_type, filter_value):
    response = requests.get(f"{base_url}/api/teacher?{filter_type}={filter_value}", headers=auth_header)
    logger_init(response)
    return response
