import sys
import unittest
from Remove_single_crase import Remove_single_crase

from Remove_three_crase import Remove_three_crase
from Remove_url import Remove_url

class Remover_test(unittest.TestCase):

    def test_remove_three_crase(self):
        tex_junk = 'Configuration Processor does not support```junk``` test'
        tex_clean = 'Configuration Processor does not support test'
        remove = Remove_three_crase()
        self.assertEqual(tex_clean,remove.clean(tex_junk))
    
    def test_remove_url(self):
        tex_junk = 'Configuration Processor does not support https://github.com/spring-projects/spring-boot/pull/27759#discussion_r691636911'
        tex_clean = 'Configuration Processor does not support '
        remove = Remove_url()
        self.assertEqual(tex_clean,remove.clean(tex_junk))

    def test_remove_single_crase(self):
        tex_junk = 'When assembling a big jar file,`Exception in threa73pringframework.boot.loader).archive.JarFileArch`'
        tex_clean = 'When assembling a big jar file,'
        remove = Remove_single_crase()
        self.assertEqual(tex_clean,remove.clean(tex_junk))

if __name__ == '__main__':
    unittest.main()
