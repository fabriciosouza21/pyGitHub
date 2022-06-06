import string
from Dao.Repository import Repository
from datetime import datetime

class GetIssuesByPeriodo:
    def __init__(self,inicio,periodo):   
        self.periodo = periodo
        self.inicio = inicio
        self.inicio_date 
        self.periodo_anterior_date
        self.periodo_date
        self.get_periodo_anterior()
        self.repository = Repository()

    def get_issues_by_periodo(self):
        issues = self.repository.get_repository(self.repositorio)
        issues_by_periodo = []
        for issue in issues:
            created_at_date = datetime.fromisoformat(issue["created_at"].replace("Z",""))
            if self.periodo_anterior_date <= created_at_date and created_at_date <= self.periodo_date:
                issues_by_periodo.append(issue)
        return issues_by_periodo
    
    def get_periodo_anterior(self)-> datetime:
        self.inicio_date = datetime.fromisoformat(self.inicio)
        self.periodo_date = datetime.fromisoformat(self.periodo)
        self.periodo_anterior_date = self.inicio_date - self.periodo_date
      