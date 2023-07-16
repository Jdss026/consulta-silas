import json
from utils import get_dir


# Escrever função retornando Id-obra para lista drop-down
def listarObras():
    caminho = get_dir()
    with open(caminho+"Clients_Json.json", 'r') as arquivo:
        dados_json = json.load(arquivo)
    arquivo.close()

    lista_obras = []
    for i in range(len(dados_json)):
        lista_obras.append(f"{dados_json[i]['id']} - {dados_json[i]['name']}")
    return lista_obras


# Escrever função que retorna uma linha com todas as requisições do excel em ordem do modelo
def linhaReq2excel(linha, idObra, idUnit):
    '''
    Função que tem como argumentos linha, idObra e retorna uma linha padrão 
    para o modelo de excel. Retorna o tamanho max do arquivo
    '''
    # Abrir o arquivo JSON e carregar os dados
    # TODO: reportar caso extremo de arquivo faltante
    caminho = get_dir()
    with open(caminho+"idObra_Json_{}_uc_{}.json".format(idObra, idUnit), 'r') as arquivo:
        dados_json = json.load(arquivo)
    arquivo.close()
    # Identificação dos registros de interesse
    # tamanho
    tam = len(dados_json)

    # Obra 
    obra = dados_json[linha]['description']

    #Id inicial
    idInicial = dados_json[linha]['id']

    # Codigo arvore
    codArv = dados_json[linha]['wbsCode']

    #descricao
    description = dados_json[linha]['description']

    #unidade
    unity = dados_json[linha]['unitOfMeasure']

    #quantidade
    quantity = dados_json[linha]['quantity']

    # mao de obra

    # Se houver LABOR (mao de obra) o valor unitario de material é unitPrice - Labor
    # Se nao houver LABOR, o valor do material é a unit prices

    try:    
        if len(dados_json[linha]['pricesByCategory']) != 0:
            for i in range(len(dados_json[linha]['pricesByCategory'])):
                if dados_json[linha]['pricesByCategory'][i]['category'] == "LABOR":
                    # Lógica para o caso de haver LABOR nas categorias
                    labor_unit = dados_json[linha]['pricesByCategory'][i]['unitPrice']
                    if dados_json[linha]['unitPrice'] is not None:
                        material_unit = dados_json[linha]['unitPrice'] - labor_unit
                    else:
                        material_unit = None
                    break
                else:
                    # Lógica para o caso de não haver LABOR nas categorias
                    labor_unit = 0.0
                    if dados_json[linha]['unitPrice'] is not None:
                        material_unit = dados_json[linha]['unitPrice']
                    else:
                        material_unit = 0.0
        else:
            labor_unit = 0.0
            material_unit = 0.0    
    except:
        labor_unit = None
        material_unit = None
    #materiais
    # try:
    #     soma = 0
    #     material_unit = dados_json['results'][linha]['pricesByCategory'][1]['unitPrice']
    # except:
    #     material_unit = None

    # unitario 
    # unity_price = dados_json[linha]['unitPrice']
    unity_price = labor_unit+material_unit
    # total    
    try:
        total = (labor_unit+material_unit)*quantity
    except: 
        total = dados_json[linha]['totalPrice']
    # total = dados_json[linha]['totalPrice']
    #Unidade Construtiva

    # Código	Descrição	Unidade	Quantidade	Mão de obra 	Materiais	Materiais Importados	Mão de obra Importada	Unitário	Total

    #labels = ['wbsCode', 'description', 'unitOfMeasure', 'quantity', str("['pricesByCategory'][1]['unitPrice']"), str("['pricesByCategory'][0]['unitPrice']"), 'unitPrice', 'totalPrice']
    # return ((codArv, description, unity, quantity, labor_unit, material_unit, unity_price, total), tam)
    return ((codArv, description, unity, quantity, labor_unit, material_unit, labor_unit+material_unit, (labor_unit+material_unit)*quantity), tam)

def TamReq(idObra, idUnit):
    caminho = get_dir()
    with open(caminho+"idObra_Json_{}_uc_{}.json".format(idObra, idUnit), 'r') as arquivo:
        dados_json = json.load(arquivo)
    arquivo.close()
    # Identificação dos registros de interesse
    # tamanho
    tam = len(dados_json)
    return tam



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

# for i in range(100):
#     print(linhaReq2excel(i, 93,1)[0])

# res = linhaReq2excel(2, 153,1)[0]
# print(res)
# print(len(res))

# Teste para buscar categorias em json

# idObra = 99
# idUnit = 1
# caminho = get_dir()
# with open(caminho+"idObra_Json_{}_uc_{}.json".format(idObra, idUnit), 'r') as arquivo:
#     dados_json = json.load(arquivo)
# arquivo.close()

# linha = 2

# for i in range(len(dados_json['results'][linha]['pricesByCategory'])):
#     print(i)
#     if dados_json['results'][linha]['pricesByCategory'][i]['category'] == "LABOR":
#         # Lógica para o caso de haver LABOR nas categorias
#         labor_unit = dados_json['results'][linha]['pricesByCategory'][i]['unitPrice']
#         if dados_json['results'][linha]['unitPrice'] is not None:
#             material_unit = dados_json['results'][linha]['unitPrice'] - labor_unit
#         else:
#             material_unit = None
#         break
#     else:
#         # Lógica para o caso de não haver LABOR nas categorias
#         labor_unit = 0.0
#         if dados_json['results'][linha]['unitPrice'] is not None:
#             material_unit = dados_json['results'][linha]['unitPrice']
#         else:
#             material_unit = 0.0


# res = dados_json['results'][9]['pricesByCategory'][0]['unitPrice']
# print(res)









