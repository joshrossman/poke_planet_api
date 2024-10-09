import requests
import json

def fetch_pokemon_data(pokemon_name):
    web_data=requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    json_data=web_data.text

    poke_data=json.loads(json_data)
    return poke_data

def calculate_average_weight(pokemon_list):
    average_weight=0
    for i in range(len(pokemon_list)):
        poke_weight=fetch_pokemon_data(pokemon_list[i])
        average_weight+=poke_weight["weight"]
    return average_weight/len(pokemon_list)
      
fetch_pokemon_data('pikachu')
pokemon_names = ["pikachu", "bulbasaur", "charmander"]
average_weight=calculate_average_weight(pokemon_names)
print(average_weight)

