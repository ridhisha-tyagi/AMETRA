from astrology.planet_profiles import PLANET_PROFILES
from astrology.planet_profiles import get_profile

def get_intensity_label(score):

    if score >= 6:
        return "Dominant Influence"

    elif score >= 4:
        return "Strong Influence"

    else:
        return "Present Influence"


SYSTEM_NAMES = {

"Sun": "Identity System",
"Moon": "Emotional System",
"Mercury": "Thinking & Communication System",
"Venus": "Relationship Pattern",
"Mars": "Action System",
"Jupiter": "Expansion & Wisdom System",
"Saturn": "Pressure & Karmic System",
"Rahu": "Growth Drive",
"Ketu": "Detachment Pattern"

}


SYSTEM_INTRO = {

"Sun": "How you experience and express your core sense of self.",
"Moon": "How your emotional mind processes safety, connection, and vulnerability.",
"Mercury": "How your mind organizes information and communicates ideas.",
"Venus": "How you experience affection, attachment, and emotional connection.",
"Mars": "How you pursue goals, express drive, and respond to challenge.",
"Jupiter": "How your worldview develops and how life expands your understanding.",
"Saturn": "Where life applies pressure in order to build maturity and awareness.",
"Rahu": "The direction life encourages you to grow toward.",
"Ketu": "Patterns that feel familiar but may require conscious balance."

}


def format_list(items):

    if not items:
        return ""

    return "\n".join([f"• {i}" for i in items])


def generate_planet_section(planet, chart_data, pii_scores):

    d1_sign = chart_data["D1"][planet]["sign"]
    d9_sign = chart_data["D9"][planet]["sign"]

    score = pii_scores.get(planet, 3)

    intensity = get_intensity_label(score)

    # THIS is where get_profile must be called
    profile = get_profile(planet, d1_sign)

    growth_profile = get_profile(planet, d9_sign)

    pattern = profile["pattern"].strip()
    stress = profile["stress"].strip()
    growth = growth_profile["growth"].strip()

    qualities = profile.get("qualities", [])
    caution = profile.get("caution", "").strip()

    system_name = SYSTEM_NAMES.get(planet,"Psychological System")
    intro = SYSTEM_INTRO.get(planet,"")

    qualities_text = format_list(qualities)

    section = f"""
    {system_name}

    {intro}

    <font color="#FFBF00"><b>Influence Level:</b></font> 
    {intensity}

    <font color="#FFBF00"><b>Core Pattern:</b></font> 
    {pattern}

    <font color="#FFBF00"><b>Stress Pattern:</b></font> 
    {stress}

    <font color="#FFBF00"><b>Growth Direction:</b></font> 
    {growth}

    <font color="#FFBF00"><b>Qualities To Preserve:</b></font> 
    {qualities_text}

    <font color="#FFBF00"><b>Caution:</b></font> 
    {caution}
    """

    return section.strip()