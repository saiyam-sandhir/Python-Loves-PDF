#MIT License Copyright (c) 2023 Saiyam Jain

from tkinter import *
import tkinter.filedialog as fd
import img2pdf

def converter(img_path, pdf_path):
    #converting image into chunks using img2pdf
    img_chunks = img2pdf.convert(img_path)

    #opening or creating a pdf file in binary format for writing
    pdfFile = open(pdf_path + "\\Python-Loves-PDF.pdf", "wb")

    #writing pdf files with the image chunks
    pdfFile.write(img_chunks)

    #closing the pdf file
    pdfFile.close()

class Image2Pdf_Win(Toplevel):
    def __init__(self, master, theme: list):
        super().__init__(master)
        BG_COL = theme[0][0]
        TXT_COL = theme[0][1]

        HEADER_TXT = theme[1][0]
        BODY_TXT = theme[1][1]

        self.title("Image to PDF")
        self.iconbitmap("images\\icon.ico")

        header = Frame(self, bg = BG_COL["header"])
        header.pack(fill = X)
        header_label = Label(header, text = "📷 ➡ 📄", font = HEADER_TXT, background = BG_COL["header"], foreground = TXT_COL["header"])
        header_label.pack(pady = (0, 15))

        body = Frame(self, bg = BG_COL["body"], height = 400)
        body.pack(fill = BOTH, expand = 1)

        self.body_select_button = Button(body, text = "Select Image file", font = BODY_TXT, command = self.open_image)
        self.body_select_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)

        body_save_button = Button(body, text = "Save as PDF...", font = BODY_TXT, command = self.save_pdf)
        body_save_button.pack(fill = BOTH, padx = 10, pady = 10, expand = 1)

    def open_image(self):
        self.file_name = fd.askopenfile().name
        self.body_select_button.config(text = self.file_name)

    def save_pdf(self):
        location = fd.askdirectory()
        converter(self.file_name, location)
