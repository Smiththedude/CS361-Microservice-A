import requests
import json

BASE_URL = "http://127.0.0.1:5000/licenses"

sample_licenses = [
    {"name": "Software A", "owner": "User1", "type": "Commercial"},
    {"name": "Software B", "owner": "User2", "type": "Open Source"},
    {"name": "Software C", "owner": "User3", "type": "Enterprise"}
]

def add_license(license_data):
    response = requests.post(BASE_URL, json=license_data)
    if response.status_code == 201:
        print(f"License Added: {response.json()}")
        return response.json()["id"]
    else:
        print(f"Failed to add license: {response.text}")

def get_all_licenses():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print(f"\nAll Licenses: {json.dumps(response.json(), indent=4)}")
    else:
        print(f"Failed to fetch licenses: {response.text}")

def get_license(license_id):
    response = requests.get(f"{BASE_URL}/{license_id}")
    if response.status_code == 200:
        print(f"\nLicense Details: {json.dumps(response.json(), indent=4)}")
    else:
        print(f"License not found: {response.text}")

def delete_license(license_id):
    response = requests.delete(f"{BASE_URL}/{license_id}")
    if response.status_code == 200:
        print(f"License {license_id} deleted successfully!")
    else:
        print(f"Failed to delete license: {response.text}")

if __name__ == "__main__":
    license_ids = []
    for lic in sample_licenses:
        license_id = add_license(lic)
        if license_id:
            license_ids.append(license_id)

    get_all_licenses()

    if license_ids:
        get_license("bb785114-a789-4cfb-86ee-3d5f2ff96a38")

    if license_ids:
        delete_license(license_ids[0])
        get_all_licenses()
