

import unittest

from ToString import toString


class TestToString(unittest.TestCase):

    def testToStringOneTone(self):
        senteceAnalise = {"sentence_id": 1,
                          "text": "Rather than that it should be opt-in",
                          "tones": [{
                              "score": 0.920855,
                              "tone_id": "analytical",
                              "tone_name": "Analytical"
                          }
                          ]
                          }
        senteceCsv = ' Analytical, 0.920855, "Rather than that it should be opt-in"\n'

        self.assertEqual(senteceCsv, toString(senteceAnalise))

    def testToStringManyTone(self):
        senteceAnalise = {"sentence_id": 1,
                          "text": "Rather than that it should be opt-in",
                          "tones": [{
                                  "score": 0.920855,
                                  "tone_id": "analytical",
                                  "tone_name": "Analytical"
                          },
                              {
                              "score": 0.968123,
                                  "tone_id": "tentative",
                                  "tone_name": "Tentative"
                          }
                          ]
                          }
        senteceCsv = ' Analytical Tentative, 0.920855 0.968123, "Rather than that it should be opt-in"\n'

        self.assertEqual(senteceCsv, toString(senteceAnalise))


if __name__ == '__main__':
    unittest.main()
