def open_file_with_encodings(file_path):
    encodings_to_try = ['utf-8', 'latin-1', 'utf-16']
    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            return content, encoding  # Return the content if successfully read
        except UnicodeDecodeError:
            pass
    return None  # Return None if all encodings fail
