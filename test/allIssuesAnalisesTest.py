import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analisesIssuesGitHub import analises_issues_github

class analises_issues_gitHub_test(unittest.TestCase):
    def test_all_analisy(self):
        path = "test/issues-test"
        result = analises_issues_github(path)
        self.assertEqual(3, len(result["projects"]))
        self.assertEqual(53, result["total_comments"])
        self.assertEqual(3, result["total_projects"])
        self.assertEqual(31, result["total_users"])
        self.assertEqual(3, result["total_issues"])
        



if __name__ == '__main__':
    unittest.main()