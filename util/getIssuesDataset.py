from util.readJson import read_json
from util.getArquivosDirectory import get_arquivo_directory

def get_issues_projec_dataset(project,path="database/issues"):
    issues = []
    arquivos = get_arquivo_directory(f"{path}/{project}")
    for arquivo in arquivos:
        issue = read_json(f"{path}/{project}/{arquivo}")
        issues.append(issue)
    return issues


