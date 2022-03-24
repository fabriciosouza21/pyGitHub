import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Repository import Repository

class TestRepository(unittest.TestCase):

    def test_deve_retornar_lista_com_repositorio(self):        
        repository = Repository()
        result = repository.get_repository("micronaut-core")
        primeiro_resultado = result[0]
        self.assertEqual(primeiro_resultado["repository"], "micronaut-core", "repositorio não é o mesmo")
if __name__ == '__main__':
    unittest.main()