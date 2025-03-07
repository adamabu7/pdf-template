from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100) # Color combination for R G B respectively range from 0 to 254.
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
         ln=1)          # border=1
    pdf.line(10, 21, 200, 21) #x1, y1, x2, y2 distances in mm.

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(277)         # Take 265 + h=12 from header to adjust the position of the footer.
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")

# Individual way to create pages.
# pdf.add_page()
#
# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello There!", align="L",
#          ln=1, border=1)
# pdf.set_font(family="Times", size=10)
# pdf.cell(w=0, h=12, txt="Hi There!", align="L",
#          ln=1, border=1)