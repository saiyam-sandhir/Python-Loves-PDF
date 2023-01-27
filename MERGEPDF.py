from PyPDF2 import PdfWriter
from tkinter import *

def pdf_merger(pdf_files: list, output_path):
    merger = PdfWriter()

    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()

class MergePdf_Win(Toplevel):
    def __init__(self, master, theme: list):
        super().__init__(master)
        BG_COL = theme[0][0]
        TXT_COL = theme[0][1]

        HEADER_TXT = theme[1][0]
        BODY_TXT = theme[1][1]

        self.title("Merge PDFs")
        self.iconbitmap("images\\icon.ico")

        header = Frame(self, bg = BG_COL["header"])
        header.pack(fill = X)
        header_label = Label(header, text = "📄 ➕ 📄", font = HEADER_TXT, background = BG_COL["header"], foreground = TXT_COL["header"])
        header_label.pack(pady = (0, 15))

        body = Frame(self, bg = BG_COL["body"], height = 400)
        body.pack(fill = BOTH, expand = 1)

        self.body_select_button = Button(body, text = "Select PDF files", font = BODY_TXT)
        self.body_select_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)

        body_save_button = Button(body, text = "Merge and save...", font = BODY_TXT)
        body_save_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)

        