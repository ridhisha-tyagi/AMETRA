import math
from datetime import datetime

SIGNS = [
"ARIES","TAURUS","GEMINI","CANCER",
"LEO","VIRGO","LIBRA","SCORPIO",
"SAGITTARIUS","CAPRICORN","AQUARIUS","PISCES"
]

NAKSHATRA_LORDS = [
"Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury",
"Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury",
"Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury"
]

DASHA_SEQUENCE = ["Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury"]

DASHA_YEARS = {
"Ketu":7,"Venus":20,"Sun":6,"Moon":10,
"Mars":7,"Rahu":18,"Jupiter":16,"Saturn":19,"Mercury":17
}

AYANAMSA = 24


# -------------------------
# JULIAN DAY
# -------------------------

def julian_day(date_str,time_str):

    dt = datetime.strptime(date_str + " " + time_str,"%Y-%m-%d %H:%M")

    y = dt.year
    m = dt.month
    d = dt.day + (dt.hour/24)

    if m <= 2:
        y -= 1
        m += 12

    A = int(y/100)
    B = 2 - A + int(A/4)

    jd = int(365.25*(y+4716)) + int(30.6001*(m+1)) + d + B - 1524.5

    return jd


# -------------------------
# SIDEREAL
# -------------------------

def sidereal(lon,jd):

    lon = lon - AYANAMSA

    if lon < 0:
        lon += 360

    return lon


# -------------------------
# SUN LONGITUDE (approx)
# -------------------------

def sun_longitude(jd):

    n = jd - 2451545.0

    L = (280.460 + 0.9856474*n) % 360
    g = math.radians((357.528 + 0.9856003*n) % 360)

    lam = L + 1.915*math.sin(g) + 0.020*math.sin(2*g)

    return lam % 360


# -------------------------
# MOON LONGITUDE (approx)
# -------------------------

def moon_longitude(jd):

    n = jd - 2451550.1

    L = (218.316 + 13.176396*n) % 360
    M = math.radians((134.963 + 13.064993*n) % 360)

    lon = L + 6.289*math.sin(M)

    return lon % 360


# -------------------------
# SIMPLE PLANET MODEL
# -------------------------

def simple_planet(base,offset):

    return (base + offset) % 360


# -------------------------
# SIGN + DEGREE
# -------------------------

def sign_degree(lon):

    sign_index = int(lon // 30)

    sign = SIGNS[sign_index]

    deg = lon % 30

    return sign,deg


# -------------------------
# HOUSE
# -------------------------

def house(planet,asc):

    h = ((planet - asc) % 360) // 30 + 1

    return int(h)


# -------------------------
# NAVAMSA
# -------------------------

def navamsa(lon):

    sign_index = int(lon // 30)

    deg_in_sign = lon % 30

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

    return SIGNS[nav_sign]


# -------------------------
# NAKSHATRA
# -------------------------

def nakshatra(moon):

    index = int(moon / 13.3333)

    return NAKSHATRA_LORDS[index]


# -------------------------
# MAHADASHA
# -------------------------

def mahadasha(moon):

    lord = nakshatra(moon)

    deg = moon % 13.3333

    remain = 13.3333 - deg

    fraction = remain / 13.3333

    balance = DASHA_YEARS[lord] * fraction

    return lord,balance