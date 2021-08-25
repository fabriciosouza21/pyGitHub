from Remove_trash import Remove_trash
import re

class Remove_url(Remove_trash):
    def clean(self,text):
        return re.sub(r"http\S+", '', text)


