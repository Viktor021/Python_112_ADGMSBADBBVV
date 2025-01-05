import img2pdf

with open("TVH.jpg", "rb") as image:
    pdf_bytes = img2pdf.convert(image.read())

with open("TVH.pdf", "wb") as pdf:
    pdf.write(pdf_bytes)

print("Image has been converted to PDF successfully")