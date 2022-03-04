from filters.Normalizer_repetetions import NormalizerRepetitions
from filters.Process_text import Process_text

def normalizeRepetitions() -> Process_text:
    process = Process_text()
    normalize = NormalizerRepetitions()
    process.add_cleaner(normalize)
    return process