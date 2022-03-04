import sys
import unittest
from Remove_single_crase import Remove_single_crase
from Remove_floating_point import Remove_floating_point
from Remove_number import Remove_number
from Remove_three_crase import Remove_three_crase
from Remove_url import Remove_url
from Remove_non_ascii import Remove_non_ascii
from Decompress_contractions import Decompress_contractions

class Remover_test(unittest.TestCase):

    def test_remove_three_crase(self):
        tex_junk = 'Configuration Processor does not support```junk``` test'
        tex_clean = 'Configuration Processor does not support test'
        remove = Remove_three_crase()
        self.assertEqual(tex_clean,remove.clean(tex_junk))
    
    def test_remove_url(self):
        tex_junk = 'Configuration Processor does not support https://github.com/spring-projects/spring-boot/pull/27759#discussion_r691636911'
        tex_clean = 'Configuration Processor does not support link'
        remove = Remove_url()
        self.assertEqual(tex_clean,remove.clean(tex_junk))

    def test_remove_single_crase(self):
        tex_junk = 'When assembling a big jar file,`Exception in threa73pringframework.boot.loader).archive.JarFileArch`'
        tex_clean = 'When assembling a big jar file,'
        remove = Remove_single_crase()
        self.assertEqual(tex_clean,remove.clean(tex_junk))

    def test_Remove_floating_point(self):
        tex_junk = "Neither one suggests use of HTML.As of Spring Boot 2.0, we've disabled by default suffix pattern matching."
        tex_clean = "Neither one suggests use of HTML.As of Spring Boot number, we've disabled by default suffix pattern matching."
        remove = Remove_floating_point()
        self.assertEqual(tex_clean,remove.clean(tex_junk))

    def test_Remove_number(self):
        tex_junk = "see 011235"
        tex_clean = "see number"
        remove = Remove_number()
        self.assertEqual(tex_clean,remove.clean(tex_junk))

    def test_Remove_non_ascii(self):
        tex_junk = "àa string withé fuünny charactersß."
        tex_clean = "a string with funny characters."
        remove = Remove_non_ascii()
        self.assertEqual(tex_clean,remove.clean(tex_junk))

    def test_Decompress_Contractions(self):
        tex_junk = ["I'd like to know how I'd done that!"]
        tex_clean = ["I had like to know how I had done that!"]
        remove = Decompress_contractions()
        self.assertEqual(tex_clean,remove.clean(tex_junk))
    
if __name__ == '__main__':
    unittest.main()
