'''I have created a sample function that can segregate data from third-party api, right now I don't
 have any 3rd Party API'''



def get_country_from_ip(ip):
    # Logic to retrieve country based on IP
    country = ip_geolocation_api.get_country(ip)
    return country

def get_city_from_ip(ip):
    # Logic to retrieve city based on IP using third party geolocation api
    city = ip_geolocation_api.get_city(ip)
    return city
def extract_browser_from_user_agent(user_agent):
    # Logic to extract browser from user
    browser = user_agent_parser.parse_browser(user_agent)
    return browser
def extract_os_from_user_agent(user_agent):
    # Logic to extract OS from user agent
    os = user_agent_parser.parse_os(user_agent)
    return os

def extract_device_from_user_agent(user_agent):
    # Logic to extract device from user 
    device = user_agent_parser.parse_device(user_agent)
    return device