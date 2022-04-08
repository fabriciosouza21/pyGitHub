import re
from pycontractions import Contractions
cont = Contractions(api_key="glove-twitter-25")
class Decompress_contractions():
    def clean(self,text):
        cont.load_models()
        text_filtering = list(cont.expand_texts([text]))
        text_filtering = text_filtering[0]
        return text_filtering
