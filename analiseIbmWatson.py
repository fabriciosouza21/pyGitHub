from ast import If
from json.tool import main
from analysesResultIbmWatson.analysisResultIbmWatson import analysisResultIbmWatson
from util.readJson import readJson
def analise():
    ibmWatsonAnalise = readJson("spring-boot-10907-ibmWatson-1")
    result = analysisResultIbmWatson(ibmWatsonAnalise)
    return result
if __name__ == '__main__':
    print (analise())