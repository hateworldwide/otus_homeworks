import json
import csv
import math

class User():
    def __init__(self, name, gender, address, age):
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

main_list = []
count = math.ceil(books.__len__()/users.__len__())
count_floor = math.floor(books.__len__()/users.__len__())
user_count = users.__len__()
book_count = books.__len__()
with open ('result.json', 'w') as jsonfile:
    for user in users:
        book_list = []
        if book_count%user_count == 0:
            count = count_floor
        for i in range(count):
            book = books[0]
            books.remove(book)
            book_dict = {'title': book.getTitle(), 'author': book.getAuthor(), 'pages': book.getPages(), 'genre': book.getGenre()}
            book_list.append(book_dict)
        template = {'name': user.getUserName(), 'gender': user.getUserGender(), 'address': user.getUserAddress(), 'age': user.getUserAge(), 'books': book_list}
        main_list.append(template)
        book_count -= count
        user_count -= 1
    json.dump(main_list, jsonfile, indent=4)
