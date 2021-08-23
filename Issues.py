class Issues:
    def __init__(self, number,author,title,body):
        self.number = number
        self.author = author
        self.title = title
        self.body = body
        self.comments = []
    
    def add_comment(self,comment):
        self.comments.append(comment)
    
    def to_dict(self):
        convert = {}
        convert["number"] = self.number
        convert["author"] = self.author
        convert["body"] = self.body
        convert["comments"] = []
        for comment in self.comments:
            convert["comments"].append(comment.to_string())
        return convert         

    def __str__(self) -> str:       
        return str(self.number)+ " " + self.author + " " + self.title
