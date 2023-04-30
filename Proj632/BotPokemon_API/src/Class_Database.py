from src.Class_WebRequests import WebRequests
import sqlite3
from tqdm import tqdm

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.curs = self.conn.cursor()
        self.create_table("pokemons", ["name"])
        self.create_table("abilities", ["name", "description"])
        self.create_table("items", ["category", "name", "link"])
        self.curs.execute("CREATE TABLE IF NOT EXISTS sprites (id INTEGER PRIMARY KEY AUTOINCREMENT, idPokemon REFERENCES pokemons (id), spriteName VARCHAR(50), url VARCHAR(255))")
        self.curs.execute("CREATE TABLE IF NOT EXISTS abilitiesOfPokemons (idPokemon REFERENCES pokemons (id), idAbility REFERENCES abilities (id), PRIMARY KEY (idPokemon, idAbility))")


    def create_table(self, table_name, columns_names) -> None:
        assert type(table_name) == str, "'table_name' doit être de type 'str'"
        assert type(columns_names) == list, "'columns_names' doit être de type 'list'"
        for i in range(len(columns_names) - 1):
            assert type(columns_names[i]) == str, f"'columns_names[{i}]' doit être de type 'str'"

        columns_names_command = columns_names[0]
        for column_name in columns_names[1:]:
            columns_names_command += f", {column_name}"
        command = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns_names_command})"
        self.curs.execute(command)

        self.conn.commit()

    def add_abilities(self, abilities):
        for key in tqdm(abilities.keys(), desc="Ajout des abilitées", ncols=150):
            if not self.curs.execute(f"SELECT * FROM abilities WHERE name = '{key}'").fetchall():
                self.curs.execute("INSERT INTO abilities ('name', 'description') VALUES (?, ?)", (key, abilities[key]))
                self.conn.commit()

    def add_sprites(self, pokemons_infos):
        for pokemon in pokemons_infos:
            name = pokemon["name"]
            idPokemon = self.curs.execute("SELECT id FROM pokemons WHERE name = ?", (name,)).fetchall()[0][0]
            for key in pokemon["sprites"].keys():
                if isinstance(pokemon["sprites"][key], str):
                    if not self.curs.execute("SELECT * FROM sprites WHERE (idPokemon, spriteName, url) = (?, ?, ?)", (idPokemon, key, pokemon["sprites"][key])).fetchall():
                        self.curs.execute("INSERT INTO sprites (idPokemon, spriteName, url) VALUES (?, ?, ?)", (idPokemon, key, pokemon["sprites"][key]))
                        self.conn.commit()


    def add_pokemons(self, pokemons_infos, abilities):
        self.add_abilities(abilities)
        for pokemon_info in tqdm(pokemons_infos, desc="ajout des pokémons", ncols=150):
            name = pokemon_info["name"]
            if not self.curs.execute(f"SELECT * FROM pokemons WHERE name = '{name}'").fetchall():
                self.curs.execute("INSERT INTO pokemons ('name') VALUES (?)", (name,))
                self.conn.commit()
            idPoke = self.curs.execute("SELECT id FROM pokemons WHERE name = ?", (name,)).fetchall()[0][0]
            for ability in pokemon_info["abilities"]:
                try:
                    idAbil = self.curs.execute("SELECT id FROM abilities WHERE name = ?", (ability["ability"]["name"],)).fetchall()[0][0]
                    if not self.curs.execute("SELECT * FROM abilitiesOfPokemons WHERE (idPokemon, idAbility) = (? ,?)", (idPoke, idAbil)).fetchall():
                        self.curs.execute("INSERT INTO abilitiesOfPokemons (idPokemon, idAbility) VALUES (?, ?)", (idPoke, idAbil))
                        self.conn.commit()
                except IndexError:
                    pass
        self.add_sprites(pokemons_infos)

    def add_items(self, nbPages):
        wb = WebRequests()
        items = wb.get_items(nbPages)
        for key in items.keys():
            for key2 in items[key]:
                self.curs.execute("INSERT INTO items (category, name, link) VALUES (?, ?, ?)", (key, key2, items[key][key2]))
                self.conn.commit()


if __name__ == "__main__":

    pokemons = WebRequests("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")
    table_name = "Pokemon"

    pokemons_infos = pokemons.get_pokemons_infos()

    # columns_names = pokemons.
    database = Database("database.db")
    # database.create_table(table_name, columns_names)
    # abilities = pokemons.get_abilities(pokemons_infos)
    # database.add_abilities(abilities)
    # database.add_pokemons(pokemons_infos, abilities)
    database.add_items()



