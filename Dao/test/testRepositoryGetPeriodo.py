import unittest
import os
import sys
from Dao.getIssuesByPeriodo import GetIssuesByPeriodo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Repository import Repository

class TestRepository(unittest.TestCase):

    def test_deve_retornar_lista_com_repositorio_periodo(self):        
        issues_periodo = GetIssuesByPeriodo()
        issues_periodo.inicio = "2022-01-01"
        issues_periodo.periodo = "2021-01-02"
        
if __name__ == '__main__':
    unittest.main()