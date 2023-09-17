import sqlite3
import os

def extract_data(file_path):
    content = ''
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    # Get the list of table names from the database schema
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [table[0] for table in cursor.fetchall()]
    # Create a data file for the database and its tables
    content = os.path.splitext(os.path.basename(file_path))[0] + '\n'
    # Loop through each table and fetch text
    for table_name in table_names:
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        content += f"{table_name}\n"
        for row in rows:
            content += '\t'.join(map(str, row)) + '\n'
    
    # Close the cursor and the database connection outside the loop
    cursor.close()
    conn.close()
    
    return content
