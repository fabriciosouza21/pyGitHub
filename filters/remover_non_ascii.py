from filters.Remove_non_ascii import Remove_non_ascii
from filters.Process_text import Process_text

def remover_non_ascii() -> Process_text:
    process = Process_text() 
    remove_non_ascii = Remove_non_ascii()
    process.add_cleaner(remove_non_ascii)
    return process