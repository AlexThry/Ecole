from Class_Database import Database
import requests
from tqdm import tqdm


class WebRequests:
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_pokemons(self):
        return self.response["results"]

    def get_pokemons_infos(self):
        pokemons = self.get_pokemons()
        pokemons_infos = []
        for pokemon in tqdm(pokemons):
            name = pokemon["name"]
            info = requests.get(pokemon["url"]).json()
            pokemon_info = {name: info}
            pokemons_infos.append(pokemon_info)
        return pokemons_infos

    def get_pokemon_attribut(self):
        for


if __name__ == "__main__":
    pokemons = WebRequests("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=9999999")
    print(pokemons.get_pokemons())
    print(pokemons.get_pokemons_infos())
