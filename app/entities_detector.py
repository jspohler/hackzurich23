from transformers import pipeline
from pathlib import Path
import os

# Get the path of the directory where this script is in
script_dir_path = os.getcwd() 
# Get the path containing the files that we want to label

from transformers import AutoModelForTokenClassification, AutoTokenizer
import os

from enum import Enum

Entity = Enum('Entity', ['AGE', 'CARD_CVV', 'COMMUNITY', 'COUNTRY', 'CREDIT_CARD', 'DATE_OF_BIRTH', 'EMAIL_ADDRESS', 'GENDER', 'GREEN_CARD', 'IDEOLOGY', 'MARITAL_STATUS', 'NATIONALITY', 'NUMBER', 'OCCUPATION', 'ORGANIZATION', 'ORIENTATION', 'PERSON', 'PHONE_NUMBER', 'PHYSICAL_LOCATION', 'POLITICAL_PARTY', 'RELIGION', 'SKILL_SET', 'TITLE', 'US_BANK_ACCOUNT', 'US_PASSPORT', 'US_SSN', 'YEAR'])

pretrained_path = os.path.join(script_dir_path, "..", "roberta_ner_personal_info")


tokenizer = AutoTokenizer.from_pretrained(pretrained_path, local_files_only=True)
model = AutoModelForTokenClassification.from_pretrained(pretrained_path, local_files_only=True)

# ner = pipeline("ner", grouped_entities=True)
ner = pipeline(task="ner", model=model, tokenizer=tokenizer)

def detect_pii_entities_in_text_ner(text: str) -> list[str]:
    result = set()
    entities = ner(text)
    for entity in entities:
        if entity['score'] > 0.5 and len(entity['word']) > 1:
            result.add(entity['entity_group'])

    return list(result)

def detect_pii_entities_in_text_spicy(text: str) -> list[str]:
    return []

def detect_pii_entities_in_text_regex(text: str) -> list[str]:
    return []

def detect_pii_entities_in_text(text: str) -> list[str]:
    ner_entitites = detect_pii_entities_in_text_ner(text)
    regex_entities = detect_pii_entities_in_text_regex(text)
    spicy_entities = detect_pii_entities_in_text_spicy

    return list(set(ner_entitites + regex_entities + spicy_entities))
