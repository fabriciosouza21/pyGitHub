import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from variaveisTestes import issues
from AgruparPorAuthor import AgruparPorAuthor

class TestAgruparPorAuthor(unittest.TestCase):

    def testDeveAgruparPorAutor(self):        
        mockResultIbmWatson = issues
        sentecasAgrupadas = AgruparPorAuthor(mockResultIbmWatson)
        author = "Andy Wilkinson"
        qtdSentencesAuthor = sentecasAgrupadas.lenAuthor(author)
        expectedQtdSentences = 2
        qtdAuthor = sentecasAgrupadas.qtdAuthors()
        expectedQtdAuthor = 4
        self.assertEqual(expectedQtdSentences,qtdSentencesAuthor, "quantidade de sentenças por authro incorreta")
        self.assertEqual(expectedQtdAuthor, qtdAuthor , "quantidade de autores incorreta")
    
if __name__ == '__main__':
    unittest.main()