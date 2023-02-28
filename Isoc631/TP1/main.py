import hug
import requests


def create_dic():
    with open("bookstore_inventory.csv", "r") as f:
        data = f.read()
    data = data.split("\n")[5:]
    books = []
    for i in data:
        try:
            book = {}
            book_info = i.split(",")
            book["stock_number"] = int(book_info[0])
            book["author"] = book_info[1]
            book["title"] = book_info[2]
            book["condition"] = book_info[3]
            book["price"] = book_info[4]
            books.append(book)
        except:
            pass
    return books


@hug.get('/api/v1/resources/books/all')
@hug.local()
def get_books():
    return books


@hug.get('/api/v1/resources/books')
@hug.local()
def get_book(id):
    for book in books:
        if book["stock_number"] == int(id):
            return book
    return None


@hug.get('/api/v1/calculatrice/add')
def calculator(val1, val2):
    return float(val1) + float(val2)

@hug.get('/api/v1/calculatrice/sub')
def calculator(val1, val2):
    return float(val1) - float(val2)

@hug.get('/api/v1/calculatrice/mul')
def calculator(val1, val2):
    return float(val1) * float(val2)

@hug.get('/api/v1/calculatrice/div')
def calculator(val1, val2):
    return float(val1) / float(val2)



@hug.post('/api/v1/resources/books')
@hug.local()
def add_book(author, title, condition, price):
    stock_number = max([book["stock_number"] for book in books]) + 1
    book = {"stock_number": stock_number, "author": author, "title": title, "condition": condition, "price": price}
    books.append(book)
    with open("bookstore_inventory.csv", "a") as f:
        f.write(f"{stock_number},{author},{title},{condition},{price}\n")




if __name__ == '__main__':
    books = create_dic()
    hug.API(__name__).http.serve()





