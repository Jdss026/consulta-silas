import requests
import json
from arq2xls import get_dir
import datetime

def pullEnterprisesList():
    '''
    Implementar lógica para puxar lista de enterprises em um arquivo json unico
    a cada abertura de tela
    '''
    clientes="/enterprises"
    r = requests.get('https://api.sienge.com.br/eduardocardoso/public/api/v1'+clientes, auth=('eduardocardoso-prevision', '2vmNEPuUuXtYOTRPtUJi1KMXVVcGGXBE'))

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

def isRequisitionCompleted(idObra, idUnit = 1):
    # TODO: implementar unidade construtiva para cada IdObra
    # idObras = ["130","148","147","132","99"]

    # empreendimentos="/enterprises"
    # titulosContasPagar="/bills"
    # cliente="/customers"
    # planejamentoObra="/building-projects/"+idObra+"/sheets/1/tasks"
    # pedidoObra="/purchase-orders/"

    orcamento="/building-cost-estimations/"+str(idObra)+"/sheets/"+str(idUnit)+"/items"
    r = requests.get('https://api.sienge.com.br/eduardocardoso/public/api/v1'+orcamento, auth=('eduardocardoso-prevision', '2vmNEPuUuXtYOTRPtUJi1KMXVVcGGXBE'))

    if r.status_code == 200:
        s = json.dumps(r.json())
        caminho = get_dir()
        directory= caminho + "idObra_Json_{}.json".format(idObra)

        with open (directory, "w") as f:
            f.write(s)
        f.close()
        return True
        
    else:
        return False

#isRequisitionCompleted(155)
#pullEnterprisesList()
