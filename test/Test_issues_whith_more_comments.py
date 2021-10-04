import unittest
from util.Issues_whith_more_comments import Issues_whith_more_comments
from Issues import Issues

class Test_issues_whith_more_comments(unittest.TestCase):

    def test_get_issues(self):
        all_issues = []

        issues1 = Issues(number=1,author="teste 1",title="tilte 1",body="comments 1")
        issues2 = Issues(number=2,author="teste 2",title="tilte 2",body="comments 2")
        issues3 = Issues(number=3,author="teste 3",title="tilte 3",body="comments 3")
        issues4 = Issues(number=4,author="teste 4",title="tilte 4",body="comments 4")
        issues5 = Issues(number=5,author="teste 5",title="tilte 5",body="comments 5")

        issues1.add_comment("1")
        issues2.add_comment("1")
        issues2.add_comment("2")
        issues3.add_comment("1")
        issues3.add_comment("2")
        issues3.add_comment("3")
        issues4.add_comment("1")
        issues4.add_comment("2")
        issues4.add_comment("3")
        issues4.add_comment("4")
        issues5.add_comment("1")
        issues5.add_comment("2")
        issues5.add_comment("3")
        issues5.add_comment("4")
        issues5.add_comment("5")
        all_issues.extend([issues1,issues2,issues3,issues4,issues5])

        more_comments =Issues_whith_more_comments(2)
        issues = more_comments.get_issues(all_issues=all_issues)
        self.assertEqual(issues5.number,issues[1].number)  
        self.assertEqual(issues4.number,issues[0].number)       
        
if __name__ == '__main__':
    unittest.main()