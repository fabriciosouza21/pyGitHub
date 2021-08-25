import sys
import unittest

from Remove_three_quotes import Remove_three_quotes

class Remover_test(unittest.TestCase):

    def remove_three_quotes_test(self):
        tex_junk = 'Configuration Processor does not support lombok @Builder.Default annotated values Hi, Spring Boot configuration processor does not set the default values for those that have the lombok `Builder.Default` annotation. Given the following class below, the default value for `foo` is present but not for `bar` in the generated configuration metadata ```lombok.Data @lombok.NoArgsContructor@lombok.AllArgsContructor@ConfigurationProperties class MyProps { String foo = "default value";@lombok.Builder.DefaultString bar = "default value"'
        tex_clean = 'Configuration Processor does not support lombok @Builder.Default annotated values Hi, Spring Boot configuration processor does not set the default values for those that have the lombok `Builder.Default` annotation. Given the following class below, the default value for `foo` is present but not for `bar` in the generated configuration metadata '
        remove = Remove_three_quotes()
        self.assertEqual(tex_clean,remove.clean(tex_junk))

if __name__ == '__main__':
    unittest.main()
