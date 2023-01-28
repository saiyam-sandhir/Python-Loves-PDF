import PyPDF2
from tkinter import *
  
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

class RotatePdf_Win(Toplevel):
    def __init__(self, master, theme: list):
        super().__init__(master)
        BG_COL = theme[0][0]
        TXT_COL = theme[0][1]

        HEADER_TXT = theme[1][0]
        BODY_TXT = theme[1][1]

        self.title("Rotate PDF pages")
        self.iconbitmap("images\\icon.ico")

        header = Frame(self, bg = BG_COL["header"])
        header.pack(fill = X)
        header_label = Label(header, text = "🔄 📄", font = HEADER_TXT, background = BG_COL["header"], foreground = TXT_COL["header"])
        header_label.pack(pady = (0, 15))

        body = Frame(self, bg = BG_COL["body"], height = 400)
        body.pack(fill = BOTH, expand = 1)

        self.body_select_button = Button(body, text = "Select PDF file", font = BODY_TXT)
        self.body_select_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)

        body_save_button = Button(body, text = "Save PDF...", font = BODY_TXT)
        body_save_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)
        