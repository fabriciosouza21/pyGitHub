from Remove_trash import Remove_trash
import re

class Remove_three_quotes(Remove_trash):
    def clean(self,text):
        return re.sub(r'\'''[^)]*\'''', '',text)


