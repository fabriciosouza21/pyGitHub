import re

class Remove_three_crase():
    def clean(self,text):
        return re.sub(r'\```[^)]*\```', '',text)


