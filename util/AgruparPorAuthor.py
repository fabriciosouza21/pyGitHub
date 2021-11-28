
class AgruparPorAuthor :
    def __init__(self,listComentarios:list):
        self.listComentarios = listComentarios
        self.dictAgrupado = {}
        self.agruparPorAuthor()

    
    def agruparPorAuthor(self):
        for comentario in self.listComentarios:
            if comentario["author"] not in self.dictAgrupado:
                self.dictAgrupado[comentario["author"]] = []
            self.dictAgrupado[comentario["author"]].append(comentario) 
                
        return self.dictAgrupado

    def lenAuthor(self,author:str)->int:
        listaAuthor:list = self.dictAgrupado.get(author,[])
        tamanho = len(listaAuthor)
        return tamanho
    
    def qtdAuthors(self)->int:
        qtd = len(self.dictAgrupado)
        return qtd