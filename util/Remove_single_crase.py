import re

class Remove_single_crase():
    def clean(self,text):
        return re.sub(r'\`[^`]*\`', '',text)