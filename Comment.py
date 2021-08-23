class Comment:
    def __init__(self, id,author,body):
        self.id = id
        self.author = author
        self.body = body
    
    def to_dict(self):
        convert = {}
        convert["id"] = self.id
        convert["author"] = self.author
        convert["body"] = self.body
        return convert         

    def __str__(self) -> str:       
        return str(self.id)+ " " + self.author
