from filters.Process_text import Process_text
from filters.Remove_number import Remove_number
from filters.Remove_floating_point import Remove_floating_point
from filters.Remove_url import Remove_url

def Replace_abslinks_and_numbers() -> Process_text:
    process = Process_text() 
    remove_number = Remove_number()
    remove_floating_point = Remove_floating_point()
    remove_url = Remove_url()
    process.add_cleaner(remove_number)
    process.add_cleaner(remove_floating_point)
    process.add_cleaner(remove_url)
    return process
