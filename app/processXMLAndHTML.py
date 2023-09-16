import os
import re

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

def remove_html_xml(file_path, name):
    try:
        # Create a directory named 'cleanXMLAndHTML' if it doesn't exist
        output_directory = 'txtFiles'
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Construct the output file path in the 'cleanXMLAndHTML' directory
        output_file_path = os.path.join(output_directory, name + '_' + file_path.suffix +  '.txt')
        
        content, encoding = open_file_with_encodings(file_path)

            # Remove HTML tags and content
        content_no_html = re.sub(r'<[^>]+>', '', content)

            # Remove XML tags and content
        content_no_xml = re.sub(r'<\?xml[^>]*\?>', '', content_no_html)

            # Remove consecutive empty lines
        content_cleaned = re.sub(r'\n\s*\n', '\n', content_no_xml)

        with open(output_file_path, 'w', encoding=encoding) as output_file:
            output_file.write(content_cleaned)

        print(f"HTML and XML content removed. Cleaned file saved in '{output_file_path}'")
    except FileNotFoundError:
        print(f"File not found: '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

