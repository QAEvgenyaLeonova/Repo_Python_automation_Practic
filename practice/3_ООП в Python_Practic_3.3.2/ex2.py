from book import Book

library = [Book ('Мастер и Маргаритта', 'Михаил булгаков'),
           Book ('Легенда об искателе', 'Алексей Иванов'),
           Book ('Война и мир', 'Лев Толстой')]

for book in library:
    print(f'{book.name_book} - {book.author_book}')