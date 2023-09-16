import os
import glob

def extract_data(file_path):
    content = ''
    with open(file_path, 'r', encoding='ISO-8859-1') as ps1_file_content:
         content = ps1_file_content.read()
    return content