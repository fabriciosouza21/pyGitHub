import sys
import unittest

from Remove_three_crase import Remove_three_crase

class Remover_test(unittest.TestCase):

    def test_remove_three_quotes(self):
        tex_junk = 'Configuration Processor does not support```junk``` test'
        tex_clean = 'Configuration Processor does not support test'
        remove = Remove_three_crase()
        print(remove.clean(tex_junk))
        self.assertEqual(tex_clean,remove.clean(tex_junk))

if __name__ == '__main__':
    unittest.main()
