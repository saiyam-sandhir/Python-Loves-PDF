import tkinter as tk
from tkinter import *
import img2pdf

def converter(img_path, pdf_path):
    #converting image into chunks using img2pdf
    img_chunks = img2pdf.convert(img_path)

    #opening or creating a pdf file in binary format for writing
    pdfFile = open(pdf_path, "wb")

    #writing pdf files with the image chunks
    pdfFile.write(img_chunks)

    #closing the pdf file
    pdfFile.close()

class Image2Pdf_Win(tk.Toplevel):
    def __init__(self, master, col_theme: list):
        super().__init__(master)
        BG_COL = col_theme[0]
        TXT_COL = col_theme[1]

        self.title("Image to PDF")
        self.iconbitmap("images\\icon.ico")

        header = Frame(self, bg = BG_COL["header"])
        header.pack(fill = X)
        header_label = Label(header, text = "📷 ➡ 📄", font = ("Bahnschrift", 50, 'bold'), background = BG_COL["header"], foreground = TXT_COL["header"])
        header_label.pack(pady = (0, 15))

        body = Frame(self, bg = BG_COL["body"], height = 400)
        body.pack(fill = BOTH, expand = 1)

        body_select_button = Button(body, text = "Select Image file", font = ("Arial", 10, "bold"))
        body_select_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)

        body_save_button = Button(body, text = "Save...", font = ("Arial", 10, "bold"))
        body_save_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)