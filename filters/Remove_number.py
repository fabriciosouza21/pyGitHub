import re

class Remove_number:
    def clean(self,text):
        return re.sub(r'[\-\+]?[0-9]+','number',text)