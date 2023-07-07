import requests

link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=5000&$format=json&$select=Data,Quantidade,Valor,Denominacao,Especie"

requisicao = requests.get(link)
informacoes = requisicao.json()

print(informacoes)
