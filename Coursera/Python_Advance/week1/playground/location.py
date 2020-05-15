from requests import get
from pprint import pprint


def get_location_info():
    return get("http://ip-api.com/json/").json()


if __name__ == "__main__":
    pprint(get_location_info())
