from util.getRepositoriesName import get_directories
from util.ImportacaoSql import importacao_sql
from util.getArquivosDirectory import get_arquivo_directory
from util.writeDictToJson import writeDictToJson
from util.readJson import readJson

def sql_import_json():
    path = "resultWatson/comments-toxico/"
    path_destino = "database/importacao-db/"
    path_projec = "database/projects"
    projetos_owner = readJson("projects", path_projec)
    tree_path_projetos = get_directories(path)
    projetos = tree_path_projetos[0]["subdirectories"]

    for projeto in projetos:
        path_projeto = path + projeto
        usuarios = get_directories(path_projeto)[0]["subdirectories"]
        for usuario in usuarios:
            path_usuario = path_projeto + "/" + usuario
            arquivos = get_arquivo_directory(path_usuario)
            qtd_comentarios = 0
            for arquivo in arquivos:
                issue = importacao_sql(projeto, usuario, arquivo, path_usuario)

                info = issue['info']
                repository = info["repository"]
                owner = projetos_owner.get(repository)
                issue['info']['owner'] = owner
                writeDictToJson(issue, f"{info['repository']}_{info['user']}_{info['issue']}_{qtd_comentarios}", path_destino)
                qtd_comentarios += 1

def sql_import_comments_json():
    path = "resultWatson/comments/"
    path_destino = "database/importacao-original/"
    path_projec = "database/projects"
    projetos_owner = readJson("projects-original.json", path_projec)
    tree_path_projetos = get_directories(path)
    projetos = tree_path_projetos[0]["subdirectories"]

    for projeto in projetos:
        path_projeto = path + projeto
        usuarios = get_directories(path_projeto)[0]["subdirectories"]
        for usuario in usuarios:
            path_usuario = path_projeto + "/" + usuario
            arquivos = get_arquivo_directory(path_usuario)
            qtd_comentarios = 0
            for arquivo in arquivos:
                issue = importacao_sql(projeto, usuario, arquivo, path_usuario)

                info = issue['info']
                repository = info["repository"]
                owner = projetos_owner.get(repository)
                issue['info']['owner'] = owner
                writeDictToJson(issue, f"{info['repository']}_{info['user']}_{info['issue']}_{qtd_comentarios}", path_destino)
                qtd_comentarios += 1

if __name__ == '__main__':
    sql_import_json()
