#MIT License Copyright (c) 2023 Saiyam Jain

from pdf2jpg import pdf2jpg
import tkinter.filedialog as fd
from tkinter import *

def converter(images_folder_path, pdf_path):
    pdf2jpg.convert_pdf2jpg(pdf_path, images_folder_path, pages="ALL")

class Pdf2Image_Win(Toplevel):
    def __init__(self, master, theme: list):
        super().__init__(master)
        BG_COL = theme[0][0]
        TXT_COL = theme[0][1]

        HEADER_TXT = theme[1][0]
        BODY_TXT = theme[1][1]

        self.title("PDF to Image")
        self.iconbitmap("images\\icon.ico")

        header = Frame(self, bg = BG_COL["header"])
        header.pack(fill = X)
        header_label = Label(header, text = "📄 ➡ 📷", font = HEADER_TXT, background = BG_COL["header"], foreground = TXT_COL["header"])
        header_label.pack(pady = (0, 15))

        body = Frame(self, bg = BG_COL["body"], height = 400)
        body.pack(fill = BOTH, expand = 1)

        self.body_select_button = Button(body, text = "Select PDF file", font = BODY_TXT, command = self.open_pdf)
        self.body_select_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)

        body_save_button = Button(body, text = "Save as image(s)...", font = BODY_TXT, command = self.save_images_folder)
        body_save_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)

    def open_pdf(self):
        self.file_name = fd.askopenfile().name
        self.body_select_button.config(text = self.file_name)

    def save_images_folder(self):
        location = fd.askdirectory()
        converter(location, self.file_name)
