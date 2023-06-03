import json
from utils import get_dir


# Escrever função retornando Id-obra para lista drop-down
def listarObras():
    caminho = get_dir()
    with open(caminho+"Clients_Json.json", 'r') as arquivo:
        dados_json = json.load(arquivo)
    arquivo.close()

    lista_obras = []
    for i in range(len(dados_json['results'])):
        lista_obras.append(f"{dados_json['results'][i]['id']} - {dados_json['results'][i]['name']}")
    return lista_obras


# Escrever função que retorna uma linha com todas as requisições do excel em ordem do modelo
def linhaReq2excel(linha, idObra):
    '''
    Função que tem como argumentos linha, idObra e retorna uma linha padrão 
    para o modelo de excel. Retorna o tamanho max do arquivo
    '''
    # Abrir o arquivo JSON e carregar os dados
    # TODO: reportar caso extremo de arquivo faltante
    caminho = get_dir()
    with open(caminho+"idObra_Json_{}.json".format(idObra), 'r') as arquivo:
        dados_json = json.load(arquivo)
    arquivo.close()
    # Identificação dos registros de interesse
    # tamanho
    tam = len(dados_json['results'])

    # Obra 
    obra = dados_json['results'][linha]['description']

    #Id inicial
    idInicial = dados_json['results'][linha]['id']

    # Codigo arvore
    codArv = dados_json['results'][linha]['wbsCode']

    #descricao
    description = dados_json['results'][linha]['description']

    #unidade
    unity = dados_json['results'][linha]['unitOfMeasure']

    #quantidade
    quantity = dados_json['results'][linha]['quantity']

    # mao de obra
    try:
        labor_unit = dados_json['results'][linha]['pricesByCategory'][0]['unitPrice']
    except:
        labor_unit = None

    #materiais
    try:
        material_unit = dados_json['results'][linha]['pricesByCategory'][1]['unitPrice']
    except:
        material_unit = None

    # unitario 
    unity_price = dados_json['results'][linha]['unitPrice']

    # total
    total = dados_json['results'][linha]['totalPrice']

    #Unidade Construtiva

    # Código	Descrição	Unidade	Quantidade	Mão de obra 	Materiais	Materiais Importados	Mão de obra Importada	Unitário	Total

    #labels = ['wbsCode', 'description', 'unitOfMeasure', 'quantity', str("['pricesByCategory'][1]['unitPrice']"), str("['pricesByCategory'][0]['unitPrice']"), 'unitPrice', 'totalPrice']
    return ((codArv, description, unity, quantity, material_unit, labor_unit, unity_price, total), tam)

    # Acessar os dados do JSON
    # valor = dados_json['results'][12]['totalPrice']
    # print(valor)

    # for elements in valor:
    #     print(elements['id'])
    #valor_sub = dados_json['chave1']['chave2']
    
    # Iterar sobre uma matriz (lista) de objetos
    # for elemento in dados_json['results']:
    #     # Faça algo com cada elemento
    #     print(elemento)

    # Outras operações com os dados JSON...

    


#res = linhaReq2excel(0, 99)[0]
#print(res)
# print(len(res))









