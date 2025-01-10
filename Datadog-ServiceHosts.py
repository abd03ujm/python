import requests

# Datadog API and Application keys
API_KEY = "your_api_key"
APP_KEY = "your_app_key"

# Base URL
BASE_URL = "https://api.datadoghq.com/api/v1"

# Fetch Services
def fetch_services():
    url = f"{BASE_URL}/services"
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": API_KEY,
        "DD-APPLICATION-KEY": APP_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # Returns list of services
    else:
        print(f"Error fetching services: {response.status_code}, {response.text}")
        return None

# Fetch Hosts
def fetch_hosts():
    url = f"{BASE_URL}/hosts"
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": API_KEY,
        "DD-APPLICATION-KEY": APP_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # Returns list of hosts
    else:
        print(f"Error fetching hosts: {response.status_code}, {response.text}")
        return None

# Fetch services and hosts
services = fetch_services()
hosts = fetch_hosts()

# Combine Services and Hosts
if services and hosts:
    print("Services and Associated Hosts:")
    for service in services:
        print(f"Service: {service['name']}")
        for host in hosts['host_list']:
            if service['name'] in host.get('services', []):  # Check if the service is on the host
                print(f"  Host: {host['name']}")
