import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from filters.removerCode import remover_code
class rank_issues_comments(unittest.TestCase):

    def test_rank_comments_test(self):
        filter = remover_code()
        filters = filter.cleaner
                
        self.assertEqual(2,len(filters))
        self.assertEqual('Remove_single_crase',filters[1].__class__.__name__)
        self.assertEqual('Remove_three_crase',filters[0].__class__.__name__)

if __name__ == '__main__':
    unittest.main()