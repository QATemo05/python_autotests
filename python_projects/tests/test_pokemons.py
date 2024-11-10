import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '142f65ec7375b3e6d63eadfecf989a83'
HEADER = {'Content-type' : 'application/json',
          "trainer_token": TOKEN}
TRAINER_ID = '9380'
TRAINER_NAME = "Temo"

def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name', TRAINER_NAME )])
def test_trainer_name(key, value):
    response_parametrize = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value