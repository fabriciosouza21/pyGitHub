import re

class Remove_non_ascii():
    def clean(self,text):
        return re.sub(r'[^\x00-\x7F]+','', text)
