from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/")
def read_root():
    '''
    Endpoint de teste
    '''
    return {"Hello World"}

@app.get("/api/restaurante/")
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para retornar os restaurantes e seus cardápios
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_restaurante = []
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        for item in dados_json:
            if item['Company'] == restaurante: 
                dados_restaurante.append({
                'item': item['Item'],
                'price': item['price'],
                'description': item['description']
            })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}

    else:
        print('Erro: 'f'{response.status_code} - {response.text}')    
        

#Exemplo de URL: http://127.0.0.1:8000/api/restaurante/?restaurante=McDonald’s
#python -m uvicorn main:app --reload