
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from sentecasNaoAtribuidas import sentecasNaoAtribuidas

class TestSentecasNaoAtribuidas(unittest.TestCase):

    def testSentecasNaoAtribuidas(self):
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
                    "sentence_id": 5,
                    "text": "```java",
                    "tones": []
                },
                {
                    "sentence_id": 7,
                    "text": "SpringApplication springApplication = new SpringApplication(Application.class);",
                    "tones": []
                },
            ]
        }
        result = sentecasNaoAtribuidas(mockResultIbmWatson)
        sentecasNaoAtribuidasEsperadas = 3
        self.assertEqual(sentecasNaoAtribuidasEsperadas, result)


if __name__ == '__main__':
    unittest.main()
