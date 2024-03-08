from models.transaction import Transaction
from storage.csv_storage import CSVStorage
from services.book_service import BookService
from services.users_service import UserService
import utils.logger as logger

class TransactionService:
    def __init__(self):
        self.storage = CSVStorage("transactions.csv")
        self.transactions = self._load_transactions()

    def _load_transactions(self):
        """Load transactions from CSV storage."""
        logger.info("Loading transactions from CSV storage")
        transactions_data = self.storage.read_transactions()
        return [Transaction(user_id=row['user_id'], book_isbn=row['book_isbn'], action=row['action']) for row in transactions_data]

    def _save_transactions(self):
        """Save the current list of transactions to CSV storage."""
        logger.info("Saving transactions to CSV storage")
        self.storage.write_transactions(self.transactions)

    def checkout_book(self, user_id, book_isbn):
        """Checkout a book."""
        logger.info(f"Checking out book with ISBN {book_isbn} by user ID {user_id}")
        if any(transaction.book_isbn == book_isbn and transaction.action == 'checkout' for transaction in self.transactions):
            print(f"Book with ISBN {book_isbn} is already checked out.")
            logger.error(f"Book with ISBN {book_isbn} is already checked out.")
            return False

        if not any(user.user_id == user_id for user in UserService().users):
            print(f"User with ID {user_id} does not exist.")
            logger.error(f"User with ID {user_id} does not exist.")
            return False

        if not any(book.isbn == book_isbn for book in BookService().books):
            logger.error(f"Book with ISBN {book_isbn} does not exist.")
            return False

        new_transaction = Transaction(user_id=user_id, book_isbn=book_isbn, action='checkout')
        self.transactions.append(new_transaction)
        self._save_transactions()
        logger.info(f"Book with ISBN {book_isbn} has been checked out by user ID {user_id}.")
        return True

    def checkin_book(self, user_id, book_isbn):
        """check in a book"""
        logger.info(f"Checking in book with ISBN {book_isbn} by user ID {user_id}")
        for transaction in self.transactions:
            if transaction.user_id == user_id and transaction.book_isbn == book_isbn and transaction.action == 'checkout':
                self.transactions.remove(transaction)
                self._save_transactions()
                logger.info(f"Book with ISBN {book_isbn} has been checked in by user ID {user_id}.")
                return True
        logger.error(f"Book with ISBN {book_isbn} is not checked out by user ID {user_id}.")
        return False

    def get_books_taken_by_user(self, user_id):
        """Retrieve the number of books taken by a user."""
        logger.info(f"Retrieving number of books taken by user ID {user_id}")
        count = sum(1 for transaction in self.transactions if transaction.user_id == user_id and transaction.action == 'checkout')
        logger.info(f"User with ID {user_id} has taken {count} book(s).")
        print(f"User with ID {user_id} has taken {count} book(s).")

    def list_books_taken_by_user(self, user_id):
        """List the details of books taken by a user."""
        logger.info(f"Listing books taken by user ID {user_id}")
        taken_books = [transaction.book_isbn for transaction in self.transactions if transaction.user_id == user_id and transaction.action == 'checkout']
        if taken_books:
            print(f"Books taken by user with ID {user_id}:")
            for isbn in taken_books:
                book = BookService().get_book_by_isbn(isbn)
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        else:
            logger.info(f"No books taken by user with ID {user_id}.")
            print(f"No books taken by user with ID {user_id}.")

    def print_all_checkins(self):
        """Print all check-in transactions."""
        logger.info("Printing all check-in transactions")
        checkins = [transaction for transaction in self.transactions if transaction.action == 'checkin']
        if checkins:
            print("All check-in transactions:")
            for transaction in checkins:
                print(f"User ID: {transaction.user_id}, Book ISBN: {transaction.book_isbn}")
        else:
            print("No check-in transactions found.")

    def print_all_checkouts(self):
        """Print all check-out transactions."""
        logger.info("Printing all check-out transactions")
        checkouts = [transaction for transaction in self.transactions if transaction.action == 'checkout']
        if checkouts:
            print("All check-out transactions:")
            for transaction in checkouts:
                print(f"User ID: {transaction.user_id}, Book ISBN: {transaction.book_isbn}")
        else:
            print("No check-out transactions found.")
