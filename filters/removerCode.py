import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util import Process_text
from util import Remove_single_crase
from util import Remove_three_crase

def removerCode()-> Process_text:
    process = Process_text() 
    remove_single_crase = Remove_single_crase()
    remove_three_crase = Remove_three_crase()
    process.add_cleaner(remove_three_crase)
    process.add_cleaner(remove_single_crase)
    return process
