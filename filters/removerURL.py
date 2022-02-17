from filters.Process_text import Process_text
from filters.Remove_url import Remove_url

def removerURL()-> Process_text:
    process = Process_text() 
    remove_url = Remove_url()
    process.add_cleaner(remove_url)
    return process