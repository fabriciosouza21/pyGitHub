from cgi import test
import re

class NormalizerRepetitions():
    def clean(self,text):
        count = 0
        default = re.compile(r'(.)\1{2,}')        
        checks = default.finditer(text)
        for check in checks:
            start = check.span()[0]
            end = check.span()[1]
            if count == 0:
                text_normalize = text.replace(text[start:end], text[start])
            else:
                text_normalize = text_normalize.replace(text[start:end], text[start])
            count = 1
        return text_normalize
