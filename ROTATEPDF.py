import PyPDF2
  
def PDFrotate(origFileName, newFile_path, rotation):
  
    pdfFileObj = open(origFileName, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    pdfWriter = PyPDF2.PdfWriter()
      
    # rotating each page
    for page in range(len(pdfReader.pages)):
  
        # creating rotated page object
        pageObj = pdfReader.pages[page]
        pageObj.rotate(rotation)
  
        # adding rotated page object to pdf writer
        pdfWriter.add_page(pageObj)
  
    with open(newFile_path + "\\pdf_rotate.pdf", "wb") as f:
    	pdfWriter.write(newFile_path + "\\pdf_rotate.pdf")