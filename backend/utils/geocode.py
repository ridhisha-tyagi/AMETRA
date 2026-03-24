import requests

def get_coordinates(place):

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": place,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "ametra-app"
    }

    r = requests.get(url, params=params, headers=headers)

    data = r.json()

    if len(data) == 0:
        raise Exception("Location not found")

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])

    return lat, lon

