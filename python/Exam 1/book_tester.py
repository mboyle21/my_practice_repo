# MARGARET MARY BOYLE

# #1
from book import Book

books = []

with open ("books.txt") as file:
    for line in file:
        title, author, genre = line.strip().split(",")
        book = Book(title, author, genre, checked_out=False)
        books.append(book)

# #2
book1 = books[0]
print(book1)

book2 = books[1]
print(book2)

book3 = books[2]
print(book3)

book4 = books[3]
print(book4)

book5 = books[4]
print(book5)

# #3
print(books[0].get_title())
print(books[0].get_author())
print(books[0].get_genre())
print(books[0].is_checked_out())

# #4
book1.check_out()
print(book1)

book1.return_book()
print(book1)
# print("Checked out status: ", book1.is_checked_out())
