class Comment:
    def __init__(self, id, author,updated_at, body=""):
        self.id = id
        self.author = author
        self.body = body
        self.updated_at=updated_at

    def to_dict(self):
        convert = {}
        convert["id"] = self.id
        convert["author"] = self.author
        convert["body"] = self.body
        convert["updated_at"]=self.updated_at.strftime("%d %B, %Y")
        return convert

    def __str__(self) -> str:
        return str(self.id) + " " + self.author
