import re

def private_key_regex(text):
    # https://regex101.com/library/Lmuf8c
    pattern = r'\s*(\bBEGIN\b).*(PRIVATE KEY\b)\s*'
    matches = re.findall(pattern, text, re.MULTILINE)
    if matches is not None:
        return 'True'
    return 'False'


