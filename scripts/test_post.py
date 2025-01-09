import requests
from requests.auth import HTTPBasicAuth

# Define API endpoint
CLIENTS_URL = "http://localhost:8000/api/v1/clients/"

# Authentication credentials
USERNAME = "admin"
PASSWORD = "password"

# Client data
client_data = {
    'name': 'Bob Misiorowski',
    'age': None,
    'gender': 'MA',
    'email': 'bobmisiorowski@gmail.co,',
    'phone': '3104860805',
    'address': 'PO Box1171',
    'zipcode': '85624',
    'ethnicity': 'WH',
    'below_poverty_line': False,
    'homeless': False,
    'veteran': False,
    'disabled': False,
    'is_active': True,
    'area_serviced': 7
}

# Make the POST request to create the client
response = requests.post(CLIENTS_URL, json=client_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))

# Check the response
if response.status_code == 201:
    print("Client created successfully!")
    print("Client ID:", response.json()["id"])
else:
    print("Failed to create client.")
    print("Status Code:", response.status_code)
    print("Response:", response.json())