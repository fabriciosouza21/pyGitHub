import shutil
from util.readJson import readJson
from util.IssueRepositoryUtills import IssueRepositoryUtils
from util.getArquivosDirectory import get_arquivo_directory

def removendo_arquivos_dataset_original():
    links = readJson("links", "issues-privadas/issues/")
    list_links = list(links["links"])
    arquivo_originais = []
    destino = "database/result-watson-dataset-original"
    origem = "database/importacao-db"
    for link in list_links:
        issue_uttil = IssueRepositoryUtils(link) 
        arquivos = get_arquivo_directory("database/importacao-db")
        issue_number_original = issue_uttil.get_issue_number()
        issue_user_original = issue_uttil.get_owner()
        issue_projeto_original = issue_uttil.repo_name
        for arquivo in arquivos:
            arquivo_info = arquivo.split("_")
            issue_number = arquivo_info[-2]
            user = arquivo_info[-3]
            projeto = arquivo_info[0:-3]
            if(len(projeto) > 1):
                projeto = "_".join(projeto)
            else:
                projeto = projeto[0]

            if(projeto == issue_projeto_original and user == issue_user_original):
                arquivo_originais.append(arquivo)
    for arquivo in arquivo_originais:
        shutil.move(f"{origem}/{arquivo}" , f"{destino}/{arquivo}")

if __name__ == '__main__':
    removendo_arquivos_dataset_original()
