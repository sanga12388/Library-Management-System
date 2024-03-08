from models.book import Book
from storage.csv_storage import CSVStorage
import utils.logger as logger


class BookService:
    def __init__(self):
        self.storage = CSVStorage("books.csv")
        self.books = self._load_books()

    def _load_books(self):
        """load books from CSV"""
        logger.info("Loading books from CSV storage")
        books_data = self.storage.read_books()
        return [Book(title=row['title'], author=row['author'], isbn=row['isbn']) for row in books_data]

    def _save_books(self):
        """save the current list of books to CSV storage"""
        logger.info("Saving books to CSV storage")
        self.storage.write_books(self.books)

    def add_book(self, title, author, isbn):
        logger.info(f"Adding book with ISBN {isbn}")
        if any(book.isbn == isbn for book in self.books):
            logger.error(f"Book with ISBN {isbn} already exists")
            return False
        new_book = Book(title=title, author=author, isbn=isbn)
        self.books.append(new_book)
        self._save_books()
        logger.info(f"Book '{title}' added successfully")
        return True

    def update_book(self, isbn, title=None, author=None):
        """Update an existing book's details"""
        logger.info(f"Updating book with ISBN {isbn}")
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self._save_books()
                logger.info(f"Book with ISBN {isbn} has been updated.")
                return True
        logger.error(f"No book found with ISBN {isbn}.")
        return False

    def delete_book(self, isbn):
        """Delete a book."""
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]
                self._save_books()
                print(f"Book with ISBN {isbn} has been deleted")
                return True
        print(f"no book found with ISBN {isbn}.")
        return False

    def list_books(self):
        logger.info("listing all books")
        if not self.books:
            logger.info("No books available")
            return
        for book in self.books:
            print(book)

    def search_books(self, title=None, author=None, isbn=None):
        """Search for books by title, author, or ISBN"""
        logger.info("Searching for books")
        found_books = []
        for book in self.books:
            if title and title.lower() in book.title.lower():
                found_books.append(book)
            elif author and author.lower() in book.author.lower():
                found_books.append(book)
            elif isbn and isbn == book.isbn:
                found_books.append(book)

        if not found_books:
            logger.info("No books found")
            return
        for book in found_books:
            print(book)
    def get_book_by_isbn(self, isbn):
        """Get a book by its ISBN"""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    def is_book_available(self, isbn):
        """Check if a book is available for checkout"""
        for book in self.books:
            if book.isbn == isbn:
                return True
        return False