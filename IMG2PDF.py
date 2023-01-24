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