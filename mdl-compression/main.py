from PIL import Image
import os
from PyPDF2 import PdfReader, PdfWriter


def compression_png():
    directory = 'data/img/'
    for filename in os.listdir(directory):
        # if filename.endswith('.png'):
            filepath = os.path.join(directory, filename)
            print(f'run ${filename}')
            with Image.open(filepath) as im:
                # im.convert('RGBA').save(filepath, format='PNG', optimize=True, quality = 10)
                # https://imagingsolution.net/program/python/pillow/save_jpeg_image_quality/
                im.save(filepath, quality = 10)
    
    
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

compression_png()
# compression_pdf()