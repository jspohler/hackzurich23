import ast
import os

def filter_code(code):
    filtered_parts = []

    # Collecting comments and inline comments
    for line in code.split("\n"):
        if "#" in line:
            comment = line.split("#", 1)[1].strip()
            filtered_parts.append(comment)
            line = line.split("#")[0]  # remove the comment part from line

    # Parsing the code into an AST
    try:
        tree = ast.parse(code)
    except SyntaxError:
        print("Couldn't parse the entire source code, proceeding with what's parsable.")
        return filtered_parts

    for node in ast.walk(tree):
        if isinstance(node, ast.Str):  # For string literals
            filtered_parts.append(node.s)
        elif isinstance(node, ast.Num):  # For numbers
            filtered_parts.append(node.n)
        elif isinstance(node, ast.Dict):  # For dictionary literals
            try:
                filtered_parts.append({k.value: v.value for k, v in zip(node.keys, node.values)})
            except:
                print("Dict")
        elif isinstance(node, ast.List):  # For list literals
            try:
                filtered_parts.append([elt.value for elt in node.elts])
            except:
                print("List")
        elif isinstance(node, ast.Tuple):  # For tuple literals
            try:
                filtered_parts.append(tuple(elt.value for elt in node.elts))
            except:
                print("Tuple")
        # Add more conditions here if you need to keep more types of values

    return filtered_parts

# Test the function


def extract_text_from_py(py_file, output_folder):
    
    with open(py_file, "r") as f:
        source_code = f.read()

    # Run the filter
    filtered_parts = filter_code(source_code)
    filtered_text = ' '.join(map(str, filtered_parts))


    os.makedirs(output_folder, exist_ok=True)

    file_name = os.path.splitext(os.path.basename(py_file))[0]
    txt_file_path = os.path.join(output_folder, f"{file_name}_py.txt")

    with open(txt_file_path, 'w', encoding='utf-8', errors='ignore') as txt_file:
        txt_file.write(str(filtered_text))

py_file = 'files/modern-former-seem.py'
output_folder = 'files_for_parser/'
extract_text_from_py(py_file, output_folder)
