from PyPDF2 import PdfWriter

def pdf_merger(pdf_files: list, output_path):
    merger = PdfWriter()

    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()