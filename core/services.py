import requests


def generate_request(url, params={}):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.ConnectionError as e:
        response = "No hay respuesta"
        return response

def get_postura():
    response = generate_request('https://gestiones.andimar.cl/api/art/getposturas')
    if response:
       return response

def get_chofer():
    response = generate_request('https://gestiones.andimar.cl/api/art/getposturas')
    if response:
       return response

