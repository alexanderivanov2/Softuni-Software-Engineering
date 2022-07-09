class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}


    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)
        if self.rented_books.get(user.username):
            self.rented_books.pop(user.username)

    def change_username(self, user_id, new_username):
        for u in self.user_records:
            if u.user_id == user_id:
                if u.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                if u.username in self.rented_books:
                    self.rented_books[new_username] = self.rented_books[u.username]
                    self.rented_books.pop(u.username)
                u.username = new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
        return f"There is no user with id = {user_id}!"