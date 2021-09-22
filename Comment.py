class Comment:
    def __init__(self, id, author, body=""):
        self.id = id
        if not body:
            self.body= ""
            self.author = author
        else:
            self.author = author
            self.body = body

    def to_dict(self):
        convert = {}
        convert["id"] = self.id
        convert["author"] = self.author
        convert["body"] = self.body
        return convert

    def __str__(self) -> str:
        return str(self.id) + " " + self.author
