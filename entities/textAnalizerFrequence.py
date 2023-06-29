from util.getArquivosDirectory import get_arquivo_directory
from util.readJson import readJson
from entities.textFrenquence import TextFrequence

class TextAnaliserFrequence:
	def __init__(self, arquivo_analisado:str) -> None:
		self.arquivo = arquivo_analisado
		self.repeticoes = set()

	def get_conteudo_arquivo(self)-> dict:
		return readJson(self.arquivo, "database/importacao-db")

	def get_arquivos_all(self):
		return get_arquivo_directory("database/importacao-db")

	def execute(self):
		arquivo_analisado_conteudo = self.get_conteudo_arquivo()
		if(arquivo_analisado_conteudo):
			text = arquivo_analisado_conteudo.get("analyzed_text")
			arquivos = self.get_arquivos_all()
			if(text == None or not arquivos):
				raise AttributeError("TextAnaliserFrequence: execute: arquivo is None")

			text_frequence = TextFrequence(text, 7)

			while(text_frequence.next_offset() != -1):
				print("----------> texto: ", text_frequence.get_text_current())
				self.get_repeticoes(arquivos, text_frequence)
			return self.repeticoes

		else:
			raise AttributeError("TextAnaliserFrequence: execute: conteudo is None")

	def get_repeticoes(self, arquivos:list, text_frequence:TextFrequence):
		for arquivo in arquivos:
			arquivo_conteudo = readJson(arquivo, "database/importacao-db")
			if(arquivo_conteudo):
				text_analisado = arquivo_conteudo.get("analyzed_text")
				if(text_analisado):
					if(text_frequence.compare_text_fragment(text_analisado)):
						self.repeticoes.add(arquivo)
				else:
					raise AttributeError("TextAnaliserFrequence: execute: conteudo all is None")
			else:
				raise AttributeError("TextAnaliserFrequence: execute: arquivo all is None")
