import requests
from datetime import datetime

TEST_MODE = True

SIGN_MAP = {
"Mesha": "ARIES",
"Vrishabha": "TAURUS",
"Mithuna": "GEMINI",
"Karka": "CANCER",
"Simha": "LEO",
"Kanya": "VIRGO",
"Tula": "LIBRA",
"Vrischika": "SCORPIO",
"Dhanu": "SAGITTARIUS",
"Makara": "CAPRICORN",
"Kumbha": "AQUARIUS",
"Meena": "PISCES"
}

TOKEN_URL = "https://api.prokerala.com/token"
CHART_URL = "https://api.prokerala.com/v2/astrology/planet-position"
DASHA_URL = "https://api.prokerala.com/v2/astrology/dasha-vimshottari"
CLIENT_ID = "e1dbb786-72d3-47cf-b4d8-d4c37ed2a12b"
CLIENT_SECRET = "YTz0Je03gJyq0NIMRWHFEfP9LvSn77VPcSALgEAl"


# ---------------------------
# ACCESS TOKEN
# ---------------------------

def get_access_token():

    r = requests.post(TOKEN_URL, data={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    })

    data = r.json()

    print("TOKEN RESPONSE:", data)   # 👈 VERY IMPORTANT

    if "access_token" not in data:
        raise Exception(f"Token Error: {data}")

    return data["access_token"]

# ---------------------------
# NAVAMSA
# ---------------------------

