from Class_WebRequests import WebRequests
import sqlite3
from tqdm import tqdm

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.curs = self.conn.cursor()


    def create_table(self, table_name, columns_names) -> None:
        assert type(table_name) == str, "'table_name' doit être de type 'str'"
        assert type(columns_names) == list, "'columns_names' doit être de type 'list'"
        for i in range(len(columns_names) - 1):
            assert type(columns_names[i]) == str, f"'columns_names[{i}]' doit être de type 'str'"

        columns_names_command = columns_names[0]
        for column_name in columns_names[1:]:
            columns_names_command += f", {column_name}"
        command = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_names_command})"
        print(command)
        self.curs.execute(command)

        self.conn.commit()

    def add_pokemon(self, pokemons_infos):
        for pokemon_info in tqdm(pokemons_infos):


if __name__ == "__main__":
    pokemons = WebRequests("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=9999999")
    table_name = "Pokemon"
    columns_names = pokemons.
    database = Database("database.db")
    database.create_table(table_name, columns_names)


