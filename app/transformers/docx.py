from docx import Document

def extract_data(file_path):
    content = ''
    doc = Document(file_path)
    for paragraph in doc.paragraphs:
            content += paragraph.text + '\n'
    return content