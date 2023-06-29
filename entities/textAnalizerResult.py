
from util.getArquivosDirectory import get_arquivo_directory
from util.readJson import readJson
from entities.textAnalizerFrequence import TextAnaliserFrequence

class TextAnalizerResult:
	def __init__(self):
		self.repeticoes = {}

	def execute(self):
		arquivos = get_arquivo_directory("database/importacao-db")
		while(arquivos):
			arquivo = arquivos.pop()
			arquivo_conteudo = readJson(arquivo, "database/importacao-db")
			if(arquivo_conteudo):
				print("----------> arquivo: ", arquivo)
				print("----------> restam: ", len(arquivos))
				text_analise = TextAnaliserFrequence(arquivo)
				repeticoes = text_analise.execute()
				self.repeticoes[arquivo] = repeticoes
				map(lambda x: arquivos.remove(x), repeticoes)
			else:
				raise AttributeError("TextAnaliserFrequence: execute: arquivo all is None")
