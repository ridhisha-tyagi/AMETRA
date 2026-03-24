from engine.interpretation import generate_planet_section
from engine.archetypes import generate_archetypes
from engine.archetype_section import build_archetype_section


PLANET_ORDER = [
    "Sun",
    "Moon",
    "Mercury",
    "Venus",
    "Mars",
    "Jupiter",
    "Saturn",
    "Rahu",
    "Ketu"
]


# ---------------------------------
# SYSTEM OVERVIEW
# ---------------------------------

def build_system_overview(pii_scores):

    system_names = {
        "Sun": "Identity System",
        "Moon": "Emotional System",
        "Mercury": "Thinking System",
        "Venus": "Relationship Pattern",
        "Mars": "Action System",
        "Jupiter": "Expansion & Wisdom",
        "Saturn": "Pressure & Karma",
        "Rahu": "Growth Drive",
        "Ketu": "Detachment Pattern"
    }

    def label(score):

        if score >= 6:
            return "Dominant"
        elif score >= 4:
            return "Strong"
        else:
            return "Present"

    section = "\nYOUR PSYCHOLOGICAL SYSTEMS\n\n"

    for planet in PLANET_ORDER:

        score = pii_scores.get(planet, 3)
        system = system_names.get(planet, planet)

        section += f"{system:<25} {label(score)}\n"

    section += "\n------------------------------------------------------------\n\n"

    return section


# ---------------------------------
# PROFILE SUMMARY
# ---------------------------------

def build_profile_summary(archetypes):

    core = archetypes.get("core", {})
    growth = archetypes.get("growth", {})

    core_title = core.get("title", "Unknown")
    growth_title = growth.get("title", "Unknown")

    qualities = core.get("qualities", [])
    limits = core.get("limitations", [])

    def format_list(items):

        text = ""

        for i in items[:3]:
            text += f"• {i}\n"

        return text

    section = f"""

PROFILE SUMMARY

Core Archetype
{core_title}

Growth Direction
{growth_title}

Primary Strengths
{format_list(qualities)}

Development Themes
{format_list(limits)}

------------------------------------------------------------

"""

    return section


# ---------------------------------
# REPORT BUILDER
# ---------------------------------

def build_report(chart_data, pii_scores):

    archetypes = generate_archetypes(chart_data, pii_scores)

    archetype_section = build_archetype_section(archetypes)

    system_overview = build_system_overview(pii_scores)

    summary = build_profile_summary(archetypes)

    report = (
        archetype_section
        + "\n\n"
        + system_overview
        + "\n\n------------------------------------------------------------\n\n"
    )

    for planet in PLANET_ORDER:

        section = generate_planet_section(
            planet,
            chart_data,
            pii_scores
        )

        report += section
        report += "\n\n------------------------------------------------------------\n\n"

    report += summary

    return {
        "report": report,
        "archetype": archetypes
    }