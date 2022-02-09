import unittest 
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import proximaPagina

class TestProximaPagina(unittest.TestCase):
    def test_deve_retornar_link_proxima_pagina(self):
        link = '<https://api.github.com/repositories/6296790/issues?state=all&per_page=100&page=2>; rel="next", <https://api.github.com/repositories/6296790/issues?state=all&per_page=100&page=295>; rel="last"'
        result = proximaPagina.proximaPaganina(link)
        expected = "https://api.github.com/repositories/6296790/issues?state=all&per_page=100&page=2"
        self.assertEqual(expected, result)