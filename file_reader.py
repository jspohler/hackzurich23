import sqlite3
import os
import glob
from docx import Document
import extract_msg
import fitz 
import olefile


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

def copy_data_from_log(log_file, output_folder):
    #TODO when doing tokenizing it may require changes
    # Extract data from a single log file
    base_name = os.path.splitext(os.path.basename(log_file))[0]

    # Rename the .log file to .txt
    txt_file_path = os.path.join(output_folder, f"{base_name}_log.txt")
    with open(ps1_file, 'r', encoding='ISO-8859-1') as ps1_file:
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(log_file.read())

def extract_log_data(folder_path, output_folder):
    # Extract data from all log files in the specified folder
    os.makedirs(output_folder, exist_ok=True)
    log_files = glob.glob(os.path.join(folder_path, '*.log'))
    
    for log_file in log_files:
        copy_data_from_log(log_file, output_folder)

def copy_data_from_md(md_file, output_folder):
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
        copy_data_from_md(md_file, output_folder)

def extract_data_from_msg(msg_file, output_folder):
    base_name = os.path.splitext(os.path.basename(msg_file))[0]
    txt_file_path = os.path.join(output_folder, f"{base_name}_msg.txt")
    
    try:
        msg = extract_msg.Message(msg_file)
        sender = msg.sender if hasattr(msg, 'sender') else "N/A"
        recipients = msg.to if hasattr(msg, 'to') else "N/A"
        subject = msg.subject if hasattr(msg, 'subject') else "N/A"
        email_text = msg.body if hasattr(msg, 'body') else "N/A"
    except (UnicodeEncodeError, AttributeError, TypeError):
        pass
    
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(f"Sender: {sender}\n")
        txt_file.write(f"Recipients: {recipients}\n")
        txt_file.write(f"Subject: {subject}\n")
        txt_file.write("Email Text:\n")
        txt_file.write(email_text)

def extract_msg_data(folder_path, output_folder):
    # Extract data from all msg files in the specified folder
    os.makedirs(output_folder, exist_ok=True)
    msg_files = glob.glob(os.path.join(folder_path, '*.msg'))
    
    for msg_file in msg_files:
        extract_data_from_msg(msg_file, output_folder)

def copy_data_from_ps1(ps1_file, output_folder):
    # Get the base name of the file (without extension)
    base_name = os.path.splitext(os.path.basename(ps1_file))[0]

    # Create a new .txt file in the output folder and copy the content
    txt_file_path = os.path.join(output_folder, f"{base_name}_ps1.txt")
    with open(ps1_file, 'r', encoding='ISO-8859-1') as ps1_file:
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(ps1_file.read())

def extract_ps1_data(folder_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    ps1_files = glob.glob(os.path.join(folder_path, '*.ps1'))

    for ps1_file in ps1_files:
        copy_data_from_ps1(ps1_file, output_folder)
    


#This code will attempt to extract the text from the files but may not preserve the layout perfectly.

def extract_data_from_pub(pub_file, output_folder):
    txt_file_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(pub_file))[0]}_pub.txt")
    try:
        with open(pub_file, 'r', encoding='utf-8', errors='ignore') as pub_file:
            rsa_key_text = pub_file.read()
        
        # Save the extracted RSA key text to a .txt file
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(rsa_key_text)
        
    except Exception as e:
        print(f"Error extracting RSA key from {pub_file}: {e}")

def extract_pub_data(folder_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pub'):
                pub_file = os.path.join(root, file)
                extract_data_from_pub(pub_file, output_folder)

        
folder_path = 'files'
    
#pub
if True:
    output_folder_pub = 'texted_from_files/pub/'
    extract_pub_data(folder_path, output_folder_pub)
        
#ps1
if False:
    output_folder_ps1 = 'texted_from_files/ps1/'
    extract_ps1_data(folder_path, output_folder_ps1)
    
#msg
if False:
    output_folder_msg = 'texted_from_files/msg/'
    extract_msg_data(folder_path, output_folder_msg)
    
#md
if False:
    output_folder_md = 'texted_from_files/md/'
    extract_md_data(folder_path, output_folder_md)
    
#log
if False:
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

