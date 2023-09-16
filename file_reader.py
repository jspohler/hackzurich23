import sqlite3
import os
import glob
import re
from docx import Document

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


def extract_data_from_db(db_file, output_folder):
    # Extract data from a single SQLite database file

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Get the list of table names from the database schema
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [table[0] for table in cursor.fetchall()]

    # Create a data file for the database and its tables
    db_file_name = os.path.splitext(os.path.basename(db_file))[0]
    txt_file_path = os.path.join(output_folder, f"{db_file_name}_db.txt")

    with open(txt_file_path, 'a') as txt_file:
        txt_file.write(f"{db_file_name}\n")

        # Loop through each table and fetch text
        for table_name in table_names:
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            txt_file.write(f"{table_name}\n")
            for row in rows:
                txt_file.write('\t'.join(map(str, row)) + '\n')
    # Close the database connection
    conn.close()

def extract_db_data(folder_path, output_folder):
    # Extract data from all SQLite database files in the specified folder
    os.makedirs(output_folder, exist_ok=True)

    db_files = glob.glob(os.path.join(folder_path, '*.db'))

    for db_file in db_files:
        extract_data_from_db(db_file, output_folder)
    
    
def extract_data_from_docx(docx_file, output_folder):
    # Extract data from a single docx database file
    
    doc = Document(docx_file)
    
    # Create a text file for the .docx file
    txt_file_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(docx_file))[0]}_docx.txt")

    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        for paragraph in doc.paragraphs:
            txt_file.write(paragraph.text + '\n')

def extract_docx_data(folder_path, output_folder):
    # Extract data from all docx files in the specified folder
    
    os.makedirs(output_folder, exist_ok=True)

    docx_files = glob.glob(os.path.join(folder_path, '*.docx'))

    for docx_file in docx_files:
        extract_data_from_docx(docx_file, output_folder)
    

def rename_log_to_txt(log_file, output_folder):
    # Get the base name of the file (without extension)
    base_name = os.path.splitext(os.path.basename(log_file))[0]

    # Rename the .log file to .txt
    txt_file_path = os.path.join(output_folder, f"{base_name}_log.txt")
    with open(log_file, 'r', encoding='utf-8') as log_file:
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(log_file.read())


def extract_log_data(folder_path, output_folder):
    # Extract data from all log files in the specified folder
    
    os.makedirs(output_folder, exist_ok=True)

    log_files = glob.glob(os.path.join(folder_path, '*.log'))

    for log_file in log_files:
        rename_log_to_txt(log_file, output_folder)
    
folder_path = 'files'

def extract_xml_data(folder_path, output_folder):
    try:
        os.makedirs(output_folder, exist_ok=True)

        xml_files = glob.glob(os.path.join(folder_path, '*.xml'))
        for xml_file in xml_files:
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(xml_file))[0]}_xml.txt")
            content, encoding = open_file_with_encodings(xml_file)

            # Remove XML tags and content
            content_no_xml = re.sub(r'<[^>]+>', '', content)

            # Remove consecutive empty lines
            content_cleaned = re.sub(r'\n\s*\n', '\n', content_no_xml)

            with open(output_file_path, 'w', encoding=encoding) as output_file:
                output_file.write(content_cleaned)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def extract_html_data(folder_path, output_folder):
    try:
        os.makedirs(output_folder, exist_ok=True)

        html_files = glob.glob(os.path.join(folder_path, '*.html'))
        for html_file in html_files:
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(xml_file))[0]}_html.txt")
            content, encoding = open_file_with_encodings(html_file)
            content_no_xml = re.sub(r'<[^>]+>', '', content)
            content_cleaned = re.sub(r'\n\s*\n', '\n', content_no_xml)

            with open(output_file_path, 'w', encoding=encoding) as output_file:
                output_file.write(content_cleaned)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

#log
if True:
    output_folder_log =  'texted_from_files/log/'
    extract_log_data(folder_path, output_folder_log)


#docx
if True:
    output_folder_docx = 'texted_from_files/docx/'
    extract_docx_data(folder_path, output_folder_docx)
    
#db
if True:
    output_folder_db = 'texted_from_files/db/'
    extract_db_data(folder_path, output_folder_db)

#xml
if True:
    output_folder_xml = 'texted_from_files/xml/'
    extract_xml_data(folder_path,output_folder_xml)

#html
if True:
    output_folder_html = 'texted_from_files/html/'
    extract_xml_data(folder_path,output_folder_html)