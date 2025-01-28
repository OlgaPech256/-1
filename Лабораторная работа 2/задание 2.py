class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

# Пример использования
if __name__ == "__main__":
    library = Library()
    print(library.get_next_book_id())  # 1

    # Добавляем книги
    book1 = Book(1, 'Книга 1', 100)
    book2 = Book(2, 'Книга 2', 200)
    library.books.extend([book1, book2])

    print(library.get_next_book_id())  # 3
    print(library.get_index_by_book_id(1))  # 0
    print(library.get_index_by_book_id(2))  # 1

    try:
        print(library.get_index_by_book_id(3))  # Ошибка
    except ValueError as e:
        print(e)  # Книги с запрашиваемым id не существует