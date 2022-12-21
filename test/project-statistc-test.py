import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.projetStatics import projetc_statics
from util.getArquivosDirectory import get_arquivo_directory
class test_repositories_name_test(unittest.TestCase):

    def test_projetc_statics_test(self):

        top_users = [
                {'user': 'jsejcksn', 'qtde_commentaries': 4}, {'user': 'brianleroux', 'qtde_commentaries': 2}, {'user': 'bartlomieju', 'qtde_commentaries': 2}, {'user': 'nayeemrmn', 'qtde_commentaries': 2}, {'user': 'ralyodio', 'qtde_commentaries': 2}, {'user': 'stale[bot]', 'qtde_commentaries': 1}, {'user': 'SinaMobasheri', 'qtde_commentaries': 1}, {'user': 'vovacodes', 'qtde_commentaries': 1}, {'user': 'kitsonk', 'qtde_commentaries': 1}, {'user': '0kku', 'qtde_commentaries': 1}, {'user': 'andreubotella', 'qtde_commentaries': 1}, {'user': 'Alhadis', 'qtde_commentaries': 1}, {'user': 'Pierstoval', 'qtde_commentaries': 1}, {'user': 'JADSN', 'qtde_commentaries': 1}, {'user': 'ry', 'qtde_commentaries': 1} 
        ]
      
               
        issues = get_arquivo_directory("test/issues-test/deno")
        
        path = "test/issues-test/deno"
        
        project = projetc_statics(issues, path=path)
        self.assertEqual(22,project["qtde_commentaries"])
        self.assertEqual(15,project["qtde_users"])
        self.assertEqual(len(top_users),len(project["top_users"]))
        self.assertEqual(top_users[0],project["top_users"][0])
        self.assertEqual(4,project["top_users"][0]["qtde_commentaries"])
if __name__ == '__main__':
    unittest.main()