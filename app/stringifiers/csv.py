
def extract_data(file_path):
    content = ''
    with open(file_path, 'r') as f:
        replaced_lines = map(lambda line: line.replace(',', ' '), f.readlines())
        content = ''.join(replaced_lines)
    return content
