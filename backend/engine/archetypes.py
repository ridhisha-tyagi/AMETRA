from collections import Counter


# --------------------------------------------------
# ARCHETYPE DEFINITIONS
# --------------------------------------------------

ARCHETYPES = {

"LUMINARY": {

"title": "The Luminary",
"symbol": "☼",

"description":
"A presence that naturally draws attention and influences the emotional tone of environments.",

"archetype_meaning":
"The Luminary archetype appears in individuals whose identity systems tend to radiate outward into their surroundings. "
"Their presence often shapes the emotional climate of groups and can encourage enthusiasm, clarity, or confidence.",

"qualities": [
"ability to inspire others",
"natural warmth and enthusiasm",
"confidence in personal expression",
"capacity to energize environments"
],

"limitations": [
"seeking validation from external attention",
"feeling responsible for maintaining group energy",
"placing too much pressure on personal visibility"
],

"tarot": {
"masculine": "The Sun",
"feminine": "Queen of Wands",
"neutral": "The Star"
},

"tarot_meaning":
"These tarot symbols represent illumination, vitality, and hope. They reflect the ability to bring clarity "
"and emotional brightness into situations."
},


"EMPATH": {

"title": "The Empath",
"symbol": "☾",

"description":
"Individuals who are naturally attentive to emotional atmosphere and relational dynamics.",

"archetype_meaning":
"The Empath archetype appears in people whose emotional systems register interpersonal signals quickly. "
"They often notice subtle shifts in mood and emotional tone in environments.",

"qualities": [
"strong emotional awareness",
"ability to understand others' feelings",
"capacity for compassion and emotional support"
],

"limitations": [
"absorbing emotional stress from others",
"difficulty separating personal feelings from group atmosphere",
"emotional exhaustion when boundaries are unclear"
],

"tarot": {
"masculine": "King of Cups",
"feminine": "Queen of Cups",
"neutral": "Ace of Cups"
},

"tarot_meaning":
"These tarot symbols reflect emotional intelligence, compassion, and the ability to hold complex feelings with steadiness."
},


"ARCHITECT": {

"title": "The Architect",
"symbol": "🏛",

"description":
"Builders of stable systems who value structure, reliability, and long-term development.",

"archetype_meaning":
"The Architect archetype appears in individuals who approach life through organization and structure. "
"They often focus on creating systems that produce reliable results over time.",

"qualities": [
"ability to build long-term systems",
"discipline and reliability",
"strategic thinking about stability"
],

"limitations": [
"resistance to sudden change",
"overemphasis on control or order",
"difficulty relaxing rigid expectations"
],

"tarot": {
"masculine": "King of Pentacles",
"feminine": "Queen of Pentacles",
"neutral": "The Emperor"
},

"tarot_meaning":
"These tarot images symbolize stability, stewardship, and the cultivation of systems that support sustainable growth."
},


"CATALYST": {

"title": "The Catalyst",
"symbol": "⚡",

"description":
"People who stimulate change when environments become stagnant.",

"archetype_meaning":
"The Catalyst archetype appears in individuals who instinctively react when systems feel stuck or outdated. "
"Their ideas or actions often provoke transformation.",

"qualities": [
"ability to initiate transformation",
"direct communication of difficult truths",
"courage to challenge stagnant systems"
],

"limitations": [
"creating disruption without intending to",
"impatience with slower processes",
"being perceived as confrontational"
],

"tarot": {
"masculine": "Knight of Swords",
"feminine": "Queen of Swords",
"neutral": "Death"
},

"tarot_meaning":
"These tarot cards represent transformation and clarity. They symbolize the ending of patterns "
"that no longer support growth."
},


"ORACLE": {

"title": "The Observer",
"symbol": "👁",

"description":
"Observers who notice patterns and underlying meanings.",

"archetype_meaning":
"The Observer archetype appears in individuals who prefer reflection before action. "
"They often notice patterns others overlook.",

"qualities": [
"strong intuition",
"pattern recognition",
"ability to observe before reacting"
],

"limitations": [
"over-withdrawing from active participation",
"remaining in observation instead of action",
"difficulty sharing insights openly"
],

"tarot": {
"masculine": "The Hermit",
"feminine": "The High Priestess",
"neutral": "The Moon"
},

"tarot_meaning":
"These tarot symbols represent introspection, intuition, and the quiet observation that precedes understanding."
},


"STRATEGIST": {

"title": "The Analyst",
"symbol": "♟",

"description":
"Analytical thinkers who evaluate situations before acting.",

"archetype_meaning":
"The Analyst archetype appears in individuals who rely strongly on reasoning and structured thinking.",

"qualities": [
"clear analytical thinking",
"objective evaluation of situations",
"ability to plan strategically"
],

"limitations": [
"overthinking decisions",
"becoming detached from emotional factors",
"difficulty acting without complete analysis"
],

"tarot": {
"masculine": "King of Swords",
"feminine": "Queen of Swords",
"neutral": "Justice"
},

"tarot_meaning":
"These tarot symbols reflect intellectual clarity, reason, and the pursuit of fair judgment."
},


"INITIATOR": {

"title": "The Initiator",
"symbol": "⚔",

"description":
"People who naturally begin actions, projects, or movements.",

"archetype_meaning":
"The Initiator archetype appears in individuals who are comfortable taking the first step in uncertain situations.",

"qualities": [
"natural courage to begin action",
"ability to motivate others into movement",
"confidence in personal initiative"
],

"limitations": [
"impatience with slower progress",
"starting projects without finishing them",
"reacting before full reflection"
],

"tarot": {
"masculine": "King of Wands",
"feminine": "Queen of Wands",
"neutral": "The Magician"
},

"tarot_meaning":
"These tarot symbols represent initiative, creative force, and the ability to translate ideas into action."
},


"NAVIGATOR": {

"title": "The Explorer",
"symbol": "🧭",

"description":
"Explorers driven by curiosity and the desire to experience new environments.",

"archetype_meaning":
"The Explorer archetype appears in individuals who learn through movement, discovery, and experience.",

"qualities": [
"curiosity about the world",
"adaptability in new environments",
"ability to learn from diverse experiences"
],

"limitations": [
"difficulty committing to one direction",
"restlessness when routines develop",
"moving forward before integrating lessons"
],

"tarot": {
"masculine": "Knight of Wands",
"feminine": "Queen of Cups",
"neutral": "Wheel of Fortune"
},

"tarot_meaning":
"These tarot images reflect journeys, cycles of change, and the unfolding path of experience."
},


"MEDIATOR": {

"title": "The Mediator",
"symbol": "⚖",

"description":
"Balancers who restore harmony between perspectives.",

"archetype_meaning":
"The Mediator archetype appears in individuals who recognize tension between viewpoints "
"and attempt to restore balance.",

"qualities": [
"ability to understand multiple perspectives",
"diplomacy in conflict situations",
"natural inclination toward fairness"
],

"limitations": [
"avoiding necessary conflict",
"delaying decisions to maintain peace",
"placing harmony above personal truth"
],

"tarot": {
"masculine": "King of Cups",
"feminine": "Queen of Cups",
"neutral": "Temperance"
},

"tarot_meaning":
"These tarot symbols represent balance, moderation, and the blending of perspectives."
},


"VISIONARY": {

"title": "The Visionary",
"symbol": "✧",

"description":
"Future-oriented thinkers who perceive possibilities others may overlook.",

"archetype_meaning":
"The Visionary archetype appears in individuals whose thinking naturally explores emerging ideas "
"or future potential.",

"qualities": [
"innovative thinking",
"ability to imagine future possibilities",
"interest in social or intellectual progress"
],

"limitations": [
"becoming detached from present realities",
"difficulty communicating complex ideas clearly",
"feeling misunderstood by others"
],

"tarot": {
"masculine": "King of Swords",
"feminine": "Queen of Swords",
"neutral": "The Star"
},

"tarot_meaning":
"These tarot images represent hope, imagination, and forward thinking."
},


"SOVEREIGN": {

"title": "The Sovereign",
"symbol": "♛",

"description":
"A stabilizing presence who organizes environments through responsibility and leadership.",

"archetype_meaning":
"The Sovereign archetype appears in individuals who naturally assume responsibility for direction "
"within systems or groups.",

"qualities": [
"ability to guide and organize groups",
"strong sense of responsibility",
"capacity to create stability"
],

"limitations": [
"taking on too much responsibility",
"difficulty delegating control",
"feeling personally accountable for everything"
],

"tarot": {
"masculine": "The Emperor",
"feminine": "Queen of Wands",
"neutral": "The Sun"
},

"tarot_meaning":
"These tarot images represent authority, structure, and the creation of stable order."
}

}


