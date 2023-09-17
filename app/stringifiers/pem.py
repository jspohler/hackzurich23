import os, glob

def extract_data(file_path):
    content = ''
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as pem_file_content:
            content = pem_file_content.read()
    except Exception as e:
        print(f"Error extracting data from .pem: {file_path}: {e}")
    return content