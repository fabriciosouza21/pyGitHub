import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.getArquivosDirectory import get_arquivo_directory

class test_arquivos_test(unittest.TestCase):

    def test_get_arquivos_test(self):
        project = get_arquivo_directory("test/issues-test/deno")
        self.assertEqual(1, len(project))
        self.assertEqual("deno-6794.json",project[0])

if __name__ == '__main__':
    unittest.main()