import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

filepath = glob.glob("files/*.txt")

pdf = FPDF(orientation="L", unit="mm", format="A4")

for i, file in enumerate(filepath):
    with open(file, "r") as f:
        data = f.read()
    filename = Path(file).stem
    title = filename.capitalize()

    pdf.add_page()
    pdf.set_font("Arial", size=18, style="B")
    pdf.multi_cell(0, 6, txt=title)
    pdf.ln(10)

    pdf.set_font("Arial", size=14)
    pdf.multi_cell(0, 6, txt=data)


pdf.output("output/result.pdf")
