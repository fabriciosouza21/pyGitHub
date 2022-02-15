
class GitApiHearderResponse:
    def __init__(self):
        self.link = ""
        self.proxima_pagina = ""
        self.last_pagina = ""
        self.limit_estante = ""
    
    def has_proxima_pagina(self)->bool:
        if (self.has_iniciado()):
            return not self.proxima_pagina == self.last_pagina
        return True
       


    def set_header(self, header):
        self.link = header["link"]
        self.proxima_pagina = ""
        self.last_pagina = ""
        self.limit_estante = header["X-RateLimit-Remaining"]
        self.process_header_response()
        
    def process_header_response(self)->str:
        headers = self.link.split(",")
        for header in headers:
            self.set_proxima_pagina(header)
            self.set_last_pagina(header)

    def set_proxima_pagina(self,link)->str:
        if 'rel="next"' in link:
            self.proxima_pagina = self.get_url(link)
    
    def set_last_pagina(self,link)->str:
        if 'rel="last"' in link:
            self.last_pagina = self.get_url(link)
            
    def get_url(self, link)->str:
        link = link.split(";")[0]
        link = link.replace("<", "")
        link = link.replace(">", "")
        return link
    
    def has_iniciado(self)->bool:
        return self.link != "" and self.proxima_pagina != "" and self.last_pagina != "" and self.limit_estante != ""          
        