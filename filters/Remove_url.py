import re
class Remove_url():
    def clean(self,text):
        return re.sub(r"http\S+", 'link', text)


