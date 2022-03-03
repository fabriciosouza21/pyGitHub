from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer

class Lemmatization:
    def clean(self, text):
        """
        This function takes as input a text on which several 
        NLTK algorithms will be applied in order to preprocess it
        """
        tokens = word_tokenize(text)
        # Lower the text
        text = text.lower()
        # Remove the punctuations
        tokens = [word for word in tokens if word.isalpha()]
        # Lower the tokens
        tokens = [word.lower() for word in tokens]
        # Remove stopword
        tokens = [word for word in tokens if not word in stopwords.words("english")]
        # Lemmatize and replace
        lemma = WordNetLemmatizer()
        for word in tokens:
            text = text.replace(word, lemma.lemmatize(word, pos = "n"))
            print(text)
            text = text.replace(word, lemma.lemmatize(word, pos = "v"))
            print(text)
        return text
