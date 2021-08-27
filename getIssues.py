from util.Remove_single_crase import Remove_single_crase
from util.Remove_url import Remove_url
from util.Remove_three_crase import Remove_three_crase
from util.Process_text import Process_text
from github import Github
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
remove_single_crase = Remove_single_crase()
process_text.add_cleaner(remove_three_crase)
process_text.add_cleaner(remove_url)
process_text.add_cleaner(remove_single_crase)
for issue in issues:
    if i>2:
        break
    custom_issue = Issues(issue.number,issue.user.name,issue.title,process_text.run_cleaner(issue.body) ) 
    comments = issue.get_comments()
    for comment in comments:
        custom_comment = Comment(comment.id,comment.user.name,process_text.run_cleaner(comment.body))
        custom_issue.add_comment(custom_comment)
  
    issues_all.append(custom_issue)
    i+=1


x = ["--->"+issue.title + "\n" + issue.body for issue in issues_all]
with open('issues.txt', 'w',encoding='utf-8') as arquivo:
    arquivo.writelines("\n---> nova linha\n".join(x))

print(remove_single_crase.clean(issues_all[0].body))

print(issues_all[0], "   ", issues_all[1])

