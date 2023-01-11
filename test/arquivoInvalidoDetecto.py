import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analisesIssuesGitHub import analises_issues_github
from util.getRepositoriesName import get_directories
from util.indentify_arquivo_invalido import identify_arquivo_invalido

class arquivo_invalido_detector_test(unittest.TestCase):
    def test_arquivo_invalido_indentify(self):
        path = "test/result-watson-test/"
        tree_path_projetos = get_directories(path)
        projetos = tree_path_projetos[0]["subdirectories"]

        
        path_projeto = path + projetos[3]
        usuarios = get_directories(path_projeto)[0]["subdirectories"]
        path_usuario = path_projeto + "/" + usuarios[0]
        arquivos_deletar = identify_arquivo_invalido(path_usuario, projetos[3])
        self.assertEqual(arquivos_deletar, ['vzool_aah_1.json','vzool_aah_2.json'])

    def test_arquivo_invalido_pypi(self):
        path = "test/result-watson-test/"
        tree_path_projetos = get_directories(path)
        projetos = tree_path_projetos[0]["subdirectories"]

        
        path_projeto = path + projetos[0]
        usuarios = get_directories(path_projeto)[0]["subdirectories"]
        path_usuario = path_projeto + "/" + usuarios[0]
        arquivos_deletar = identify_arquivo_invalido(path_usuario, projetos[0])
        self.assertEqual(18, len(arquivos_deletar))
  

    def test_arquivo_invalido_vazio_indentify(self):
        path = "test/result-watson-test/"
        tree_path_projetos = get_directories(path)
        projetos = tree_path_projetos[0]["subdirectories"]

        
        path_projeto = path + projetos[1]
        usuarios = get_directories(path_projeto)[0]["subdirectories"]
        path_usuario = path_projeto + "/" + usuarios[1]
        arquivos_deletar = identify_arquivo_invalido(path_usuario, projetos[0])
        self.assertEqual(arquivos_deletar, [])
        path_usuario = path_projeto + "/" + usuarios[0]
        arquivos_deletar = identify_arquivo_invalido(path_usuario, projetos[1])
        self.assertEqual(arquivos_deletar, [])
         
    def test_arquivo_invalido_tres_file_indentify(self):
        path = "test/result-watson-test/"
        tree_path_projetos = get_directories(path)
        projetos = tree_path_projetos[0]["subdirectories"]

        
        path_projeto = path + projetos[2]
        usuarios = get_directories(path_projeto)[0]["subdirectories"]
        path_usuario = path_projeto + "/" + usuarios[0]
        arquivos_deletar = identify_arquivo_invalido(path_usuario, projetos[2])
        self.assertEqual(arquivos_deletar, ["rscano_ableplayer_1.json", "rscano_ableplayer_2.json"])


    def test_arquivo_invalido_tres_file_indentify(self):
        path = "test/result-watson-test/"
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


        self.assertEquals(20, len(arquivos_deletar_all))

        

if __name__ == '__main__':
    unittest.main()