import csv
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

from dme_helper import get_dme_id

# Define API endpoints
API_BASE_URL = "http://localhost:8000/api/v1"

# DME API endpoints
EQUIPMENT_URL = f"{API_BASE_URL}/equipment/"
DME_ORDER_URL = f"{API_BASE_URL}/equipment_orders/"
DME_ORDER_ITEMS_URL = f"{API_BASE_URL}/equipment_order_items/"

# Client API endpoints
CLIENTS_URL = f"{API_BASE_URL}/clients/"
AREAS_URL = f"{API_BASE_URL}/clients_area_serviced/"

# CSV file path
CSV_FILE_PATH = "./data/dme-orders.csv"

# Authentication credentials
USERNAME = "admin"
PASSWORD = "password"

# Format helper functions
def format_gender(input):
    # make the input lowercase
    input = input.lower()
    if input == "m":
        return "MA"
    elif input == "f":
        return "FE"
    elif input == "female":
        return "FE"
    elif input == "male":
        return "MA"
    return None

def format_ethnicity(input):
    input = input.lower()
    if "asian" in input:
        return "AS"
    elif "black" in input:
        return "BL"
    elif "hispanic" in input or "latino" in input or "spanish" in input:
        return "HI"
    elif "white" in input:
        return "WH"
    else:
        return "OT"
    
def format_date(date_str):
    try:
        # Parse the input date string
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        # Format the date to the desired format
        formatted_date = date_obj.strftime("%Y-%m-%d")
    except ValueError:
        # If there's an error with the date, use the current date
        formatted_date = datetime.now().strftime("%Y-%m-%d")
    return formatted_date

def format_age(age_str):
    try:
        return int(age_str)
    except ValueError:
        print (f"Invalid age value: {age_str}")
        return None
    
def map_time_needed(time_needed_str):
    time_needed_map = {
        "1 week": "1W",
        "2 weeks": "2W",
        "1 month": "1M",
        "3 months": "3M",
        "6 months": "6M",
        "1 year": "1Y",
        "indefinitely": "1Y",  # Assuming indefinite means 1 year
        "Unknown": "1W",  # Default to 1 week if unknown
        "Not known yet": "1W",  # Default to 1 week if not known
        "to be determined": "1W"  # Default to 1 week if to be determined
    }
    return time_needed_map.get(time_needed_str.lower(), "1W")

# Helper functions to interact with the API
def get_area_by_zipcode(zipcode):
    response = requests.get(AREAS_URL, params={"search": zipcode}, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    response.raise_for_status()
    areas = response.json()
    if areas:
        return areas[0]["id"]
    return None

def get_client_by_name(client_name):
    response = requests.get(CLIENTS_URL, params={"search": client_name}, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    response.raise_for_status()
    clients = response.json()
    if clients:
        return clients[0]["id"]
    return None

def create_client(client_data):
    
    print (f"Client Data: ", client_data)

    client_id = get_client_by_name(client_data["name"])
    if client_id:
        return client_id
    response = requests.post(CLIENTS_URL, json=client_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    response.raise_for_status()
    return response.json()["id"]

# Helper functions to interact with the DME API
def get_dme_by_name(dme_name):
    response = requests.get(EQUIPMENT_URL, params={"search": dme_name}, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    response.raise_for_status()
    equipment = response.json()
    if equipment:
        return equipment[0]["id"]
    return None

def create_dme_order(order_data):
    response = requests.post(DME_ORDER_URL, json=order_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    response.raise_for_status()
    return response.json()["id"]

def create_dme_order_item(order_item_data):
    print (f"Order Item Data: {order_item_data}")
    response = requests.post(DME_ORDER_ITEMS_URL, json=order_item_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    response.raise_for_status()
    return response.json()["id"]

# Main script
def ingest_data():
    with open(CSV_FILE_PATH, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")

        for row in reader:
            # Check if client already exists
            client_id = get_client_by_name(row["Name of Recipient"])
            if not client_id:
                # Map client data
                client_data = {
                    "name": row["Name of Recipient"],
                    "age": format_age(row["Age"]) if row["Age"] else None,
                    "gender": format_gender(row["Gender"]),
                    "email": row["Email Address"],
                    "phone": row["Phone Number"],
                    "address": row["Address of Recipient"],
                    "zipcode": row["ZIPCODE"],
                    "ethnicity": format_ethnicity(row["Race/Ethnicity"]),
                    "below_poverty_line": row["Under Poverty Level? (Below $1,250 a month)"].lower() == "yes",
                    "homeless": row["Homeless?"].lower() == "yes",
                    "veteran": row["Military Veteran?"].lower() == "yes" if "Military Veteran?" in row else False,
                    "disabled": row["Disabled?"].lower() == "yes",
                    "is_active": True,
                    "area_serviced": get_area_by_zipcode(row["ZIPCODE"])
                }
                client_id = create_client(client_data)

            # Map DME order data
            order_data = {
                "client": client_id,
                "status": "RT",
                "time_needed": map_time_needed(row["Approximate Length of Time Needed"]),
                "rental_date": format_date(row["Date Received"])
            }

            print(f"Creating DME order for client: {client_id}")
            dme_order_id = create_dme_order(order_data)

            # Map supplies and supply order items
            for i in range(22, 36):  
                # Get header name at index i
                equipment_name = reader.fieldnames[i]
                # Get quantity of equipment
                equipment_quantity = row[equipment_name]

                # Check if equipment name and quantity are not empty
                if equipment_name and equipment_quantity:
                    
                    supplies_id = get_dme_id(equipment_name)

                    print (f"Supplies ID: {supplies_id}")
                    print (f"Equipment Quantity: {equipment_quantity}")

                    if supplies_id and equipment_quantity:
                        supply_order_item_data = {
                            "quantity": int(equipment_quantity),
                            "other_notes": "",
                            "order": dme_order_id,
                            "equipment": supplies_id
                        }
                        create_dme_order_item(supply_order_item_data)

if __name__ == "__main__":
    try:
        ingest_data()
        print("Data ingested successfully!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
