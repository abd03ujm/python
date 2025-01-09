from datadog import initialize, api

# Replace with your Datadog API and application keys
API_KEY = 'your_api_key'
APP_KEY = 'your_app_key'

# Initialize the Datadog client
initialize(api_key=API_KEY, app_key=APP_KEY)

def get_services_and_hosts():
    """
    Fetch services and their associated hosts from Datadog.
    """
    try:
        # Fetch the list of hosts
        hosts = api.Hosts.search()
        if 'host_list' not in hosts:
            print("No hosts found.")
            return
        
        host_data = hosts['host_list']
        
        print("Service and Host Mapping:")
        for host in host_data:
            host_name = host.get('name', 'Unknown')
            services = host.get('tags_by_source', {}).get('datadog', [])
            
            print(f"\nHost: {host_name}")
            if services:
                print("  Services:")
                for service in services:
                    print(f"    - {service}")
            else:
                print("  No services found for this host.")
                
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_services_and_hosts()
