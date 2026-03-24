from flask import Flask, render_template, request, send_from_directory
import os

from backend.charts.chart_generator import generate_chart_data
from backend.engine.scoring import calculate_pii
from backend.engine.archetypes import generate_archetypes
from backend.pdf_generator import generate_pdf


app = Flask(__name__)
app.secret_key = "ametra_secret_key_123"

# -----------------------------
# SYSTEM NAME MAP
# -----------------------------

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


# -----------------------------
# BASIC PAGES
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/generate")
def generate_page():
    return render_template("generate.html")


# -----------------------------
# GENERATE PREVIEW
# -----------------------------
from flask import session

@app.route("/generate", methods=["POST"])
def generate():

    birth_data = {
        "name": request.form.get("name"),
        "date": request.form.get("date"),
        "time": request.form.get("time"),
        "place": request.form.get("place"),
        "lat": request.form.get("lat"),
        "lon": request.form.get("lon")
    }

    # -----------------------------
    # GENERATE CORE DATA
    # -----------------------------
    chart_data = generate_chart_data(birth_data)

    pii_scores = calculate_pii(chart_data)

    archetypes = generate_archetypes(chart_data, pii_scores)

    user_name = birth_data.get("name", "User")

    # -----------------------------
    # FIND TOP SYSTEMS (🔥 FIXED POSITION)
    # -----------------------------
    top_systems = sorted(
        pii_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    top_system_names = [SYSTEM_NAMES[p] for p, s in top_systems]

    # -----------------------------
    # SAVE TO DATABASE (🔥 NOW SAFE)
    # -----------------------------
    from database import get_connection

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO reports (name, date, time, place, archetype, top_system, payment_status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        birth_data["name"],
        birth_data["date"],
        birth_data["time"],
        birth_data["place"],
        archetypes["core"]["title"],
        top_system_names[0] if top_system_names else "",
        "preview"
    ))

    conn.commit()
    conn.close()

    # -----------------------------
    # GENERATE PREVIEW PDF
    # -----------------------------
    preview_pdf_path = generate_pdf(
        chart_data,
        archetypes,
        pii_scores,
        user_name,
        preview=True
    )

    preview_filename = os.path.basename(preview_pdf_path)
    preview_pdf_url = f"/pdf/{preview_filename}"

    # -----------------------------
    # SAVE TO SESSION
    # -----------------------------
    session["chart_data"] = chart_data
    session["pii_scores"] = pii_scores
    session["archetypes"] = archetypes
    session["birth_data"] = birth_data

    # -----------------------------
    # RETURN PREVIEW PAGE
    # -----------------------------
    return render_template(
        "preview.html",
        birth_data=birth_data,
        archetype_title=archetypes["core"]["title"],
        archetype_desc=archetypes["core"]["description"],
        archetype_symbol=archetypes["core"].get("symbol", "✦"),
        systems=top_system_names,
        preview_pdf_url=preview_pdf_url
    )
    
# -----------------------------
# SERVE GENERATED PDF
# -----------------------------

@app.route("/pdf/<filename>")
def serve_pdf(filename):

    folder = os.path.join(os.path.dirname(__file__), "generated_pdf")

    return send_from_directory(folder, filename)


# -----------------------------
# DOWNLOAD FULL REPORT ONLY
# -----------------------------

@app.route("/download", methods=["POST"])
def download():

    from flask import session
    from database import get_connection

    # 🔒 check unlock
    if request.form.get("unlocked") != "true":
        return "Access Denied"

    chart_data = session.get("chart_data")
    pii_scores = session.get("pii_scores")
    archetypes = session.get("archetypes")
    birth_data = session.get("birth_data")

    if not chart_data:
        return "Session expired. Please generate again."

    user_name = birth_data.get("name", "User")

    # 🔥 generate FULL PDF here ONLY
    full_pdf_path = generate_pdf(
        chart_data,
        archetypes,
        pii_scores,
        user_name,
        preview=False
    )

    folder = os.path.dirname(full_pdf_path)
    filename = os.path.basename(full_pdf_path)
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE reports
    SET payment_status = 'paid'
    WHERE id = (
        SELECT id FROM reports
        WHERE name = ? AND date = ? AND time = ?
        ORDER BY id DESC
        LIMIT 1
    )
    """, (
        birth_data["name"],
        birth_data["date"],
        birth_data["time"]
    ))

    conn.commit()
    conn.close()

    return send_from_directory(
        folder,
        filename,
        as_attachment=True
    )


# -----------------------------
# RUN SERVER
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)