import PyPDF2
from tkinter import *
import tkinter.filedialog as fd
  
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

class SplitPdf_Win(Toplevel):
    def __init__(self, master, theme: list):
        super().__init__(master)
        BG_COL = theme[0][0]
        TXT_COL = theme[0][1]

        HEADER_TXT = theme[1][0]
        BODY_TXT = theme[1][1]

        self.title("Split PDF")
        self.iconbitmap("images\\icon.ico")

        header = Frame(self, bg = BG_COL["header"])
        header.pack(fill = X)

        header_label = Label(header, text = "🪓 📄", font = HEADER_TXT, background = BG_COL["header"], foreground = TXT_COL["header"])
        header_label.pack(pady = (0, 15))

        body = Frame(self, bg = BG_COL["body"], height = 400)
        body.pack(fill = BOTH, expand = 1)

        Grid.columnconfigure(body, 0, weight = 1)
        Grid.columnconfigure(body, 1, weight = 1)

        self.body_select_button = Button(body, text = "Select PDF file", font = BODY_TXT, command = self.open_pdf)
        self.body_select_button.grid(column = 0, row = 0, columnspan = 2, padx = 10, pady = 10, sticky = EW)

        From = IntVar()
        self.body_spinbox_from = Spinbox(body, values = list(range(1, 1)), textvariable = From, wrap = True)
        self.body_spinbox_from.grid(column = 0, row = 1, padx = 10, pady = 10)

        To = IntVar()
        self.body_spinbox_to = Spinbox(body, values = list(range(1, 1)), textvariable = To, wrap = True)
        self.body_spinbox_to.grid(column = 1, row = 1, padx = 10, pady = 10)

        body_save_button = Button(body, text = "Save the split PDF...", font = BODY_TXT, command = self.save_split_pdf)
        body_save_button.grid(column = 0, row = 2, columnspan = 2, padx = 10, pady = 10, sticky = EW)

    def open_pdf(self):
        self.file_name = fd.askopenfile().name

        pdfFileObj = open(self.file_name, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        self.body_spinbox_from.config(values = list(range(1, len(pdfReader.pages) + 1)))
        self.body_spinbox_to.config(values = list(range(1, len(pdfReader.pages) + 1)))
        self.body_select_button.config(text = self.file_name)

    def save_split_pdf(self):
        location = fd.askdirectory()
        PDFsplit(self.file_name, [int(self.body_spinbox_from.get()), int(self.body_spinbox_to.get())], location)
