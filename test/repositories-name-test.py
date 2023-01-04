import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.getRepositoriesName import get_repositories_name, get_directories

class test_repositories_name(unittest.TestCase):

    def test_repositories_name_test(self):
        repositories_expect = ["bootstrap", "deno", "vite"]
        repositories = get_repositories_name("test/issues-test")
        repositories.sort()
        self.assertEqual(3,len(repositories))
        self.assertEqual(repositories_expect,repositories)
    
    def test_repositories_watson_test(self):
        expected = ['4chan-x', 'ableplayer', 'aah']
        diretorio = get_directories("test/result-watson-test")
        directories = diretorio[0]["subdirectories"]
        self.assertEqual(3,len(directories))
        self.assertEqual(expected,directories)

    

if __name__ == '__main__':
    unittest.main()