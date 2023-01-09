from util.getArquivosDirectory import get_arquivo_directory
def identify_arquivo_invalido(path, project):
    """Identifica o arquivo inválido e retorna o nome do arquivo"""
    arquivos = get_arquivo_directory(path)
    arquivos = sorted(arquivos, key=len)

    """ """
    if(len(arquivos)>=3):
        if(len(arquivos[0]) + len(project) > len(arquivos[2]) ):
            return []
    else:
        return []     
    
    return arquivos[:2]
    