
class GitApiHearderResponse:
    def __init__(self):
        self.link = ""
        self.proxima_pagina = ""
        self.limit_estante = ""
    

    def set_header(self, header):
        self.link = header["link"]
        self.proxima_pagina = ""
        self.limit_estante = int(header["X-RateLimit-Remaining"])
        self.process_header_response()
        
    def process_header_response(self)->str:
        headers = self.link.split(",")
        for header in headers:
            self.set_proxima_pagina(header)

    def set_proxima_pagina(self,link)->str:
        if 'rel="next"' in link:
            self.proxima_pagina = self.get_url(link)
    
            
    def get_url(self, link:str)->str:
        link = link.split(";")[0]
        link = link.replace("<", "")
        link = link.replace(">", "")
        return link.strip()
    
