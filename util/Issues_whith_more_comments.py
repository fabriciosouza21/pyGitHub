
class Issues_whith_more_comments:
    def __init__(self,qtd_issues):
        self.qtd_issues = qtd_issues
    
    def get_issues(self, all_issues):
        largers = []
        for issue in all_issues:
            size_comments = len(issue.comments)
            if (len(largers) < self.qtd_issues):
                largers.append(issue)
            else:
                for larger in largers:
                    if (size_comments > len(larger.comments)):
                        largers.append(issue)
                        largers.remove(larger)                        
                        break
        return largers