import os
import requests
os.system('cls' if os.name == 'nt' else 'clear')


base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data for {name}. Status code: {response.status_code}")


pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].title()}")
    print(f"{pokemon_info['name'].title()} has {pokemon_info['height']} decimetres height and weighs {pokemon_info['weight']} hectograms.")
    for item in pokemon_info['held_items']:
         print(f"Held item: {item['item']['name']}")
    for i, move in enumerate(pokemon_info['moves']):
        if i==0:
            print(f"First move: {move['move']['name']}")
            break
        