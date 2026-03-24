def calculate_pii(chart_data):

    scores = {}

    for planet, data in chart_data["D1"].items():

        score = 3

        house = data.get("house", 0)

        # Angular houses
        if house in [1,4,7,10]:
            score += 2

        # Trinal houses
        elif house in [5,9]:
            score += 1

        # Difficult houses
        elif house in [6,8,12]:
            score -= 1

        # Retrograde
        if data.get("retrograde"):
            score += 1

        # Luminaries naturally louder
        if planet in ["Sun", "Moon"]:
            score += 1

        scores[planet] = score

    return scores