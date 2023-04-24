from src.Class_Database import Database
from src.Class_WebRequests import WebRequests


if __name__ == "__main__":
    database = Database("database.db")
    database.add_items(20)
    pokemons = WebRequests("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")
    pokemons_infos = pokemons.get_pokemons_infos()
    abilities = pokemons.get_abilities(pokemons_infos)
    database.add_pokemons(pokemons_infos, abilities)

