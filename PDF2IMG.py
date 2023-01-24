from pdf2jpg import pdf2jpg

def converter(images_folder_path, pdf_path):
    pdf2jpg.convert_pdf2jpg(pdf_path, images_folder_path, pages="ALL")

