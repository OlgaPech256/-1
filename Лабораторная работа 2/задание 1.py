class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'

# Пример использования
if __name__ == "__main__":
    book = Book(1, 'test_name_1', 200)
    print(str(book))   # Книга "test_name_1"
    print(repr(book))  # Book(id_=1, name='test_name_1', pages=200)