import requests
import json
from arq2xls import get_dir
import configparser
import math

# Read credentials from a configuration file
config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('Credentials', 'username')
password = config.get('Credentials', 'password')


def pullEnterprisesList():
    '''
    Implementar lógica para puxar lista de enterprises em um arquivo json unico
    a cada abertura de tela
    '''
    clientes="/enterprises?limit=200"
    r = requests.get('https://api.sienge.com.br/eduardocardoso/public/api/v1'+clientes, auth=(str(username), str(password)))

    if r.status_code == 200:
        s = json.dumps(r.json())
        caminho = get_dir()
        directory= caminho + "Clients_Json.json"

        with open (directory, "w") as f:
            f.write(s)
        f.close()
        return True
        
    else:
        return False

def isRequisitionCompleted(idObra, idUnit):
    # TODO: implementar unidade construtiva para cada IdObra
    # idObras = ["130","148","147","132","99"]

    # empreendimentos="/enterprises"
    # titulosContasPagar="/bills"
    # cliente="/customers"
    # planejamentoObra="/building-projects/"+idObra+"/sheets/1/tasks"
    # pedidoObra="/purchase-orders/"

    orcamento="/building-cost-estimations/"+str(idObra)+"/sheets/"+str(idUnit)+"/items?limit=200"
    r = requests.get('https://api.sienge.com.br/eduardocardoso/public/api/v1'+orcamento, auth=(str(username), str(password)))
    api = r.json() # transforma req em json

    if r.status_code == 200:
        lista_mestre = [] # lista que recolhe todas as paginas do Id requerido
        lista_mestre = api['results'] # recolhe a primeira pagina

        #####################
        num_linhas = api['resultSetMetadata']['count']
        num_paginas = math.ceil(num_linhas/200)

        for _ in range(num_paginas-1):
            prox = str(api['links'][1]['href']) # caminho para link da proxima pagina
            req = requests.get(prox, auth=(str(username), str(password))) # requisição da proxima pagina
            api = req.json()
            results = api['results']
            lista_mestre.extend(results) # recolhe os resultados na lista mestre
        ######################
        s = json.dumps(lista_mestre)
        caminho = get_dir()
        directory= caminho + "idObra_Json_{}_uc_{}.json".format(idObra, idUnit)

        with open (directory, "w") as f:
            f.write(s)
        f.close()
        return True
        
    else:
        return False

#isRequisitionCompleted(93,1)
#pullEnterprisesList()
