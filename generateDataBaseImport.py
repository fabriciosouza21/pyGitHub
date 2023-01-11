from util.getRepositoriesName import get_directories
from util.ImportacaoSql import importacao_sql
from util.getArquivosDirectory import get_arquivo_directory
from util.writeDictToJson import writeDictToJson

def sql_import_json():
    path = "resultWatson/comments-toxico/"
    path_destino = "database/importacao-db/" 
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
                writeDictToJson(issue, f"{info['repository']}_{info['user']}_{info['issue']}_{qtd_comentarios}", path_destino)
                qtd_comentarios += 1

if __name__ == '__main__':
    sql_import_json()