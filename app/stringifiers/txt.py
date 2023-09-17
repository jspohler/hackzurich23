
def extract_data(file_path):
    content = ''
    try:
        with open(file_path, 'r', encoding='utf-8') as txt_content:
            content = txt_content.read()
    except Exception as e:
        print(f"Error transforming txt from {file_path}: {e}")
    return content