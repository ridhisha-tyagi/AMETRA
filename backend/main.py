from engine.scoring import calculate_pii
from engine.report_builder import build_report
from charts.chart_generator import generate_chart_data
from pdf.pdf_generator import generate_pdf


def generate_report(birth_data):

    chart_data = generate_chart_data(birth_data)

    pii_scores = calculate_pii(chart_data)

    report_data = build_report(chart_data, pii_scores)

    return report_data


if __name__ == "__main__":

    birth_data = {
        "name": "Test User",
        "date": "2000-10-20",
        "time": "08:20",
        "place": "Yamunanagar"
    }

    report_data = generate_report(birth_data)

    preview_report = report_data["preview"]
    full_report = report_data["full"]

    print("\n\n--- REPORT PREVIEW ---\n\n")
    print(preview_report)

    pdf_file = generate_pdf(full_report)

    print("\nPDF generated:", pdf_file)
