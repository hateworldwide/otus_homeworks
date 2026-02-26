import json
import csv
import math

class User():
    def __init__(self, name, gender, address, age):
        self.books = None
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age

class Book():
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
    @classmethod
    def from_dict(cls, book_dict: dict):
        return cls(
            book_dict.get("Title"),
            book_dict.get("Author"),
            int(book_dict.get("Pages")),
            book_dict.get("Genre")
        )

def devide_books(books, users):
    count = math.ceil(len(books) / len(users))
    count_floor = math.floor(len(books) / len(users))
    user_count = len(users)
    book_count = len(books)
    for user in users:
        book_list = []
        if book_count % user_count == 0:
            count = count_floor
        for i in range(count):
            book = books[0]
            books.remove(book)
            book_dict = {'title': book.title,
                         'author': book.author,
                         'pages': book.pages,
                         'genre': book.genre}
            book_list.append(book_dict)
        user.putBooks(book_list)
        book_count -= count
        user_count -= 1

books = []
users = []

with open('books.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
        book = dict(zip(header, row))
        books.append(Book.from_dict(book))

with open('users.json', 'r') as jsonfile1:
    data = json.load(jsonfile1)
    for user in data:
        users.append(User(user.get('name'), user.get('gender'), user.get('address'), str(user.get('age'))))

devide_books(books, users)

main_list = []

with open ('result.json', 'w') as jsonfile:
    for user in users:
        template = {'name': user.getUserName(),
                    'gender': user.getUserGender(),
                    'address': user.getUserAddress(),
                    'age': user.getUserAge(),
                    'books': user.getBooks()}
        main_list.append(template)

    json.dump(main_list, jsonfile, indent=4)
