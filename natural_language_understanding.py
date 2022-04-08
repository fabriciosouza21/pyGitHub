
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from filters.textTestes.text_issue import text
from util.writeDictToJson import writeDictToJson
def authenticator():
    apiKey = 's64nMgYUz9CPXTU9Icz5gc3pGd-Xs8RtB09-qpkcBisp'
    url = 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/fe11b374-6b44-4a27-b12a-2672741bedb5'
    authenticator = IAMAuthenticator(apiKey)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator)
    natural_language_understanding.set_service_url(url)
    return natural_language_understanding

def request_ibm_watson_natural_language_understanding():
    natural_language_understanding = authenticator()
    response = natural_language_understanding.analyze(
    text=text,
    return_analyzed_text=True,
    features=Features(
        keywords=KeywordsOptions(emotion=True, sentiment=True)
        )).get_result()
    writeDictToJson(response)

if __name__ == '__main__':
    request_ibm_watson_natural_language_understanding()