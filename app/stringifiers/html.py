import re
import sys
sys.path.append("..") 
from util import open_file_with_encodings

def extract_data(file_path):
    content = ''
    try:
        content, encoding = open_file_with_encodings(file_path)
        content = re.sub(r'<[^>]+>', '', content)
        content = re.sub(r'\n\s*\n', '\n', content)
        return content
    except Exception as e:
        print(f"An error occurred: {str(e)}")