import unittest

from topAuthors import topAuthors


class TestTopAuthor(unittest.TestCase):
    def testTopAuthor(self):
        comments = [
             {"author": "Josh Cummings"},
             {"author": "Andy Wilkinson"},
             {"author": "Andy Wilkinson"},
             {"author": "Josh Cummings"},
             {"author": "Stéphane Nicoll"},
             {"author": "Andy Wilkinson"}
            ]
        expectAuthors = ["Andy Wilkinson"]
        authors = topAuthors(comments=comments)
        self.assertListEqual(expectAuthors,authors)

        
    
        
if __name__ == '__main__':
    unittest.main()