def navamsa(longitude):

    signs = [
        "ARIES","TAURUS","GEMINI","CANCER",
        "LEO","VIRGO","LIBRA","SCORPIO",
        "SAGITTARIUS","CAPRICORN","AQUARIUS","PISCES"
    ]

    sign_index = int(longitude // 30)

    deg_in_sign = longitude % 30

    nav = int(deg_in_sign / 3.3333)

    if sign_index in [0,4,8]:
        start = 0
    elif sign_index in [1,5,9]:
        start = 9
    elif sign_index in [2,6,10]:
        start = 6
    else:
        start = 3

    nav_sign = (start + nav) % 12

    return signs[nav_sign]


# ---------------------------
# DASHAS (API)
# ---------------------------

DASHA_SEQUENCE = [
"Ketu","Venus","Sun","Moon","Mars",
"Rahu","Jupiter","Saturn","Mercury"
]

DASHA_YEARS = {
"Ketu":7,
"Venus":20,
"Sun":6,
"Moon":10,
"Mars":7,
"Rahu":18,
"Jupiter":16,
"Saturn":19,
"Mercury":17
}
def calculate_dasha(moon_long, birth_date):

    DASHA_SEQUENCE = [
        "Ketu","Venus","Sun","Moon","Mars",
        "Rahu","Jupiter","Saturn","Mercury"
    ]

    DASHA_YEARS = {
        "Ketu":7,
        "Venus":20,
        "Sun":6,
        "Moon":10,
        "Mars":7,
        "Rahu":18,
        "Jupiter":16,
        "Saturn":19,
        "Mercury":17
    }

    # ---- Find Nakshatra ----

    nak_index = int(moon_long / 13.333333)

    maha = DASHA_SEQUENCE[nak_index % 9]

    # ---- Balance at birth ----

    deg_in_nak = moon_long % 13.333333
    remaining = 13.333333 - deg_in_nak

    fraction = remaining / 13.333333

    balance_years = DASHA_YEARS[maha] * fraction

    # ---- Years since birth ----

    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    now = datetime.now()

    years_passed = (now - birth).days / 365.25

    # ---- Advance timeline ----

    index = DASHA_SEQUENCE.index(maha)

    years_left = balance_years - years_passed

    while years_left < 0:

        index = (index + 1) % 9
        maha = DASHA_SEQUENCE[index]

        years_left += DASHA_YEARS[maha]

    # ---- Antardasha ----

    antara_index = (index + 1) % 9
    antara = DASHA_SEQUENCE[antara_index]

    return maha, antara

# ---------------------------
# MAIN CHART ENGINE
# ---------------------------

def generate_chart_data(birth_data):
    
    if TEST_MODE:
        return {
            "D1": {
                "Sun": {"sign": "LIBRA", "degree": 10, "longitude": 190, "retrograde": False, "house": 1},
                "Moon": {"sign": "CANCER", "degree": 15, "longitude": 105, "retrograde": False, "house": 10},
                "Mercury": {"sign": "LIBRA", "degree": 5, "longitude": 185, "retrograde": False, "house": 1},
                "Venus": {"sign": "SCORPIO", "degree": 12, "longitude": 222, "retrograde": False, "house": 2},
                "Mars": {"sign": "ARIES", "degree": 18, "longitude": 18, "retrograde": False, "house": 7},
                "Jupiter": {"sign": "SAGITTARIUS", "degree": 25, "longitude": 265, "retrograde": False, "house": 3},
                "Saturn": {"sign": "TAURUS", "degree": 2, "longitude": 32, "retrograde": False, "house": 8},
                "Rahu": {"sign": "GEMINI", "degree": 10, "longitude": 70, "retrograde": True, "house": 9},
                "Ketu": {"sign": "SAGITTARIUS", "degree": 10, "longitude": 250, "retrograde": True, "house": 3}
            },
            "D9": {
                "Sun": {"sign": "ARIES"},
                "Moon": {"sign": "PISCES"},
                "Mercury": {"sign": "TAURUS"},
                "Venus": {"sign": "LIBRA"},
                "Mars": {"sign": "SCORPIO"},
                "Jupiter": {"sign": "CANCER"},
                "Saturn": {"sign": "CAPRICORN"},
                "Rahu": {"sign": "VIRGO"},
                "Ketu": {"sign": "PISCES"}
            },
            "Dasha": {
                "Mahadasha": "Venus",
                "Antardasha": "Moon"
            }
        }

    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "datetime": f"{birth_data['date']}T{birth_data['time']}:00+05:30",
        "coordinates": f"{birth_data['lat']},{birth_data['lon']}",
        "ayanamsa": 1
    }

    r = requests.get(CHART_URL, headers=headers, params=params)

    response = r.json()

    if "data" not in response or "planet_position" not in response["data"]:
        raise Exception(f"Chart API error: {response}")

    planets = response["data"]["planet_position"]

    D1 = {}
    D9 = {}

    asc_long = None


    # ---------------------------
    # COLLECT PLANETS
    # ---------------------------
    
    moon_long = None

    for p in planets:

        name = p["name"]

        if name == "Ascendant":
            asc_long = p["longitude"]
            continue

        if name == "Moon":
            moon_long = p["longitude"]

        sign = SIGN_MAP.get(
            p["rasi"]["name"],
            p["rasi"]["name"].upper()
        )

        degree = round(p["degree"], 2)

        longitude = p["longitude"]

        retro = p["is_retrograde"]

        D1[name] = {
            "sign": sign,
            "degree": degree,
            "longitude": longitude,
            "retrograde": retro
        }


    # ---------------------------
    # SAFETY CHECK
    # ---------------------------

    if moon_long is None:
        raise Exception("Moon longitude not found in API response")


    # ---------------------------
    # HOUSES
    # ---------------------------

    SIGNS = [
        "ARIES","TAURUS","GEMINI","CANCER",
        "LEO","VIRGO","LIBRA","SCORPIO",
        "SAGITTARIUS","CAPRICORN","AQUARIUS","PISCES"
        ]

    asc_sign_index = int(asc_long // 30)

    for planet in D1:
        planet_long = D1[planet]["longitude"]

        planet_sign_index = int(planet_long // 30)

        house = ((planet_sign_index - asc_sign_index) % 12) + 1

        D1[planet]["house"] = house

    # ---------------------------
    # NAVAMSA
    # ---------------------------

    for planet in D1:

        lon = D1[planet]["longitude"]

        D9[planet] = {
            "sign": navamsa(lon)
        }


    # ---------------------------
    # DASHAS
    # ---------------------------

    maha, antara = calculate_dasha(moon_long, birth_data["date"])

    Dasha = {
        "Mahadasha": maha,
        "Antardasha": antara
    }


    return {
        "D1": D1,
        "D9": D9,
        "Dasha": Dasha
    }