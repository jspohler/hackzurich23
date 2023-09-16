import sqlite3
import os
import glob



def extract_data_from_db(db_file, output_folder):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Get the list of table names from the database schema
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [table[0] for table in cursor.fetchall()]

    # Create a text file for the database and its tables
    db_file_name = os.path.splitext(os.path.basename(db_file))[0]
    txt_file_path = os.path.join(output_folder, f"{db_file_name}.txt")

    with open(txt_file_path, 'a') as txt_file:
        txt_file.write(f"{db_file_name}\n")

        # Loop through each table and fetch data
        for table_name in table_names:
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            txt_file.write(f"{table_name}\n")
            for row in rows:
                txt_file.write('\t'.join(map(str, row)) + '\n')

    # Close the database connection
    conn.close()
    
    
folder_path = 'files'
output_folder = 'texted_from_files/db/'
os.makedirs(output_folder, exist_ok=True)

db_files = glob.glob(os.path.join(folder_path, '*.db'))


for db_file in db_files:
    print(f"Extracting data from {db_file}:")
    extract_data_from_db(db_file, output_folder)
