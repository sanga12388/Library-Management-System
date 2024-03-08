class Transaction:
    def __init__(self, user_id, book_isbn, action):
        self.user_id = user_id
        self.book_isbn = book_isbn
        self.action = action
