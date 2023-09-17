import pandas as pd

def extract_data(file_path):
    content = ''
    df_dict = pd.read_excel(file_path, sheet_name=None)
    
    # Iterate through each sheet in the dictionary
    for sheet_name, df in df_dict.items():
        content += f"Sheet: {sheet_name}\n"
        content += '\n'.join(df.apply(lambda row: ' '.join(row.astype(str)), axis=1))
    
    return content
