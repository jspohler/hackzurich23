"""
This is a simple crawler that you can use as a boilerplate for your own
implementation. The crawler labels `.txt` files that contain the word
"hello" as "true", `.txt` files without "hello" as "false" and every other
item as "review". Try to modify this simple implementation so that it finds
some sensitive data and then expand your crawler from there.

You can change the code however you want, just make sure that following
things are satisfied:

- Grab the files from the directory "../files" relative to this script
- If you use Python packages, add a "requirements.txt" to your submission
- If you need to download larger files, e.g. NLP models, don't add them to
  the `app` folder. Instead, download them when the Docker image is build by
  changing the Docker file.
- Save your labels as a pickled dictionary in the `../results` directory.
  Use the filename as the key and the label as the value for each file.
- Your code cannot the internet during evaluation. Design accordingly.
"""
from typing import List
import os
from pathlib import Path
import pickle

from entities_detector import detect_pii_entities_in_text
from entity import Entity
from decide_label import decide_label_from_entities
from file_reader import extract_str_from_docx
import reader_function

def save_dict_as_pickle(labels, filename):
    with open(filename, "wb") as handle:
        pickle.dump(labels, handle, protocol=pickle.HIGHEST_PROTOCOL)


def classifier(file_path):
    text = reader_function.reader_function(file_path)
    entities = detect_pii_entities_in_text(text)
    label = decide_label_from_entities(entities)
    return label

def main():
    # Get the path of the directory where this script is in
    script_dir_path = Path(os.path.realpath(__file__)).parents[1]
    # Get the path containing the files that we want to label
    file_dir_path = script_dir_path / "files"
    if os.path.exists(file_dir_path):
        # Initialize the label dictionary
        labels = {}
        #file_path = file_dir_path / "baby-thing-follow.docx"
        #labels = classifier(file_path)
        
        # Loop over all items in the file directory
        files = os.listdir(file_dir_path)
        for idx, file_name in enumerate(files):
            file_path = file_dir_path / file_name
            print(f'file {idx}/{len(files)}')
            labels[file_name] = classifier(file_path)

        print('final labels', labels)

        # Save the label dictionary as a Pickle file
        save_dict_as_pickle(labels, script_dir_path / 'results' / 'crawler_labels.pkl')
    else:
        print("Please place the files in the corresponding folder")


if __name__ == "__main__":
    main()
