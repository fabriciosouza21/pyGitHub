import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entities.textAnalizerFrequence import  TextAnaliserFrequence


class text_frequence_test(unittest.TestCase):

	def test_frequence(self):
		text_analiser_frequence = TextAnaliserFrequence("android_github-actions[bot]_3569_44.json")
		repeticoes = text_analiser_frequence.execute()
		self.assertTrue(len(repeticoes) > 0)





if __name__ == '__main__':
    unittest.main()
