import json
from util.Remove_url import Remove_url
from util.Remove_three_crase import Remove_three_crase
from util.Process_text import Process_text
from github import Github
from pprint import pprint
from Issues import Issues
from Comment import Comment

token = "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"
g = Github(token)
repo = g.get_repo("spring-projects/spring-boot")
issues = repo.get_issues(state="all")
issues_all = []
i = 0
process_text = Process_text()
remove_three_crase = Remove_three_crase()
remove_url = Remove_url()
process_text.add_cleaner(remove_three_crase)
process_text.add_cleaner(remove_url)
for issue in issues:
    if i>1:
        break
    custom_issue = Issues(issue.number,issue.user.name,issue.title,issue.body) 
    comments = issue.get_comments()
    for comment in comments:
        custom_comment = Comment(comment.id,comment.user.name,comment.body)
        custom_issue.add_comment(custom_comment)
  
    issues_all.append(custom_issue)
    i+=1




x = [issue.title + "\n" + issue.body for issue in issues_all]
with open('issues.txt', 'w',encoding='utf-8') as arquivo:
    arquivo.writelines("\n".join(x))

print(issues_all[0], "   ", issues_all[1])

