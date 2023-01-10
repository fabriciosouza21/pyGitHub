import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.ImportacaoSql import importacao_sql
class importacao_sql_test(unittest.TestCase):
    
    def test_importacao_sql_test(self):
        path = "test/result-watson-test/4chan-x/ghost"
        result = importacao_sql("4chan-x","ghost", "ghost_4chan-x_4chan-x-2500_0.json", path)
        info = result["info"]
        self.assertEqual("4chan-x", info["repository"])
        self.assertEqual("ghost", info["user"])
        self.assertEqual(2500, info["issue"])                    

    
if __name__ == '__main__':
    unittest.main()