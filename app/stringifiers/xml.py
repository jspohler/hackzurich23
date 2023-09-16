import sys, re
sys.path.append("..") 
from util import open_file_with_encodings

def extract_data(file_path):
    content = ''
    try:
        content = open_file_with_encodings(file_path)
            # Remove XML tags and content
        content = re.sub(r'<[^>]+>', '', content)
            # Remove consecutive empty lines
        content = re.sub(r'\n\s*\n', '\n', content)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return content