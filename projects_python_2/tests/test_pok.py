import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '75c5b99e82e40f0cba4094bff14dd4b1'
HEADR = {'Content-Type' : 'application/json','trainer_token':TOKEN}
TRAINER_ID='12434'

def test_status_cod():
    response=requests.get(url=f'{URL}pokemons', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_part_of_respons():
    response_get=requests.get(url=f'{URL}pokemons', params={'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'GoRGa'
    
    
@pytest.mark.parametrize('key,value',[('name','GoRGa'),('trainer_id', TRAINER_ID),('id', '159667')])
def test_parametrize(key, value):
    response_parametrize=requests.get(url=f'{URL}pokemons', params={'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value