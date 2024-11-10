import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '142f65ec7375b3e6d63eadfecf989a83'
HEADER = {'Content-type' : 'application/json',
          "trainer_token": TOKEN}

body_create = {
    "name": "Terminator",
    "photo_id": 1
}

response_pokemons = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_pokemons.text)

pokemoon_id = response_pokemons.json()['id']
print(pokemoon_id)

body_pokemons = {
    "pokemon_id": pokemoon_id,
    "name": "bubblegum",
    "photo_id":  -1
}

response_ppokemons = requests.put(url= f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print (response_ppokemons.text)

body_traines ={
    "pokemon_id": pokemoon_id
}
response_trainers = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_traines)
print (response_trainers.text)
