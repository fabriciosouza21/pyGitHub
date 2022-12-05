import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.projetStatics import projetc_statics

class test_repositories_name_test(unittest.TestCase):

    def test_projetc_statics_test(self):
        project_expect = {
            "projeto": "deno",
            "qtde_commentaries": 21,
            "qtde_users": 15        
        }
        project = projetc_statics("/test/issues-test")
        self.assertEqual(project_expect,project)

if __name__ == '__main__':
    unittest.main()