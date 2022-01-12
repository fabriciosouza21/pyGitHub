
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from util.textComments import textComments
from util.writeDictToJson import writeDictToJson
from util.Remove_single_crase import Remove_single_crase
from util.Remove_three_crase import Remove_three_crase
from util.Process_text import Process_text
import os
def authenticator():
    apiKey = os.environ["API_KEY"]
    url = os.environ["URL"]
    authenticator = IAMAuthenticator(apikey=apiKey)
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )
    tone_analyzer.set_service_url(service_url=url)
    return tone_analyzer

def requestIbmWatsonTone():
    tone_analyzer = authenticator()
    process = Process_text() 
    remove_three_crase = Remove_three_crase()
    remove_single_crase = Remove_single_crase()
    process.add_cleaner(remove_three_crase)
    process.add_cleaner(remove_single_crase)

    filters = {"1": Process_text()}

    text = textComments(arquivo="spring-boot-10907")
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    writeDictToJson(tone_analysis,fileName="spring-boot-10907-ibmWatson")

if __name__ == '__main__':
    requestIbmWatsonTone()

