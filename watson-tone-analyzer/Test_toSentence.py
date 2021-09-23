
import unittest

from toSentence import toSentence

class TestToString(unittest.TestCase):

    def testTosentence(self):
        comments = "The source jar for  currently includes the standard (not source) jars for  and . This seems a bit pointless as the  files in the nested jars aren't of much use to anyone who cares about the source."
        sentences = ["The source jar for  currently includes the standard (not source) jars for  and .", " This seems a bit pointless as the  files in the nested jars aren't of much use to anyone who cares about the source."]
        self.assertEqual(sentences,toSentence(comments))



if __name__ == '__main__':
    unittest.main()