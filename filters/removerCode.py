from Process_text import Process_text
from Remove_single_crase import Remove_single_crase
from Remove_three_crase import Remove_three_crase

def remover_code()-> Process_text:
    process = Process_text() 
    remove_single_crase = Remove_single_crase()
    remove_three_crase = Remove_three_crase()
    process.add_cleaner(remove_three_crase)
    process.add_cleaner(remove_single_crase)
    return process
