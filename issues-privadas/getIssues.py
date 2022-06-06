from github import Github
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.readJson import readJson
token = os.environ["TOKEN"]
headers = {'Authorization': f'token {token}'}
links = readJson("links", "issues-privadas/issues/")
listLinks = list(links["links"])

