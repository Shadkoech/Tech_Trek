import requests

response = requests.get('http://127.0.0.1:8000/api/trucks/')
if response.status_code == 200:
    trucks_data = response.json()  # Parse the JSON response
    truck_list = [
        {"id": truck["id"], "cab_plate": truck["cab_plate"], "driver": truck["driver"]}
        for truck in trucks_data["all_trucks"]
    ]
    print(truck_list)
else:
    print("Something went wrong!")
    print(response.text)  # Print the error response
