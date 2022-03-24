
from Conection import Connection


class Repository : 
    def __init__(self):
        self.conection = Connection()

    def get_repository(self, repository:str) -> list:
        myquery = {"repository": repository}
        return self.conection.collection.find(myquery)