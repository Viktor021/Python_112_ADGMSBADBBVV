from PyPDF import PdfReader, PdfWriter
import getpass
def protect_pdf(input_pdf, output_pdf):
    reader = PdfReader('clcoding.pdf')
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    password = getpass.getpass('Enter a password: ')
    writer.encrypt(password)
    with open(output_pdf) as output_file:
        writer.write(output_file)
    print(f"The PDF has password.")

protect_pdf("clcoding.pdf", "protected_file.pdf")