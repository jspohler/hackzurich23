import re
import spacy
from spacy.matcher import Matcher

from entity import Entity

nlp = spacy.load("en_core_web_lg")

# Define a custom pattern for recognizing email addresses
email_pattern = [{"TEXT": {"REGEX": r"[\w\.-]+@[\w\.-]+"}}]

# Define a custom pattern for recognizing phone numbers (example: +1 (123) 456-7890)
# phone_pattern = [{"TEXT": {"REGEX": r"^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{4}$"}}]

# Create a Matcher object and add the email and phone patterns
matcher = Matcher(nlp.vocab)
matcher.add("EMAIL", [email_pattern])

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

def phone_number_regex(text):
    phone_numbers = []
    pattern = r'\+?\d{2,}\s?\(?\d{0,}\)?\s?\d+\s?\d+'
    matches = re.findall(pattern, text, re.MULTILINE)

    for match in matches:
        if len(match) > 8:
            phone_numbers.append(match)
    print(phone_numbers)

    if phone_numbers != []: 
        return True
    return False

def NER(text: str) -> list[str]:
    texts = text.split("\n\n") # common way to split on paragraphs

    full_names = []
    emails = []
    phones = []
    org = []

    result = set()

    for data in nlp.pipe(texts):
        doc = nlp(data)
        # print([t for t in doc])
        matches = matcher(doc)
        # print(matches)

        for match_id, start, end in matches:
            span = doc[start:end]
            if match_id == nlp.vocab.strings["EMAIL"]:
                emails.append(span.text)
                result.add(Entity.EMAIL_ADDRESS)
            # elif match_id == nlp.vocab.strings["PHONE"]:
            #     phones.append(span.text)

        # print("DOC ENTS: ", doc.ents)

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                print(ent.text)
                # Check if the entity contains a space (indicating a full name)
                if " " in ent.text:
                    full_names.append(ent.text)
                    result.add(Entity.PERSON)
            elif ent.label_ == "ORG":
                print(ent.text)
                org.append(ent.text)
                result.add(Entity.ORGANIZATION)
            else:
                pass # print(ent.text, ent.start_char, ent.end_char, ent.label_)
        
        
        # for match_id, start, end in matches:
        #     span = doc[start:end]
        #     print(span.text
    print('---')
    print(full_names)
    print(emails)
    # print(phones)

    return list(result)

def full_name_ner(doc):
    pass