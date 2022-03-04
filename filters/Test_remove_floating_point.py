import unittest
from Remove_floating_point import Remove_floating_point

class Test_floating_point_text(unittest.TestCase):

    def test_run_clean(self):
        tex_junk = 'Configuration Processor does not support 4.5.x best.'
        tex_clean = 'Configuration Processor does not support number best.'
        remove = Remove_floating_point()
        self.assertEqual(tex_clean,remove.clean(tex_junk))
    

if __name__ == '__main__':
    unittest.main()