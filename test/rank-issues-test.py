import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class rank_issues_comments(unittest.TestCase):

    def rank_comments(self):
        filter = removerCode()
        filters = filter.cleaner
        filters.length()
        
        self.assertEqual(2,filters.length())
        self.assertEqual('Remove_single_crase',filters[0].__str__())
        self.assertEqual('Remove_three_crase',filters[1].__str__())

if __name__ == '__main__':
    unittest.main()