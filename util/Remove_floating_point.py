import re
class Remove_floating_point:
    def clean(self,text):
        return re.sub(r'[\-\+]?[0-9]*(\.[0-9-x]+)+','',text)

