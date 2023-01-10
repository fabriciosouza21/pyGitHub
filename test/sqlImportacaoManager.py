import unittest
import os
import shutil
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.getRepositoriesName import get_directories
from util.ImportacaoSql import importacao_sql
from util.getArquivosDirectory import get_arquivo_directory
from util.writeDictToJson import writeDictToJson
class test_arquivos_test(unittest.TestCase):

    def test_arquivo_invalido_tres_file_indentify(self):
        path = "test/result-watson-test/"
        path_destino = "test/importacao-db/" 
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
    unittest.main()