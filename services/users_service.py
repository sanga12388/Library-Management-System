from models.user import User
from storage.csv_storage import CSVStorage
import utils.logger as logger

class UserService:
    def __init__(self):
        self.storage = CSVStorage("users.csv")
        self.users = self._load_users()

    def _load_users(self):
        """Load users from CSV storage."""
        logger.info("Loading users from CSV storage")
        users_data = self.storage.read_users()
        return [User(name=row['name'], user_id=row['user_id']) for row in users_data]

    def _save_users(self):
        """Save the current list of users to CSV storage."""
        logger.info("Saving users to CSV storage")
        self.storage.write_users(self.users)

    def add_user(self, name, user_id):
        logger.info(f"Adding user with ID {user_id}")
        if any(user.user_id == user_id for user in self.users):
            logger.error(f"User with ID {user_id} already exists.")
            return False
        new_user = User(name=name, user_id=user_id)
        self.users.append(new_user)
        self._save_users()
        logger.info(f"User '{name}' added successfully.")
        return True

    def update_user(self, user_id, name=None):
        """Update an existing user's details."""
        logger.info(f"Updating user with ID {user_id}")
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self._save_users()
                logger.info(f"User with ID {user_id} has been updated.")
                return True
        logger.error(f"No user found with ID {user_id}.")
        return False

    def delete_user(self, user_id):
        """Delete a user."""
        logger.info(f"Deleting user with ID {user_id}")
        for i, user in enumerate(self.users):
            if user.user_id == user_id:
                del self.users[i]
                self._save_users()
                logger.info(f"User with ID {user_id} has been deleted.")
                return True
        logger.error(f"No user found with ID {user_id}.")
        return False

    def list_users(self):
        """List all users."""
        logger.info("Listing all users")
        if not self.users:
            logger.info("No users available.")
            return
        for user in self.users:
            print(user)

    def search_users(self, name=None, user_id=None):
        """Search for users by name or user ID."""
        logger.info("Searching for users")
        found_users = []
        for user in self.users:
            if name and name.lower() in user.name.lower():
                found_users.append(user)
            elif user_id and user_id == user.user_id:
                found_users.append(user)

        if not found_users:
            logger.info("No users found.")
            return
        for user in found_users:
            print(user)
