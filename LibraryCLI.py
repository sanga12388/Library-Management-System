from services.book_service import BookService
from services.users_service import UserService
from services.transaction_service import TransactionService

class LibraryCLI:
    def __init__(self):
        self.book_service = BookService()
        self.user_service = UserService()
        self.transaction_service = TransactionService()

    def run(self):
        while True:
            print("\nLibrary Management System")
            print("1. Manage Books")
            print("2. Manage Users")
            print("3. Manage Transactions")
            print("4. Check out Book")
            print("5. Check in Book")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.manage_books()
            elif choice == "2":
                self.manage_users()
            elif choice == "3":
                self.manage_transactions()
            elif choice == "4":
                self.check_out_book()
            elif choice == "5":
                self.check_in_book()
            elif choice == "6":
                print("exiting...")
                break
            else:
                print("invalid choice, please try again")

    def manage_books(self):
        while True:
            print("\nManage Books")
            print("1. Add book")
            print("2. Update book")
            print("3. Delete book")
            print("4. List all books")
            print("5. Search books")
            print("6. Back to main menu")
            choice = input("choose an option: ")

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                isbn = input("Enter book ISBN: ")
                self.book_service.add_book(title, author, isbn)
            elif choice == "2":
                isbn = input("Enter book ISBN to update: ")
                title = input("Enter new title (leave blank to not change): ")
                author = input("Enter new author (leave blank to not change): ")
                self.book_service.update_book(isbn, title, author)
            elif choice == "3":
                isbn = input("Enter book ISBN to delete: ")
                self.book_service.delete_book(isbn)
            elif choice == "4":
                self.book_service.list_books()
            elif choice == "5":
                title = input("Enter title to search (leave blank for no title search): ")
                author = input("Enter author to search (leave blank for no author search): ")
                isbn = input("Enter ISBN to search (leave blank for no ISBN search): ")
                self.book_service.search_books(title, author, isbn)
            elif choice == "6":
                break
            else:
                print("invalid choice, please try again")

    def manage_users(self):
        while True:
            print("\nManage Users")
            print("1. Add user")
            print("2. Update user")
            print("3. Delete user")
            print("4. List all users")
            print("5. Search users")
            print("6. Back to main menu")
            choice = input("choose an option: ")

            if choice == "1":
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                self.user_service.add_user(name, user_id)
            elif choice == "2":
                user_id = input("Enter user ID to update: ")
                name = input("Enter new name (leave blank to not change): ")
                self.user_service.update_user(user_id, name)
            elif choice == "3":
                user_id = input("Enter user ID to delete: ")
                self.user_service.delete_user(user_id)
            elif choice == "4":
                self.user_service.list_users()
            elif choice == "5":
                name = input("Enter name to search (leave blank for no name search): ")
                user_id = input("Enter user ID to search (leave blank for no ID search): ")
                self.user_service.search_users(name, user_id)
            elif choice == "6":
                break
            else:
                print("invalid choice, please try again.")

    def manage_transactions(self):
        while True:
            print("\nManage Transactions")
            print("1. List books taken by user")
            print("2. Retrieve number of books taken by user")
            print("3. Back to main menu")
            choice = input("choose an option: ")

            if choice == "1":
                user_id = input("Enter user ID: ")
                self.transaction_service.list_books_taken_by_user(user_id)
            elif choice == "2":
                user_id = input("Enter user ID: ")
                self.transaction_service.get_books_taken_by_user(user_id)
            elif choice == "3":
                break
            else:
                print("Invalid choice, please try again")

    def check_out_book(self):
        print("\nCheck Out Book")
        user_id = input("Enter user ID: ")
        book_isbn = input("Enter book ISBN: ")
        if self.book_service.is_book_available(book_isbn):
            if self.transaction_service.checkout_book(user_id, book_isbn):
                self.book_service.list_books()
        else:
            print(f"book with ISBN {book_isbn} is not available for checkout.")

    def check_in_book(self):
        print("\ncheck In Book")
        user_id = input("Enter user ID: ")
        book_isbn = input("Enter book ISBN: ")
        if self.transaction_service.checkin_book(user_id, book_isbn):
            self.book_service.list_books()

if __name__ == "__main__":
    cli = LibraryCLI()
    cli.run()
