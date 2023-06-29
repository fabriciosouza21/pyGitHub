from entities.textAnalizerResult import TextAnalizerResult
from util.writeDictToJson import writeDictToJson

def identificar_repitidos():
	text_analizer_result = TextAnalizerResult()
	result = text_analizer_result.execute()
	writeDictToJson(result,"textos_repitidos","database/repitidos/")

if __name__ == "__main__":
	identificar_repitidos()
