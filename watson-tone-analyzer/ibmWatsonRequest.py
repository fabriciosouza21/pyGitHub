import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from LOCAL_VARIABLES import apiKey,url


def escrever_json(dados):
    with open('issue.json', 'w', encoding='utf16') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ':'))

authenticator = IAMAuthenticator(apikey=apiKey)
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url(service_url=url)


tone_analysis = tone_analyzer.tone(
    {'text': issue_8115},
    content_type='application/json'
).get_result()

escrever_json(tone_analysis)




