import unittest
import os
import sys
import re
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.getArquivosDirectory import get_arquivo_directory
from entities.textFrenquence import TextFrequence
class test_arquivos_test(unittest.TestCase):

	def setUp(self) -> None:
		self.text_source = "o sol brilha radiante, iluminando tudo ao seu redor e transmitindo"
		self.text_target = "Em um dia ensolarado, com o céu de um azul vibrante e sem nuvens, o sol brilha radiante, iluminando tudo ao seu redor e transmitindo calor e energia para aqueles que o contemplam"
		return super().setUp()

	def test_basic(self):
		text_frequence = TextFrequence(self.text_source, 4)
		text = text_frequence.get_text_current()
		self.assertEqual(text, "o sol brilha radiante,")
		result = text_frequence.compare_text_fragment(self.text_target)
		self.assertEqual(True, result)
		text_frequence.next_offset()
		text = text_frequence.get_text_current()
		self.assertEqual(text, "iluminando tudo ao seu")
		result = text_frequence.compare_text_fragment(self.text_target)
		self.assertEqual(True, result)
		text_frequence.next_offset()
		text = text_frequence.get_text_current()
		self.assertEqual(text, "redor e transmitindo")
		result = text_frequence.compare_text_fragment(self.text_target)
		self.assertEqual(True, result)



	def test_step(self):
		text_frequence = TextFrequence(self.text_source, 4)
		self.assertEqual(text_frequence.get_text_current(), "o sol brilha radiante,")
		text_frequence.next_offset()
		text = text_frequence.get_text_current()
		self.assertEqual(text, "iluminando tudo ao seu")
		text_frequence.next_offset()
		self.assertEqual(text_frequence.get_text_current(), "redor e transmitindo")
		text_frequence.next_offset()

if __name__ == '__main__':
    unittest.main()
