from src.Class_Database import Database
from src.Class_WebRequests import WebRequests
import requests


def create_database():
    request = requests.get("https://pokeapi.co/api/v2").json()
    database = Database("database.db")
    for key in request.keys():
        print(requests.get(request[key]).json())


if __name__ == "__main__":
    database = Database("database.db")
