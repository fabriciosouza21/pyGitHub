import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.getRepositoriesName import get_repositories_name

class test_repositories_name(unittest.TestCase):

    def test_repositories_name_test(self):
        repositories_expect = ["angular-cli", "audacity", "bootstrap", "deno", "vite", "vscode"]
        repositories = get_repositories_name("test/issues-test")
        repositories.sort()
        self.assertEqual(6,len(repositories))
        self.assertEqual(repositories_expect,repositories)

if __name__ == '__main__':
    unittest.main()