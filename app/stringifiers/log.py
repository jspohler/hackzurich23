
def extract_data(file_path):
    content = ''
    # Extract data from all log files in the specified folder
    with open(file_path, 'r', encoding='ISO-8859-1') as log_file_content:
        content = log_file_content.read()
    return content