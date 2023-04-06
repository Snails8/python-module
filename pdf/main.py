from PIL import Image
import os
from PyPDF2 import PdfReader, PdfWriter


def compression_png():
    directory = 'data/xxx/'
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as im:
                im.convert('RGBA').save(filepath, format='PNG', optimize=True)
                # im.save(filepath, "PNG", optimize=True)
    
    
    return print('success')

def compression_pdf():
    input_file = 'data/pdf/before.pdf'
    output_file = 'data/result.pdf'
    
    with open(input_file, 'rb') as f:
        pdf = PdfReader(f)
        output_pdf = PdfWriter()

        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            page.compress_content_streams()
            output_pdf.add_page(page)

        with open(output_file, 'wb') as output:
            output_pdf.write(output)

    return print('success')

# compression_pdf()
compression_pdf()