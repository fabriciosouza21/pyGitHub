import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.getIssuesFromJson import  get_issues_from_json
from util.getArquivosDirectory import get_arquivo_directory
from util.usuarioList import usuario_list

class test_user_list_test(unittest.TestCase):
    def test_users_list_test(self):
        path = "test/issues-test/deno"
        project = get_arquivo_directory(path)
        self.assertEqual(1, len(project))
        self.assertEqual("deno-6794.json",project[0])  
        comments = get_issues_from_json(project[0], path=path)
        users = usuario_list(comments)
        self.assertEqual(15, len(users))

if __name__ == '__main__':
    unittest.main()