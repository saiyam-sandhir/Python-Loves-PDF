#MIT License Copyright (c) 2023 Saiyam Jain

import configparser
from tkinter import *
from PDF2IMG import Pdf2Image_Win
from IMG2PDF import Image2Pdf_Win

config = configparser.ConfigParser()
config.read('settings.ini')

BG_COL = dict(config["BG_COL"])
TXT_COL = dict(config["TXT_COL"])
col_theme = [BG_COL, TXT_COL]

HEADER_TXT = (config["HEADER_TXT"]["family"], int(config["HEADER_TXT"]["size"]), config["HEADER_TXT"]["style"])
BODY_TXT = (config["BODY_TXT"]["family"], int(config["BODY_TXT"]["size"]))
font_theme = [HEADER_TXT, BODY_TXT]

main = Tk()

main.title("Python Loves PDF")
main.iconbitmap("images\\icon.ico")

header = Frame(main, bg = BG_COL["header"])
header.pack(fill = X)
header_label = Label(header, text = "Welcome!\n🐍 ♥ 📄", font = HEADER_TXT, background = BG_COL["header"], foreground = TXT_COL["header"])
header_label.pack(pady = (0,15))

body = Frame(main, bg = BG_COL["body"])
body.pack(fill = BOTH, expand = 1)

body_LabelFrame_pdfNimg = LabelFrame(body, text = "PDF & Image", font = (BODY_TXT[0], BODY_TXT[1], "bold"), background = BG_COL["body"], foreground = TXT_COL["body"], relief = "ridge")
body_LabelFrame_pdfNimg.pack(padx = 20, pady = 20, fill = X)

#Giving equal weightage to the 2 columns in body_LabelFrame_pdfNimg's grid
Grid.columnconfigure(body_LabelFrame_pdfNimg, 0, weight = 1)
Grid.columnconfigure(body_LabelFrame_pdfNimg, 1, weight = 1)

pdf2img_image = PhotoImage(file = "images\\pdf2img.png")
body_Pdf2Img_button = Button(body_LabelFrame_pdfNimg, image = pdf2img_image, command = lambda: Pdf2Image_Win(main, [col_theme, font_theme]))
body_Pdf2Img_button.grid(column = 0, row = 0, pady = (10, 5))
body_Pdf2Img_Label = Label(body_LabelFrame_pdfNimg, text = "PDF ➡ Image", font = BODY_TXT, background = BG_COL["body"], foreground = TXT_COL["body"])
body_Pdf2Img_Label.grid(column = 0, row = 1, pady = (0, 10))

img2pdf_image = PhotoImage(file = "images\\img2pdf.png")
body_Img2Pdf_button = Button(body_LabelFrame_pdfNimg, image = img2pdf_image, command = lambda: Image2Pdf_Win(main, [col_theme, font_theme]))
body_Img2Pdf_button.grid(column = 1, row = 0, pady = (10, 5))
body_Img2Pdf_Label = Label(body_LabelFrame_pdfNimg, text = "Image ➡ PDF", font = BODY_TXT, background = BG_COL["body"], foreground = TXT_COL["body"])
body_Img2Pdf_Label.grid(column = 1, row = 1, pady = (0, 10))

main.mainloop()