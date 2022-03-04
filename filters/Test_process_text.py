import unittest
from Remove_url import Remove_url
from Process_text import Process_text

from Remove_three_crase import Remove_three_crase

class Test_process_text(unittest.TestCase):

    def test_run_clean(self):
        tex_junk = 'Configuration Processor does not support```junk``` test1 https://github.com/fjakop/spring-boot-configuration-processor-description'
        tex_clean = 'Configuration Processor does not support test1 link'
        process = Process_text()
        remove_three_crase = Remove_three_crase()
        remove_url = Remove_url()
        process.add_cleaner(remove_three_crase)
        process.add_cleaner(remove_url)
        text_cleanly = process.run_cleaner(tex_junk)
        self.assertEqual(tex_clean,text_cleanly)
    

if __name__ == '__main__':
    unittest.main()