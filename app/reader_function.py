import os
import file_reader
import stringifiers.csv
import stringifiers.pub
import stringifiers.log
import stringifiers.html
import stringifiers.mp3
import stringifiers.pem
import stringifiers.md
import stringifiers.ps1
import stringifiers.xlsx
import stringifiers.txt
import stringifiers.db
import stringifiers.png
import stringifiers.jpg
import stringifiers.pdf
import stringifiers.docx
import stringifiers.zip
import stringifiers.xml
import stringifiers.msg
import stringifiers.py
file_endings = ['.csv', '.pub', '.log', '.html', '.mp3', '.pem', '.md', '.ps1', '.xlsx', '.txt', '.db', '.png', '.jpg', '.pdf', '.docx', '.zip', '.xml', '.msg', '.py']

function_map = {'.csv': stringifiers.csv.extract_data, '.pub': stringifiers.pub.extract_data, '.log': stringifiers.log.extract_data, '.html': stringifiers.html.extract_data, '.mp3': stringifiers.mp3.extract_data, '.pem': stringifiers.pem.extract_data, '.md': stringifiers.md.extract_data, '.ps1': stringifiers.ps1.extract_data, '.xlsx': stringifiers.xlsx.extract_data, '.txt': stringifiers.txt.extract_data, '.db': stringifiers.db.extract_data, '.png': stringifiers.png.extract_data, '.jpg': stringifiers.jpg.extract_data, '.pdf': stringifiers.pdf.extract_data, '.docx': stringifiers.docx.extract_data, '.zip': stringifiers.zip.extract_data, '.xml': stringifiers.xml.extract_data, '.msg': stringifiers.msg.extract_data, '.py': stringifiers.py.extract_data}

def reader_function(file_path):
    if os.path.exists(file_path):
        if file_path.suffix in file_endings:
            function_to_run = function_map[file_path.suffix]
            return function_to_run(file_path)
        else:
            # If it is not a known file the set the label to "review"
            return ""
    else:
        print("Please place the files in the corresponding folder")
        return ""