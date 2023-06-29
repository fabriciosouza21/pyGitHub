import re

class TextFrequence:
	def __init__(self, text:str, text_break:int):
		self.text = self.atribuir_texto(text)
		self.text_break = text_break
		self.text_current_step = -1

	def atribuir_texto(self, text:str):
		text_explit = text.split(" ")
		return list(filter(lambda x: x != "", text_explit))

	def get_text(self):
		return self.text

	def get_text_break(self):
		return self.text_break

	def get_text_current_offset(self):
		return self.text_current_step

	def get_text_limit(self):
		return self.get_text_current_offset() + self.text_break

	def get_text_current(self):
		if(self.get_text_current_offset() < len(self.text) and self.get_text_limit() < len(self.text)):
			return " ".join(self.text[self.get_text_current_offset():self.get_text_limit()])
		elif(self.get_text_current_offset() <= len(self.text)):
			return " ".join(self.text[self.get_text_current_offset():])
		else:
			raise IndexError("TextFrequence: get_text_current: text_current_step is out of range")


	def next_offset(self):
		if(self.text_current_step+self.text_break < len(self.text) ):
			self.text_current_step += 1
			return self.text_current_step
		else:
			return -1

	def get_offset(self):
		return self.text_current_step

	def compare_text_fragment(self, text):
		padrao = re.compile( re.escape(self.get_text_current()))
		return  padrao.search(text) != None


