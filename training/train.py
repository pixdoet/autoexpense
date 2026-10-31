from spacy.lang.en import English
from spacy import load

# from spacy import displacy
import re

import os

nlp = load("en_core_web_sm")


def extract_entities(text):
    # extarct text using spacy
    doc = nlp(text)
    # displacy.serve(docs=doc, style="ent", port=5050)

    entities = []

    for entity in doc.ents:
        entities.append({"value": entity.text, "type": entity.label_, "count": 1})

    ringgitMatch = re.findall(
        r"(?:Total|Amount|MYR|RM|Ringgit Malaysia|Ringgit|Jumlah|Bayar)[\s:]*(\d+\.\d{2})",
        string=text,
        flags=re.IGNORECASE,
    )
    if ringgitMatch:
        entities.append(f"Regex match:{ringgitMatch}")
    return entities


datasetFiles = os.listdir("./dataset/")

for file in datasetFiles:
    with open(f"./dataset/{file}", "r") as f:
        print(" ")
        print(f"Current file: {file}")
        print(extract_entities(text=f.read()))
        print("=====")
        print(f"")
        # print(f.read())
