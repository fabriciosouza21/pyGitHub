import csv
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.writeDictToJson import writeDictToJson

arquivo = open('issues-privadas/issues/ToxicityReplicationDataset.csv')

issues = csv.DictReader(arquivo)
links = {"links": []}
for issue in issues:
    if(str(issue["link"]).find("localhost") == -1):
        links["links"].append(issue["link"])

writeDictToJson(links, "links", 'issues-privadas/issues/')