# --------------------------------------------------
# PLANET → ARCHETYPE MAP
# --------------------------------------------------

PLANET_ARCHETYPE_MAP = {
"Sun": "LUMINARY",
"Moon": "EMPATH",
"Mercury": "STRATEGIST",
"Venus": "MEDIATOR",
"Mars": "INITIATOR",
"Jupiter": "NAVIGATOR",
"Saturn": "ARCHITECT",
"Rahu": "VISIONARY",
"Ketu": "ORACLE"
}


# --------------------------------------------------
# DOMINANT PLANET
# --------------------------------------------------

def get_dominant_planet(pii_scores):
    return max(pii_scores, key=pii_scores.get)


# --------------------------------------------------
# CORE ARCHETYPE
# --------------------------------------------------

def get_core_archetype(pii_scores):

    dominant = get_dominant_planet(pii_scores)

    archetype_key = PLANET_ARCHETYPE_MAP.get(dominant)

    return ARCHETYPES.get(archetype_key, ARCHETYPES["EMPATH"])


# --------------------------------------------------
# GROWTH ARCHETYPE
# --------------------------------------------------

def get_growth_archetype(chart_data ,  pii_scores=None):

    # fallback safety
    if not pii_scores:
        d9 = chart_data["D9"]
        signs = [data["sign"] for data in d9.values()]
        dominant_sign = Counter(signs).most_common(1)[0][0]

        if dominant_sign in ["ARIES","CANCER","LIBRA","CAPRICORN"]:
            return ARCHETYPES["INITIATOR"]

        if dominant_sign in ["TAURUS","LEO","SCORPIO","AQUARIUS"]:
            return ARCHETYPES["SOVEREIGN"]

        if dominant_sign in ["GEMINI","VIRGO","SAGITTARIUS","PISCES"]:
            return ARCHETYPES["VISIONARY"]


    # -----------------------------
    # NEW LOGIC (SMART GROWTH)
    # -----------------------------

    sorted_planets = sorted(
        pii_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # top 3 planets
    top_planets = [p for p, _ in sorted_planets[:3]]

    # get archetypes from them
    archetype_keys = [
        PLANET_ARCHETYPE_MAP.get(p)
        for p in top_planets
        if PLANET_ARCHETYPE_MAP.get(p)
    ]

    # remove duplicates
    archetype_keys = list(dict.fromkeys(archetype_keys))

    # if multiple, pick second strongest as growth
    if len(archetype_keys) > 1:
        return ARCHETYPES.get(archetype_keys[1])

    # fallback
    return ARCHETYPES.get(archetype_keys[0], ARCHETYPES["EMPATH"])


# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------

def generate_archetypes(chart_data, pii_scores):

    core = get_core_archetype(pii_scores)

    growth = get_growth_archetype(chart_data, pii_scores)   
    
    return {
        "core": core,
        "growth": growth
    }