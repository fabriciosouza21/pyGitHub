import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from emptySentence import emptySentence

class Test_empty_sentence(unittest.TestCase):

    def test_empty_sentence(self):
        
        mockResultIbmWatson = [
        {
      "sentence_id":1,
      "text":"behavior is quite intentional and I don't think it should change for the following reasons:",
      "tones":[
        {
          "score":0.882284,
          "tone_id":"analytical",
          "tone_name":"Analytical"
        }
      ]
    },
    {
      "sentence_id":2,
      "text":"",
      "tones":[]
    },
    {
      "sentence_id":3,
      "text":"",
      "tones":[]
    },
    {
      "sentence_id":4,
      "text":"",
      "tones":[]
    }]
        quantityEmptySentences = emptySentence(mockResultIbmWatson)
        expectedEmptySentences = 3
        self.assertEqual(expectedEmptySentences,quantityEmptySentences)
          

if __name__ == '__main__':
    unittest.main()