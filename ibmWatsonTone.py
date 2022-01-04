
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from LOCAL_VARIABLE import url,apiKey
from util.textComments import textCommensts
from util.writeDictToJson import writeDictToJson

def authenticator():
    authenticator = IAMAuthenticator(apikey=apiKey)
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )
    tone_analyzer.set_service_url(service_url=url)
    return tone_analyzer

def requestIbmWatsonTone():
    tone_analyzer = authenticator() 
    text = textCommensts(database = "database/issue")
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    writeDictToJson(tone_analysis,fileName="database/responseIbmWatson")

if __name__ == '__main__':
    requestIbmWatsonTone()

