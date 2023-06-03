import os

def get_dir():
    '''
    Função que retorna o caminho atual dependendo do sistema
    '''
    if os.name == "posix":  # Verifica se está no Linux
        caminho = str(os.getcwd())+"/arquivos/"
    elif os.name == "nt":  # Verifica se está no Windows
        caminho = str(os.getcwd())+"\\arquivos\\"
    return caminho

def caminhos_arq(num_idObra):
    '''
    Função para organizar e retornar o nome dos arquivos xlsx
    '''
    if os.name == "posix":  # Verifica se está no Linux
        caminho = str(os.getcwd())+"/arquivos/"
    elif os.name == "nt":  # Verifica se está no Windows
        caminho = str(os.getcwd())+"\\arquivos\\"
    destino = caminho+'SIEGE-ORCAMENTO-ID_'+str(num_idObra)+'.xlsx'
    return destino