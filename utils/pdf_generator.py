from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def create_pdf(data):
    report_text = data.get('ai_report', 'No report provided.')
    filename = f"BugReport_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    file_path = os.path.join("static", "reports", filename)

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, height - 50, "BugSmith - AI Generated Bug Report")

    c.setFont("Helvetica", 12)
    y = height - 100
    lines = report_text.split('\n')
    for line in lines:
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 50
        c.drawString(40, y, line.strip())
        y -= 18

    c.save()
    return file_path
