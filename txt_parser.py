import markdown
import re
from bs4 import BeautifulSoup
import os 

def remove_urls(text):
    # This regular expression pattern matches most URLs but avoids email addresses
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    # Remove URLs
    text = url_pattern.sub('', text)
    
    return text

def extract_data_from_md(md_file, output_folder):
    
    with open(md_file, 'r', encoding='ISO-8859-1') as f:
        text = f.read()
        text = text.replace("```", "")
        text = remove_urls(text)
        html = markdown.markdown(text)
        # extract text
        soup = BeautifulSoup(html, "lxml")
        text = ''.join(soup.findAll(text=True))

        
        file_name = os.path.splitext(os.path.basename(md_file))[0]
        txt_file_path = os.path.join(output_folder, f"{file_name}_md.txt")

        with open(txt_file_path, 'w', encoding='utf-8', errors='ignore') as txt_file:
            txt_file.write(text)


output_folder = 'files_for_parser/'
os.makedirs(output_folder, exist_ok=True)
# extract_data_from_md('files/again-tax-environment.md', output_folder)