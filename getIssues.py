import json
from util.Remove_floating_point import Remove_floating_point
from util.Remove_single_crase import Remove_single_crase
from util.Remove_url import Remove_url
from util.Remove_three_crase import Remove_three_crase
from util.Process_text import Process_text
from github import Github
from Comment import Comment
from LOCAL_VARIABLE import token
from VARIABLE_PAGE import current_page


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
remove_fluating_point = Remove_floating_point
process_text.add_cleaner(remove_three_crase)
process_text.add_cleaner(remove_url)
process_text.add_cleaner(remove_single_crase)

last_page = last_page(issues)


for i in range(current_page,last_page+1):
    try:
        pages = issues.get_page(i)
        for issue in pages:
            if issue.body:
                comment = Comment(issue.number, issue.user.name,
                                issue.created_at, issue.body)
                comment.body = process_text.run_cleaner(comment.body)
                all_comments.append(comment)
            comments = issue.get_comments()
            for comment in comments:
                if comment.body:
                    custom_comment = Comment(
                        issue.number, comment.user.name, comment.created_at, comment.body)
                    custom_comment.body = process_text.run_cleaner(custom_comment.body)
                    all_comments.append(custom_comment)
    except:
       with open('VARIABLE_PAGE.py', 'w', encoding='utf8') as f: 
           f.write(f'page = {i}')
           
writeCommentsJson(all_comments)
