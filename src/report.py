# src/report.py
from fpdf import FPDF

def generate_report(route, demand, health_status, path="data/report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "RPM Hire - Sustainability Report", ln=True, align="C")

    pdf.cell(200, 10, f"Optimal Route: {route}", ln=True)
    pdf.cell(200, 10, f"Demand Forecast: {demand.to_dict('records')}", ln=True)
    pdf.cell(200, 10, f"Equipment Health: {health_status}", ln=True)

    pdf.output(path)
    return path

if __name__ == "__main__":
    print("Report generated at:", generate_report([0,1,2,3], None, "OK"))
