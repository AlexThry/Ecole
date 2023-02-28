import requests

def add_book(author, title, condition, price):
    data = {"author": author, "title": title, "condition": condition, "price": price}
    requests.post("http://localhost:8000/api/v1/resources/books", data)

if __name__ == "__main__":
    add_book("Tolkien", "LOTR", "new", "3.2")