class Issues:
    def __init__(self, number,author,title,body):
        self.number = number
        self.author = self.empty(author)
        self.title = self.empty(title)
        self.body = self.empty(body)
        self.comments = []
    
    def add_comment(self,comment):
        self.comments.append(comment)
    
    def empty(self,text):
        if not text:
            return " "
        return text

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
