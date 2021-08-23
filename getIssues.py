import json
from github import Github
from pprint import pprint
from Issues import Issues
from Comment import Comment

token = "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"
g = Github(token)
repo = g.get_repo("spring-projects/spring-boot")
issues = repo.get_issues(state="open")
issues_all = []
i = 0
for issue in issues:
    custom_issue = Issues(issue.number,issue.user.name,issue.title,issue.body) 
    comments = issue.get_comments()
    for comment in comments:
        custom_comment = Comment(comment.id,comment.user.name,comment.body)
        custom_issue.add_comment(custom_comment)

    issues_all.append(custom_issue)

x = [issue.title + "\n" + issue.body for issue in issues_all]
with open('issues.txt', 'w') as arquivo:
    arquivo.writelines("###\n".join(x))

print(issues_all[0], "   ", issues_all[1])

