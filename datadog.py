import requests

def check_datadog_url(url, api_key, app_key):
    """
    Checks access to a Datadog URL using API and Application keys.
    
    Args:
        url (str): The Datadog URL to check.
        api_key (str): Datadog API key.
        app_key (str): Datadog Application key.

    Returns:
        str: The status of the URL access.
    """
    headers = {
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return f"Success: Able to access {url} (Status Code: 200)"
        else:
            return f"Warning: Access to {url} returned status code {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to access {url}. Reason: {e}"

if __name__ == "__main__":
    # Replace these values with your Datadog keys
    datadog_api_key = "your_api_key_here"
    datadog_app_key = "your_application_key_here"

    # Datadog endpoint to validate API and Application keys
    datadog_url = "https://api.datadoghq.com/api/v1/validate"

    result = check_datadog_url(datadog_url, datadog_api_key, datadog_app_key)
    print(result)
