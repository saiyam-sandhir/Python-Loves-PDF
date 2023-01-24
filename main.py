import tkinter as tk
from tkinter import *
from PDF2IMG import Pdf2Image_Win
from IMG2PDF import Image2Pdf_Win

BG_COL = {
    "header": "#7286D3",
    "body": "#E5E0FF"
}
TXT_COL = {
    "header": "#FFFBF5",
    "body": "#03001C"
}
col_theme = [BG_COL, TXT_COL]

main = Tk()

main.title("Python Loves PDF")
main.iconbitmap("images\\icon.ico")

main_header = Frame(main, bg = BG_COL["header"])
main_header.pack(fill = X)
main_header_label = Label(main_header, text = "Welcome!\n🐍 ♥ 📄", font = ("Bahnschrift", 50, 'bold'), background = BG_COL["header"], foreground = TXT_COL["header"])
main_header_label.pack(pady = (0,15))

main_body = Frame(main, bg = BG_COL["body"], height = 400)
main_body.pack(fill = BOTH, expand = 1)

main_body_LabelFrame_pdfNimg = LabelFrame(main_body, text = "PDF & Image", font = ("Arial", 15, "bold"), background = BG_COL["body"], foreground = TXT_COL["body"], relief = "ridge")
main_body_LabelFrame_pdfNimg.pack(padx = 20, pady = 20, fill = X)

#Giving equal weightage to the 2 columns in main_body_LabelFrame_pdfNimg's grid
Grid.columnconfigure(main_body_LabelFrame_pdfNimg, 0, weight = 1)
Grid.columnconfigure(main_body_LabelFrame_pdfNimg, 1, weight = 1)

pdf2img_image = PhotoImage(file = "images\\pdf2img.png")
main_body_Pdf2Img_button = Button(main_body_LabelFrame_pdfNimg, image = pdf2img_image, command = lambda: Pdf2Image_Win(main, col_theme))
main_body_Pdf2Img_button.grid(column = 0, row = 0, pady = (10, 5))
main_body_Pdf2Img_Label = Label(main_body_LabelFrame_pdfNimg, text = "PDF ➡ Image", font = ("Arial", 15), background = BG_COL["body"], foreground = TXT_COL["body"])
main_body_Pdf2Img_Label.grid(column = 0, row = 1, pady = (0, 10))

img2pdf_image = PhotoImage(file = "images\\img2pdf.png")
main_body_Img2Pdf_button = Button(main_body_LabelFrame_pdfNimg, image = img2pdf_image, command = lambda: Image2Pdf_Win(main, col_theme))
main_body_Img2Pdf_button.grid(column = 1, row = 0, pady = (10, 5))
main_body_Img2Pdf_Label = Label(main_body_LabelFrame_pdfNimg, text = "Image ➡ PDF", font = ("Arial", 15), background = BG_COL["body"], foreground = TXT_COL["body"])
main_body_Img2Pdf_Label.grid(column = 1, row = 1, pady = (0, 10))

main.mainloop()