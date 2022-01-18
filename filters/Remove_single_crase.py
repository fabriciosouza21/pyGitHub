import re

class Remove_single_crase():
    def clean(self,text):
        return re.sub(r'\`[^`]*\`', '',text)
    
    def __str__(self) -> str:
        return self.__class__.__name__

"[\-\+]?[0-9]*(\.[0-9]+)?"
"(0|-?[1-9][0-9]*)?"