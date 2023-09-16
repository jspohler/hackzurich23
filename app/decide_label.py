import random

def decide_label_from_entities(entities: list[str]) -> str:
    return random.choice(["True", "False", "review"])