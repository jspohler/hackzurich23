
def extract_data(file_path):
    content = ''
    with open(file_path, 'r', encoding='ISO-8859-1') as md_file_instance:
        content = md_file_instance.read()
    return content