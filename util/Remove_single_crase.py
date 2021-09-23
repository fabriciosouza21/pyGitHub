import re

class Remove_single_crase():
    def clean(self,text):
        return re.sub(r'\`[^`]*\`', '',text)


"[\-\+]?[0-9]*(\.[0-9]+)?"
"(0|-?[1-9][0-9]*)?"