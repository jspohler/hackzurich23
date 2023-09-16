import fitz
import io
from PIL import Image
from pytesseract import pytesseract

def extract_data(file_path):
    pdf_file = fitz.open(file_path)
    pdf_text = ""
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        pdf_text += page.get_text()
        image_list = page.get_images()
        # printing number of images found in this page
        if image_list:
            print('images_found: ' + str(len(image_list)))
            for image in image_list:
                base_image = pdf_file.extract_image(image[0])
                image_bytes = base_image["image"]
                # Get the image extension
                image_ext = base_image["ext"]
                # dict_keys(['ext', 'smask', 'width', 'height', 'colorspace', 'bpc', 'xres', 'yres', 'cs-name', 'image'])
                # Load it to PIL
                image = Image.open(io.BytesIO(image_bytes))
                pytesseract.tesseract_cmd = 'tesseract'
                img_text = pytesseract.image_to_string(image)
                if img_text != "":
                    pdf_text += img_text
    return pdf_text
