import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_restaurante = {}
    dados_json = response.json()
    for item in response.json():
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        dados_restaurante[nome_restaurante].append(item)

        dados_restaurante[nome_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })

else:
    print('Erro na requisição')

for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)