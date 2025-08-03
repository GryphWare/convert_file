from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

#dang ky font (arial co ho tro vn)
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))

#duong dan file
text_path = "C:\\Users\\chanh\\code\\bin\\song.txt"

with open(text_path, 'r', encoding = "utf-8") as file_txt:
    content = file_txt.read()

pdf_path = os.path.splitext(text_path)[0] + ".pdf"
c = canvas.Canvas(pdf_path)
c.setFont("Arial", 12)

y = 800
for line in content.splitlines():
    c.drawString(50, y, line)
    y -= 15
    if y < 50:
        c.showPage()
        c.setFont("Arial", 12)
        y = 800

c.save()
print("xong:", pdf_path)
    
