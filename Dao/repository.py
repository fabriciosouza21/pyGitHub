from Dao.conection import Connection


class issuesRepository :
    def __init__(self):
        self.conection = Connection()
    #incopleto
    def getRepository(self):
        return self.conection.collection.find()