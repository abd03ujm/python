import requests
import time
from datetime import datetime, timedelta

# Replace with your Datadog credentials
API_KEY = "your_api_key"
APP_KEY = "your_app_key"
DATADOG_SITE = "datadoghq.com"  # Use datadoghq.eu or other regional sites if applicable

# Convert current time to timestamp (in milliseconds)
current_time = time.time()  # Current time in seconds
current_time_ms = int(current_time * 1000)  # Convert to milliseconds

# Define time range in minutes (e.g., last 10 minutes)
minutes_ago = 10  # Adjust as needed
from_time = current_time_ms - (minutes_ago * 60 * 1000)
to_time = current_time_ms

# Datadog Logs Aggregation API URL
LOGS_API_URL = f"https://api.{DATADOG_SITE}/api/v2/logs/analytics/aggregate"

def fetch_service_and_hosts(from_ts, to_ts):
    """
    Fetch aggregated logs from Datadog and extract service names and their associated hosts.
    """
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": API_KEY,
        "DD-APPLICATION-KEY": APP_KEY,
    }

    # Request body for the aggregation (service and host)
    body = {
        "query": "",  # Empty query (can be modified if needed, e.g., filter by specific service)
        "time": {
            "from": from_ts,
            "to": to_ts,
        },
        "aggregations": [
            {"field": "service", "type": "count"},  # Aggregate by service
            {"field": "host", "type": "count"}     # Aggregate by host
        ],
        "limit": 50  # Adjust to fetch more results if needed
    }

    try:
        # Make the API request
        response = requests.post(LOGS_API_URL, headers=headers, json=body)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response
        data = response.json()

        # Process and extract service and host information
        buckets = data.get("data", {}).get("buckets", [])
        print("Service and Host Information:")
        for bucket in buckets:
            service = bucket.get("by", {}).get("service", "Unknown")
            host = bucket.get("by", {}).get("host", "Unknown")
            count = bucket.get("doc_count", 0)
            print(f"Service: {service}, Host: {host}, Log Count: {count}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching aggregated logs: {e}")

if __name__ == "__main__":
    fetch_service_and_hosts(from_time, to_time)
