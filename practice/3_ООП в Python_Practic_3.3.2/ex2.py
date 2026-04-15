'''from book import Book

library = [Book ('Мастер и Маргаритта', 'Михаил булгаков'),
           Book ('Легенда об искателе', 'Алексей Иванов'),
           Book ('Война и мир', 'Лев Толстой')]

for book in library:
    print(f'{book.name_book} - {book.author_book}')
'''

from book import Book

library = [
    Book('Книга_1', 'Автор_1'),
    Book('Книга_2', 'Автор_2'),
    Book('Книга_3', 'Автор_3')
]

for book in library:
    print(f'Название книги: {book.name_book} Автор: {book.author_book}')

book = library[1]
print(book.name_book, book.author_book)






















