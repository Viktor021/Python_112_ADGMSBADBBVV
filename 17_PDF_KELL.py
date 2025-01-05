from PyPDF2 import PdfReader, PdfWriter
import getpass

def protect_pdf(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    password = getpass.getpass("Enter a password: ")
    writer.encrypt(password)
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    print("The PDF has password protection.")

protect_pdf("clcoding.pdf", "protected_file.pdf")
