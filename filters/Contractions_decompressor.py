from filters.Process_text import Process_text
from filters.Decompress_contractions import Decompress_contractions

def decompress_contractions()-> Process_text:
    process = Process_text() 
    dec_contractions = Decompress_contractions()
    process.add_cleaner(dec_contractions)
    return process