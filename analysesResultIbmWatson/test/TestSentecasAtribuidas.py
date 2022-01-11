import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from sentecasAtribuidas import sentecasAtribuidas

class TestSentecasAtribuidas(unittest.TestCase):

    def testSentecasAtribuidas(self):
        mockResultIbmWatson = {
            "document_tone": {
                "tones": [
                    {
                        "score": 0.771774,
                        "tone_id": "tentative",
                        "tone_name": "Tentative"
                    },
                    {
                        "score": 0.805331,
                        "tone_id": "analytical",
                        "tone_name": "Analytical"
                    }
                ]
            },
            "sentences_tone": [
                {
                    "sentence_id": 0,
                    "text": "`SpringApplication` makes it hard to get hold of the application context before it's refreshed.",
                    "tones": [
                        {
                            "score": 0.561416,
                            "tone_id": "sadness",
                            "tone_name": "Sadness"
                        }
                    ]
                },
                {
                    "sentence_id": 1,
                    "text": "@michael-simons came up with this:",
                    "tones": []
                },
                {
                    "sentence_id": 4,
                    "text": "",
                    "tones": []
                },
                {
                    "sentence_id": 21,
                    "text": "It would be nice if the initialiser wasn't needed and the API provided an easier way to access the context before it's refreshed.Background was (again) creating an example for my book how to use Spring 5 enhancements out of the box with Spring Boot.",
                    "tones": [
                        {
                            "score": 0.699569,
                            "tone_id": "joy",
                            "tone_name": "Joy"
                        },
                        {
                            "score": 0.582267,
                            "tone_id": "analytical",
                            "tone_name": "Analytical"
                        }
                    ]
                },
                {
                    "sentence_id": 22,
                    "text": "I assume that this question will arise, especially with the functional router.>",
                    "tones": [
                        {
                            "score": 0.920855,
                            "tone_id": "analytical",
                            "tone_name": "Analytical"
                        }
                    ]
                },

            ]
        }
        result = sentecasAtribuidas(mockResultIbmWatson)
        sentecasAtribuidasEsperadas = 3
        self.assertEqual(sentecasAtribuidasEsperadas, result)


if __name__ == '__main__':
    unittest.main()
