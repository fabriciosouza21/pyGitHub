
from util.getArquivosDirectory import get_arquivo_directory
from util.readJson import readJson
from entities.textAnalizerFrequence import TextAnaliserFrequence
from util.writeDictToJson import writeDictToJson
from threading import Thread

class TextAnalizerResult:
	def __init__(self):
		self.repeticoes = {}
		self.arquivos_ignorados = []
		self.arquivos = []

	def execute(self):

		arquivos_dict = readJson("textos_repitidos_controll.json","database/repitidos/")

		arquivos = arquivos_dict.get("arquivos", None)
		if(arquivos == None):
			arquivos = get_arquivo_directory("database/importacao-db")

		arquivos_ignorados_dict = readJson("textos_ignorados_controll.json","database/repitidos/")
		self.arquivos_ignorados = arquivos_ignorados_dict.get("arquivos", [])
		self.arquivos = arquivos

		i = 0
		threadings = []
		while(self.arquivos):
			try:
				arquivo = self.arquivos.pop()
				t = Thread(target=self.executar_arquivo, args=(arquivo, i))
				t.start()
				threadings.append(t)
				i += 1
				if(i % 500 == 0):
					print("-------------->Esperando as threads<------------")
					for t in threadings:
						t.join()
					print("-------------->Salvando arquivos<------------")
					writeDictToJson({"arquivos":self.arquivos_ignorados},"textos_ignorados_controll","database/repitidos/")
					writeDictToJson({"arquivos":self.arquivos},"textos_repitidos_controll","database/repitidos/")
					print("-------------->arquivos salvos<--------------")
					threadings = []
			except Exception as e:
				print("Erro: ", e)
				continue

		return self.repeticoes

	def executar_arquivo(self,arquivo, thread_id):

		try:
			arquivo_conteudo = readJson(arquivo, "database/importacao-db")
			if(arquivo_conteudo):
				text_analise = TextAnaliserFrequence(arquivo, self.arquivos_ignorados)
				repeticoes = text_analise.execute()
				if(len(repeticoes) > 0 ):
					data = {}
					data[arquivo] = repeticoes
					writeDictToJson(data,f"{arquivo}","database/repitidos/")
				for repeticao in repeticoes:
					self.arquivos_ignorados.append(list(repeticao.keys())[0])
					arquivo_repetido_remove = repeticao.keys()
					if(len(arquivo_repetido_remove)==2):
						if(list(arquivo_repetido_remove)[0] in self.arquivos):
							self.arquivos.remove(list(arquivo_repetido_remove)[0])

				if(len(repeticoes) > 0 ):
					self.repeticoes[arquivo] = repeticoes
				print(f"Thread - finalizada {thread_id} - {arquivo} ")
			else:
				raise AttributeError("TextAnaliserFrequence: execute: arquivo all is None")
		except Exception as e:
			print("TextAnalizerResult: execute: ", e)
			print("arquivo: ", arquivo)

