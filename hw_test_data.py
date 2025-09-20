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
    def getUserName(self):
        return self.name
    def getUserGender(self):
        return self.gender
    def getUserAddress(self):
        return self.address
    def getUserAge(self):
        return self.age
    def putBooks(self, books):
        self.books = books
    def getBooks(self):
        return self.books

class Book():
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getPages(self):
        return self.pages
    def getGenre(self):
        return self.genre

def devide_books(books, users):
    count = math.ceil(books.__len__() / users.__len__())
    count_floor = math.floor(books.__len__() / users.__len__())
    user_count = users.__len__()
    book_count = books.__len__()
    for user in users:
        book_list = []
        if book_count % user_count == 0:
            count = count_floor
        for i in range(count):
            book = books[0]
            books.remove(book)
            book_dict = {'title': book.getTitle(),
                         'author': book.getAuthor(),
                         'pages': book.getPages(),
                         'genre': book.getGenre()}
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
        books.append(Book(book.get("Title"), book.get("Author"), book.get("Pages"), book.get("Genre")))

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
