
class IssueRepositoryUtils:
    def __init__(self, link:str):
        self.link = link
        self.repo_name = ""
        self.__remover_prefixo()
        self.__get_repo_name()
       
    def __remover_prefixo(self):
        self.link = self.link.removeprefix("https://github.com/")

    def get_owner(self)->str:
        split_link = self.link.split("/")
        return split_link[0]
    
    def __get_repo_name(self)->str:
        split_link = self.link.split("/")
        self.repo_name = split_link[1]
    
    def get_issue_number(self)->str:
        split_link = self.link.split("/")
        return split_link[3]