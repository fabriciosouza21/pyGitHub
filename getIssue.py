from entities.Comment import Comment
from util.writeCommentsJson import writeCommentsJson
from LOCAL_VARIABLE.LOCAL_VARIABLE import token

from github import Github


def InstantiateComments(issue):
    all_comments = []
    comment = Comment(issue.number, issue.user.name,
                      issue.created_at, issue.body)
    all_comments.append(comment)
    comments = issue.get_comments()
    for comment in comments:
        custom_comment = Comment(
            issue.number, comment.user.name, comment.created_at, comment.body)
        all_comments.append(custom_comment)
    return all_comments


def getIssue():
    g = Github(token)
    repo = g.get_repo("spring-projects/spring-boot")
    issue = repo.get_issue(number=10907)
    result = InstantiateComments(issue)
    writeCommentsJson(result,nameFile="issue")

if __name__ == '__main__':
    getIssue()

