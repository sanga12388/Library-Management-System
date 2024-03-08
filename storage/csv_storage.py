import csv
import utils.logger as logger

class CSVStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_books(self):
        books_data = []
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    books_data.append(row)
        except FileNotFoundError:
            logger.error(f"File '{self.file_path}' not found.")
        return books_data

    def write_books(self, books):
        try:
            with open(self.file_path, 'w', newline='') as file:
                fieldnames = ['title', 'author', 'isbn']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for book in books:
                    writer.writerow({'title': book.title, 'author': book.author, 'isbn': book.isbn})
            logger.info(f"Books data written to '{self.file_path}' successfully.")
        except Exception as e:
            logger.error(f"Error writing books data to '{self.file_path}': {e}")

    def read_users(self):
        users_data = []
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    users_data.append(row)
        except FileNotFoundError:
            logger.error(f"File '{self.file_path}' not found.")
        return users_data

    def write_users(self, users):
        try:
            with open(self.file_path, 'w', newline='') as file:
                fieldnames = ['name', 'user_id']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for user in users:
                    writer.writerow({'name': user.name, 'user_id': user.user_id})
            logger.info(f"Users data written to '{self.file_path}' successfully.")
        except Exception as e:
            logger.error(f"Error writing users data to '{self.file_path}': {e}")

    def read_transactions(self):
        transactions_data = []
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transactions_data.append(row)
        except FileNotFoundError:
            logger.error(f"File '{self.file_path}' not found")
        return transactions_data

    def write_transactions(self, transactions):
        try:
            with open(self.file_path, 'w', newline='') as file:
                fieldnames = ['user_id', 'book_isbn', 'action']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for transaction in transactions:
                    writer.writerow({'user_id': transaction.user_id, 'book_isbn': transaction.book_isbn, 'action': transaction.action})
            logger.info(f"Transactions data written to '{self.file_path}' successfully.")
        except Exception as e:
            logger.error(f"Error writing transactions data to '{self.file_path}': {e}")
