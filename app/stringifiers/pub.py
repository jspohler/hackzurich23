
def extract_data(file_path):
    content = ''
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as pub_file_content:
            content = pub_file_content.read()
    except Exception as e:
        print(f"Error extracting from {file_path}: {e}")
    return content