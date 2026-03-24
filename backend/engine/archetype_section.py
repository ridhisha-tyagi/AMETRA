def format_list(items):

    if not items:
        return ""

    lines = "\n".join([f"• {item}" for item in items])

    return lines


def build_archetype_section(archetypes):

    core = archetypes.get("core", {})
    growth = archetypes.get("growth", {})

    def extract_tarot(archetype):

        tarot = archetype.get("tarot")

        if isinstance(tarot, dict):
            return tarot.get("neutral", "Unknown")

        return tarot or "Unknown"


    def build_section(archetype, title):

        name = archetype.get("title", "Unknown Archetype")

        overview = archetype.get("description", "")
        meaning = archetype.get("archetype_meaning", "")

        qualities = format_list(archetype.get("qualities", []))
        limits = format_list(archetype.get("limitations", []))

        tarot = extract_tarot(archetype)

        tarot_meaning = archetype.get("tarot_meaning", "")

        section = f"""
{title}

{name}

Archetype Overview
{overview}

Psychological Meaning
{meaning}

Qualities To Preserve
{qualities}

Common Limitations
{limits}

Tarot Mirror
{tarot}

Symbolic Meaning
{tarot_meaning}

------------------------------------------------------------
"""

        return section


    core_section = build_section(core, "CORE ARCHETYPE")

    growth_section = build_section(growth, "GROWTH ARCHETYPE")

    return core_section + growth_section