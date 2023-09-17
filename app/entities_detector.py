from transformers import pipeline
from pathlib import Path
import os

# Get the path of the directory where this script is in
script_dir_path = os.getcwd() 
# Get the path containing the files that we want to label

from transformers import AutoModelForTokenClassification, AutoTokenizer
import os

pretrained_path = os.path.join(script_dir_path, "..", "roberta_ner_personal_info")


tokenizer = AutoTokenizer.from_pretrained(pretrained_path, local_files_only=True)
model = AutoModelForTokenClassification.from_pretrained(pretrained_path, local_files_only=True)

# ner = pipeline("ner", grouped_entities=True)
ner = pipeline(task="ner", model=model, tokenizer=tokenizer)

def detect_pii_entities_in_text_ner(text: str) -> list[str]:
    result = set()
    # print('input text', text)
    entities = ner(text)
    for entity in entities:
        if entity['score'] > 0.5 and len(entity['word']) > 1:
            # print(entity)
            result.add(entity['entity'][2:])

    return list(result)


# from funcs import NER

# def detect_pii_entities_in_text_spacy(text: str) -> list[str]:
#     return NER(text)


def detect_pii_entities_in_text(text: str) -> list[str]:
    ner_entitites = detect_pii_entities_in_text_ner(text)
    spacy_entities =[]# detect_pii_entities_in_text_spacy(text)

    return list(set(ner_entitites  + spacy_entities))
