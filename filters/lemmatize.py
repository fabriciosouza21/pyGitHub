from concurrent.futures import process
from filters.Process_text import Process_text
from filters.Lemmatization import Lemmatization

def lemmatize() -> Process_text:
    process = Process_text()
    lemmatize = Lemmatization()
    process.add_cleaner(lemmatize)
    return process