import re

def private_key_regex(text):
    # https://regex101.com/library/Lmuf8c
    pattern = r'\s*(\bBEGIN\b).*(PRIVATE KEY\b)\s*'
    matches = re.findall(pattern, text, re.MULTILINE)
    
    if matches != []:
        return 'True'
    return 'False'

def iban_regex(text):
    # https://stackoverflow.com/questions/40615902/detect-iban-in-text
    pattern = r'[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16}'
    matches = re.findall(pattern, text, re.MULTILINE)

    if matches != []:
        # TODO: print(matches) returns like ['', '']
        return 'True'
    return 'False'
