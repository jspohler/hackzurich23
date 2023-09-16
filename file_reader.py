import sqlite3
import os
import glob
from docx import Document


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
    # Extract data from a single docx file
    
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
    # Extract data from a single log file
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
    

def copy_md_to_txt(md_file, output_folder):
    # Extract data from a single md file
    base_name = os.path.splitext(os.path.basename(md_file))[0]

    # Create a new .txt file in the output folder and copy the content
    txt_file_path = os.path.join(output_folder, f"{base_name}_md.txt")
    with open(md_file, 'r', encoding='ISO-8859-1') as md_file:
        with open(txt_file_path, 'w', encoding='utf-8', errors='ignore') as txt_file:
            txt_file.write(md_file.read())

def extract_md_data(folder_path, output_folder):
    # Extract data from all md files in the specified folder
    os.makedirs(output_folder, exist_ok=True)
    md_files = glob.glob(os.path.join(folder_path, '*.md'))
    
    for md_file in md_files:
        copy_md_to_txt(md_file, output_folder)


folder_path = 'files'

#md
if True:
    output_folder_md = 'texted_from_files/md/'
    extract_md_data(folder_path, output_folder_md)
    
#log
if True:
    output_folder_log = 'texted_from_files/log/'
    extract_log_data(folder_path, output_folder_log)


#docx
if False:
    output_folder_docx = 'texted_from_files/docx/'
    extract_docx_data(folder_path, output_folder_docx)
    
#db
if False:
    output_folder_db = 'texted_from_files/db/'
    extract_db_data(folder_path, output_folder_db)

