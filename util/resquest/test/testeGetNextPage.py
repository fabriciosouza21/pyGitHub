import unittest 
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from GitApiHearderResponse import GitApiHearderResponse

class TestProximaPagina(unittest.TestCase):
    def test_deve_retornar_link_proxima_pagina(self):
        header = {}
        header["link"] = '<https://api.github.com/repositories/6296790/issues?state=all&per_page=100&page=2>; rel="next", <https://api.github.com/repositories/6296790/issues?state=all&per_page=100&page=295>; rel="last"'
        header["X-RateLimit-Remaining"] = "60"
        response = GitApiHearderResponse(header)
        result = response.proxima_pagina
        expected = "https://api.github.com/repositories/6296790/issues?state=all&per_page=100&page=2"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()