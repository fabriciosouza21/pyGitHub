import unittest
import os
import shutil
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.getRepositoriesName import get_directories
from util.indentify_arquivo_invalido import identify_arquivo_invalido

class test_arquivos_test(unittest.TestCase):

    def test_arquivo_invalido_tres_file_indentify(self):
        path = "test/result-watson-test/"
        path_destino = "test/result-invalidos" 
        tree_path_projetos = get_directories(path)
        projetos = tree_path_projetos[0]["subdirectories"]

        arquivos_deletar_all = []
        arquivos_deletar_dict = []
        for projeto in projetos:
            path_projeto = path + projeto
            usuarios = get_directories(path_projeto)[0]["subdirectories"]
            for usuario in usuarios:
                path_usuario = path_projeto + "/" + usuario
                arquivos_deletar = identify_arquivo_invalido(path_usuario, projeto)
                if(len(arquivos_deletar) > 0):
                    path_user_dict = {}
                    path_user_dict[path_usuario] = arquivos_deletar
                    arquivos_deletar_all.extend(arquivos_deletar)
                    arquivos_deletar_dict.append(path_user_dict)
        for arquivo in arquivos_deletar_dict:
            key = list(arquivo.keys())[0]
            arquivos = arquivo[key]
            for arquivo_user in arquivos:
                shutil.move(f"{key}/{arquivo_user}" , f"{path_destino}/{arquivo_user}")


if __name__ == '__main__':
    unittest.main()