import string
from Dao.Repository import Repository
from datetime import datetime

class GetIssuesByPeriodo:
    def __init__(self,inicio,periodo, repositorio):   
        self.periodo = periodo
        self.periodo_anterior
        self.get_periodo_anterior(inicio)
        self.repository = Repository()
    def get_issues_by_periodo(self):
        issues = self.repository.get_repository(self.repositorio)
        issues_by_periodo = []
        for issue in issues:
            if self.periodo in issue["created_at"]:
                issues_by_periodo.append(issue)
        return issues_by_periodo
    
    def get_periodo_anterior(self,inicio:string)-> datetime:
        self.periodo_anterior = datetime.fromisoformat(inicio)