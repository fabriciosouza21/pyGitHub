from util.getArquivosDirectory import get_arquivo_directory
from util.readJson import readJson
from entities.textFrenquence import TextFrequence
class TextAnaliserFrequence:
	def __init__(self, arquivo_analisado:str, arquivos_ignorados) -> None:
		self.arquivo = arquivo_analisado
		self.arquivos_ignorados = arquivos_ignorados
		self.repeticoes = []

	def get_conteudo_arquivo(self)-> dict:
		return readJson(self.arquivo, "database/importacao-db")

	def get_arquivos_all(self):
		arquivos = get_arquivo_directory("database/importacao-db")
		arquivo_info = self.arquivo.split("_")

		# Filtra os arquivos que tem o mesmo projeto ou o mesmo nome
		arquivos_filtrados = list(filter(lambda x: (x.split("_")[0] == arquivo_info[0]) and (x.split("_")[1] == arquivo_info[1]) , arquivos))

		# Remove os arquivos que estão na lista de arquivos ignorados
		for arquivo_ignorado in self.arquivos_ignorados:
			if(arquivo_ignorado in arquivos_filtrados):
				arquivos_filtrados.remove(arquivo_ignorado)

		# Remove o arquivo que está sendo analisado
		arquivos_filtrados.remove(self.arquivo)
		return arquivos_filtrados

	def execute(self) -> list:
		usuario = self.arquivo.split("_")[1]
		if(usuario == "flutter_github-actions[bot]"):
			return []
		arquivo_analisado_conteudo = self.get_conteudo_arquivo()
		if(arquivo_analisado_conteudo):
			text = arquivo_analisado_conteudo.get("analyzed_text")
			arquivos = self.get_arquivos_all()
			if(text == None or not arquivos):
				raise AttributeError("TextAnaliserFrequence: execute: arquivo is None")

			text_frequence = TextFrequence(text, 7)

			while(text_frequence.next_offset() != -1):
				self.get_repeticoes(arquivos, text_frequence)
				if(len(self.repeticoes)):
					break
			return self.repeticoes

		else:
			raise AttributeError("TextAnaliserFrequence: execute: conteudo is None")

	def get_repeticoes(self, arquivos:list, text_frequence:TextFrequence):
		for arquivo in arquivos:
			self.executa_verificacao_arquivo(arquivo, text_frequence)


	def executa_verificacao_arquivo(self,arquivo:str, text_frequence:TextFrequence):
		arquivo_conteudo = readJson(arquivo, "database/importacao-db")
		if(arquivo_conteudo):
			text_analisado = arquivo_conteudo.get("analyzed_text")
			if(text_analisado):
				if(text_frequence.compare_text_fragment(text_analisado)):
					arquivo_texto = {}
					arquivo_texto[arquivo] = text_analisado
					arquivo_texto["frequency"] = text_frequence.get_text_current()
					if arquivo_texto not in self.repeticoes:
						self.repeticoes.append(arquivo_texto)
			else:
				raise AttributeError("TextAnaliserFrequence: execute: conteudo all is None")
		else:
			raise AttributeError("TextAnaliserFrequence: execute: arquivo all is None")
