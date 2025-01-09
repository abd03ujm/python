from datadog import initialize, api
https://app.datadoghq.com/logs?query=&agg_m=count&agg_m_source=base&agg_q=service%2Chost&agg_q_source=base%2Cbase&agg_t=count&cols=host%2Cservice&fromUser=true&messageDisplay=inline&refresh_mode=sliding&sort_m=count%2Ccount&sort_m_source=base%2Cbase&sort_t=count%2Ccount&storage=flex_tier&stream_sort=desc&top_n=50%2C50&top_o=top%2Ctop&viz=query_table&x_missing=true%2Ctrue&from_ts=1736439211869&to_ts=1736440111869&live=true

# Replace with your Datadog API and application keys
API_KEY = 'your_api_key'
APP_KEY = 'your_app_key'

# Replace with your Datadog site URL and specific service name
DATADOG_SITE = 'datadoghq.com'  # Use datadoghq.eu if you're in the EU
SERVICE_NAME = 'your_service_name'

# Initialize the Datadog client with the site URL
options = {
    'api_key': API_KEY,
    'app_key': APP_KEY,
    'api_host': f'https://api.{DATADOG_SITE}'
}
initialize(**options)

def get_hosts_for_service(service_name):
    """
    Fetch hosts associated with a specific service from Datadog.
    """
    try:
        # Fetch the list of hosts
        hosts = api.Hosts.search()
        if 'host_list' not in hosts:
            print("No hosts found.")
            return

        host_data = hosts['host_list']
        associated_hosts = []

        print(f"Hosts associated with service '{service_name}':")
        for host in host_data:
            host_name = host.get('name', 'Unknown')
            services = host.get('tags_by_source', {}).get('datadog', [])

            if service_name in services:
                associated_hosts.append(host_name)

        if associated_hosts:
            for host in associated_hosts:
                print(f"  - {host}")
        else:
            print("No hosts found for the specified service.")
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_hosts_for_service(SERVICE_NAME)
