
import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '75c5b99e82e40f0cba4094bff14dd4b1'
HEADR = {'Content-Type' : 'application/json','trainer_token':TOKEN}

create_a_pokemon={
    "name": "GoRGa",
    "photo_id": "1000"
} # СОЗДАНИЕ ПОКЕМОНА БОДИ
body_confirmation:{TOKEN}

name_change={
    "pokemon_id": "159472",
    "name": "Fill",
    "photo_id": 200
}#      СМЕНА ИМЕНИ

in_pokeball={
    "pokemon_id": "159472"
}

response_create=requests.post(url=f'{URL}pokemons',headers=HEADR,json=create_a_pokemon)
print(response_create.text,response_create.status_code)
message=response_create.json()['message']
print(message)


response_create=requests.put(url=f'{URL}pokemons',headers=HEADR,json=name_change)
print(response_create.text,response_create.status_code)
message=response_create.json()['message']
print(message)

response_create=requests.post(url=f'{URL}trainers/add_pokeball',headers=HEADR,json=in_pokeball)
print(response_create.text,response_create.status_code)
message=response_create.json()['message']
print(message)




