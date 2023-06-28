from ip_details import (
    get_country_from_ip,
    get_city_from_ip,
    extract_browser_from_user_agent,
    extract_os_from_user_agent,
    extract_device_from_user_agent
)

def process_clickstream_data(clickstream_data):
    # Assuming clickstream_data is a dictionary with keys: 'UserID', 'Timestamp', 'URL', 'IP', 'UserAgent' and other details
    processed_data = {
        'UserID': clickstream_data['UserID'],
        'Timestamp': clickstream_data['Timestamp'],
        'URL': clickstream_data['URL'],
        'Country': get_country_from_ip(clickstream_data['IP']),
        'City': get_city_from_ip(clickstream_data['IP']),
        'Browser': extract_browser_from_user_agent(clickstream_data['UserAgent']),
        'OS': extract_os_from_user_agent(clickstream_data['UserAgent']),
        'Device': extract_device_from_user_agent(clickstream_data['UserAgent'])
    }
    return processed_data