
# for slug generate 
import re 
import unicodedata


def serialize_document(document:dict)->dict:
    document = document.copy()

    if '_id' in document:
        document['id'] = str(document.pop('_id'))
    return document

def generate_slug(text:str)-> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    text = text.strip("-")

    return text

