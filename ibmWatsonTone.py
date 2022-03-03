
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from util.textComments import textComments
from util.writeDictToJson import writeDictToJson
from filters.lemmatize import lemmatize
from filters.normalizeRepetitions import normalizeRepetitions
import os
def authenticator():
    apiKey = 'EKw-EqYxrU-Foz30Jo5KvKRv1GOYUFHTRw1g8sp2h-lW'
    url = 'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/143a31fb-2ad1-48a8-8398-0ed711c39d25'
    authenticator = IAMAuthenticator(apikey=apiKey)
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )
    tone_analyzer.set_service_url(service_url=url)
    return tone_analyzer

def requestIbmWatsonTone():
    tone_analyzer = authenticator()
    filters = lemmatize()
    text = textComments(filters, arquivo="spring-boot-10907-ibmWatson")
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    writeDictToJson(tone_analysis,fileName=f"spring-boot-10907-ibmWatson-lemmatization")

if __name__ == '__main__':
    requestIbmWatsonTone()
