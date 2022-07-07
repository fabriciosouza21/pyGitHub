
import json
import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, EmotionOptions, SentimentOptions, CategoriesOptions, ConceptsOptions, SemanticRolesOptions, RelationsOptions, SyntaxOptions, SummarizationOptions, TokenResult, SentenceResult


def authenticator():
    apiKey = os.environ["API_KEY"]
    url = os.environ["URL"]
    authenticator = IAMAuthenticator(apiKey)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2021-03-25',
        authenticator=authenticator)
    natural_language_understanding.set_service_url(url)
    return natural_language_understanding


def request_ibm_watson_natural_language_understanding(text, repo):
    natural_language_understanding = authenticator()
    response = natural_language_understanding.analyze(
        text=text,
        return_analyzed_text=True,
        features=Features(
            emotion=EmotionOptions()              
        )).get_result()
    return response



