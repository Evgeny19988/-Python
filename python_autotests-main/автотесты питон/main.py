import requests


response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/reg',
              json={
                  "trainer_token": "02980d35b2a648928ea2eb17275a4e25",
                   "email": "evgenypopov1998@yandex.ru",
                   "password": "Negjcnm13524"
                   },
              headers={'Content-Type': 'application/json'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/confirm_email',
              json={"trainer_token": "02980d35b2a648928ea2eb17275a4e25"},
              headers={'Content-Type': 'application/json'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
              json={
                   "name": "Мяу",
                   "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
              headers={'Content-Type': 'application/json', 'trainer_token': '02980d35b2a648928ea2eb17275a4e25'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
             json={
                 "pokemon_id": "29783",
                 "name": "Myu",
                 "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                 headers={'Content-Type': 'application/json', 'trainer_token': '02980d35b2a648928ea2eb17275a4e25'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

requests.put(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
             json={"pokemon_id": "29783"},
             headers={'Content-Type': 'application/json', 'trainer_token': '02980d35b2a648928ea2eb17275a4e25'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

response = requests.get(url='https://api.pokemonbattle.me:9104/trainers',
              json={
                  "trainer_token": "02980d35b2a648928ea2eb17275a4e25"
                   },
              headers={'Content-Type': 'application/json'}, timeout=5)
print(response)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

if response.status_code == 200:
    print('Ok!')
else:
    print('Bad!')
    
