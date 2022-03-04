import re
from pycontractions import Contractions

cont = Contractions(api_key="glove-twitter-25")
class Decompress_contractions():
    def clean(self,text):
        text_filtering = list(cont.expand_texts([text]))
        return text_filtering[0]
