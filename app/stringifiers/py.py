
def extract_data(file_path):
    content = ''
    try:
        with open(file_path, 'r', encoding='utf-8') as py_file_content:
            content = py_file_content.read()
    except Exception as e:
        print(f"Error transforming Python code from {file_path}: {e}")
    return content