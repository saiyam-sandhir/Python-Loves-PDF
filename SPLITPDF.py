import PyPDF2
  
def PDFsplit(pdf_file, splits: list, output_path):
    pdfFileObj = open(pdf_file, 'rb')

    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    pdfWriter = PyPDF2.PdfWriter()
    outputpdf = output_path + "\\pdf_split" + '.pdf'
    for page in range(splits[0] - 1, splits[1]):
        pdfWriter.add_page(pdfReader.pages[page])
          
    with open(outputpdf, "wb") as f:
        pdfWriter.write(f)
          
    pdfFileObj.close()