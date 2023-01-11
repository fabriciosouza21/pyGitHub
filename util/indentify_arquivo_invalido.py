from util.getArquivosDirectory import get_arquivo_directory
def identify_arquivo_invalido(path, project):
    """Identifica o arquivo inválido e retorna o nome do arquivo"""
    arquivos = get_arquivo_directory(path)
    arquivos = sorted(arquivos, key=len)
    """ """
    arquivos_invalidos = []
    if(len(arquivos) > 3):
        for arquivo in arquivos:
            issue_projeto_number = arquivo.split("_")[-2]
            issue_number = issue_projeto_number.split("-")[-1]
            try:
                issue_number = int(issue_number)
            except(ValueError):
                arquivos_invalidos.append(arquivo)
    return arquivos_invalidos

    