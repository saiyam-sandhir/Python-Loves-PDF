from pdf2jpg import pdf2jpg
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import *

def converter(images_folder_path, pdf_path):
    pdf2jpg.convert_pdf2jpg(pdf_path, images_folder_path, pages="ALL")

class Pdf2Image_Win(tk.Toplevel):
    def __init__(self, master, col_theme: list):
        super().__init__(master)
        BG_COL = col_theme[0]
        TXT_COL = col_theme[1]

        self.title("PDF to Image")
        self.iconbitmap("images\\icon.ico")

        header = Frame(self, bg = BG_COL["header"])
        header.pack(fill = X)
        header_label = Label(header, text = "📄 ➡ 📷", font = ("Bahnschrift", 50, 'bold'), background = BG_COL["header"], foreground = TXT_COL["header"])
        header_label.pack(pady = (0, 15))

        body = Frame(self, bg = BG_COL["body"], height = 400)
        body.pack(fill = BOTH, expand = 1)

        self.body_select_button = Button(body, text = "Select PDF file", font = ("Arial", 10, "bold"), command = self.open_pdf)
        self.body_select_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)

        body_save_button = Button(body, text = "Save...", font = ("Arial", 10, "bold"), command = self.save_images_folder)
        body_save_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)

    def open_pdf(self):
        self.file_name = fd.askopenfile().name
        self.body_select_button.config(text = self.file_name)

    def save_images_folder(self):
        location = fd.askdirectory()
        converter(location, self.file_name)
