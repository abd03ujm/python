from datadog import initialize, api
import datetime

# Replace with your Datadog API and application keys
API_KEY = 'your_api_key'
APP_KEY = 'your_app_key'

# Initialize the Datadog client
initialize(api_key=API_KEY, app_key=APP_KEY)

def fetch_hosts_for_service(service_name):
    """
    Fetch hosts for a specific service from Datadog Log Explorer.
    """
    try:
        # Define the time window for the logs (last 1 hour)
        end_time = datetime.datetime.utcnow()
        start_time = end_time - datetime.timedelta(hours=1)

        # Query logs using the Datadog API for the specific service
        response = api.Logs.query(
            start=start_time.isoformat(),
            end=end_time.isoformat(),
            query=f"service:{service_name}",  # Specific service name filter
            limit=100,  # Limit the number of logs retrieved (adjust as necessary)
        )
        
        # Check if there are logs
        if 'data' in response:
            hosts = set()  # Use a set to avoid duplicate hosts
            for log in response['data']:
                # Extract host information from the log
                host = log.get('host', None)
                if host:
                    hosts.add(host)
            
            # Display hosts found
            if hosts:
                print(f"Hosts for service '{service_name}':")
                for host in hosts:
                    print(f"  - {host}")
            else:
                print(f"No hosts found for service '{service_name}'.")
        else:
            print(f"No logs found for service '{service_name}' in the given time range.")
    
    except Exception as e:
        print(f"Error fetching logs: {e}")

if __name__ == "__main__":
    service_name = "your_service_name"  # Replace with the service name you want to query
    fetch_hosts_for_service(service_name)
