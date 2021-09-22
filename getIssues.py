import json
from util.Issues_whith_more_comments import Issues_whith_more_comments
from util.Remove_single_crase import Remove_single_crase
from util.Remove_url import Remove_url
from util.Remove_three_crase import Remove_three_crase
from util.Process_text import Process_text
from github import Github
from Issues import Issues
from Comment import Comment
from LOCAL_VARIABLE import token


def writeCommentsJson(comments):
    commentsjson = {}
    commentslist = []
    for comment in comments:
        commentslist.append(comment.to_dict())
    commentsjson["comments"] = commentslist

    with open('comments.json', 'a', encoding='utf16') as f:
        json.dump(commentsjson, f, ensure_ascii=False,
                  sort_keys=True, indent=2, separators=(',', ':'))


def last_page(issues):
    last_page_index = issues._getLastPageUrl().find("page")
    pages = issues._getLastPageUrl()
    _, last_page = pages[last_page_index:].split("=")
    return int(last_page)

g = Github(token)
repo = g.get_repo("spring-projects/spring-boot")
issues = repo.get_issues(state="all")
all_comments = []
process_text = Process_text()
remove_three_crase = Remove_three_crase()
remove_url = Remove_url()
remove_single_crase = Remove_single_crase()
process_text.add_cleaner(remove_three_crase)
process_text.add_cleaner(remove_url)
process_text.add_cleaner(remove_single_crase)

last_page = last_page(issues)
print(last_page)
pages = issues.get_page(0)
'''
for issue in pages:
    comment = Comment(issue.number, issue.user.name, issue.body)
    comment.body = process_text.run_cleaner(comment.body)
    all_comments.append(comment)
    comments = issue.get_comments()
    for comment in comments:
        comment = Comment(issue.number, comment.user.name,comment.body)
        comment.body = process_text.run_cleaner(comment.body)
        all_comments.append(comment)
   
writeCommentsJson(all_comments)

'''
