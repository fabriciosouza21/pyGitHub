
class GitApiHearderResponse:
    def __init__(self, link: str):
        self.link = link
        self.proximaPagina = ""
        self.lastPagina = ""
        self.limitRestante = ""
        self.processHeaderResponse(link)
        
    def processHeaderResponse(self, link: str)->str:
        links = link.split(",")
        for link in links:
            self.setProximaPagina(link)
            self.setLastPagina(link)

    def setProximaPagina(self,link: str)->str:
        if 'rel="next"' in link:
            self.proximaPagina = self.getUrl(link)
    
    def setLastPagina(self, link):
        if 'rel="last"' in link:
            self.lastPagina = self.getUrl(link)
            
    def getUrl(self,link :str)->str:
        link = link.split(";")[0]
        link = link.replace("<", "")
        link = link.replace(">", "")
        self.link = link
        return link