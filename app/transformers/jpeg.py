from pytesseract import pytesseract
from PIL import Image
import io
import os

def extract_data(file_path):
    content = ''
    pytesseract.tesseract_cmd = 'C:/Users/Anything/Desktop/HackZurich/tesseract/tesseract.exe'

    img = Image.open(file_path)
    content = pytesseract.image_to_string(img)
    return content