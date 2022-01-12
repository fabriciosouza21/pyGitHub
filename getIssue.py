from entities.Comment import Comment
from util.writeCommentsJson import writeCommentsJson
from github import Github
import os


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
    token = os.environ["TOKEN"]
    g = Github(token)
    commentsTotal = []
    repo = g.get_repo("spring-projects/spring-boot")
    issues = repo.get_issue(10907)
    comments = InstantiateComments(issues)
    writeCommentsJson(comments,"spring-boot-10907")  

if __name__ == '__main__':
    getIssue()

